%---------------------------------------------------------------------%
% File: LateralForce.al
% Creation Date: November 23, 2011
% Author: Jason K. Moore
% Description: Generates the nonlinear and linear equations of motion
% for the Whipple bicycle model with four inputs. The additional input
% is a lateral force acting on the rear frame.
%---------------------------------------------------------------------%
%         Default Settings
%---------------------------------------------------------------------%

autoz on
autorhs off
overwrite all
beepsound off

%---------------------------------------------------------------------%
%         newtonian, bodies, frames, particles, points
%---------------------------------------------------------------------%

% declare the inertial reference frame

newtonian n

% declare two intermediate frames
% a: yaw frame
% b: roll frame

frames a, b

% declare the four bodies
% c: bicycle frame
% d: rear wheel
% e: fork/handlebar
% f: front wheel

bodies c, d, e, f

% declare two points for the wheel contacts
% dn: rear contact point
% fn: front contact point
% ce: steer axis point
% cl : lateral force point

points dn, fn, ce, cl

%---------------------------------------------------------------------%
%         constants and variables
%---------------------------------------------------------------------%

% rF: radius of front wheel
% rR: radius of rear wheel
% d1: the perpendicular distance from the steer axis to the center
%     of the rear wheel (rear offset)
% d2: the distance between the wheels along the steer axis
% d3: the perpendicular distance from the steer axis to the center
%     of the front wheel (fork offset)
% d4: the c1> distance from the rear wheel center to the lateral force point
% d5: the c3> distance from the rear wheel center to the lateral force point
% l1: the distance in the c1> direction from the center of the rear
%     wheel to the frame center of mass
% l2: the distance in the c3> direction from the center of the rear
%     wheel to the frame center of mass
% l3: the distance in the e1> direction from the front wheel center to
%     the center of mass of the fork
% l4: the distance in the e3> direction from the front wheel center to
%     the center of mass of the fork

constants rF, rR, d{1:5}, l{1:4}

% gravity

constants g

% masses

constants mc, md, me, mf

% inertia

constants ic11, ic22, ic33, ic31
constants id11, id22
constants ie11, ie22, ie33, ie31
constants if11, if22

% input torques
% T4: roll torque
% T6: rear wheel torque
% T7: steer torque
% input forces
% Fcl : lateral force

specified T4, T6, T7, Fcl

%---------------------------------------------------------------------%
% declare the generalized coordinates
%---------------------------------------------------------------------%

% q1:  perpendicular distance from the n2> axis to the rear contact
%      point in the ground plane
% q2:  perpendicular distance from the n1> axis to the rear contact
%      point in the ground plane
% q3:  frame yaw angle
% q4:  frame roll angle
% q5:  frame pitch angle
% q6:  rear wheel rotation angle
% q7:  steering rotation angle
% q8:  front wheel rotation angle

variables q{8}'

%---------------------------------------------------------------------%
%         generalized speeds
%---------------------------------------------------------------------%

motionvariables' u{8}'

%---------------------------------------------------------------------%
%         mass and inertia properties
%---------------------------------------------------------------------%

mass c=mc, d=md, e=me, f=mf
inertia c, ic11, ic22, ic33, 0, 0, ic31
inertia d, id11, id22, id11
inertia e, ie11, ie22, ie33, 0, 0, ie31
inertia f, if11, if22, if11

%---------------------------------------------------------------------%
%         angular relationships                                       %
%---------------------------------------------------------------------%

% frame yaw
simprot(n, a, 3, q3)

% frame roll
simprot(a, b, 1, q4)

% frame pitch
simprot(b, c, 2, q5)

% rear wheel rotation
simprot(c, d, 2, q6)

% steering angle
simprot(c, e, 3, q7)

% front wheel rotation
simprot(e, f, 2, q8)

%---------------------------------------------------------------------%
%         position vectors
%---------------------------------------------------------------------%

% locate the center of mass for each body

% newtonian origin to rear wheel center
p_no_do> = q1 * n1> + q2 * n2> - rR * b3>

% rear wheel center to bicycle frame center
p_do_co> = l1 * c1> + l2 * c3>

% rear wheel center to steer axis point
p_do_ce> = d1 * c1>

% steer axis point to the front wheel center
p_ce_fo> = d2 * c3> + d3 * e1>

