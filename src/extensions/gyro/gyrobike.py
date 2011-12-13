#!/usr/bin/env python

# built in imports
import sys

# dependencies
import numpy as np
import bicycleparameters as bp
from dtk import bicycle

# local dependencies
sys.path.append('/media/Data/Documents/School/UC Davis/Bicycle Mechanics/bicycle/alparse')
from models.GyroBike.GyroBike import GyroBike, LinearGyroBike

# create the Whipple model (with my parameters)
gyroNonLinear = GyroBike()

# load the benchmark parameters
pathToData='/media/Data/Documents/School/UC Davis/Bicycle Mechanics/BicycleParameters/data/'
benchmark = bp.Bicycle('Benchmark', pathToData)
benchmarkPar = bp.io.remove_uncertainties(benchmark.parameters['Benchmark'])
# convert to my parameter set
moorePar = bicycle.benchmark_to_moore(benchmarkPar, oldMassCenter=False)
moorePar['mg'] = moorePar['mf']
moorePar['ig11'] = moorePar['if11']
moorePar['ig22'] = moorePar['if22']
gyroNonLinear.set_parameters(moorePar)

# set the initial conditions to match Meijaard2007
speedNaught = 0.5 #4.6
rollRateNaught = 0.5
pitchAngle = bicycle.pitch_from_roll_and_steer(0., 0., moorePar['rF'], moorePar['rR'],
        moorePar['d1'], moorePar['d2'], moorePar['d3'])
wheelAngSpeed = -speedNaught / moorePar['rR']
gyroNonLinear.initialConditions[gyroNonLinear.stateNames.index('q5')] = pitchAngle
gyroNonLinear.initialConditions[gyroNonLinear.stateNames.index('u4')] = rollRateNaught
gyroNonLinear.initialConditions[gyroNonLinear.stateNames.index('u6')] = wheelAngSpeed
gyroNonLinear.initialConditions[gyroNonLinear.stateNames.index('u9')] = 0.5 * wheelAngSpeed

# integration settings
ts = 0.01 # step size
tf = 5. # final time
gyroNonLinear.intOpts['ts'] = ts
gyroNonLinear.intOpts['tf'] = tf

gyroNonLinear.simulate()

# plot figure 4 from Meijaard2007 using my model
rollRate = gyroNonLinear.simResults['y'][:, gyroNonLinear.outputNames.index('u4')]
speed = -gyroNonLinear.simResults['y'][:, gyroNonLinear.outputNames.index('u6')] * gyroNonLinear.parameters['rR']
steerRate = gyroNonLinear.simResults['y'][:, gyroNonLinear.outputNames.index('u7')]
time = gyroNonLinear.simResults['t']
newFig = bicycle.meijaard_figure_four(time, rollRate, steerRate, speed)
newFig.savefig('../../figures/extensions/gyro-nonlin-sim.png', dpi=300)

#
equilibrium = np.zeros(len(gyroNonLinear.stateNames))
equilibrium[gyroNonLinear.stateNames.index('q5')] = pitchAngle
equilibrium[gyroNonLinear.stateNames.index('u6')] = wheelAngSpeed
#equilibrium[gyroNonLinear.stateNames.index('u9')] = 0.5 * wheelAngSpeed
gyroLin = LinearGyroBike()
gyroLin.linear(equilibrium)
