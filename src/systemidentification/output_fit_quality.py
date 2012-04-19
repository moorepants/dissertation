#/usr/bin/env python

# Creates restructured text tables with the results of the simulation output
# percent variance for the set of runs.

import os
import numpy as np
from scipy.io import loadmat
import pandas

directory = '/media/Data/Documents/School/UC Davis/Bicycle Mechanics/BicycleSystemID/scripts/canonicalid'
fit = loadmat(os.path.join(directory, 'output-compare.mat'))

# The simulations of the unstable system may blow up in the time span and the
# resulting variance values are extremely small numbers. Here I replace those
# numbers with NaN to ignore them in the following calculations.
fit['fits'][fit['fits'] < -100.] = np.nan

p = pandas.Panel(fit['fits'],
                 items=[str(x[0]) for x in fit['goodRuns']],
                 major_axis=[str(x[0][0]) for x in fit['models']],
                 minor_axis=['phi', 'delta', 'phiDot', 'deltaDot'])

# This gives the median value across runs for each model and output.
outputMedian = p.median('items')
# This gives the mean of the previous results across the outputs.
totalMedian = p.median('items').mean(1)

# Create an restructuredtext table for each of the input measures.
per = lambda x: '{:.1%}'.format(x / 100.)

html = outputMedian.to_html(float_format=per)
with open('output-median.html', 'w') as f:
    f.write(html)
os.system('pandoc -f html -t rst -o output-median.rst output-median.html')
os.system('mv output-median.rst ../../tables/systemidentification/')
