#!/usr/bin/env python

"""
This script generates a rigid body model of the bicycle roll angle trailer and
generates a graph showing the effect the height of the yoke axis on the yoke
angle and roll angle.
"""

import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import sympy as sym
import sympy.physics.mechanics as me

# theta is the bicycle roll angle and beta is potentiometer angle
theta, alpha, beta = sym.symbols('theta alpha beta')

rr, h, l, rt = sym.symbols('rr h l rt')

# newtonian reference frame
N = me.ReferenceFrame('N', indices=('1', '2', '3'))
# rear wheel rolls with respect to the newtonian frame
R = N.orientnew('R', 'Axis', (theta, N['1']), indices=('1', '2', '3'))
# the yolk pitches with respect to the wheel
Y = R.orientnew('Y', 'Axis', (alpha, R['2']), indices=('1', '2', '3'))
# the trailer rolls with respect to the yolk (beta is the potentiometer angle)
T = Y.orientnew('T', 'Axis', (beta, Y['1']), indices=('1', '2', '3'))

# rear wheel contact to the center of the trailer axle
rAcNo = -rr * R['3'] + h * Y['3'] - l * Y['1'] - (h + rt - rr) * T['3']

holo = []
# the axle must be the wheel radius above the ground
holo.append(rAcNo.dot(N['3']) + rt)

# the trailer must be horizontal with respect to the ground
holo.append(T['2'].dot(N['3']))

def constrain(q, num, var, eq):
    subDict = {var[0] : q[0], # alpha
               var[1] : q[1], # beta
               var[2] : num[0], # theta
               var[3] : num[1], # rr
               var[4] : num[2], # h
               var[5] : num[3], # l
               var[6] : num[4]} # rt

    zero = np.zeros(2)
    for i, con in enumerate(eq):
        zero[i] = con.subs(subDict)

    return zero
var = (alpha, beta, theta, rr, h, l, rt)

thetaRange = np.linspace(-np.pi / 4.5, np.pi / 4.5, num=100)
alphaBeta = np.zeros((len(thetaRange), 2))

golden_mean = (np.sqrt(5) - 1.0) / 2.0
fig_width = 4.0
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

fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)
ax1.set_ylabel(r'$\alpha$ [deg]')
ax1.set_xlabel(r'$\theta$ [deg]')
ax2 = fig.add_subplot(2, 1, 2)
ax2.set_ylabel(r'$\beta$ [deg]')
ax2.set_xlabel(r'$\theta$ [deg]')

for height in [0., 0.05, 0.1, 0.15, 0.2, 0.25, 0.3]:
    for i, th in enumerate(thetaRange):
        # todo make these the correct values for the trailer that was built
        num = (th, 0.3, height, 0.5, 0.05)
        alphaBeta[i] = fsolve(constrain, [0., 0.], args=(num, var, holo))

    ax1.plot(np.rad2deg(thetaRange), np.rad2deg(alphaBeta[:, 0]),
            label=str(height))
    ax2.plot(np.rad2deg(thetaRange), np.rad2deg(alphaBeta[:, 1]),
            label=str(height))

ax1.legend()
ax2.legend()

fig.savefig('../../figures/davisbicycle/trailer-angle.png', dpi=200)
fig.savefig('../../figures/davisbicycle/trailer-angle.pdf')
fig.show()

