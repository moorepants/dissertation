#!/usr/env python

# Compare the frequency response of the identified models

import sys
sys.path.append('..')
from load_paths import read
import cPickle

import numpy as np
import matplotlib.pyplot as plt
from dtk import bicycle, control

pathToIdMat = read('pathToIdMat')

with open(pathToIdMat) as f:
    idMat = cPickle.load(f)

inputNames = ['$T_\phi$', '$T_\delta$']
stateNames = ['$\phi$', '$\delta$', '$\dot{\phi}$', '$\dot{\delta}$']
outputNames = ['$\phi$', '$\delta$']

C = np.array([[1.0, 0.0, 0.0, 0.0],
              [0.0, 1.0, 0.0, 0.0]])
D = np.array([[0.0, 0.0],
              [0.0, 0.0]])


speeds = [2.0, 5.5, 9.0]

linestyles = ['-'] * 3 + ['--'] * 3 + ['-.'] * 3 + [':'] * 3

sysNames = sorted(idMat.keys())

for speed in speeds:
    systems = []
    for k in sysNames:

        M, C1, K0, K2, H = idMat[k]
        A, B = bicycle.benchmark_state_space(M, C1, K0, K2, speed, 9.81)

        systems.append(control.StateSpace(A, B, C, D, name=k,
            stateNames=stateNames, inputNames=inputNames, outputNames=outputNames))

    w = np.logspace(-1, 2)

    bode = control.Bode(w, *systems, linestyles=linestyles)
    bode.plot()

    for f in bode.figs:
        leg = f.phaseAx.legend(loc=4)
        plt.setp(leg.get_texts(), fontsize='6.0') #'xx-small')
    bode.figs[2].savefig('../../figures/systemidentification/compare-id-bode-{}.png'.format(speed))
