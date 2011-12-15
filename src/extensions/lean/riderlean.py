#!/usr/bin/env python

# dependencies
import numpy as np
import bicycleparameters as bp
from dtk import bicycle

# local dependencies
try:
    f = open('RiderLean.py', 'r')
except IOError:
    from altk import alparse
    alparse.alparse('RiderLean', 'RiderLean', code='Python')
else:
    f.close()
    del f

from RiderLean import LinearRiderLean

# create the linear bike model
bike = LinearRiderLean()

# load the benchmark parameters
pathToData='/media/Data/Documents/School/UC Davis/Bicycle Mechanics/BicycleParameters/data/'
bikeWithLegs = bp.Bicycle('Browserlegs', pathToData)
#bikeWithLegs = bp.Bicycle('Lukelegs', pathToData)
benchmarkPar = bp.io.remove_uncertainties(bikeWithLegs.parameters['Benchmark'])

# convert to my parameter set
moorePar = bicycle.benchmark_to_moore(benchmarkPar, oldMassCenter=False)
pitchAngle = bicycle.pitch_from_roll_and_steer(0., 0., moorePar['rf'], moorePar['rr'],
        moorePar['d1'], moorePar['d2'], moorePar['d3'])

# from my inertia model
moorePar['d4'] = -1.011421527346159 + moorePar['rr']
moorePar['l5'] = 0.231223496809401
moorePar['l6'] = -1.283035074598082 + moorePar['rr'] - moorePar['d4']
moorePar['lam'] = pitchAngle
moorePar['mg'] = 48.816
moorePar['ig11'] = 2.038073562525466
moorePar['ig22'] = 1.692108544034995
moorePar['ig33'] = 1.100753962972129
moorePar['ig31'] = 0.002113501449812
moorePar['k9'] = 0.0 #128.0
moorePar['c9'] = 0.0 #50.0
# from luke's paper
#moorePar['d4'] = -0.9 + moorePar['rr']
#moorePar['l5'] = 0.27
#moorePar['l6'] = -0.99 + moorePar['rr'] - moorePar['d4']
#moorePar['lam'] = pitchAngle
#moorePar['mg'] = 51.0
#moorePar['ig11'] = 4.299
#moorePar['ig22'] = 5.186
#moorePar['ig33'] = 1.413
#moorePar['ig31'] = 1.444
#moorePar['k9'] = 0.0
#moorePar['c9'] = 0.0
bike.set_parameters(moorePar)

# set the equilibrium point
speedNaught = 5.0
pitchAngle = bicycle.pitch_from_roll_and_steer(0., 0., moorePar['rf'], moorePar['rr'],
        moorePar['d1'], moorePar['d2'], moorePar['d3'])
wheelAngSpeed = -speedNaught / moorePar['rr']
equilibrium = np.zeros(len(bike.stateNames))
equilibrium[bike.stateNames.index('q5')] = pitchAngle
equilibrium[bike.stateNames.index('u6')] = wheelAngSpeed
bike.linear(equilibrium)

settings = {'num':100,
            'axes':'parameter',
            'pub':True,
            #'ylim':(-10, 10),
            'width':5.0}

# plot a root loci
start = 0.
stop = -10.0 / moorePar['rr']
free = bike.plot_root_loci('u6', start, stop,
        factor=('v', -moorePar['rr']), units='m/s', **settings)
free.savefig('../../../figures/extensions/rider-lean.png', dpi=200)

moorePar['k9'] = 128.0
moorePar['c9'] = 50.0
bike.set_parameters(moorePar)
bike.linear(equilibrium)
# plot a root loci
start = 0.
stop = -10.0 / moorePar['rr']
free = bike.plot_root_loci('u6', start, stop,
        factor=('v', -moorePar['rr']), units='m/s', **settings)
free.savefig('../../../figures/extensions/rider-lean-damp-stiff.png', dpi=200)
