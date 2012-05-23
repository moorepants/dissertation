#!/usr/bin/env python

# This script requires the ImageMagick montage command line tool.

import os
import numpy as np
import matplotlib.pyplot as plt
import bicycleparameters as bp
from dtk import bicycle

# local dependencies
from Whipple import LinearWhipple

fig_size =  [3., 3.]
params = {'backend': 'ps',
          'axes.labelsize': 10,
          'axes.titlesize': 10,
          'text.fontsize': 10,
          'legend.fontsize': 8,
          'xtick.labelsize': 8,
          'ytick.labelsize': 8,
          'text.usetex': True,
          'figure.figsize': fig_size,
          'figure.dpi': 200}
plt.rcParams.update(params)

# create the Whipple model (with my parameters)
try:
    f = open('Whipple.py', 'r')
except IOError:
    from altk import alparse
    alparse.alparse('Whipple', 'Whipple', code='Python')
else:
    f.close()
    del f

whip = LinearWhipple()

# load the benchmark parameters
pathToData='/media/Data/Documents/School/UC Davis/Bicycle Mechanics/BicycleParameters/data/'
benchmark = bp.Bicycle('Benchmark', pathToData)
benchmarkPar = bp.io.remove_uncertainties(benchmark.parameters['Benchmark'])
# convert to my parameter set
moorePar = bicycle.benchmark_to_moore(benchmarkPar, oldMassCenter=False)
whip.set_parameters(moorePar)

# linearize about the nominal configuration
equilibrium = np.zeros(len(whip.stateNames))
pitchAngle = bicycle.pitch_from_roll_and_steer(0., 0., moorePar['rf'], moorePar['rr'],
        moorePar['d1'], moorePar['d2'], moorePar['d3'])
equilibrium[whip.stateNames.index('q5')] = pitchAngle

# below the weave bifurcation
speedNaught = 0.5
u6Naught = -speedNaught / moorePar['rr']
equilibrium[whip.stateNames.index('u6')] = u6Naught
whip.linear(equilibrium)

figs = whip.plot_eigenvectors(states=('q4', 'q7'))

for i, f in enumerate(figs):
    legTexts = f.axes[0].legend_.texts
    for text in legTexts:
        text.set_text('$' + text.get_text()[0] + '_' + text.get_text()[1] + '$')
    speed = 'Half'
    f.savefig('../../figures/eom/eVec' + speed + '-' + str(i + 1) + '.png')
figPath = '../../figures/eom/'
os.system('montage -geometry +0+0 {0}eVecHalf-1.png {0}eVecHalf-2.png {0}eVecHalf-3.png {0}eVecHalf-4.png {0}eVecHalf.png'.format(figPath))

fig_size =  [2., 2.]
params = {'figure.figsize': fig_size}
plt.rcParams.update(params)

# unstable weave
speedNaught = 3.0
u6Naught = -speedNaught / moorePar['rr']
equilibrium[whip.stateNames.index('u6')] = u6Naught
whip.linear(equilibrium)

figs = whip.plot_eigenvectors(states=('q4', 'q7'))

for i, f in enumerate(figs):
    legTexts = f.axes[0].legend_.texts
    for text in legTexts:
        text.set_text('$' + text.get_text()[0] + '_' + text.get_text()[1] + '$')
    speed = 'Three'
    ax = f.axes[0]
    bbox = ax.get_position()
    ax.set_position([0.125, 0.1, 0.9 - 0.125, 0.9 - 0.2])
    f.savefig('../../figures/eom/eVec' + speed + '-' + str(i + 1) + '.png')
os.system('montage -geometry +0+0 {0}eVecThree-1.png {0}eVecThree-2.png {0}eVecThree-3.png {0}eVecThree.png'.format(figPath))

# stable
speedNaught = 5.0
u6Naught = -speedNaught / moorePar['rr']
equilibrium[whip.stateNames.index('u6')] = u6Naught
whip.linear(equilibrium)

figs = whip.plot_eigenvectors(states=('q4', 'q7'))

for i, f in enumerate(figs):
    legTexts = f.axes[0].legend_.texts
    for text in legTexts:
        text.set_text('$' + text.get_text()[0] + '_' + text.get_text()[1] + '$')
    speed = 'Five'
    ax = f.axes[0]
    bbox = ax.get_position()
    ax.set_position([0.125, 0.1, 0.9 - 0.125, 0.9 - 0.2])
    f.savefig('../../figures/eom/eVec' + speed + '-' + str(i + 1) + '.png')
os.system('montage -geometry +0+0 {0}eVecFive-1.png {0}eVecFive-2.png {0}eVecFive-3.png {0}eVecFive.png'.format(figPath))

# unstable capsize
speedNaught = 8.0
u6Naught = -speedNaught / moorePar['rr']
equilibrium[whip.stateNames.index('u6')] = u6Naught
whip.linear(equilibrium)

figs = whip.plot_eigenvectors(states=('q4', 'q7'))

for i, f in enumerate(figs):
    legTexts = f.axes[0].legend_.texts
    for text in legTexts:
        text.set_text('$' + text.get_text()[0] + '_' + text.get_text()[1] + '$')
    speed = 'Seven'
    ax = f.axes[0]
    bbox = ax.get_position()
    ax.set_position([0.125, 0.1, 0.9 - 0.125, 0.9 - 0.2])
    f.savefig('../../figures/eom/eVec' + speed + '-' + str(i + 1) + '.png')
os.system('montage -geometry +0+0 {0}eVecSeven-1.png {0}eVecSeven-2.png {0}eVecSeven-3.png {0}eVecSeven.png'.format(figPath))
