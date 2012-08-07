#!usr/bin/env python

# This file derives the non-linear equations of motion of the Whipple bicycle
# model.

import sympy as sym
import sympy.physics.mechanics as mec

mec.Vector.simp = False
#mec.Kane.simp = False # If True it takes forever to compute, probably more than and hour or even more! wft

##################
# Reference Frames
##################

# Newtonian Frame
N = mec.ReferenceFrame('N', indices=('1', '2', '3'),
        latexs=('\hat{n}_1', '\hat{n}_2', '\hat{n}_3'))
# Yaw Frame
A = mec.ReferenceFrame('A', indices=('1', '2', '3'),
        latexs=('\hat{a}_1', '\hat{a}_2', '\hat{a}_3'))
# Roll Frame
B = mec.ReferenceFrame('B', indices=('1', '2', '3'),
        latexs=('\hat{b}_1', '\hat{b}_2', '\hat{b}_3'))
# Pitch & Bicycle Frame
C = mec.ReferenceFrame('C', indices=('1', '2', '3'),
        latexs=('\hat{c}_1', '\hat{c}_2', '\hat{c}_3'))
# Rear Wheel Frame
D = mec.ReferenceFrame('D', indices=('1', '2', '3'),
        latexs=('\hat{d}_1', '\hat{d}_2', '\hat{d}_3'))
# Steer & Fork/Handlebar Frame
E = mec.ReferenceFrame('E', indices=('1', '2', '3'),
        latexs=('\hat{e}_1', '\hat{e}_2', '\hat{e}_3'))
# Front Wheel Frame
F = mec.ReferenceFrame('F', indices=('1', '2', '3'),
        latexs=('\hat{f}_1', '\hat{f}_2', '\hat{f}_3'))

####################################
# Generalized Coordinates and Speeds
####################################

# q1: perpendicular distance from the n2> axis to the rear contact
#     point in the ground plane
# q2: perpendicular distance from the n1> axis to the rear contact
#     point in the ground plane
# q3: frame yaw angle
# q4: frame roll angle
# q5: frame pitch angle
# q6: rear wheel rotation angle
# q7: steering rotation angle
# q8: front wheel rotation angle
q1, q2, q3, q4 = mec.dynamicsymbols('q1 q2 q3 q4')
q5, q6, q7, q8 = mec.dynamicsymbols('q5 q6 q7 q8')
q1d, q2d, q3d, q4d = mec.dynamicsymbols('q1 q2 q3 q4', 1)
q5d, q6d, q7d, q8d = mec.dynamicsymbols('q5 q6 q7 q8', 1)

u1, u2, u3, u4 = mec.dynamicsymbols('u1 u2 u3 u4')
u5, u6, u7, u8 = mec.dynamicsymbols('u5 u6 u7 u8')
u1d, u2d, u3d, u4d = mec.dynamicsymbols('u1 u2 u3 u4', 1)
u5d, u6d, u7d, u8d = mec.dynamicsymbols('u5 u6 u7 u8', 1)

#################################
# Orientation of Reference Frames
#################################

# bicycle frame yaw
A.orient(N, 'Axis', [q3, N['3']])
# bicycle frame roll
B.orient(A, 'Axis', [q4, A['1']])
# bicycle frame pitch
C.orient(B, 'Axis', [q5, B['2']])
# rear wheel rotation
D.orient(C, 'Axis', [q6, C['2']])
# fork/handlebar steer
E.orient(C, 'Axis', [q7, C['3']])
# front wheel rotation
F.orient(E, 'Axis', [q8, E['2']])

###########
# Constants
###########

