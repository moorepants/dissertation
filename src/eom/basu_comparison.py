#!/usr/bin/env python

# This file computes the derivatives of the coordinates and speeds for a single
# state provided by Table 1 in BasuMandall2007 with my model and compares the
# results.

# built in imports
import sys

# dependencies
import numpy as np
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
whip.constants() # make sure the constants are recalculated with the new parameters

# load the input values specified in table one of Basu-Mandal2007
basuInput = bicycle.basu_table_one_input()
# convert the values to my coordinates and speeds
mooreInput = bicycle.basu_to_moore_input(basuInput, benchmarkPar['rR'],
        benchmarkPar['lam'])
# store them in a state array
x = np.array([mooreInput[x] for x in whip.stateNames])

# see if my pitch angle calculations are working
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
mooreOutput = {k : v for k, v in zip(whip.outputNames, y)}
mooreOutputBasu = bicycle.moore_to_basu(mooreOutput, benchmarkPar['rR'], benchmarkPar['lam'])
basuOutput = bicycle.basu_table_one_output()
sigFigs = bicycle.basu_sig_figs()
print('These are comparisons from BasuMandal2007 table one.')
# make an rst list table
table = """.. list-table:: Nonlinear Whipple Model Comparision
   :header-rows: 1

   * - Variable
     - Basu-Mandal
     - Moore\n"""
variables = basuInput.keys() + basuOutput.keys()
variables.sort()

def rst_math(s):
    mapping = {'x': r'x',
               'y': r'y',
               'z': r'z',
               'theta': r'\theta',
               'psi': r'\psi',
               'phi': r'\phi',
               'psif': r'\psi_f',
               'betar': r'\beta_r',
               'betaf': r'\beta_f'}
    if s.endswith('dd'):
        s = r'\ddot{' + mapping[s[:-2]] + '}'
    elif s.endswith('d'):
        s = r'\dot{' + mapping[s[:-1]] + '}'
    else:
        s = mapping[s]

    return ':math:`' + s + '`'

for v in variables:
    sig = '%1.' + str(sigFigs[v] - 1) + 'e'
    try:
        basu = basuOutput[v]
    except KeyError:
        basu = basuInput[v]
    finally:
        if basu == 0:
            basu = '0'
            moore = '0'
        else:
            basu = sig % basu
            moore = sig % mooreOutputBasu[v]
    if basu.endswith('e+00'):
        basu = basu[:-4]
    if moore.endswith('e+00'):
        moore = moore[:-4]
    table += (' ' * 3 + '* - ' + rst_math(v) + '\n' + ' ' * 5 + '- ' + basu +
        '\n' + ' ' * 5 + '- ' + moore + '\n')

print table
