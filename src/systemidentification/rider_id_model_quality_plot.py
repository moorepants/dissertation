#/usr/bin/env python

import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt

# Plot parameters for Latex output
params = {'backend': 'ps',
          'axes.labelsize': 10,
          'text.fontsize': 10,
          'legend.fontsize': 8,
          'xtick.labelsize': 8,
          'ytick.labelsize': 8,
          'text.usetex': True,
          'figure.dpi': 200,
          }
plt.rcParams.update(params)

environments = ['treadmill', 'pavilion']
files = ['riderIdTreadmill.mat', 'riderIdPavilion.mat']

for filename, env in zip(files, environments):
    treadmillRun = loadmat('../../data/systemidentification/' +
            filename, squeeze_me=True)

    outputNames = [str(name) for name in treadmillRun['outputNames']]
    outputLabels = ['$\psi$ [rad]', '$\phi$ [rad]', '$\delta$ [rad]',
            '$\dot{\psi}$', '$\dot{\phi}$', '$\dot{\delta}$', '$T_\delta$']
    outputFit = treadmillRun['fit'][1]

    numSamp = treadmillRun['inputData'].shape[0]
    time = np.linspace(0, (numSamp - 1) / 200, num=numSamp)

    fig, axes = plt.subplots(8, 1, sharex=True)
    fig.set_size_inches(4, 8)

    for i, ax in enumerate(axes):
        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
        if i == 0:
            ax.plot(time, treadmillRun['inputData'], 'k-', label='Measured')
            ax.set_ylabel('$F_B$')
        else:
            ax.plot(time, treadmillRun['outputData'][:, i - 1], 'k-', label='Measured')
            ax.plot(time, treadmillRun['simoY'][:, i - 1], 'b-', alpha=0.6,
                    label='SIMO {:1.1f}\%'.format(outputFit[i - 1]))
            ax.set_ylabel(outputLabels[i - 1])
        ax.locator_params(axis='y', nbins=5)
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        if env == 'treadmill':
            ax.set_xlim((53, 79))

    axes[3].plot(time, treadmillRun['sisoY'], 'g-', alpha=0.6,
            label='SISO {:1.1f}\%'.format(treadmillRun['fit'][1][4]))
    axes[3].legend(loc='center left', bbox_to_anchor=(1, 0.5))

    fig.savefig('../../figures/systemidentification/rider-id-' + env + '-run.png')
    fig.savefig('../../figures/systemidentification/rider-id-' + env + '-run.pdf')
