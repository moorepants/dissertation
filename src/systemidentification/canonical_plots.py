import sys
sys.path.append('..')
from load_paths import read
import cPickle

import numpy as np
from dtk import bicycle, control
from canonicalbicycleid import canonical_bicycle_id as cbi

pathToIdMat = read('pathToIdMat')

with open(pathToIdMat) as f:
    idMat = cPickle.load(f)

# First create all of the plots for the model identified from all riders and
# all environments.
allRiders = ['Charlie', 'Jason', 'Luke']
# load M, C1, K0, K2 for each rider
canon = cbi.load_benchmark_canon(allRiders)
# load the H lateral force vector for each rider
H = cbi.lateral_force_contribution(allRiders)

# Eigenvalues versus speed plot.
v0 = 0.
vf = 10.
num = 100

# identified for all rider and all environments
iM, iC1, iK0, iK2, iH = idMat['A-A']
speeds, iAs, iBs = bicycle.benchmark_state_space_vs_speed(iM, iC1, iK0, iK2,
        v0=v0, vf=vf, num=num)
w, v = control.eigen_vs_parameter(iAs)
iEigenvalues, iEigenvectors = control.sort_modes(w, v)

# whipple model (mean)
wM, wC1, wK0, wK2, wH = cbi.mean_canon(allRiders, canon, H)
speeds, wAs, wBs = bicycle.benchmark_state_space_vs_speed(wM, wC1, wK0, wK2,
        v0=v0, vf=vf, num=num)
w, v = control.eigen_vs_parameter(wAs)
wEigenvalues, wEigenvectors = control.sort_modes(w, v)

# arm model (mean)
aAs, aBs, aSpeed = cbi.mean_arm(allRiders)
indices = np.int32(np.round(speeds * 10))
w, v = control.eigen_vs_parameter(aAs[indices])
aEigenvalues, aEigenvectors = control.sort_modes(w, v)

rlfig = cbi.plot_rlocus_parts(speeds, iEigenvalues, wEigenvalues,
        aEigenvalues)
rlfig.savefig('../../figures/systemidentification/A-A-eig.png')

# Root locus with respect to speed.
v0 = 0.
vf = 10.
num = 20
speeds, iAs, iBs = bicycle.benchmark_state_space_vs_speed(iM, iC1, iK0, iK2,
        v0=v0, vf=vf, num=num)
iEig, null = control.eigen_vs_parameter(iAs)

speeds, wAs, wBs = bicycle.benchmark_state_space_vs_speed(wM, wC1, wK0, wK2,
        v0=v0, vf=vf, num=num)
wEig, null = control.eigen_vs_parameter(wAs)

indices = np.int32(np.round(speeds * 10))
aEig, null = control.eigen_vs_parameter(aAs[indices])
rlcfig = cbi.plot_rlocus(speeds, iEig, wEig, aEig)
rlcfig.savefig('../../figures/systemidentification/A-A-rlocus.png')

# bode plots
speeds = np.array([2.0, 4.0, 6.0, 9.0])
null, iAs, iBs = bicycle.benchmark_state_space_vs_speed(iM, iC1, iK0, iK2,
        speeds)
null, wAs, wBs = bicycle.benchmark_state_space_vs_speed(wM, wC1, wK0, wK2,
        speeds)
figs = cbi.plot_bode(speeds, iAs, iBs, wAs, wBs, aAs, aBs)
figs[0].savefig('../../figures/systemidentification/A-A-Tphi-Phi.png')
figs[1].savefig('../../figures/systemidentification/A-A-Tphi-Del.png')
figs[2].savefig('../../figures/systemidentification/A-A-Tdel-Phi.png')
figs[3].savefig('../../figures/systemidentification/A-A-Tdel-Del.png')
