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
from models.WhippleMoorePar.WhippleMoorePar import WhippleMoorePar
from models.Whipple.Whipple import Whipple

# load the benchmark parameters
pathToData='/media/Data/Documents/School/UC Davis/Bicycle Mechanics/BicycleParameters/data/'
benchmark = bp.Bicycle('Benchmark', pathToData)
benchmarkPar = bp.io.remove_uncertainties(benchmark.parameters['Benchmark'])

# initial conditions if other than zero
speedNaught = 4.6
rollRateNaught = 0.5

# integration settings
ts = 0.01 # step size
tf = 5. # final time

## orginal working whipple model that I created##

# create my original working whipple model
whipOld = Whipple()

# set up the simulation
whipOld.initialConditions = np.array([0.0] * 8 + [rollRateNaught, -speedNaught /
    benchmarkPar['rR'], 0.0])

whipOld.intOpts['ts'] = ts
whipOld.intOpts['tf'] = tf

whipOld.simulate()

# plot figure 4 from Meijaard2007
rollRate = whipOld.simResults['y'][:, 11]
speed = -whipOld.simResults['y'][:, 13] * whipOld.parameters['rR']
steerRate = whipOld.simResults['y'][:, 14]
time = whipOld.simResults['t']

oldFig = bicycle.meijaard_figure_four(time, rollRate, steerRate, speed)

## new Whipple model with the Moore parameters ##

# calculate the moore2012 parameters and compare them with the same parameters
# that are computed from the original working autolev code
moorePar = bicycle.benchmark_to_moore(benchmarkPar, oldMassCenter=True)

for k, v in moorePar.items():
    if k.startswith('m'):
        print k, whipOld.parameters['mass' + k[-1]], v
        np.testing.assert_almost_equal(whipOld.parameters['mass' + k[-1]], v)
    else:
        print k, whipOld.parameters[k], v
        np.testing.assert_almost_equal(whipOld.parameters[k], v)

# now output the parameter set with the location of the fork center of
# mass redefined from the front wheel center
moorePar = bicycle.benchmark_to_moore(benchmarkPar, oldMassCenter=False)

# create the whipple model
whip = WhippleMoorePar()

# set up the simulation
whip.parameters = moorePar
whip.initialConditions = np.array([0.0] * 8 + [rollRateNaught, -speedNaught /
    moorePar['rR'], 0.0])
# Nominal pitch for the WhippleMoorePar is equal to the steer axis tilt
# this is only valid for roll and steer equal to zero
pitchAngle = bicycle.pitch_from_roll_and_steer(0., 0., moorePar['rF'], moorePar['rR'],
        moorePar['d1'], moorePar['d2'], moorePar['d3'])
whip.initialConditions[whip.stateNames.index('q5')] = pitchAngle
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

# load the input values specified in table one of Basu-Mandal2007
basuInput = bicycle.basu_table_one_input()
# convert the values to my coordinates and speeds
mooreInput = bicycle.basu_to_moore_input(basuInput, benchmarkPar['rR'],
    benchmarkPar['lam'])
# store them in a state array
x = np.zeros(11)
x[0] = mooreInput['q1']
x[1] = mooreInput['q2']
x[2] = mooreInput['q3']
x[3] = mooreInput['q4']
x[4] = mooreInput['q5']
x[5] = mooreInput['q6']
x[6] = mooreInput['q7']
x[7] = mooreInput['q8']
x[8] = mooreInput['u4']
x[9] = mooreInput['u6']
x[10] = mooreInput['u7']
pitchAngle = bicycle.pitch_from_roll_and_steer(x[3], x[6], moorePar['rF'], moorePar['rR'],
        moorePar['d1'], moorePar['d2'], moorePar['d3'])
print x[4], pitchAngle

xd = whip.f(x, 0.)
y = whip.outputs(x)
basuOutput = bicycle.basu_table_one_output()
print xd
print xd[8], basuOutput['psidd']
print xd[9], basuOutput['betardd']
print xd[10], basuOutput['psifdd']
