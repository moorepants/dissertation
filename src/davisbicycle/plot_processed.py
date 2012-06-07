#!/usr/bin/env python

import bicycledataprocessor as bdp
import os
import numpy as np
import matplotlib.pyplot as plt

pathToBicycleMechanics = '/media/Data/Documents/School/UC Davis/Bicycle Mechanics'
pathToDatabase = os.path.join(pathToBicycleMechanics, 'BicycleDataProcessor/InstrumentedBicycleData.h5')
pathToParameterData = os.path.join(pathToBicycleMechanics, 'BicycleParameters/data')

dataset = bdp.DataSet(fileName=pathToDatabase)
dataset.open()

trial = bdp.Run('00699', dataset,
        pathToParameterData=pathToParameterData, filterFreq=40.)

dataset.close()

golden_mean = (np.sqrt(5) - 1.0) / 2.0
fig_width = 6.0
fig_height = fig_width * golden_mean
params = {'backend': 'ps',
          'axes.labelsize': 8,
          'axes.titlesize': 10,
          'text.fontsize': 8,
          'legend.fontsize': 6,
          'xtick.labelsize': 8,
          'ytick.labelsize': 8,
          'text.usetex': True,
          'figure.titlesize': 10,
          'figure.figsize': [fig_width,fig_height],
          'figure.dpi' : 200,
          'figure.subplot.left' : 0.2,
          'figure.subplot.bottom' : 0.15}
plt.rcParams.update(params)

sigs = ['PullForce', 'RollAngle', 'SteerAngle', 'SteerTorque']

mx = {sig : abs(trial.taskSignals[sig]).max() for sig in sigs}

plotStrings = [('%1.0f' % (mx['PullForce'] / v)) + '*' + k for k, v in mx.items()]

fig = trial.plot(*plotStrings)

fig.savefig('../../figures/davisbicycle/processed-data.png')
fig.savefig('../../figures/davisbicycle/processed-data.pdf')
