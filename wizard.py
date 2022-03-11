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


TEMPLATES_FILE = Path('templates.yml')
SRC_PATH = Path('src')

jinja_env = Environment()
jinja_env.block_start_string = '[%'
jinja_env.block_end_string = '%]'
jinja_env.variable_start_string = '[['
jinja_env.variable_end_string = ']]'


class DocTemplate:
    def __init__(
        self, 
        title: str, 
        prefix: str, 
        template: Path,
        extra_vars: Optional[dict] = None
    ):
        self.variables = {
            'title': title,
            'prefix': prefix,
            'date': datetime.date.today().isoformat().replace('-', '/'),
            'author': 'Nomone Cognomone'
        }
        if extra_vars:
            for v in extra_vars:
                self.variables.update(v)
        self.template = template

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

    def render_template(self, variables: dict):
        with open(self.template, 'r') as f:
            template = jinja_env.from_string(f.read())
        return template.render(variables)

    def create_new(self, variables: dict, filename: Optional[str] = None) -> Optional[Path]:
        if not filename:
            prefix = variables['prefix']
            date = variables['date'].replace('/', '')
            filename = f'{prefix}_{date}.tex'
        path = SRC_PATH.joinpath(filename)
        if path.is_file():
            return None
        rendered = self.render_template(variables)
        with open(path, 'w') as f:
            f.write(rendered)
        return path


def main():
    with open(TEMPLATES_FILE, 'r') as f:
        templates = load(f, Loader)

    template_name = Bullet('Select a template: ', choices=[t['title'] for t in templates]).launch()
    template = next(filter(lambda t: t['title'] == template_name, templates))
    
    template = DocTemplate(
        template['title'], 
        template['prefix'], 
        Path(template['template']),
        template.get('extra_vars')
    )

    variables = template.ask_variables()
    print(variables)

    proceed = YesNo('Are you sure to create a new document from template? ').launch()
    if proceed:
        path = template.create_new(variables)
        if not path:
            print('Cannot create because it already exists.')
        else:
            print(f'Successfuly created new document at \'{path}\'')


if __name__ == '__main__':
    main()
