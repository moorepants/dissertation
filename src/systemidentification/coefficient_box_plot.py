#!/usr/bin/env python

import sys
sys.path.append('..')
from load_paths import read

import cPickle
import numpy as np
from scipy.io import loadmat
#from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from matplotlib import rcParams
from bicycleid import data, model
import dtk.bicycle

params = {'axes.labelsize': 8,
          'axes.titlesize': 10,
          'text.fontsize': 10,
          'legend.fontsize': 10,
          'xtick.labelsize': 8,
          'ytick.labelsize': 8,
          'text.usetex': True,
          'figure.subplot.wspace': 0.25}
rcParams.update(params)

# load in the system identification results and select out the desired runs
dat = data.ExperimentalData()

subDef = {}
subDef['Rider'] = ['Charlie', 'Jason', 'Luke']
subDef['Environment'] = ['Treadmill', 'Pavilion']
subDef['Maneuver'] = ['Balance', 'Track Straight Line',
    'Balance With Disturbance', 'Track Straight Line With Disturbance']
subDef['Speed'] = ['1.4', '2.0', '3.0', '4.0', '4.92', '5.8', '7.0', '9.0']
subDef['MeanFit'] = -1e16
subDef['Duration'] = 0.0

subDat = dat.subset(**subDef)

# whipple model
speedRange = np.linspace(0.0, 10.0, num=50)
whipple = model.Whipple('Charlie').matrices(speedRange)

# arm model
m = loadmat('../../data/extensions/armsAB-Charlie.mat', squeeze_me=True) # this is charlie at 101 speeds

inputMats = np.zeros((101, 4, 2))
for i, B in enumerate(m['inputMatrices']):
    inputMats[i] = B[:, 1:]

# best identified model
with open(read('pathToIdMat')) as f:
    idMat = cPickle.load(f)

M, C1, K0, K2, H = idMat['L-P']
speeds = np.linspace(0, 10, num=50)
As = np.zeros((len(speeds), 4, 4))
Bs = np.zeros((len(speeds), 4, 2))

for i, v in enumerate(speeds):
    A, BT = dtk.bicycle.benchmark_state_space(M, C1, K0, K2, v, 9.81)
    As[i] = A
    BF = np.dot(BT[2:, :], H)
    Bs[i] = np.hstack((BT[:, 1].reshape(4,1), np.vstack((np.zeros((2,1)), BF))))

# A matrix box plot
nBins = 25
speedBins = np.linspace(0.0, 10.0, num=nBins)
nums = []
binDur = []
meanFits = []
labels = ['a' + str(i) + str(j) for i in [3, 4] for j in [1, 2, 3, 4]]
plotData = {lab: [] for lab in labels}
for v in speedBins:
    sbin = subDat[(v - 0.25 < subDat['ActualSpeed']) & (subDat['ActualSpeed'] < v + 0.25)]
    nums.append(len(sbin))
    binDur.append(sbin['Duration'].sum())
    for lab in labels:
        plotData[lab].append(sbin[lab])

widths = 10.0 / nBins * (np.sqrt(nums) / max(np.sqrt(nums)))
widths = 10.0 / nBins * (np.sqrt(binDur) / max(np.sqrt(binDur)))

fig, axs = plt.subplots(2, 4, sharex=True)
fig.set_figwidth(6.5)

ylims = {'a31': (0, 40),
         'a32': (-70, 0),
         'a33': (-4, 4),
         'a34': (-10, 0),
         'a41': (-50, 200),
         'a42': (-200, 50),
         'a43': (0, 60),
         'a44': (-100, 0),
         'b31': (-0.2, 1.0),
         'b32': (0.0, 0.02),
         'b41': (0.0, 20.0),
         'b42': (-0.05, 0.05)}

#constant = lambda x, c: c * np.ones_like(x)
#lineInterceptZero = lambda x, b: b * x
#line = lambda x, b, c: b * x + c
#quadratic = lambda x, a, b, c: a * x**2 + b * x + c
#
#fitEqs = {'a31': constant,
          #'a32': quadratic,
          #'a33': lineInterceptZero,
          #'a34': lineInterceptZero,
          #'a41': constant,
          #'a42': quadratic,
          #'a43': lineInterceptZero,
          #'a44': lineInterceptZero}