# geometry
# rf: radius of front wheel
# rr: radius of rear wheel
# d1: the perpendicular distance from the steer axis to the center
#     of the rear wheel (rear offset)
# d2: the distance between wheels along the steer axis
# d3: the perpendicular distance from the steer axis to the center
#     of the front wheel (fork offset)
# l1: the distance in the c1> direction from the center of the rear
#     wheel to the frame center of mass
# l2: the distance in the c3> direction from the center of the rear
#     wheel to the frame center of mass
# l3: the distance in the e1> direction from the front wheel center to
#     the center of mass of the fork
# l4: the distance in the e3> direction from the front wheel center to
#     the center of mass of the fork

rf, rr = sym.symbols('rf rr')
d1, d2, d3 = sym.symbols('d1 d2 d3')
l1, l2, l3, l4 = sym.symbols('l1 l2 l3 l4')

# acceleration due to gravity
g = sym.symbols('g')

# mass
mc, md, me, mf = sym.symbols('mc md me mf')

# inertia
ic11, ic22, ic33, ic31 = sym.symbols('ic11 ic22 ic33 ic31')
id11, id22 = sym.symbols('id11 id22')
ie11, ie22, ie33, ie31 = sym.symbols('ie11 ie22 ie33 ie31')
if11, if22 = sym.symbols('if11 if22')

###########
# Specified
###########

# control torques
# T4 : roll torque
# T6 : rear wheel torque
# T7 : steer torque
T4, T6, T7 = mec.dynamicsymbols('T4 T6 T7')

###################
# Positions Vectors
###################

# newtonian origin
no = mec.Point('no')

# newtonian origin to rear wheel center
do = mec.Point('do')
do.set_pos(no, q1 * N['1'] + q2 * N['2'] - rr * B['3'])

# rear wheel center to bicycle frame center
co = mec.Point('co')
co.set_pos(do, l1 * C['1'] + l2 * C['3'])

# rear wheel center to steer axis point
ce = mec.Point('ce')
ce.set_pos(do, d1 * C['1'])

# steer axis point to the front wheel center
fo = mec.Point('fo')
fo.set_pos(ce, d2 * E['3'] + d3 * E['1'])

# front wheel center to fork/handlebar center
eo = mec.Point('eo')
eo.set_pos(fo, l3 * E['1'] + l4 * E['3'])

# locate the points fixed on the wheel which instaneously touch the ground
# rear
dn = mec.Point('dn')
dn.set_pos(do, rr * B['3'])
# front
fn = mec.Point('fn')
fn.set_pos(fo, rf * E['2'].cross(A['3']).cross(E['2']).normalize())

######################
# Holonomic Constraint
######################

# this constraint is enforced so that the front wheel contacts the ground
holonomic = fn.pos_from(dn).dot(A['3'])

####################################
# Kinematical Differential Equations
####################################

kinematical = [q1d - u1,
               q2d - u2,
               q3d - u3,
               q4d - u4,
               q5d - u5,
               q6d - u6,
               q7d - u7,
               q8d - u8]

####################
# Angular Velocities
####################

A.set_ang_vel(N, u3 * N['3'])
B.set_ang_vel(A, u4 * A['1'])
C.set_ang_vel(B, u5 * B['2'])
D.set_ang_vel(C, u6 * C['2'])
E.set_ang_vel(C, u7 * C['3'])
F.set_ang_vel(E, u8 * E['2'])

###################
# Linear Velocities
###################

# origin is fixed
no.set_vel(N, 0.0 * N['1'])

# mass centers
do.set_vel(N, do.pos_from(no).dt(N).subs({q1d:u1, q2d:u2}))
co.v2pt_theory(do, N, C)
ce.v2pt_theory(do, N, C)
fo.v2pt_theory(ce, N, E)
eo.v2pt_theory(fo, N, E)

# wheel contact velocities
dn.v2pt_theory(do, N, D)
fn.v2pt_theory(fo, N, F)

######################
# Linear Accelerations
######################

#do.set_acc(N, do.vel(N).dt(N))
#co.a2pt_theory(do, N, C)
#ce.a2pt_theory(do, N, C)
#fo.a2pt_theory(ce, N, E)
#eo.a2pt_theory(fo, N, E)

