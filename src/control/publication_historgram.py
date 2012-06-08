#!/usr/bin/env python

from pybtex.database.input import bibtex
import matplotlib.pyplot as plt

parser = bibtex.Parser()
path = '/media/Data/Documents/School/UC Davis/Bicycle Mechanics/Papers/bicycle.bib'
bib_data = parser.parse_file(path)
years = []
for entry in bib_data.entries:
    try:
        years.append(int(bib_data.entries[entry].fields['year']))
    except:
        pass

plt.hist(years, bins=40)
plt.title('{} Total Publications'.format(len(years)))
plt.xticks(range(1860, 2030, 10), fontsize=6, rotation=20.0)
plt.yticks(range(0, 140, 20), fontsize=6)
plt.ylabel('Number of Publications')
plt.xlabel('Year')
fig = plt.gcf()
fig.set_size_inches(4.0, 4.0)
fig.savefig('../../figures/control/pub-hist.png', dpi=200)
fig.savefig('../../figures/control/pub-hist.pdf')
plt.show()
