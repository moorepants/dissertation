#!/usr/bin/env python

# This script plots the results of the time synchronization of the acceleration
# signals caused by the bump.

import bicycledataprocessor as bdp
import os
import numpy as np
import matplotlib.pyplot as plt

pathToBicycleMechanics = '/media/Data/Documents/School/UC Davis/Bicycle Mechanics'
pathToDatabase = os.path.join(pathToBicycleMechanics, 'BicycleDataProcessor/InstrumentedBicycleData.h5')
pathToParameterData = os.path.join(pathToBicycleMechanics, 'BicycleParameters/data')

dataset = bdp.DataSet(fileName=pathToDatabase)
dataset.open()

trial = bdp.Run('00690', dataset, pathToParameterData=pathToParameterData,
        forceRecalc=True)

dataset.close()

golden_mean = (np.sqrt(5) - 1.0) / 2.0
fig_width = 4.0
fig_height = fig_width * golden_mean
params = {'backend': 'ps',
          'axes.labelsize': 8,
          'axes.titlesize': 10,
          'text.fontsize': 8,
          'legend.fontsize': 6,
          'xtick.labelsize': 8,
          'ytick.labelsize': 8,
          'text.usetex': True,
          'figure.figsize': [fig_width,fig_height],
          'figure.dpi' : 200,
          'figure.subplot.left' : 0.25,
          'figure.subplot.bottom' : 0.15}
plt.rcParams.update(params)

# plot the data before it is synchronized
unsync = trial.plot('-AccelerometerAccelerationY', 'AccelerationZ',
        signalType='calibrated')

ax = unsync.axes[0]
ax.set_xlim((0., 3.))
ax.set_ylabel(r'Acceleration $\left[\frac{m}{s^2}\right]$')
ax.set_xlabel('Time [s]')
ax.set_title('Vertical Accelerometer Signals Before Synchronization')

niLeg = ax.legend_.get_texts()[0]
niLeg.set_text('NI USB-6218')
vnLeg = ax.legend_.get_texts()[1]
vnLeg.set_text('VN-100')

unsync.savefig('../../figures/davisbicycle/unsync.png')
unsync.savefig('../../figures/davisbicycle/unsync.pdf')

# plot the data after synchronization
sync = trial.plot('-AccelerometerAccelerationY', 'AccelerationZ',
        signalType='truncated')

ax = sync.axes[0]
ax.set_xlim((0., 3.))
ax.set_ylabel(r'Acceleration $\left[\frac{m}{s^2}\right]$')
ax.set_xlabel('Time [s]')
ax.set_title('Vertical Accelerometer Signals After Synchronization')

niLeg = ax.legend_.get_texts()[0]
niLeg.set_text('NI USB-6218')
vnLeg = ax.legend_.get_texts()[1]
vnLeg.set_text('VN-100')

sync.savefig('../../figures/davisbicycle/sync.png')
sync.savefig('../../figures/davisbicycle/sync.pdf')
