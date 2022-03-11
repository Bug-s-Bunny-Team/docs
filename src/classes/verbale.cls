\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{verbale}[2022/03/11 Verbale]

\LoadClass[12pt]{article}

\RequirePackage[utf8]{inputenc}
\RequirePackage[a4paper,margin=2.5cm,headheight=32pt]{geometry}
\RequirePackage[sfdefault]{quattrocento}
\RequirePackage{graphicx}
\RequirePackage{fancyhdr}

\input{common/variables}

\pagestyle{fancy}
\fancyhead[R]{\@title}
\fancyhead[L]{
    \includegraphics[width=0.8cm]{assets/logo}
}
\fancyfoot[C]{\thepage}

\renewcommand{\maketitle}{
    \begin{titlepage}
        \begin{center}
            \vspace*{\fill}
            
            \includegraphics[width=5cm]{assets/logo}
            
            \Huge{\textbf{\teamname}}
            
            \vspace{3cm}
            
            \Huge
            \textbf{\@title}
            
            \Large{\@date}
    
            \vspace{3cm}
            
            \textbf{Redattore:} \@author
            
            \vfill	
        \end{center}
    \end{titlepage}    
}
