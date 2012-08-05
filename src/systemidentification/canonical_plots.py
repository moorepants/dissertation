import sys
sys.path.append('..')
from load_paths import read
import cPickle

import numpy as np
import matplotlib.pyplot as plt
from dtk import bicycle, control
from canonicalbicycleid import canonical_bicycle_id as cbi

goldenRatio = (1. + np.sqrt(5.)) / 2.
params = {'axes.labelsize': 10,
          'axes.grid': False,
          'text.fontsize': 10,
          'legend.fontsize': 8,
          'xtick.labelsize': 8,
          'ytick.labelsize': 8,
          'text.usetex': True,
          }
plt.rcParams.update(params)

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
w, v = control.eig_of_series(iAs)
iEigenvalues, iEigenvectors = control.sort_modes(w, v)

# whipple model (mean)
wM, wC1, wK0, wK2, wH = cbi.mean_canon(allRiders, canon, H)
speeds, wAs, wBs = bicycle.benchmark_state_space_vs_speed(wM, wC1, wK0, wK2,
        v0=v0, vf=vf, num=num)
w, v = control.eig_of_series(wAs)
wEigenvalues, wEigenvectors = control.sort_modes(w, v)

# arm model (mean)
aAs, aBs, aSpeed = cbi.mean_arm(allRiders)
indices = np.int32(np.round(speeds * 10))
w, v = control.eig_of_series(aAs[indices])
aEigenvalues, aEigenvectors = control.sort_modes(w, v)

rlfig = cbi.plot_rlocus_parts(speeds, iEigenvalues, wEigenvalues,
        aEigenvalues)
rlfig.set_size_inches(5., 5. / goldenRatio)
rlfig.savefig('../../figures/systemidentification/A-A-eig.png')
rlfig.savefig('../../figures/systemidentification/A-A-eig.pdf')

# Root locus with respect to speed.
v0 = 0.
vf = 10.
num = 20
speeds, iAs, iBs = bicycle.benchmark_state_space_vs_speed(iM, iC1, iK0, iK2,
        v0=v0, vf=vf, num=num)
iEig, null = control.eig_of_series(iAs)

speeds, wAs, wBs = bicycle.benchmark_state_space_vs_speed(wM, wC1, wK0, wK2,
        v0=v0, vf=vf, num=num)
wEig, null = control.eig_of_series(wAs)

indices = np.int32(np.round(speeds * 10))
aEig, null = control.eig_of_series(aAs[indices])
rlcfig = cbi.plot_rlocus(speeds, iEig, wEig, aEig)
rlcfig.set_size_inches(4., 4.)
rlcfig.savefig('../../figures/systemidentification/A-A-rlocus.png')
rlcfig.savefig('../../figures/systemidentification/A-A-rlocus.pdf')

# bode plots
speeds = np.array([2.0, 4.0, 6.0, 9.0])
null, iAs, iBs = bicycle.benchmark_state_space_vs_speed(iM, iC1, iK0, iK2,
        speeds)
null, wAs, wBs = bicycle.benchmark_state_space_vs_speed(wM, wC1, wK0, wK2,
        speeds)
figs = cbi.plot_bode(speeds, iAs, iBs, wAs, wBs, aAs, aBs)
for fig in figs:
    fig.set_size_inches(5., 5. / goldenRatio)
    leg = fig.phaseAx.legend(loc=4)
    plt.setp(leg.get_texts(), fontsize='4.0') #'xx-small')

figs[0].savefig('../../figures/systemidentification/A-A-Tphi-Phi.png')
figs[0].savefig('../../figures/systemidentification/A-A-Tphi-Phi.pdf')

figs[1].savefig('../../figures/systemidentification/A-A-Tphi-Del.png')
figs[1].savefig('../../figures/systemidentification/A-A-Tphi-Del.pdf')

figs[2].savefig('../../figures/systemidentification/A-A-Tdel-Phi.png')
figs[2].savefig('../../figures/systemidentification/A-A-Tdel-Phi.pdf')

figs[3].savefig('../../figures/systemidentification/A-A-Tdel-Del.png')
figs[3].savefig('../../figures/systemidentification/A-A-Tdel-Del.pdf')
