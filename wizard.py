import os
import sys
from typing import Optional, List
from pathlib import Path
import datetime

from bullet import Bullet, YesNo
from jinja2 import Template, Environment
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


###############################################################


TEMPLATES_FILE = Path('templates.yml')
SRC_PATH = Path('src')

jinja_env = Environment()
jinja_env.block_start_string = '[%'
jinja_env.block_end_string = '%]'
jinja_env.variable_start_string = '[['
jinja_env.variable_end_string = ']]'
jinja_env.comment_start_string = '[#'
jinja_env.comment_end_string = '#]'

###############################################################


def dateformat(value: str) -> str:
    return value.replace('/', '').replace('-', '')


jinja_env.filters['dateformat'] = dateformat


def slugify(value: str) -> str:
    return value.replace(' ', '_')


jinja_env.filters['slugify'] = slugify

###############################################################


class DocTemplate:
    def __init__(
        self,
        title: str,
        template: Path,
        filename_template: str,
        path: Path,
        create_dir: bool = False,
        extra_vars: Optional[dict] = None
    ):
        self.filename_template = filename_template
        self.variables = {
            'title': title,
            'date': datetime.date.today().isoformat().replace('-', '/'),
            'author': 'Nome Cognome'
        }
        if extra_vars:
            for v in extra_vars:
                self.variables.update(v)
        self.template = template
        self.path = path
        self.create_dir = create_dir

    def ask_variables(self):
        _variables = {}
        for name, default in self.variables.items():
            prompt = f'{name} ({default}): ' if default else f'{name}: '
            res = input(prompt)
            if default:
                if res == '':
                    _variables[name] = default
                else:
                    _variables[name] = res
            else:
                _variables[name] = res
        return _variables

    def render_template(self, variables: dict) -> str:
        with open(self.template, 'r') as f:
            template = jinja_env.from_string(f.read())
        return template.render(variables)

    def render_filename(self, variables: dict) -> str:
        template = jinja_env.from_string(self.filename_template)
        return template.render(variables)

    def create_symlinks(self, path: Path):
        links = ['assets', 'classes', 'common']
        try:
            for l in links:
                src = f'../../{l}'
                dest = path / l
                os.symlink(src, dest)
        except OSError as e:
            print(e)
            print('Are you on Windows? Try enabling Developer Mode or running this script with admin privileges')
            sys.exit(1)

    def create_new(self, variables: dict) -> Optional[Path]:
        filename = self.render_filename(variables)

        if self.create_dir:
            path = SRC_PATH / self.path / slugify(variables['title']) / filename
            path.parent.mkdir(parents=True, exist_ok=True)
            self.create_symlinks(path.parent)
        else:
            path = SRC_PATH / self.path / filename

        if path.is_file():
            return None

        rendered = self.render_template(variables)
        with open(path, 'w') as f:
            f.write(rendered)
        return path

###############################################################


def parse_templates(templates_file: Path) -> list:
    with open(templates_file, 'r') as f:
        templates = load(f, Loader)

    for index, t in enumerate(templates):
        base = t.get('from')
        if base:
            base = next(filter(lambda x: x['id'] == base, templates))

            derived = base.copy()
            derived.update(t)

            if t.get('extra_vars') and base.get('extra_vars'):
                derived['extra_vars'] += base['extra_vars']

            derived['show'] = True
            templates[index] = derived

    return [t for t in templates if t.get('show', True)]


def main():
    templates = parse_templates(TEMPLATES_FILE)

    template_name = Bullet(
        'Select a template: ',
        choices=[t['title'] for t in templates]
    ).launch()
    template = next(filter(lambda t: t['title'] == template_name, templates))

    template = DocTemplate(
        title=template['title'],
        template=Path(template['template']),
        filename_template=template['filename_template'],
        extra_vars=template.get('extra_vars'),
        path=Path(template['path']),
        create_dir=template.get('create_dir', False)
    )

    variables = template.ask_variables()
    print(variables)

    proceed = YesNo(
        'Are you sure to create a new document from template? ').launch()
    if proceed:
        path = template.create_new(variables)
        if not path:
            print('Cannot create because it already exists.')
        else:
            print(f'Successfuly created new document at \'{path}\'')

###############################################################


if __name__ == '__main__':
    main()
