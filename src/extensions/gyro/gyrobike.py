#!/usr/bin/env python

# This file generates a non-linear simulation of the GyroBike at low speeds and
# plots the results.

import pickle
from numpy import pi, sqrt
import matplotlib.pyplot as plt
import bicycleparameters as bp
from dtk import bicycle

try:
    # this file should be deleted if you want to force the simulation
    f = open('../../../data/extensions/gyrobikedata.p', 'r')
except IOError:
    try:
        f = open('GyroBike.py', 'r')
    except IOError:
        from altk import alparse
        alparse.alparse('GyroBike', 'GyroBike', code='Python')
    else:
        f.close()
        del f

    from GyroBike import GyroBike

    # create the Whipple model (with my parameters)
    gyroNonLinear = GyroBike()

    # load the benchmark parameters
    pathToData='/media/Data/Documents/School/UC Davis/Bicycle Mechanics/BicycleParameters/data/'
    gyro = bp.Bicycle('Gyro', pathToData, forceRawCalc=True)
    gyro.add_rider('Child', reCalc=True)
    benchmarkPar = bp.io.remove_uncertainties(gyro.parameters['Benchmark'])
    # convert to my parameter set
    moorePar = bicycle.benchmark_to_moore(benchmarkPar, oldMassCenter=False)
    moorePar['mg'] = benchmarkPar['mD']
    moorePar['ig11'] = benchmarkPar['IDxx']
    moorePar['ig22'] = benchmarkPar['IDyy']
    gyroNonLinear.set_parameters(moorePar)

    # set the initial conditions to match Meijaard2007
    speedNaught = 0.5
    rollRateNaught = 0.5
    pitchAngle = bicycle.pitch_from_roll_and_steer(0., 0., moorePar['rf'], moorePar['rr'],
            moorePar['d1'], moorePar['d2'], moorePar['d3'])
    wheelAngSpeed = -speedNaught / moorePar['rr']
    gyroNonLinear.initialConditions[gyroNonLinear.stateNames.index('q5')] = pitchAngle
    gyroNonLinear.initialConditions[gyroNonLinear.stateNames.index('u4')] = rollRateNaught
    gyroNonLinear.initialConditions[gyroNonLinear.stateNames.index('u6')] = wheelAngSpeed
    gyroNonLinear.initialConditions[gyroNonLinear.stateNames.index('u9')] = -5000. / 60. * 2 * pi

    # integration settings
    ts = 0.01 # step size
    tf = 5. # final time
    gyroNonLinear.intOpts['ts'] = ts
    gyroNonLinear.intOpts['tf'] = tf

    gyroNonLinear.simulate()

    # There is currenlty a bug in which the parameters do not get saved with
    # the gyroNonLinear object. Maybe they need to be copied or something...
    with open('../../../data/extensions/gyrobikedata.p', 'w') as f:
        pickle.dump(gyroNonLinear, f)
else:
    with open('../../../data/extensions/gyrobikedata.p', 'r') as f:
        gyroNonLinear = pickle.load(f)

# grab the interesting variables
rollRate = gyroNonLinear.get_sim_output('u4')
speed = -gyroNonLinear.get_sim_output('u6') * gyroNonLinear.parameters['rr']
steerRate = gyroNonLinear.get_sim_output('u7')
flywheelRate = gyroNonLinear.get_sim_output('u9') * -60. / 2. / pi
time = gyroNonLinear.simResults['t']

width = 5.0 # inches
golden_ratio = (sqrt(5.0) - 1.0) / 2.0
height = width * golden_ratio
fig = plt.figure()
fig.set_size_inches([width, height])
params = {'backend': 'ps',
          'axes.labelsize': 10,
          'text.fontsize': 10,
          'legend.fontsize': 8,
          'xtick.labelsize': 8,
          'ytick.labelsize': 8,
          'text.usetex': True}
plt.rcParams.update(params)

fig.subplots_adjust(right=0.85, left=0.15, bottom=0.15)

rateAxis = fig.add_subplot(2, 1, 1)
speedAxis = fig.add_subplot(2, 1, 2)
flywheelAxis = speedAxis.twinx()

p1, = rateAxis.plot(time, rollRate, "k-",label="$u_4$")
p2, = rateAxis.plot(time, steerRate, "k:", label="$u_7$")
p3, = speedAxis.plot(time, speed, "k-", label="$v$")
p4, = flywheelAxis.plot(time, flywheelRate, "k:", label="$-u_9$")

rateAxis.set_ylabel('Angular Rate [rad/sec]')
rateAxis.legend()

speedAxis.set_ylabel('Speed [m/s]')
speedAxis.set_xlabel('Time [sec]')
flywheelAxis.set_ylabel('Angular Rate [rpm]')
lines = [p3, p4]
speedAxis.legend(lines, [l.get_label() for l in lines], loc=4)

fig.savefig('../../../figures/extensions/gyro-nonlin-sim.png', dpi=300)
fig.savefig('../../../figures/extensions/gyro-nonlin-sim.pdf')
