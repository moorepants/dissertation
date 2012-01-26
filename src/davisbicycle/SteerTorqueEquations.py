import sympy as sym
import sympy.physics.mechanics as me

"""
This script calculates the actual steer torque applied to the handlebars as a
function of the measurements taken on the bicycle.
"""

#--------------------#
# measured constants #
#--------------------#

# d : distance from the handlebar center of mass to the point s on the steer
# axis
# ds1, ds3 : measure numbers for the location of the vectornav to the point on
# the steer axis, s
d, ds1, ds3 = sym.symbols('d ds1 ds3')

# handlebar inertia and mass
IG11, IG22, IG33, IG31 = sym.symbols('IG11 IG22 IG33 IG31')
mG = sym.symbols('mG')

#----------------------------------------------------------------#
# time varying signals that are directly measured on the bicycle #
#----------------------------------------------------------------#

# measured steer column torque and upper bearing friction force
Tm, Tu = me.dynamicsymbols('Tm Tu')
# steer angle and body fixed handlebar rate about steer axis
delta, wg3 = me.dynamicsymbols('delta wg3')
# body fixed angular rates of the bicycle frame
wb1, wb2, wb3  = me.dynamicsymbols('wb1 wb2 wb3')
# body fixed acceleration of the vectornav point
av1, av2, av3  = me.dynamicsymbols('av1 av2 av3')

#-----------------------------------------------------------------------#
# time varying signals that can be calculated from the measured signals #
#-----------------------------------------------------------------------#

# steer
deltad, wg3d = me.dynamicsymbols('delta wg3', 1)
# body fixed angular acceleration
wb1d, wb2d, wb3d  = me.dynamicsymbols('wb1 wb2 wb3', 1)

#-----------------------------#
# define the reference frames #
#-----------------------------#

# newtonian frame
N = me.ReferenceFrame('N', indices=('1', '2', '3'))
# bicycle frame
B = me.ReferenceFrame('B', indices=('1', '2', '3'))
# handlebar frame
G = me.ReferenceFrame('G', indices=('1', '2', '3'))
G.orient(B, 'Axis', (delta, B['3']))

#------------------------------------#
# define the locations of the points #
#------------------------------------#

# vectornav center
v = me.Point('v')

# point on the steer axis
s = me.Point('s')
s.set_pos(v, ds1 * B['1'] + ds3 * B['3'])

# handlebar center of mass
go = me.Point('go')
go.set_pos(s, d * G['1'])

#---------------------------------------------------#
# set the known angular velocites and accelerations #
#---------------------------------------------------#

# set the angular velocities of B and G
B.set_ang_vel(N, wb1 * B['1'] + wb2 * B['2'] + wb3 * B['3'])
G.set_ang_vel(N, (wb1 * sym.cos(delta) + wb2 * sym.sin(delta)) * G['1'] +
    (-wb1 * sym.sin(delta) + wb2 * sym.cos(delta)) * G['2'] + wg3 * G['3'])

# set the acceleration of point v
v.set_acc(N, av1 * B['1'] + av2 * B['2'] + av3 * B['3'])

#------------------------------------------------------------#
# calculate the acceleration of the handlebar center of mass #
#------------------------------------------------------------#

s.a2pt_theory(v, N, B)
go.a2pt_theory(s, N, G)

#-------------------------------#
# handlebar equations of motion #
#-------------------------------#

# calculate the angular momentum of the handlebar in N about the center of mass
# of the handlebar
IG = me.inertia(G, IG11, IG22, IG33, 0, 0, IG31)
H_G_N_go = IG.dot(G.ang_vel_in(N))

Hdot = H_G_N_go.dt(N)

# euler's equation about an arbitrary point, s
sumT = Hdot + go.pos_from(s).cross(mG * go.acc(N))

# calculate the steer torque
Tdelta = sumT.dot(G['3']) + Tm + Tu

# let's make use of the steer rate gyro and frame rate gyro measurement instead
# of differentiating delta
Tdelta = Tdelta.subs(deltad, wg3 - wb3)

print "Tdelta as a function of the measured data:\nTdelta =", Tdelta
