#!/usr/bin/env python

"""This file needs to be run in after Sphinx's tex generation but before the
latex or pdflatex calls."""

import re

# Remove the numbering and page style stuff in the toc redefintion in the class
# file. I'm setting these in the toc variable in conf.py.
with open('_build/latex/sphinxmanual.cls', 'r') as f:
    text = f.read()

pattern = r"\\setcounter{page}\{1\}%\n  \\pagebreak%\n  \\pagestyle{plain}%"
replace = r"\pagebreak%"
fixed = re.sub(pattern, replace, text)
fixed = fixed.replace(r'\pagenumbering{arabic}', '')

with open('_build/latex/sphinxmanual.cls', 'w') as f:
    f.write(fixed)

# Add a new frontmatter header style to the sphinx style file.
with open('_build/latex/sphinx.sty', 'r') as f:
    text = f.read()

pattern = (r"    \\renewcommand{\\headrulewidth}{0pt}\n" +
r"    \\renewcommand{\\footrulewidth}{0.4pt}\n  }")

replace = \
r"""    \\renewcommand{\\headrulewidth}{0pt}
    \\renewcommand{\\footrulewidth}{0.4pt}
  }
  \\fancypagestyle{frontmatter}{
    \\fancyhf{}
    \\fancyfoot[CE,CO]{{--\\py@HeaderFamily\\thepage--}}
    \\renewcommand{\\headrulewidth}{0pt}
    \\renewcommand{\\footrulewidth}{0pt}
  }"""

fixed = re.sub(pattern, replace, text)

with open('_build/latex/sphinx.sty', 'w') as f:
    f.write(fixed)
