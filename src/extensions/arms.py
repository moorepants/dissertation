from numpy.linalg import norm
from math import sin, cos
from scipy import io
import bicycleparameters as bp
from dtk import bicycle

pathToParameters = '/media/Data/Documents/School/UC Davis/Bicycle Mechanics/BicycleParameters/data'

# load the rigid bicycle and seat Jason on it
rigidWithRider = bp.Bicycle('Rigid', forceRawCalc=True, pathToData=pathToParameters)
rigidWithRider.add_rider('Jason', reCalc=True)
h = rigidWithRider.human

# find the inertia of the humans without arms, this is with respect to the
# benchmark coordinate system and about the CoM of the subset of parts
humanMass, humanCoM, humanInertia = h.combine_inertia(('P', 'T', 'C', 'K1', 'K2', 'J1', 'J2'))
riderPar = {'IBxx': humanInertia[0, 0],
            'IByy': humanInertia[1, 1],
            'IBzz': humanInertia[2, 2],
            'IBxz': humanInertia[2, 0],
            'mB': humanMass,
            'xB': humanCoM[0][0],
            'yB': humanCoM[1][0],
            'zB': humanCoM[2][0]}

rigid = bp.Bicycle('Rigid', forceRawCalc=True, pathToData=pathToParameters)
benchmark = bp.rider.combine_bike_rider(rigid.parameters['Benchmark'], riderPar)
benchmark = bp.io.remove_uncertainties(benchmark)
par = bicycle.benchmark_to_moore(benchmark)

# get the arm parameters
# note that the right and left arms have the same parameters due to symmetry, I
# should probably reduce the number of parameters in the analytical model to
# reflect this

# right upper arm, G
par['mg'] = h.B1.Mass
par['l4'] = h.B1.relCOM[2][0]
IG = h.B1.relInertia
par['ig11'] = IG[0, 0]
par['ig33'] = IG[2, 2]
par['d6'] = (h.B1.pos[0, 0] * cos(benchmark['lam']) - h.B1.pos[2, 0] * sin(benchmark['lam']) -
        benchmark['rR'] * sin(benchmark['lam']))
par['d7'] = abs(h.B1.pos[1, 0])
par['d8'] = (h.B1.pos[0, 0] * sin(benchmark['lam']) + h.B1.pos[2, 0] * cos(benchmark['lam']) +
        benchmark['rR'] * cos(benchmark['lam']))
par['d12'] = h.B1.length

# right lower arm, H
par['mh'] = h.B2.Mass
par['l5'] = h.B2.relCOM[2][0]
IH = h.B2.relInertia
par['ih11'] = IH[0, 0]
par['ih33'] = IH[2, 2]
knuckle = h.b[6].pos
par['d11'] = ((knuckle[2, 0] + benchmark['rF']) * cos(benchmark['lam']) +
        (knuckle[0, 0] - benchmark['w'])
            * sin(benchmark['lam']))
par['d9'] = ((knuckle[0, 0] - benchmark['w'] - par['d11'] * sin(benchmark['lam'])) /
            cos(benchmark['lam']))
par['d10'] = abs(knuckle[1, 0])
par['d13'] = norm(knuckle - h.B2.pos)

# left upper arm, I
par['mi'] = h.A1.Mass
II = h.A1.relInertia
par['ii11'] = II[0, 0]
par['ii33'] = II[2, 2]

# left lower arm, J
par['mj'] = h.A2.Mass
IJ = h.A2.relInertia
par['ij11'] = IJ[0, 0]
par['ij33'] = IJ[2, 2]

# now get some guesses for the arm angles at the nominal configuration

q = {}

# right arm
q['q9'] = h.CFG['CB1abduction']
q['q10'] = h.CFG['CB1elevation']
q['q11'] = h.CFG['CB1rotation']
q['q12'] = h.CFG['B1B2flexion']

# left arm
q['q13'] = h.CFG['CA1abduction']
q['q14'] = h.CFG['CA1elevation']
q['q15'] = h.CFG['CA1rotation']
q['q16'] = h.CFG['A1A2flexion']

io.savemat('armspar.mat', par)
io.savemat('armsinit.mat', q)
