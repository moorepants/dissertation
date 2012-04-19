import sys
sys.path.append('..')
from load_paths import read

import os
import cPickle
from numpy import linspace, sqrt, zeros
from scipy.io import loadmat
from matplotlib import rcParams
from bicycleid import data, plot, model
import dtk.bicycle

params = {'axes.labelsize': 10,
          'text.fontsize': 10,
          'legend.fontsize': 10,
          'xtick.labelsize': 8,
          'ytick.labelsize': 8,
          'text.usetex': True}
rcParams.update(params)

dat = data.ExperimentalData()

coefPlot = plot.CoefficientPlot()

subDef = {}
subDef['Rider'] = ['Charlie', 'Jason', 'Luke']
subDef['Environment'] = ['Treadmill', 'Pavilion']
subDef['Maneuver'] = ['Balance', 'Track Straight Line',
    'Balance With Disturbance', 'Track Straight Line With Disturbance']
subDef['Speed'] = ['1.4', '2.0', '3.0', '4.0', '4.92', '5.8', '7.0', '9.0']
subDef['MeanFit'] = 0.0
subDef['Duration'] = 0.0

subDat = dat.subset(**subDef)

speedRange = linspace(0.0, 10.0, num=50)
models = {rider: model.Whipple(rider).matrices(speedRange) for rider in ['Charlie']}

coefPlot.update_graph(subDat, models)

# now add the arm model
m = loadmat('../extensions/arms/armsAB-Charlie.mat', squeeze_me=True) # this is charlie at 101 speeds

inputMats = zeros((101, 4, 1))
for i, B in enumerate(m['inputMatrices']):
    inputMats[i] = B[:, 1].reshape(4, 1)

for lab, ax in coefPlot.axes.items():
    row, col = int(lab[-2]), int(lab[-1])
    if lab[0] == 'a':
        ax.plot(m['speed'], m['stateMatrices'][:, row - 1, col - 1], 'r')
    elif lab[0] == 'b':
        ax.plot(m['speed'], inputMats[:, row - 1, col - 1], 'r')

# now add the model identified from the runs with Luke on the Pavilion floor
# with the canonical realization
with open(read('pathToIdMat')) as f:
    idMat = cPickle.load(f)

M, C1, K0, K2, H = idMat['L-P']
speeds = linspace(0, 10, num=50)
As = zeros((len(speeds), 4, 4))
Bs = zeros((len(speeds), 4, 1))

for i, v in enumerate(speeds):
    A, B = dtk.bicycle.benchmark_state_space(M, C1, K0, K2, v, 9.81)
    As[i] = A
    Bs[i] = B[:, 1].reshape(4, 1)

for lab, ax in coefPlot.axes.items():
    row, col = int(lab[-2]), int(lab[-1])
    if lab[0] == 'a':
        ax.plot(speeds, As[:, row - 1, col - 1], 'orange')
    elif lab[0] == 'b':
        ax.plot(speeds, Bs[:, row - 1, col - 1], 'orange')

coefPlot.title.set_fontsize(10.0)
coefPlot.figure.set_figwidth(7.5)
goldenRatio = (sqrt(5)-1.0)/2.0
coefPlot.figure.set_figheight(7.5 * goldenRatio)
coefPlot.figure.savefig('../../figures/systemidentification/coefficients.pdf')
os.system('convert ../../figures/systemidentification/coefficients.pdf ../../figures/systemidentification/coefficients.png')
