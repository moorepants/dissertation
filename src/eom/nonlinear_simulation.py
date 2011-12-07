#!/usr/bin/env python

# This reproduces Figure 4 in Meijaard 2007 with my model.

# dependencies
import numpy as np
import bicycleparameters as bp
from dtk import bicycle

# local dependencies
from Whipple import Whipple

# create the Whipple model (with my parameters)
whip = Whipple()

# load the benchmark parameters
pathToData='/media/Data/Documents/School/UC Davis/Bicycle Mechanics/BicycleParameters/data/'
benchmark = bp.Bicycle('Benchmark', pathToData)
benchmarkPar = bp.io.remove_uncertainties(benchmark.parameters['Benchmark'])
# convert to my parameter set
moorePar = bicycle.benchmark_to_moore(benchmarkPar, oldMassCenter=False)
# set the parameters
whip.parameters = moorePar

# set the initial conditions to match Meijaard2007
speedNaught = 4.6
rollRateNaught = 0.5
pitchAngle = bicycle.pitch_from_roll_and_steer(0., 0., moorePar['rF'], moorePar['rR'],
        moorePar['d1'], moorePar['d2'], moorePar['d3'])
# set up the simulation
whip.initialConditions = np.array([0.0] * 8 + [rollRateNaught, -speedNaught /
    moorePar['rR'], 0.0])
whip.initialConditions[whip.stateNames.index('q5')] = pitchAngle

# integration settings
ts = 0.01 # step size
tf = 5. # final time
whip.intOpts['ts'] = ts
whip.intOpts['tf'] = tf

whip.simulate()

# plot figure 4 from Meijaard2007 using my model
rollRate = whip.get_sim_output('u4')
speed = -whip.get_sim_output('u6') * whip.parameters['rR']
steerRate = whip.get_sim_output('u7')
time = whip.simResults['t']
newFig = bicycle.meijaard_figure_four(time, rollRate, steerRate, speed)
newFig.savefig('../../figures/eom/meijaard2007-figure-four.png', dpi=300)
