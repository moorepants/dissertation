#/usr/bin/env python

# This makes a simple collage of all of the bicycle images.

import os

figPath = '../../figures/physicalparameters'

bicycles = ['browser_sub.jpg',
            'browserIns_sub.jpg',
            'crescendo_sub.jpg',
            'stratos_sub.jpg',
            'fisher_sub.jpg',
            'pista_sub.jpg',
            'yellow_sub.jpg',
            'yellowRev_sub.jpg',
            'davisBicycle_sub.jpg',
            'gyroBicycle_sub.jpg']

names = ["'(a)'",
         "'(b)'",
         "'(c)'",
         "'(d)'",
         "'(e)'",
         "'(f)'",
         "'(g)'",
         "'(h)'",
         "'(i)'",
         "'(j)'"]

args = ''
for bike, name in zip(bicycles, names):
    args += '-label ' + name + ' ' + os.path.join(figPath, bike) + ' '

spacing = 0.0625 * 525.0 / 1.75

os.system('montage -density 300x300 -tile 2x5 -geometry +{:1.0f}+{:1.0f}'.format(spacing,
    spacing) + ' '
        + args + os.path.join(figPath, 'bicycles.jpg'))
