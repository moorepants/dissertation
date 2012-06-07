#!/usr/bin/env python

# This computes the shear and bending diagrams for a fork underload to help
# understand where an appropriate location of a steer torque sensor could be
# placed and to get an idea of the magnitudes of the loads in the steer tube
# for comparison to steer torques.

import numpy as np
import matplotlib.pyplot as plt

# define variables

# these are from Moore2009a
mB = 86.0 # mass of rider and frame [kg]
mR = 3.12 # mass of rear wheel [kg]
mH = 4.35 # mass of fork/handlebar assembly [kg]
mF = 2.02 # mass of front wheel [kg]
lam = 0.38 # steer axis tilt [rad]
rR = 0.342 # rear wheel radius [m]
rF = 0.342 # front wheel radius [m]
xB = 0.28 # rider/frame CoM [m]
zB = -1.03 # rider/frame CoM [m]
xH = 0.88 # fork/handlebar CoM [m]
zH = -0.78 # fork/handlebar CoM [m]
w = 1.120 # wheelbase [m]
g = 9.8 # gravity [m/s**2]
c = 0.055 # trail [m]
lfo = -np.cos(lam)*(c - rF*np.tan(lam)) # fork offset [m]
print "The fork offset =", lfo

# these are crude measurements from the Surly 1x1
lh = 0.1524 # handle length [m]
ls = 0.2032 # stem length [m]
lhd = 0.1524 # headset length [m]
lf = 0.4318 # fork length [m]
lhw = 0.5588 # handlebar width [m]

# from Shigley and Mischke 5th Edition
E = 207E9 # modulus of elasticity of steel [Pa]

# forces applied the handlebars, a percent of the riders weight
FHl = 0.0 * mB * g # downward force on the left handle
FHr = 0.125 * mB * g # downward force on the right handle

# define the mass and CoM locations
masses = np.array([mB, mF, mH, mR])
print masses
xes = np.array([xB, w, xH, 0.0])
zes = np.array([zB, -rF, zH, -rR])
# calculate the total mass
mTot = np.sum(masses)
print mTot
# total CoM
xCoM = np.sum(masses*xes)/mTot
zCoM = np.sum(masses*zes)/mTot
# dynamic multiplier (g's of accel)
# this can effectively simulate hitting a bump
dm = 2
mTot = dm*mTot
print mTot
# static contact forces
FF = mTot*g*xCoM/w # front wheel contact force [N]
FR = mTot*g - FF # rear wheel contact force [N]
# forces and moments at point A
FAx = -(FHr + FHl)*np.sin(lam)
FAz = (FHr + FHl)*np.cos(lam)
MAx = -(FHl - FHr)*lhw/2*np.cos(lam)
MAy = (FHr + FHl)*lh
# forces and moments at point B
FBx = FF*np.sin(lam)
FBz = -FF*np.cos(lam)
MBx = 0.0
MBy = FF*lfo*np.cos(lam)
# solve for the bearing reaction forces
A = np.array([[1, 1], [ls, ls + lhd]])
B = np.array([[-FAx - FBx], [-MAy - FBx*(ls + lhd + lf) - MBy]])
sol = np.linalg.solve(A, B)
FCx = sol[0]
FDx = sol[1]
# solve for the y bearing reaction forces
A = np.array([[1, 1], [ls, ls + lhd]])
B = np.array([[0.0], [-MAx]])
sol = np.linalg.solve(A, B)
FCy = sol[0]
FDy = sol[1]
# define the z coordinate
z = np.linspace(0, ls + lhd + lf, num=1000)
My = np.zeros_like(z)
Vx = np.zeros_like(z)
Mx = np.zeros_like(z)
Vy = np.zeros_like(z)
# calculate the moment and shear along the beam
for i, v in enumerate(z):
    if v <= ls:
        Vx[i] = FAx
        My[i] = FAx*v - MAy
        Vy[i] = 0.0
        Mx[i] = -MAx
    elif v > ls and v <= ls + lhd:
        Vx[i] = FAx + FCx
        My[i] = -MAy + FAx*v + FCx*(v - ls)
        Vy[i] = FCy
        Mx[i] = FCy*(v - ls) - MAx
    elif v > ls + lhd:
        Vx[i] = FAx + FCx + FDx
        My[i] = -MAy + FAx*v + FCx*(v - ls) + FDx*(v - ls - lhd)
        Vy[i] = FCy + FDy
        Mx[i] = FCy*(v - ls) + FDy*(v - ls - lhd) - MAx
