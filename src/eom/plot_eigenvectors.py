#!/usr/bin/env python

# dependencies
import numpy as np
import bicycleparameters as bp
from dtk import bicycle

# local dependencies
from Whipple import LinearWhipple

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
pitchAngle = bicycle.pitch_from_roll_and_steer(0., 0., moorePar['rF'], moorePar['rR'],
        moorePar['d1'], moorePar['d2'], moorePar['d3'])
equilibrium[whip.stateNames.index('q5')] = pitchAngle
speedNaught = 0.5
u6Naught = -speedNaught / moorePar['rR']
equilibrium[whip.stateNames.index('u6')] = u6Naught
whip.linear(equilibrium)

figs = whip.plot_eigenvectors(states=('u4', 'u7'), pub=True)

for i, f in enumerate(figs):
    speed = 'Half'
    f.savefig('../../figures/eom/eVec' + speed + '-' + str(i + 1) + '.png')

speedNaught = 3.0
u6Naught = -speedNaught / moorePar['rR']
equilibrium[whip.stateNames.index('u6')] = u6Naught
whip.linear(equilibrium)

figs = whip.plot_eigenvectors(states=('u4', 'u7'), pub=True)

for i, f in enumerate(figs):
    speed = 'Three'
    f.savefig('../../figures/eom/eVec' + speed + '-' + str(i + 1) + '.png')

speedNaught = 5.0
u6Naught = -speedNaught / moorePar['rR']
equilibrium[whip.stateNames.index('u6')] = u6Naught
whip.linear(equilibrium)

figs = whip.plot_eigenvectors(states=('u4', 'u7'), pub=True)

for i, f in enumerate(figs):
    speed = 'Five'
    f.savefig('../../figures/eom/eVec' + speed + '-' + str(i + 1) + '.png')

speedNaught = 8.0
u6Naught = -speedNaught / moorePar['rR']
equilibrium[whip.stateNames.index('u6')] = u6Naught
whip.linear(equilibrium)

figs = whip.plot_eigenvectors(states=('u4', 'u7'), pub=True)

for i, f in enumerate(figs):
    speed = 'Seven'
    f.savefig('../../figures/eom/eVec' + speed + '-' + str(i + 1) + '.png')
