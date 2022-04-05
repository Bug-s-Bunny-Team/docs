\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{base}
\LoadClass[12pt]{article}

\RequirePackage[utf8]{inputenc}
\RequirePackage[a4paper,margin=2.5cm,headheight=32pt]{geometry}
%\RequirePackage[sfdefault]{quattrocento}
\RequirePackage{graphicx}
\RequirePackage{fancyhdr}
\RequirePackage{xcolor}

\input{common/variables}
\input{common/headfoot}

\renewcommand{\maketitle}{
    \input{common/titlepage}
}

\newcommand*{\verificatore}[1]{\gdef\@verificatore{#1}}
\newcommand*{\approvatore}[1]{\gdef\@approvatore{#1}}
\newcommand*{\uso}[1]{\gdef\@uso{#1}}