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

# create the Whipple model (with my parameters)
whip = WhippleMoorePar()

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
rollRate = whip.simResults['y'][:, whip.outputNames.index('u4')]
speed = -whip.simResults['y'][:, whip.outputNames.index('u6')] * whip.parameters['rR']
steerRate = whip.simResults['y'][:, whip.outputNames.index('u7')]
time = whip.simResults['t']
newFig = bicycle.meijaard_figure_four(time, rollRate, steerRate, speed)
newFig.savefig('../../figures/eom/meijaard2007-figure-four.png', dpi=300)

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

# see if my pitch angle caluculations are working
pitchAngle = bicycle.pitch_from_roll_and_steer(x[3], x[6], moorePar['rF'], moorePar['rR'],
        moorePar['d1'], moorePar['d2'], moorePar['d3'], guess=x[4])
print('This compares the pitch angle from BasuMandal2007 in my coordinate\
       frame with the pitch angle calculated from the BasuMandal2007 roll\
       and steer angle in my coordinate frame.')
print x[4], pitchAngle

# calculate the derivatives of the state using my model and compare it to
# BasuMandal2007
xd = whip.f(x, 0.)
y = whip.outputs(x)
basuOutput = bicycle.basu_table_one_output()
print('These are comparisons from BasuMandal2007 table one.')
print 'u4p =', xd[8], 'psidd =', basuOutput['psidd']
print 'u6p =', xd[9], 'betardd =', basuOutput['betardd']
print 'u7p =', xd[10], 'psifdd =', basuOutput['psifdd']