titles = {'a31': r'$a_{\ddot{\phi}\phi}$',
          'a32': r'$a_{\ddot{\phi}\delta}$',
          'a33': r'$a_{\ddot{\phi}\dot{\phi}}$',
          'a34': r'$a_{\ddot{\phi}\dot{\delta}}$',
          'a41': r'$a_{\ddot{\delta}\phi}$',
          'a42': r'$a_{\ddot{\delta}\delta}$',
          'a43': r'$a_{\ddot{\delta}\dot{\phi}}$',
          'a44': r'$a_{\ddot{\delta}\dot{\delta}}$',
          'b31': r'$b_{\ddot{\phi}T_\delta}$',
          'b32': r'$b_{\ddot{\phi}F}$',
          'b41': r'$b_{\ddot{\delta}T_\delta}$',
          'b42': r'$b_{\ddot{\delta}F}$'}

for i in [3, 4]:
    for j in [1, 2, 3, 4]:
        lab = 'a' + str(i) + str(j)
        ax = axs[i - 3, j - 1]
        ax.plot(whipple['Speed'], whipple[lab], 'g')
        ax.plot(m['speed'], m['stateMatrices'][:, i - 1, j - 1], 'r')
        ax.plot(speeds, As[:, i - 1, j - 1], 'orange')
        ax.boxplot(plotData[lab], positions=speedBins,
                widths=widths)

        # This code plot a fit through the medians of the data, but only "works
        # when the mean fit percentage is above 75%...i.e. the data is fucking
        # way to variable.
        #y = array([sbin.median() for sbin in plotData[lab]])
        #x = speedBins
        #sol, cov = curve_fit(fitEqs[lab], x[~isnan(y)], y[~isnan(y)],
                #sigma=1. / widths[~isnan(y)])
        #ax.plot(x, fitEqs[lab](x, *sol), 'k')

        ax.set_xticks(np.arange(0, 11))
        ax.set_xlim((1.0, 8.0))
        ax.set_ylim(ylims[lab])
        ax.set_title(titles[lab])
        if ax.is_last_row():
            ax.set_xlabel('$v$ [m/s]')

fig.suptitle('{} runs with at least {:1.0f}\% mean fit and max {} per bin'.format(len(subDat),
    subDef['MeanFit'], max([len(d) for d in plotData['a31']])))

fig.savefig('../../figures/systemidentification/a-matrix-box-plot.png')
fig.savefig('../../figures/systemidentification/a-matrix-box-plot.pdf')

# B matrix boxplot
bfig, baxs = plt.subplots(2, 2, sharex=True)
bfig.set_figwidth(6.0)
nums = []
meanFits = []
labels = ['b' + str(i) + str(j) for i in [3, 4] for j in [1, 2]]
plotData = {lab: [] for lab in labels}
for v in speedBins:
    sbin = subDat[(v - 0.25 < subDat['ActualSpeed']) & (subDat['ActualSpeed'] < v + 0.25)]
    nums.append(len(sbin))
    for lab in labels:
        plotData[lab].append(sbin[lab])

for i in [3, 4]:
    for j in [1, 2]:
        lab = 'b' + str(i) + str(j)
        ax = baxs[i - 3, j - 1]

        ax.plot(whipple['Speed'], whipple[lab], 'g')
        ax.plot(m['speed'], inputMats[:, i - 1, j - 1], 'r')
        ax.plot(speeds, Bs[:, i - 1, j - 1], 'orange')
        ax.boxplot(plotData[lab], positions=speedBins,
                widths=widths)

        ax.set_xticks(np.arange(0, 11))
        ax.set_xlim((1.0, 8.0))
        ax.set_ylim(ylims[lab])
        ax.set_title(titles[lab])
        if ax.is_last_row():
            ax.set_xlabel('$v$ [m/s]')

bfig.suptitle('{} runs with at least {:1.0f}\% mean fit and max {} per bin'.format(len(subDat),
    subDef['MeanFit'], max([len(d) for d in plotData['b31']])))

bfig.savefig('../../figures/systemidentification/b-matrix-box-plot.png')
bfig.savefig('../../figures/systemidentification/b-matrix-box-plot.pdf')
