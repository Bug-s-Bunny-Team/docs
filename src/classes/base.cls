\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{base}
\LoadClass[12pt]{article}

\RequirePackage[utf8]{inputenc}
\RequirePackage[italian]{babel}	%rende figure -> figura o table -> tabella; per i caption
\RequirePackage[a4paper,margin=2.5cm,headheight=32pt]{geometry}
%\RequirePackage[sfdefault]{quattrocento}
\RequirePackage{graphicx}
\RequirePackage{fancyhdr}
\RequirePackage[table]{xcolor}
\RequirePackage{tabularx} %tabelle larghe
\RequirePackage{longtable} %una tabella può continuare su più pagine
\RequirePackage{booktabs} %toprule e midrule usati al posto di hline
\RequirePackage{multirow} %utile per visualizzare una cella su più righe
\RequirePackage{float} %per poter usare l'opzione [H] nelle figure
\RequirePackage{array}
\RequirePackage{listings}   % formattazione e highlight codice
\RequirePackage[hidelinks]{hyperref}
\RequirePackage{eurosym}

% colorazione e sottolineatura url
% \hypersetup{
%     colorlinks=false,
% 	urlbordercolor=Arancione,
% 	pdfborderstyle={/S/U/W 1}
% }

\setcounter{secnumdepth}{5}
\setcounter{tocdepth}{5} 

\input{common/variables}
\input{common/headfoot}

\renewcommand{\maketitle}{
    \input{common/titlepage}
}

\newcommand*{\versione}[1]{\gdef\@versione{#1}}
\newcommand*{\verificatore}[1]{\gdef\@verificatore{#1}}
\newcommand*{\approvatore}[1]{\gdef\@approvatore{#1}}
\newcommand*{\uso}[1]{\gdef\@uso{#1}}

% creazione e applicazione stile per formattazione e highlight codice
\lstdefinestyle{style}{
    backgroundcolor=\color{backcolour},   
    commentstyle=\color{codegreen},
    keywordstyle=\color{magenta},
    numberstyle=\tiny\color{codegray},
    stringstyle=\color{codepurple},
    basicstyle=\ttfamily\footnotesize,
    breakatwhitespace=false,
    breaklines=true,
    captionpos=b,
    keepspaces=false,
    numbers=left,
    numbersep=5pt,
    showspaces=false,
    showstringspaces=false,
    showtabs=false,
    tabsize=2
}
\lstset{style=style}

%formattazione e higlight per files.json
\lstdefinelanguage{JSON}{
    numbers=left,
    numberstyle=\small,
    rulecolor=\color{black},
    showspaces=false,
    showtabs=false,
    breaklines=true,
    postbreak=\raisebox{0ex}[0ex][0ex]{\ensuremath{\color{gray}\hookrightarrow\space}},
    breakatwhitespace=true,
    basicstyle=\ttfamily\small,
    upquote=true,
    morestring=[b]",
    stringstyle=\color{string},
    literate=
     *{0}{{{\color{numb}0}}}{1}
      {1}{{{\color{numb}1}}}{1}
      {2}{{{\color{numb}2}}}{1}
      {3}{{{\color{numb}3}}}{1}
      {4}{{{\color{numb}4}}}{1}
      {5}{{{\color{numb}5}}}{1}
      {6}{{{\color{numb}6}}}{1}
      {7}{{{\color{numb}7}}}{1}
      {8}{{{\color{numb}8}}}{1}
      {9}{{{\color{numb}9}}}{1}
      {\{}{{{\color{delim}{\{}}}}{1}
      {\}}{{{\color{delim}{\}}}}}{1}
      {[}{{{\color{delim}{[}}}}{1}
      {]}{{{\color{delim}{]}}}}{1},
}


\renewcommand*\contentsname{Indice}
