from numpy import load
import matplotlib.pyplot as plt

goldenRatio = (5**0.5 - 1.0) / 2.0
fig_width = 4.0
fig_height = fig_width * goldenRatio
fig_size =  [fig_width, fig_height]
params = {'axes.labelsize': 8,
          'axes.titlesize': 10,
          'text.fontsize': 8,
          'legend.fontsize': 8,
          'xtick.labelsize': 8,
          'ytick.labelsize': 8,
          'text.usetex': True,
          'figure.figsize': fig_size,
          }
plt.rcParams.update(params)

fileName = '/media/Data/Documents/School/TU Delft/MotionCapture/data/npy/hip/3104Hip.npy'
HipVec = load(fileName)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, aspect='equal')
# right hip
ax.plot(-HipVec[:, 0, 1], -HipVec[:, 0, 2], '.')
# left hip
ax.plot(-HipVec[:, 1, 1], -HipVec[:, 1, 2], '.')
# plot butt
ax.plot(-HipVec[:, 2, 1], -HipVec[:, 2, 2], '.')
ax.set_ylim((0, .5))
ax.set_ylabel('Distance [m]')
ax.set_xlabel('Distance [m]')
ax.legend(['Right Hip', 'Left Hip', 'Butt'])
fig.subplots_adjust(bottom=0.15)

fig.savefig('../../figures/extensions/hip-trace.png', dpi=300)
fig.savefig('../../figures/extensions/hip-trace.pdf')
