\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{verbale}[2022/03/11 Verbale]

\LoadClass[12pt]{article}

\RequirePackage[utf8]{inputenc}
\RequirePackage[a4paper,margin=2.5cm,headheight=32pt]{geometry}
\RequirePackage[sfdefault]{quattrocento}
\RequirePackage{graphicx}
\RequirePackage{fancyhdr}

\input{common/variables}
\input{common/headfoot}

\renewcommand{\maketitle}{
    \input{common/titlepage}
}