####################
# Motion Constraints
####################

# this definition is causing problems because it is difficult to solve for the
# independent u's with 5 equations with 3 being really long, basically
# Kane.speeds seems to balk on anything that is complicated if Kane.simp=True
nonholonomic = [dn.vel(N).dot(A['1'].simplify()),
                dn.vel(N).dot(A['2'].simplify()),
                fn.vel(N).dot(A['1']),
                fn.vel(N).dot(A['2']),
                holonomic.diff(mec.dynamicsymbols._t).subs({q4d:u4, q5d:u5,
                    q7d:u7})]
#########
# Inertia
#########

Ic = mec.inertia(C, ic11, ic22, ic33, 0.0, 0.0, ic31)
Id = mec.inertia(D, id11, id22, id11, 0.0, 0.0, 0.0)
Ie = mec.inertia(E, ie11, ie22, ie33, 0.0, 0.0, ie31)
If = mec.inertia(F, if11, if22, if11, 0.0, 0.0, 0.0)

##############
# Rigid Bodies
##############

rearFrame = mec.RigidBody('Rear Frame', co, C, mc, (Ic, co))
rearWheel = mec.RigidBody('Rear Wheel', do, D, md, (Id, do))
frontFrame = mec.RigidBody('Front Frame', eo, E, me, (Ie, eo))
frontWheel = mec.RigidBody('Front Wheel', fo, F, mf, (If, fo))

bodyList = [rearFrame, rearWheel, frontFrame, frontWheel]

###########################
# Generalized Active Forces
###########################

# gravity
Fco = (co, mc * g * A['3'])
Fdo = (do, md * g * A['3'])
Feo = (eo, me * g * A['3'])
Ffo = (fo, mf * g * A['3'])

# input torques
Tc = (C, T4 * A['1'] - T6 * C['2'] - T7 * C['3'])
Td = (D, T6 * C['2'])
Te = (E, T7 * C['3'])

forceList = [Fco, Fdo, Feo, Ffo, Tc, Td, Te]

###############
# Kane's Method
###############

kane = mec.Kane(N)
kane.coords([q1, q2, q3, q4, q6, q7, q8], qdep=[q5], coneqs=[holonomic])
print('Computing speeds.')
mec.Kane.simp = False
# This method takes forever if you have Kane.simp=False. This can't be that
# hard of a computation...but maybe we are supplying something wrong.
kane.speeds([u4, u6, u7], udep=[u1, u2, u3, u5, u8], coneqs=nonholonomic)
print('Done.')
mec.Kane.simp = True
print('Computing kindiffeq.')
kane.kindiffeq(kinematical)
print('Done.')
fr, frstar = kane.kanes_equations(forceList, bodyList)
M = kane.mass_matrix_full
F = kane.forcing_full

# Linearization
# this is incomplete

#FA, FB, u = kane.linearize()
#
#Mred = M.extract([3, 5, 8, 10], [3, 5, 8, 10])
#v = sym.symbols('v')
#test = Mred.subs({q1: 0.0,
                  #q2: 0.0,
                  #q3: 0.0,
                  #q4: 0.0,
           #q5: 0.314,
           #q6: 0.0,
           #q7: 0.0,
           #q8: 0.0,
           #u1: 0.0,
           #u2: 0.0,
           #u3: 0.0,
           #u4: 0.0,
           #u5: 0.0,
           #u6: -v / rr,
           #u7: 0.0,
           #u8: -v / rf})
#
#FAred = FA.extract([3, 5, 8, 10], [3, 5, 7, 9])
#
#bp = benchmark_parameters()
#mp = benchmark_to_moore(bp)
#subs = {eval(k) : v for k, v in mp.items()}
# # add in the linearization point substitutions
#
## Not sure of the proper solve method to use here
#A = sym.solve(Mred.subs(subs), FAred.subs(subs))
