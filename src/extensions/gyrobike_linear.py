#!/usr/bin/env python

# built in imports
import sys

# dependencies
import numpy as np
import bicycleparameters as bp
from dtk import bicycle

# local dependencies
sys.path.append('/media/Data/Documents/School/UC Davis/Bicycle Mechanics/bicycle/alparse')
from models.GyroBike.GyroBike import LinearGyroBike

# create the linear gyrobike model
gyrobike = LinearGyroBike()

# load the benchmark parameters
pathToData='/media/Data/Documents/School/UC Davis/Bicycle Mechanics/BicycleParameters/data/'
benchmark = bp.Bicycle('Benchmark', pathToData)
benchmarkPar = bp.io.remove_uncertainties(benchmark.parameters['Benchmark'])
# convert to my parameter set
moorePar = bicycle.benchmark_to_moore(benchmarkPar, oldMassCenter=False)
moorePar['mg'] = moorePar['mf']
moorePar['ig11'] = moorePar['if11']
moorePar['ig22'] = moorePar['if22']
gyrobike.set_parameters(moorePar)

# set the equilibrium point
speedNaught = 0.5
pitchAngle = bicycle.pitch_from_roll_and_steer(0., 0., moorePar['rF'], moorePar['rR'],
        moorePar['d1'], moorePar['d2'], moorePar['d3'])
wheelAngSpeed = -speedNaught / moorePar['rR']
equilibrium = np.zeros(len(gyrobike.stateNames))
equilibrium[gyrobike.stateNames.index('q5')] = pitchAngle
equilibrium[gyrobike.stateNames.index('u6')] = wheelAngSpeed

equilibrium[gyrobike.stateNames.index('u9')] = 0.
gyrobike.linear(equilibrium)
start = 0.
stop = -10.0 / moorePar['rR']
off = gyrobike.plot_root_loci('u6', start, stop, num=50, axes='parameter',
        parts='real')
off.savefig('../../figures/extensions/gyrobike-flywheel-off.png')

equilibrium[gyrobike.stateNames.index('u9')] = -50.0
gyrobike.linear(equilibrium)
start = 0.
stop = -10.0 / moorePar['rR']
med = gyrobike.plot_root_loci('u6', start, stop, num=50, axes='parameter',
        parts='real')
med.savefig('../../figures/extensions/gyrobike-flywheel-medium.png')

equilibrium[gyrobike.stateNames.index('u9')] = -100.0
gyrobike.linear(equilibrium)
start = 0.
stop = -10.0 / moorePar['rR']
fast = gyrobike.plot_root_loci('u6', start, stop, num=50, axes='parameter',
        parts='real')
fast.savefig('../../figures/extensions/gyrobike-flywheel-fast.png')

#
equilibrium[gyrobike.stateNames.index('u6')] = wheelAngSpeed
gyrobike.linear(equilibrium)
start = 0.
stop = -300.
fast = gyrobike.plot_root_loci('u9', start, stop, num=50, axes='parameter',
        parts='real')
fast.savefig('../../figures/extensions/gyrobike-vary-flywheel.png')