% front wheel center to fork/handlebar center
p_fo_eo> = l3 * e1> + l4 * e3>

% locate the ground contact points
p_do_dn> = rR * b3>
p_fo_fn> = rF * unitvec(cross(cross(e2>, a3>), e2>))

% locate the lateral force point
p_do_cl> = d4 * c1> + d5 * c3>

%---------------------------------------------------------------------%
%         define the pitch configuration constraint
%---------------------------------------------------------------------%

% set the a3> component of p_dn_fn> equal to zero
pzero = dot(p_dn_fn>, a3>)

%---------------------------------------------------------------------%
%         define the kinematical differential equations
%---------------------------------------------------------------------%

q1' = u1
q2' = u2
q3' = u3
q4' = u4
q5' = u5
q6' = u6
q7' = u7
q8' = u8

%---------------------------------------------------------------------%
%         angular velocities
%---------------------------------------------------------------------%

angvel(n, a)
angvel(n, b)
angvel(n, c)
angvel(n, d)
angvel(n, e)
angvel(n, f)

%---------------------------------------------------------------------%
%         velocities
%---------------------------------------------------------------------%

v_do_n> = dt(p_no_do>, n)
v2pts(n, c, do, co)
v2pts(n, c, do, ce)
v2pts(n, e, ce, fo)
v2pts(n, e, ce, eo)

% wheel contact velocities
v2pts(n, d, do, dn)
v2pts(n, f, fo, fn)

% lateral force velocity
v2pts(n, c, do, cl)

%---------------------------------------------------------------------%
%         angular accelerations
%---------------------------------------------------------------------%

alf_c_n> = dt(w_c_n>, n)
alf_d_n> = dt(w_d_n>, n)
alf_e_n> = dt(w_e_n>, n)
alf_f_n> = dt(w_f_n>, n)

%---------------------------------------------------------------------%
%         accelerations
%---------------------------------------------------------------------%

a_do_n> = dt(v_do_n>, n)
a2pts(n, c, do, co)
a2pts(n, c, do, ce)
a2pts(n, e, ce, fo)
a2pts(n, e, ce, eo)

%---------------------------------------------------------------------%
%         forces and torques
%---------------------------------------------------------------------%

gravity(g * n3>, c, d, e, f)
force_cl> += Fcl * n2> % lateral force
torque(n/c, T4 * a1>) % roll torque
torque(c/d, T6 * c2>) % rear wheel torque
torque(c/e, T7 * c3>) % steer torque

%---------------------------------------------------------------------%
%         motion constraints
%---------------------------------------------------------------------%

% due to the assumptions of no side slip and no slip rolling the
% velocities of the front and rear wheel contact points, dn and fn,
% cannot have components of velocity in the ground plane

dependent[1] = dot(v_dn_n>, a1>)
dependent[2] = dot(v_dn_n>, a2>)
dependent[3] = dot(v_fn_n>, a1>)
dependent[4] = dot(v_fn_n>, a2>)

% this holonomic motion contraint is associated with the fact that the
% front wheel must touch the ground
dependent[5] = dt(pzero)

% the rear wheel angular speed, u6, the roll rate, u4,the steering rate, u7,
% are taken to be the independent generalized speeds

constrain(dependent[u1, u2, u3, u5, u8])

%---------------------------------------------------------------------%
%         equations of motion
%---------------------------------------------------------------------%

zero = fr() + frstar()
%solve(zero, u4', u6', u7')

unitsystem kg, meter, sec

input q1=0.0 m, q2=0.0 m, q3=0.0 rad, q4=0.0 rad, q5=0.0 rad, q6=0.0 rad, q7=0.0 rad, q8=0.0 rad
input u4=0.0 rad/s, u6=0.0 rad/s, u7=0.0 rad/s

output q1 m, q2 m, q3 rad, q4 rad, q5 rad, q6 rad, q7 rad, q8 rad
output u1 m/s, u2 m/s, u3 rad/s, u4 rad/s, u5 rad/s, u6 rad/s, u7 rad/s, u8 rad/s

code dynamics() LateralForceDynamics.c

%---------------------------------------------------------------------%
%         save output
%---------------------------------------------------------------------%

save LateralForce.all

%---------------------------------------------------------------------%
