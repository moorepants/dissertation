import bicycledataprocessor as bdp
import matplotlib.pyplot as plt
from math import sqrt

pathToBicycle = '/media/Data/Documents/School/UC Davis/Bicycle Mechanics'
pathToDatabase = pathToBicycle + '/BicycleDataProcessor/InstrumentedBicycleData.h5'
pathToParameters = pathToBicycle + '/BicycleParameters/data'

dataset = bdp.DataSet(fileName=pathToDatabase)
dataset.open()

trial = bdp.Run('00700', dataset, pathToParameters, forceRecalc=True)

dataset.close()

fig_width = 5.5
fig_height = 7.5
params = {'backend': 'ps',
          'axes.labelsize': 10,
          'text.fontsize': 10,
          'legend.fontsize': 6,
          'xtick.labelsize': 8,
          'ytick.labelsize': 8,
          'text.usetex': True,
          'figure.figsize': [fig_width,fig_height],
          'figure.dpi' : 200,
          'figure.subplot.left' : 0.1,
          'figure.subplot.bottom' : 0.1}
plt.rcParams.update(params)

fig = trial.compute_steer_torque(plot=True)

fig.savefig('../../figures/davisbicycle/steer-torque-components.png')
fig.savefig('../../figures/davisbicycle/steer-torque-components.pdf')
