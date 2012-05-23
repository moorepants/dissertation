#!/usr/bin/env python

# dependencies
import numpy as np
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

from GyroBike import LinearGyroBike

# create the linear gyrobike model
gyrobike = LinearGyroBike()

# create the gyro bike
pathToData='/media/Data/Documents/School/UC Davis/Bicycle Mechanics/BicycleParameters/data/'
gyro = bp.Bicycle('Gyro', pathToData, forceRawCalc=True)

# set the model parameters
benchmarkPar = bp.io.remove_uncertainties(gyro.parameters['Benchmark'])
moorePar = bicycle.benchmark_to_moore(benchmarkPar)
moorePar['mg'] = benchmarkPar['mD']
moorePar['ig11'] = benchmarkPar['IDxx']
moorePar['ig22'] = benchmarkPar['IDyy']
gyrobike.set_parameters(moorePar)

# set the default equilibrium point
speedNaught = 0.5 # just over 1 mph, really slow walking
pitchAngle = bicycle.pitch_from_roll_and_steer(0., 0., moorePar['rf'],
        moorePar['rr'], moorePar['d1'], moorePar['d2'], moorePar['d3'])
wheelAngSpeed = -speedNaught / moorePar['rr']
equilibrium = np.zeros(len(gyrobike.stateNames))
equilibrium[gyrobike.stateNames.index('q5')] = pitchAngle
equilibrium[gyrobike.stateNames.index('u6')] = wheelAngSpeed

figDir = '../../../figures/extensions/'

settings = {'num':100,
            'axes':'parameter',
            'pub':True,
            'ylim':(-10, 10),
            'width':5.0}

# generate a root locus with respect to speed for a baseline
gyrobike.linear(equilibrium)
start = 0.
stop = -10.0 / moorePar['rr']
flywheelOff = gyrobike.plot_root_locus('u6', start, stop, factor=('v',
    -moorePar['rr']), units='m/s', **settings)
flywheelOff.savefig(figDir + 'gyrobike-flywheel-off.png', dpi=200)

# now generate a root locus with respect to flywheel speed
gyrobike.linear(equilibrium)
start = 0.
stop = -10000. / 60. * 2 * np.pi
flywheelOn = gyrobike.plot_root_locus('u9', start, stop, factor=('$u_9$', -60. /
    2 / np.pi), units='rpm', **settings)
flywheelOn.savefig(figDir + 'gyrobike-vary-flywheel.png', dpi=200)

# create the same graphs but with a rider
# warning, as of now the arms are not properly set for this bicycle
gyro.add_rider('Child')
benchmarkPar = bp.io.remove_uncertainties(gyro.parameters['Benchmark'])
moorePar = bicycle.benchmark_to_moore(benchmarkPar)
moorePar['mg'] = benchmarkPar['mD']
moorePar['ig11'] = benchmarkPar['IDxx']
moorePar['ig22'] = benchmarkPar['IDyy']
gyrobike.set_parameters(moorePar)

# generate a root locus with respect to speed for a baseline
gyrobike.linear(equilibrium)
start = 0.
stop = -10.0 / moorePar['rr']
flywheelOffRider = gyrobike.plot_root_locus('u6', start, stop, factor=('v',
    -moorePar['rr']), units='m/s', **settings)
flywheelOffRider.savefig(figDir + 'gyrobike-flywheel-off-rider.png', dpi=200)

# now generate a root locus with respect to flywheel speed
gyrobike.linear(equilibrium)
start = 0.
stop = -10000. / 60. * 2 * np.pi
flywheelOnRider = gyrobike.plot_root_locus('u9', start, stop, factor=('$u_9$', -60. /
    2 / np.pi), units='rpm',  **settings)
flywheelOnRider.savefig(figDir + 'gyrobike-vary-flywheel-rider.png', dpi=200)
