#!/usr/bin/env python

# built in imports
import sys

# other packages
import numpy as np
import bicycleparameters as bp
from dtk.bicycle import (benchmark_whipple_to_moore_whipple,
    pitch_from_roll_and_steer)

sys.path.append('/media/Data/Documents/School/UC Davis/Bicycle Mechanics/bicycle/alparse')
from models.WhippleMoorePar.WhippleMoorePar import WhippleMoorePar

# load the benchmark parameters
benchmark = bp.Bicycle('Benchmark', pathToData='/media/Data/Documents/School/UC Davis/Bicycle Mechanics/BicycleParameters/data/')
benchmarkPar = bp.io.remove_uncertainties(benchmark.parameters['Benchmark'])

# calculate the moore2012 parameters
moorePar = benchmark_whipple_to_moore_whipple(benchmarkPar)
moorePar['g'] = 9.81

# create the whipple model
whip = WhippleMoorePar()

# set up the simulation
whip.parameters = moorePar
whip.initialConditions = np.array([0.] * 8 + [0.5, -5. / moorePar['rR'], 0.])
# this is only valid for roll and steer equal to zero
pitchAngle = pitch_from_roll_and_steer(0., 0., moorePar['rF'], moorePar['rR'],
        moorePar['d1'], moorePar['d2'], moorePar['d3'])
whip.initialConditions[4] = pitchAngle

whip.intOpts['ts'] = 0.01
whip.intOpts['tf'] = 3.

whip.simulate()

whip.plot()
