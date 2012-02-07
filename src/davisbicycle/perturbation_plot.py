from math import sqrt
import bicycledataprocessor.main as bdp
import matplotlib.pyplot as plt

pathToBicycle = '/media/Data/Documents/School/UC Davis/Bicycle Mechanics'
pathToDatabase = pathToBicycle + '/BicycleDataProcessor/InstrumentedBicycleData.h5'
pathToParameters = pathToBicycle + '/BicycleParameters/data'

dataset = bdp.DataSet(fileName=pathToDatabase)
dataset.open()

trialNum = '00312'
trial = bdp.Run(trialNum, dataset.database, pathToParameters)

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

latForce = trial.taskSignals['PullForce']
time = latForce.time()

fig = plt.figure()
fig.suptitle(r'Run \#' + trialNum, fontsize=10)

axFull = fig.add_subplot(1, 2, 1)
axFull.plot(time, latForce)
axFull.set_xlabel('Time [s]')
axFull.set_ylabel('Force [N]')

axZoom = fig.add_subplot(1, 2, 2)
axZoom.plot(time, latForce)
axZoom.set_xlim([11., 12.])
axZoom.set_ylim([-50., 250.])
axZoom.set_xlabel('Time [s]')

fig.savefig('../../figures/davisbicycle/perturbation.png')
fig.savefig('../../figures/davisbicycle/perturbation.pdf')
fig.show()
