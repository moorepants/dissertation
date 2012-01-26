import bicycledataprocessor.main as bdp
import matplotlib.pyplot as plt
from math import sqrt

pathToBicycle = '/media/Data/Documents/School/UC Davis/Bicycle Mechanics'
pathToDatabase = pathToBicycle + '/BicycleDataProcessor/InstrumentedBicycleData.h5'
pathToParameters = pathToBicycle + '/BicycleParameters/data'

dataset = bdp.DataSet(fileName=pathToDatabase)
dataset.open()

trial = bdp.Run('00700', dataset.database, pathToParameters)

dataset.close()

golden_mean = (sqrt(5) - 1.0) / 2.0
fig_width = 5.0
fig_height = fig_width * golden_mean
params = {'backend': 'ps',
          'axes.labelsize': 10,
          'text.fontsize': 10,
          'legend.fontsize': 6,
          'xtick.labelsize': 8,
          'ytick.labelsize': 8,
          'text.usetex': True,
          'figure.figsize': [fig_width,fig_height],
          'figure.dpi' : 200,
          'figure.subplot.left' : 0.2,
          'figure.subplot.bottom' : 0.15}
plt.rcParams.update(params)

fig = trial.compute_steer_torque(plot=True)

fig.savefig('../../figures/davisbicycle/steer-torque-components.png')
fig.savefig('../../figures/davisbicycle/steer-torque-components.pdf')
