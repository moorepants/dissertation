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
fixed = re.sub(r'      {\\em\\LARGE\\py@HeaderFamily \\py@release\\releaseinfo \\par}\n', '', fixed)
fixed = re.sub(r'    \\rule{\\textwidth}{1pt}%\n', '', fixed)

fixed = re.sub(r'    \\let\\footnotesize\\small\n',
r'    \\setcounter{page}{3}\n    \\let\\footnotesize\\small\n', fixed)

# if i try to add frontmatter to the title page to get a page number on the
# page but the the /marks seem to break in the document
#\\thispagestyle{frontmatter}\n
# or
# \\pagestyle{frontmatter}

fixed = fixed.replace(r'\@date', 'August 2012')
fixed = fixed.replace(r'\vfill\vfill', r'\vfill')

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

fixed = re.sub(r', \\py@release', '', fixed)

fixed = re.sub(r'\\py@HeaderFamily \\@title}}\n',
r'\\py@HeaderFamily \\@title}}\n    \\fancyhead[RE,LO]{{\\py@HeaderFamily \\@author}}\n',
fixed)

with open('_build/latex/sphinx.sty', 'w') as f:
    f.write(fixed)

# Add the signature pages to the front of the document.
with open('_build/latex/HumanControlofaBicycle.tex', 'r') as f:
    text = f.read()

fixed = re.sub(r'\\maketitle',
    r'\\includepdf[pages={3,{}}]{../../../ucdthesis/skeleton-thesis.pdf}\n\\maketitle',
    text)

with open('_build/latex/HumanControlofaBicycle.tex', 'w') as f:
    f.write(fixed)
