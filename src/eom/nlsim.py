#!/usr/bin/env python

# built in imports
import sys

# dependencies
import numpy as np
import matplotlib.pyplot as plt
import bicycleparameters as bp

# local dependencies
from dtk.bicycle import (benchmark_whipple_to_moore_whipple,
    pitch_from_roll_and_steer, basu_to_moore_input, basu_table_one_input,
    basu_table_one_output)
sys.path.append('/media/Data/Documents/School/UC Davis/Bicycle Mechanics/bicycle/alparse')
from models.WhippleMoorePar.WhippleMoorePar import WhippleMoorePar
from models.Whipple.Whipple import Whipple

def meijaard_figure_four(time, rollRate, steerRate, speed):
    width = 3.0 # inches
    golden_ratio = (np.sqrt(5.0) - 1.0) / 2.0
    height = width * golden_ratio
    fig = plt.figure()
    fig.set_figsize_inches([width, height])
    fig.subplots_adjust(right=0.75)
    rateAxis = fig.add_subplot(111)
    speedAxis = rateAxis.twinx()

    p1, = rateAxis.plot(time, rollRate, "k--",label="Roll Rate")
    p2, = rateAxis.plot(time, steerRate, "k:", label="Steer Rate")
    p3, = speedAxis.plot(time, speed, "k-", label="Speed")

    rateAxis.set_ylim(-0.5, 1.0)
    rateAxis.set_yticks([-0.5, 0.0, 0.5, 1.0])
    rateAxis.set_xticks([0., 1., 2., 3., 4., 5.])
    rateAxis.set_xlabel('Time [sec]')
    rateAxis.set_ylabel('Angular Rate [rad/sec]')
    lines = [p1, p2, p3]
    rateAxis.legend(lines, [l.get_label() for l in lines])
    speedAxis.set_ylim(4.55, 4.7)
    speedAxis.set_yticks([4.55, 4.60, 4.65, 4.70])
    speedAxis.set_ylabel('Speed [m/s]')

    return fig

# load the benchmark parameters
pathToData='/media/Data/Documents/School/UC Davis/Bicycle Mechanics/BicycleParameters/data/'
benchmark = bp.Bicycle('Benchmark', pathToData)
benchmarkPar = bp.io.remove_uncertainties(benchmark.parameters['Benchmark'])

# couple of extra parameters
gravity = 9.81

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

###whipOld.simulate()
###
#### plot figure 4 from Meijaard2007
###rollRate = whipOld.simResults['y'][:, 11]
###speed = -whipOld.simResults['y'][:, 13] * whipOld.parameters['rR']
###steerRate = whipOld.simResults['y'][:, 14]
###time = whipOld.simResults['t']
###
###oldFig = meijaard_figure_four(time, rollRate, steerRate, speed)

## new Whipple model with the Moore parameters ##

# calculate the moore2012 parameters
moorePar = benchmark_whipple_to_moore_whipple(benchmarkPar, oldMassCenter=False)
moorePar['g'] = 9.81

for k, v in moorePar.items():
    if k.startswith('m'):
        print k, whipOld.parameters['mass' + k[-1]], v
    else:
        print k, whipOld.parameters[k], v

# create the whipple model
whip = WhippleMoorePar()

# set up the simulation
whip.parameters = moorePar

whip.initialConditions = np.array([0.] * 8 + [rollRateNaught, -speedNaught / moorePar['rR'], 0.])
# this is only valid for roll and steer equal to zero
pitchAngle = pitch_from_roll_and_steer(0., 0., moorePar['rF'], moorePar['rR'],
        moorePar['d1'], moorePar['d2'], moorePar['d3'])
whip.initialConditions[4] = pitchAngle

whip.intOpts['ts'] = ts
whip.intOpts['tf'] = tf

whip.simulate()

# plot figure 4 from Meijaard2007
rollRate = whip.simResults['y'][:, whip.outputNames.index('u4')]
speed = -whip.simResults['y'][:, whip.outputNames.index('u6')] * whip.parameters['rR']
steerRate = whip.simResults['y'][:, whip.outputNames.index('u7')]
time = whip.simResults['t']
newFig = meijaard_figure_four(time, rollRate, steerRate, speed)

plt.show()

# load the input values specified in table one of Basu-Mandal2007
basuInput = basu_table_one_input()
# convert the values to my coordinates and speeds
mooreInput = basu_to_moore_input(basuInput, benchmarkPar['rR'],
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
pitchAngle = pitch_from_roll_and_steer(x[3], x[6], moorePar['rF'], moorePar['rR'],
        moorePar['d1'], moorePar['d2'], moorePar['d3'])
print x[4], pitchAngle

xd = whip.f(x, 0.)
y = whip.outputs(x)
basuOutput = basu_table_one_output()
print xd
print xd[8], basuOutput['psidd']
print xd[9], basuOutput['betardd']
print xd[10], basuOutput['psifdd']
