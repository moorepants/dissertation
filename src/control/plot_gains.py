#!/usr/bin/env python

# This plots the change in gains computed by our bicycle Human control software
# for a particular bicycle.

import matplotlib.pyplot as plt

def load_gains(fileName):
    """Loads the gains from the file into a dictionary."""
    f = open(fileName, 'r')
    header = f.readline()
    variables = header.strip().split(',')
    data = {k : [] for k in variables}
    for line in f:
        values = line.strip().split(',')
        for i, val in enumerate(values):
            data[variables[i]].append(val)
    return data

data = load_gains('/media/Data/Documents/School/UC Davis/Bicycle Mechanics/HumanControl/gains/RigidJasonSteerGains.txt')

fig_width = 4.0
fig_height = 5.0
fig_size =  [fig_width, fig_height]
params = {'axes.labelsize': 10,
          'text.fontsize': 10,
          'legend.fontsize': 10,
          'xtick.labelsize': 8,
          'ytick.labelsize': 8,
          'text.usetex': True,
          'figure.figsize': fig_size,
          'figure.subplot.hspace': 0.15,
          'figure.subplot.bottom': 0.1,
          'figure.subplot.left': 0.2}
plt.rcParams.update(params)

fig = plt.figure()

gains = ['kDelta', 'kPhiDot', 'kPhi', 'kPsi', 'kY']
labels = ['$k_\delta$', '$k_\dot{\phi}$', '$k_\phi$', '$k_\psi$', '$k_{y_q}$']
axes = []

for i, (gain, label) in enumerate(zip(gains, labels)):
    ax = (fig.add_subplot(5, 1, i + 1))
    ax.plot(data['speed'], data[gain])
    ax.set_ylabel(label)
    axes.append(ax)
    ax.locator_params(axis='y', nbins=5)

for ax in axes[0:-1]:
    ax.set_xticklabels('')

axes[-1].set_xlabel('Speed [m/s]')

fig.savefig('../../figures/control/gains.png', dpi=200)
fig.savefig('../../figures/control/gains.pdf')
