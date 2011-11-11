#!/usr/bin/env python

# built in imports
import sys

# dependencies
import numpy as np
import matplotlib.pyplot as plt
import bicycleparameters as bp
from dtk import bicycle

# local dependencies
sys.path.append('/media/Data/Documents/School/UC Davis/Bicycle Mechanics/bicycle/alparse')
from models.WhippleIncremental.WhippleIncremental import WhippleIncremental

# load the benchmark parameters
pathToData='/media/Data/Documents/School/UC Davis/Bicycle Mechanics/BicycleParameters/data/'
benchmark = bp.Bicycle('Benchmark', pathToData)
benchmarkPar = bp.io.remove_uncertainties(benchmark.parameters['Benchmark'])
moorePar = bicycle.benchmark_whipple_to_moore_whipple(benchmarkPar, oldMassCenter=True)

# couple of extra parameters
gravity = 9.81
moorePar['g'] = gravity

# initial conditions if other than zero
speedNaught = 4.6
rollRateNaught = 0.5

# integration settings
ts = 0.01 # step size
tf = 5. # final time

#### create the whipple model
whip = WhippleIncremental()

# set up the simulation
whip.parameters = moorePar
whip.initialConditions = np.array([0.0] * 8 + [rollRateNaught, -speedNaught /
    moorePar['rR'], 0.0])
whip.initialConditions[whip.stateNames.index('q5')] = benchmarkPar['lam']
whip.intOpts['ts'] = ts
whip.intOpts['tf'] = tf

whip.simulate()

# plot figure 4 from Meijaard2007
rollRate = whip.simResults['y'][:, whip.outputNames.index('u4')]
speed = -whip.simResults['y'][:, whip.outputNames.index('u6')] * whip.parameters['rR']
steerRate = whip.simResults['y'][:, whip.outputNames.index('u7')]
time = whip.simResults['t']
newFig = bicycle.meijaard_figure_four(time, rollRate, steerRate, speed)

plt.show()
