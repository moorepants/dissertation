#!/usr/bin/env python

# This script calculates the zeros of the steer torque to steer and roll angle
# tranfer functions as a function of the canonical matrix entries given in
# Meijaard2007.

# Warning! This script does not work if their are complex zeros, as I haven't
# figured out how to change the sympy `I` into a numpy complex number.

import numpy as np
import matplotlib.pyplot as plt
from sympy import Symbol, Matrix, symbols, eye, zeros, roots
import uncertainties as un
import bicycleparameters as bp

# v = speed, g = acceleration due to gravity, s = Laplace variable
v, g, s = symbols('v g s')

# build the canoncial matrices, setting some entries to zero
# I did not include these realtionships yet: M[0, 1] = M[1, 0] and K0[0, 1] =
# K0[1, 0]. It is possible that they help simplify things.
# I did set C[0, 0] = 0 and K2[0, 0] = K2[1, 0] = 0.
M = Matrix(2, 2, lambda i, j: Symbol('m' + str(i + 1) + str(j + 1)))
C1 = Matrix(2, 2, lambda i, j: 0 if i == 0 and j == 0 else
        Symbol('c1' + str(i + 1) + str(j + 1)))
K0 = Matrix(2, 2, lambda i, j: Symbol('k0' + str(i + 1) + str(j + 1)))
K2 = Matrix(2, 2, lambda i, j: 0 if j == 0 else
        Symbol('k2' + str(i + 1) + str(j + 1)))

# Build the A, B and C matrices such that steer torque is the only input and
# phi and delta are the only outputs.
Minv = M.inv()

Abl = -Minv * (g * K0 + v**2 * K2)
Abr = -Minv * v * C1

A = zeros(2).row_join(eye(2)).col_join(Abl.row_join(Abr))

#B = zeros((2, 1)).col_join(Minv[:, 1])
B = zeros(2).col_join(Minv)

C = Matrix([[1, 0, 0, 0], [0, 1, 0, 0]])

# Calculate the transfer function numerator polynomial. See Hoagg2007 for the
# equation.
N = C * (s * eye(4) - A).adjugate() * B
# These are the roll and steer numerator polynomials, respectively.
phiTphi = N[0, 0]
deltaTphi = N[1, 0]
phiTdelta = N[0, 1]
deltaTdelta = N[1, 1]

# Find the zeros
phiTphiZeros = roots(phiTphi, s, multiple=True)
deltaTphiZeros = roots(deltaTphi, s, multiple=True)
phiTdeltaZeros = roots(phiTdelta, s, multiple=True)
deltaTdeltaZeros = roots(deltaTdelta, s, multiple=True)

# Load a bicycle with some parameters and calculate the canonical matrices.
pathToData = '/media/Data/Documents/School/UC Davis/Bicycle Mechanics/BicycleParameters/data'
bicycle = bp.Bicycle('Rigidcl', pathToData=pathToData, forceRawCalc=True)
bicycle.add_rider('Charlie')
#bicycle = bp.Bicycle('Benchmark', pathToData=pathToData)
Mn, C1n, K0n, K2n = bicycle.canonical()
Mn = un.unumpy.nominal_values(Mn)
C1n = un.unumpy.nominal_values(C1n)
K0n = un.unumpy.nominal_values(K0n)
K2n = un.unumpy.nominal_values(K2n)

# Create a dictionary to substitute numerical values.

# These are the benchmark bicycle parameters.
#num = {M[0, 0] : 80.81722,
       #M[0, 1] : 2.31941332208709,
       #M[1, 0] : 2.31941332208709,
       #M[1, 1] : 0.29784188199686,
       #K0[0, 0] : -80.95,
       #K0[0, 1] : -2.59951685249872,
       #K0[1, 0] : -2.59951685249872,
       #K0[1, 1] : -0.80329488458618,
       #K2[0, 1] : 76.59734589573222,
       #K2[1, 1] : 2.65431523794604,
       #C1[0, 1] : 33.86641391492494,
       #C1[1, 0] : -0.85035641456978,
       #C1[1, 1] : 1.68540397397560,
       #g : 9.81}

num = {M[0, 0] : Mn[0, 0],
       M[0, 1] : Mn[0, 1],
       M[1, 0] : Mn[1, 0],
       M[1, 1] : Mn[1, 1],
       K0[0, 0] : K0n[0, 0],
       K0[0, 1] : K0n[0, 1],
       K0[1, 0] : K0n[1, 0],
       K0[1, 1] : K0n[1, 1],
       K2[0, 1] : K2n[0, 1],
       K2[1, 1] : K2n[1, 1],
       C1[0, 1] : C1n[0, 1],
       C1[1, 0] : C1n[1, 0],
       C1[1, 1] : C1n[1, 1],
       g : 9.81}

# Now calculate the zeros as a function of speed and plot them.
speeds = np.linspace(0, 10)

phiTphiRoots = []
deltaTphiRoots = []
phiTdeltaRoots = []
deltaTdeltaRoots = []

for speed in speeds:
    # set the speed
    num[v] = speed
    phiTphiRoots.append([x.subs(num) for x in phiTphiZeros])
    deltaTphiRoots.append([x.subs(num) for x in deltaTphiZeros])
    phiTdeltaRoots.append([x.subs(num) for x in phiTdeltaZeros])
    deltaTdeltaRoots.append([x.subs(num) for x in deltaTdeltaZeros])

goldenRatio = (5**0.5 - 1.0) / 2.0
fig_width = 4.0
fig_height = fig_width * goldenRatio
fig_size =  [fig_width, fig_height]
params = {'axes.labelsize': 10,
          'text.fontsize': 8,
          'legend.fontsize': 10,
          'xtick.labelsize': 6,
          'ytick.labelsize': 6,
          'text.usetex': True,
          'figure.figsize': fig_size,
          'figure.subplot.hspace': 0.1,
          'figure.subplot.bottom': 0.15,
          'figure.subplot.left': 0.15}
plt.rcParams.update(params)

fig = plt.figure()

ax1 = fig.add_subplot(4, 1, 1)
ax1.plot(speeds, phiTphiRoots, '-k')
ax1.set_ylabel(r'$\frac{\phi}{T_\phi}$')
ax1.set_title('Transfer function zeros.')
ax1.set_xticklabels('')
ax1.grid()

ax2 = fig.add_subplot(4, 1, 2)
ax2.plot(speeds, deltaTphiRoots, '-k')
ax2.set_ylabel(r'$\frac{\delta}{T_\phi}$')
ax2.set_xlabel('Speed [m/s]')
ax2.set_xticklabels('')
ax2.grid()

ax3 = fig.add_subplot(4, 1, 3)
ax3.plot(speeds, phiTdeltaRoots, '-k')
ax3.set_ylabel(r'$\frac{\phi}{T_\delta}$')
ax3.set_xticklabels('')
ax3.grid()

ax4 = fig.add_subplot(4, 1, 4)
ax4.plot(speeds, deltaTdeltaRoots, '-k')
ax4.set_ylabel(r'$\frac{\delta}{T_\delta}$')
ax4.set_xlabel('Speed [m/s]')
ax4.set_ylim((-3.5, 3.5))
ax4.grid()

fig.savefig('../../figures/control/zeros-wrt-speed.png', dpi=200)
fig.savefig('../../figures/control/zeros-wrt-speed.pdf')
