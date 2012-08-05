#!/usr/bin/env python

# This creates two example time history plots, one for a treadmill run and one
# for a pavilion run.

import matplotlib.pyplot as plt
import bicycledataprocessor as bdp

dataset = bdp.DataSet()

fig_width = 6.0
goldenRatio = (5**0.5 - 1.0) / 2.0
fig_height = fig_width * goldenRatio
fig_size =  [fig_width, fig_height]
params = {'axes.labelsize': 8,
          'axes.titlesize': 8,
          'text.fontsize': 8,
          'legend.fontsize': 6,
          'xtick.labelsize': 6,
          'ytick.labelsize': 6,
          'text.usetex': True,
          'figure.figsize': fig_size,
          #'figure.subplot.hspace': 0.3,
          'figure.subplot.wspace': 0.25,
          #'figure.subplot.bottom': 0.1,
          #'figure.subplot.left': 0.1,
          'figure.dpi': 300}

plt.rcParams.update(params)

for r, lims, tag in zip([283, 592], [(8., 24.), (0., 6.)], ['treadmill', 'pavilion']):
    trial = bdp.Run(r, dataset, filterFreq=15.)

    fig = plt.figure()

    sigs = trial.taskSignals

    plotSigs = [['YawRate', 'RollRate', 'PitchRate', 'SteerRate'],
                ['ForwardSpeed'],
                ['YawAngle', 'RollAngle', 'SteerAngle'],
                ['LateralRearContact', 'LateralFrontContact'],
                ['SteerTorque'],
                ['PullForce']]

    legends = [[r'$\dot{\psi}$', r'$\dot{\phi}$', r'$\dot{\theta}_B$', r'$\dot{\delta}$'],
               [r'$v$'],
               [r'$\psi$', r'$\phi$', r'$\delta$'],
               [r'$y_p$', r'$y_q$'],
               [r'$T_\delta$'],
               [r'$F_{c_l}$']]

    ylabels = ['Anglur Rate [rad/s]',
               'Speed [m/s]',
               'Angle [rad]',
               'Distance [m]',
               'Torque [N-m]',
               'Force [n]']

    for i, group in enumerate(plotSigs):
        ax = fig.add_subplot(3, 2, i + 1)
        for s in group:
            time = sigs[s].time()
            ax.plot(time, sigs[s])
        ax.legend(legends[i])
        ax.set_xlim(lims)
        ax.set_ylabel(ylabels[i])

    fig.axes[-1].set_xlabel('Time [s]')
    fig.axes[-2].set_xlabel('Time [s]')
    l1 = r'Run \# {RunID}: {Rider} on the {Environment}'.format(**trial.metadata)
    l2 = r'performing {Maneuver} at speed {Speed} m/s'.format(**trial.metadata)
    fig.suptitle(l1 + '\n' + l2, fontsize=10)

    fig.savefig('../../figures/systemidentification/time-history-' + tag + '.png')
    fig.savefig('../../figures/systemidentification/time-history-' + tag +
            '.pdf')
    fig.savefig('../../figures/systemidentification/time-history-' + tag + '.png')
