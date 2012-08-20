import re

with open('_build/latex/sphinxmanual.cls', 'r') as f:
    text = f.read()

pattern = r"\\setcounter{page}\{1\}%\n  \\pagebreak%\n  \\pagestyle{plain}%"

replace = \
r"""\setcounter{page}{2}%
  \pagebreak%
  \pagestyle{frontmatter}%"""

fixed = re.sub(pattern, replace, text)

with open('_build/latex/sphinxmanual.cls', 'w') as f:
    f.write(fixed)