# find the location between the bearings where the moment is zero
zM0 = (MAy + FCx*ls)/(FAx + FCx)
print zM0

title = 'Dynamic weight = {0} N\nHandlebar forces: left = {1} N, right = {2} N'.format(mTot*g, FHl, FHr)
# plot the shear/moment diagrams from the side
golden_mean = (np.sqrt(5) - 1.0) / 2.0
fig_width = 5.0
fig_height = fig_width * golden_mean
params = {'backend': 'ps',
          'axes.labelsize': 8,
          'ytick.labelsize': 6,
          'axes.titlesize': 8,
          'text.fontsize': 8,
          'legend.fontsize': 6,
          'xtick.labelsize': 6,
          'text.usetex': True,
          'figure.figsize': [fig_width,fig_height],
          'figure.dpi' : 200,
          'figure.title.fontsize': 8,
          'figure.subplot.bottom' : 0.1,
          'figure.subplot.hspace' : 0.05,
          }
plt.rcParams.update(params)
fig = plt.figure(0)

a = plt.subplot(411)
a.set_xticklabels('')
plt.title(title)
plt.plot(z, Vx)
plt.grid(b=True)
cylim = np.array(a.get_ylim())
mcylim = np.max(np.abs(cylim))
nylim = cylim + np.array([-0.1*mcylim, 0.1*mcylim])
plt.ylim(tuple(nylim))
plt.axvline(x = ls, color='k', linewidth=3)
plt.axvline(x = ls + lhd, color='k', linewidth=3)
plt.ylabel('Vx [N]')

a = plt.subplot(412)
a.set_xticklabels('')
plt.plot(z, My)
plt.grid(b=True)
cylim = np.array(a.get_ylim())
mcylim = np.max(np.abs(cylim))
nylim = cylim + np.array([-0.1*mcylim, 0.1*mcylim])
plt.ylim(tuple(nylim))
plt.axvline(x = ls, color='k', linewidth=3)
plt.axvline(x = ls + lhd, color='k', linewidth=3)
plt.ylabel('My [Nm]')

# plot the shear/moment diagrams from the front
a = plt.subplot(413)
a.set_xticklabels('')
plt.plot(z, Vy)
plt.grid(b=True)
cylim = np.array(a.get_ylim())
print cylim
mcylim = np.max(np.abs(cylim))
print mcylim
nylim = cylim + np.array([-0.1*mcylim, 0.1*mcylim])
print nylim
plt.ylim(tuple(nylim))
plt.axvline(x = ls, color='k', linewidth=3)
plt.axvline(x = ls + lhd, color='k', linewidth=3)
plt.ylabel('Vy [N]')

a = plt.subplot(414)
plt.plot(z, Mx)
plt.grid(b=True)
cylim = np.array(a.get_ylim())
mcylim = np.max(np.abs(cylim))
nylim = cylim + np.array([-0.1*mcylim, 0.1*mcylim])
plt.ylim(tuple(nylim))
plt.axvline(x = ls, color='k', linewidth=3)
plt.axvline(x = ls + lhd, color='k', linewidth=3)
plt.ylabel('Mx [Nm]')
plt.xlabel('z [m]')

plt.gcf().savefig('../../figures/davisbicycle/fork-load-diagram.png', dpi=200)
plt.gcf().savefig('../../figures/davisbicycle/fork-load-diagram.pdf')
plt.show()
