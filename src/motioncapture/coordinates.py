#!/usr/bin/env python

# This script remakes the coordinate time history plots in the ISEA2010 paper
# with proper sizing and such.

import string as st
import numpy as np
import matplotlib.pyplot as plt

run = '3017'

stateDir = '/media/Data/Documents/School/TU Delft/MotionCapture/data/npy/states/'

q = np.load(stateDir + run + 'q.npy')

# name the states
qName = ['1 distance to rear wheel contact',
         '2 distance to the rear wheel contact',
         'yaw angle',
         'roll angle',
         'pitch angle',
         'steer angle',
         '1 distance to front wheel contact',
         '2 distance to front wheel contact',
         'crank rotation',
         'right knee lateral distance',
         'left knee lateral distance',
         'butt lateral distance',
         'lean angle',
         'twist angle']

tSteps = len(q[0])
t = np.linspace(0, 59.99, tSteps)

goldenRatio = (5**0.5 - 1.0) / 2.0
fig_width = 3.0
fig_height = fig_width * goldenRatio
fig_size =  [fig_width, fig_height]
params = {'axes.labelsize': 8,
          'text.fontsize': 8,
          'legend.fontsize': 6,
          'xtick.labelsize': 8,
          'ytick.labelsize': 8,
          'text.usetex': True,
          'savefig.dpi': 200,
          'figure.subplot.hspace': 0.2,
          'figure.subplot.bottom': 0.2,
          'figure.subplot.left': 0.2,
          'figure.figsize': fig_size}

plt.rcParams.update(params)

# wheel contact locations
plt.figure(0)
speed = 2.7778 # meters/second
distance = speed * t
plt.plot(q[0] + distance, 100 * q[7], '-', color='black',
        label='Rear Wheel')
plt.plot(q[6] + distance, 100 * q[1], '-', color='grey',
        label='Front Wheel')
plt.ylabel('Distance [cm]')
plt.xlabel('Distance [m]')
plt.xlim((q[0][0], distance[-1] + q[0][-1]))
plt.legend()

plt.savefig('../../figures/motioncapture/' + run + 'wheel.pdf')
plt.savefig('../../figures/motioncapture/' + run + 'wheel.png')

# yaw, roll and steer angle
plt.figure(1)
plt.plot(t, np.rad2deg(q[2]), '-', label=st.capwords(qName[2]),
        color='black', linewidth=2)
plt.plot(t, np.rad2deg(q[3]), '-', label=st.capwords(qName[3]),
        color='grey', linewidth=2)
plt.plot(t, np.rad2deg(q[5]), ':', label=st.capwords(qName[5]),
        color='black', linewidth=1)
plt.legend()
plt.ylabel('Angle [deg]')
plt.xlabel('Time [s]')
plt.ylim((-4, 4))
plt.xlim((0, 10))
plt.savefig('../../figures/motioncapture/' + run + 'bAng.pdf')
plt.savefig('../../figures/motioncapture/' + run + 'bAng.png')

# knee and butt lateral distance
plt.figure(2)
plt.subplot(211)
plt.plot(t, 100.0 * q[9], '-', label=st.capwords(qName[9]),
        color='black', linewidth=2)
plt.plot(t, 100.0 * q[10], '-', label=st.capwords(qName[10]),
        color='grey', linewidth=2)
plt.legend(loc=0)
plt.ylabel('Distance [cm]')
plt.xlim((0, 10))
plt.gca().set_xticklabels('')

plt.subplot(212)
plt.plot(t, 100.0 * q[11], '-', label=st.capwords(qName[11]),
        color='black', linewidth=2)
plt.legend(loc = 0)
plt.ylabel('Distance [cm]')
plt.xlabel('Time [s]')
plt.xlim((0, 10))
plt.savefig('../../figures/motioncapture/' + run + 'rLat.pdf')
plt.savefig('../../figures/motioncapture/' + run + 'rLat.png')

# lean and twist
plt.figure(3)
plt.plot(t, np.rad2deg(q[12]), '-',
        label=st.capwords(qName[12]), color='black', linewidth=2)
plt.plot(t, np.rad2deg(q[13]), '-',
        label=st.capwords(qName[13]), color='grey', linewidth=2)
plt.legend()
plt.ylabel('Angle [deg]')
plt.xlabel('Time [s]')
plt.xlim((0, 10))
plt.savefig('../../figures/motioncapture/' + run + 'rAng.pdf')
plt.savefig('../../figures/motioncapture/' + run + 'rAng.png')
