#!/usr/bin/env python

# This compares the mean frequency response of all the state space identified
# models with the Whipple and Arm models.
import os
from numpy import logspace, sqrt, array, zeros, log10, rad2deg
from scipy.io import loadmat
from matplotlib import rcParams
from bicycleid import data, plot, model
from dtk import control

params = {'axes.labelsize': 8,
          'text.fontsize': 8,
          'legend.fontsize': 6,
          'xtick.labelsize': 8,
          'ytick.labelsize': 8,
          'text.usetex': True}
rcParams.update(params)

subDef = {}
subDef['Rider'] = ['Charlie', 'Jason', 'Luke']
subDef['Environment'] = ['Treadmill', 'Pavilion']
subDef['Maneuver'] = ['Balance', 'Track Straight Line',
    'Balance With Disturbance', 'Track Straight Line With Disturbance']
subDef['Speed'] = ['4.0']
subDef['MeanFit'] = 0.0
subDef['Duration'] = 0.0

w = logspace(-1, 2, num=100)
dat = data.ExperimentalData(w=w)

models = {rider: model.Whipple(rider) for rider in ['Charlie']}

bodePlot = plot.BodePlot(w)
bodeData = dat.subset_bode(**subDef)
bodePlot.update_graph(bodeData, models)

# this is the Whipple model line
bodePlot.bode.figs[0].axes[0].lines[3].set_color('g')
bodePlot.bode.figs[0].axes[1].lines[3].set_color('g')

# arm model at the mean speed for this run
m = loadmat('../extensions/arms/armsAB-Charlie.mat', squeeze_me=True) # this is charlie at 101 speeds

# @ 4.0 m/s
A = m['stateMatrices'][40]
B = m['inputMatrices'][40, :, 1].reshape(4, 1)
C = array([[1.0, 0.0, 0.0, 0.0]])
D = zeros((1, 1))
sys = control.StateSpace(A, B, C, D)
mag, phase = bodePlot.bode.mag_phase_system(sys)

# arm model lines
# mag
bodePlot.bode.figs[0].axes[0].lines[4].set_ydata(20 * log10(mag[:, 0, 0]))
bodePlot.bode.figs[0].axes[0].lines[4].set_color('r')
# phase
bodePlot.bode.figs[0].axes[1].lines[4].set_ydata(rad2deg(phase[:, 0, 0]))
bodePlot.bode.figs[0].axes[1].lines[4].set_color('r')

bodePlot.bode.figs[0].axes[0].set_ylim((-120, 0))
bodePlot.bode.figs[0].axes[1].set_ylim((-250, 0))

# move the y axis labels
x, y = bodePlot.bode.figs[0].axes[0].yaxis.get_label().get_position()
bodePlot.bode.figs[0].axes[0].yaxis.set_label_coords(x - 0.1, y)

x, y = bodePlot.bode.figs[0].axes[1].yaxis.get_label().get_position()
bodePlot.bode.figs[0].axes[1].yaxis.set_label_coords(x - 0.1, y)

goldenRatio = (1 + sqrt(5.)) / 2.
figWidth = 5.
figHeight = figWidth / goldenRatio

bodePlot.bode.figs[0].set_figwidth(figWidth)
bodePlot.bode.figs[0].set_figheight(figHeight)
bodePlot.bode.figs[0].savefig('../../figures/systemidentification/state-space-bode.pdf')
# following line isn't working
#bodePlot.bode.figs[0].savefig('../../figures/systemidentification/state-space-bode.png')
os.system('convert ../../figures/systemidentification/state-space-bode.pdf ../../figures/systemidentification/state-space-bode.png')
