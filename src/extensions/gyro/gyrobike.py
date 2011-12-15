#!/usr/bin/env python

# dependencies
import bicycleparameters as bp
from dtk import bicycle

# local dependencies
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
speedNaught = 4.6
rollRateNaught = 0.5
pitchAngle = bicycle.pitch_from_roll_and_steer(0., 0., moorePar['rf'], moorePar['rr'],
        moorePar['d1'], moorePar['d2'], moorePar['d3'])
wheelAngSpeed = -speedNaught / moorePar['rr']
gyroNonLinear.initialConditions[gyroNonLinear.stateNames.index('q5')] = pitchAngle
gyroNonLinear.initialConditions[gyroNonLinear.stateNames.index('u4')] = rollRateNaught
gyroNonLinear.initialConditions[gyroNonLinear.stateNames.index('u6')] = wheelAngSpeed
gyroNonLinear.initialConditions[gyroNonLinear.stateNames.index('u9')] = 4 * wheelAngSpeed
print 4 * wheelAngSpeed

# integration settings
ts = 0.01 # step size
tf = 5. # final time
gyroNonLinear.intOpts['ts'] = ts
gyroNonLinear.intOpts['tf'] = tf

gyroNonLinear.simulate()

# plot figure 4 from Meijaard2007 using my model
rollRate = gyroNonLinear.simResults['y'][:, gyroNonLinear.outputNames.index('u4')]
speed = -gyroNonLinear.simResults['y'][:, gyroNonLinear.outputNames.index('u6')] * gyroNonLinear.parameters['rr']
steerrate = gyroNonLinear.simResults['y'][:, gyroNonLinear.outputNames.index('u7')]
time = gyroNonLinear.simResults['t']
newFig = bicycle.meijaard_figure_four(time, rollRate, steerrate, speed)
newFig.savefig('../../../figures/extensions/gyro-nonlin-sim.png', dpi=300)
