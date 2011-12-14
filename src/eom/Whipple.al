%---------------------------------------------------------------------%
% File: Whipple.al
% Creation Date: October 4, 2011
% Author: Jason K. Moore
% Description: Generates the nonlinear and linear equations of motion
% for the Whipple bicycle model with three inputs. This is the code for
% generating the Whipple model described in my dissertation.
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

points dn, fn

% declare a point on the steer axis
points ce

%---------------------------------------------------------------------%
%         constants and variables
%---------------------------------------------------------------------%

% rf: radius of front wheel
% rr: radius of rear wheel
% d1: the perpendicular distance from the steer axis to the center
%     of the rear wheel (rear offset)
% d2: the distance between the intersections of the front and rear
%     offset lines with the steer axis
% d3: the perpendicular distance from the steer axis to the center
%     of the front wheel (fork offset)
% l1: the distance in the c1> direction from the center of the rear
%     wheel to the frame center of mass
% l2: the distance in the c3> direction from the center of the rear
%     wheel to the frame center of mass
% l3: the distance in the e1> direction from the front wheel center to
%     the center of mass of the fork
% l4: the distance in the e3> direction from the front wheel center to
%     the center of mass of the fork

constants rf, rr, d{1:3}, l{1:4}

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

specified T4, T6, T7

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
p_no_do> = q1 * n1> + q2 * n2> - rr * b3>

% rear wheel center to bicycle frame center
p_do_co> = l1 * c1> + l2 * c3>

% rear wheel center to steer axis point
p_do_ce> = d1 * c1>

% steer axis point to the front wheel center
p_ce_fo> = d2 * c3> + d3 * e1>

% front wheel center to fork/handlebar center
p_fo_eo> = l3 * e1> + l4 * e3>

% locate the ground contact points
p_do_dn> = rr * b3>
p_fo_fn> = rf * unitvec(cross(cross(e2>, a3>), e2>))

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
torque(n/c, T4 * a1>) % roll torque
torque(c/d, T6 * c2>) % rear wheel torque
torque(c/e, T7 * c3>) % steer torque

%---------------------------------------------------------------------%
%         equations of motion
%---------------------------------------------------------------------%

zero = fr() + frstar()
solve(zero, u4', u6', u7')

%---------------------------------------------------------------------%
%         linearization
%---------------------------------------------------------------------%
% linearizes the equations of motion by generating A, B, C, and D where
% x' = A(dx) * x + B(dx) * u
% y = C(dx) * x + D(dx) * u
% and dx is the point at which the system is linearized about.
%
% Warning: These partials do not take into account the fact that q5 is
% a dependent coordinate.

A[1, 1] = d(q1', q1)
A[1, 2] = d(q1', q2)
A[1, 3] = d(q1', q3)
A[1, 4] = d(q1', q4)
A[1, 5] = d(q1', q5)
A[1, 6] = d(q1', q6)
A[1, 7] = d(q1', q7)
A[1, 8] = d(q1', q8)
A[1, 9] = d(q1', u4)
A[1, 10] = d(q1', u6)
A[1, 11] = d(q1', u7)

A[2, 1] = d(q2', q1)
A[2, 2] = d(q2', q2)
A[2, 3] = d(q2', q3)
A[2, 4] = d(q2', q4)
A[2, 5] = d(q2', q5)
A[2, 6] = d(q2', q6)
A[2, 7] = d(q2', q7)
A[2, 8] = d(q2', q8)
A[2, 9] = d(q2', u4)
A[2, 10] = d(q2', u6)
A[2, 11] = d(q2', u7)

A[3, 1] = d(q3', q1)
A[3, 2] = d(q3', q2)
A[3, 3] = d(q3', q3)
A[3, 4] = d(q3', q4)
A[3, 5] = d(q3', q5)
A[3, 6] = d(q3', q6)
A[3, 7] = d(q3', q7)
A[3, 8] = d(q3', q8)
A[3, 9] = d(q3', u4)
A[3, 10] = d(q3', u6)
A[3, 11] = d(q3', u7)

A[4, 1] = d(q4', q1)
A[4, 2] = d(q4', q2)
A[4, 3] = d(q4', q3)
A[4, 4] = d(q4', q4)
A[4, 5] = d(q4', q5)
A[4, 6] = d(q4', q6)
A[4, 7] = d(q4', q7)
A[4, 8] = d(q4', q8)
A[4, 9] = d(q4', u4)
A[4, 10] = d(q4', u6)
A[4, 11] = d(q4', u7)

A[5, 1] = d(q5', q1)
A[5, 2] = d(q5', q2)
A[5, 3] = d(q5', q3)
A[5, 4] = d(q5', q4)
A[5, 5] = d(q5', q5)
A[5, 6] = d(q5', q6)
A[5, 7] = d(q5', q7)
A[5, 8] = d(q5', q8)
A[5, 9] = d(q5', u4)
A[5, 10] = d(q5', u6)
A[5, 11] = d(q5', u7)

A[6, 1] = d(q6', q1)
A[6, 2] = d(q6', q2)
A[6, 3] = d(q6', q3)
A[6, 4] = d(q6', q4)
A[6, 5] = d(q6', q5)
A[6, 6] = d(q6', q6)
A[6, 7] = d(q6', q7)
A[6, 8] = d(q6', q8)
A[6, 9] = d(q6', u4)
A[6, 10] = d(q6', u6)
A[6, 11] = d(q6', u7)

A[7, 1] = d(q7', q1)
A[7, 2] = d(q7', q2)
A[7, 3] = d(q7', q3)
A[7, 4] = d(q7', q4)
A[7, 5] = d(q7', q5)
A[7, 6] = d(q7', q6)
A[7, 7] = d(q7', q7)
A[7, 8] = d(q7', q8)
A[7, 9] = d(q7', u4)
A[7, 10] = d(q7', u6)
A[7, 11] = d(q7', u7)

A[8, 1] = d(q8', q1)
A[8, 2] = d(q8', q2)
A[8, 3] = d(q8', q3)
A[8, 4] = d(q8', q4)
A[8, 5] = d(q8', q5)
A[8, 6] = d(q8', q6)
A[8, 7] = d(q8', q7)
A[8, 8] = d(q8', q8)
A[8, 9] = d(q8', u4)
A[8, 10] = d(q8', u6)
A[8, 11] = d(q8', u7)

A[9, 1] = d(u4', q1)
A[9, 2] = d(u4', q2)
A[9, 3] = d(u4', q3)
A[9, 4] = d(u4', q4)
A[9, 5] = d(u4', q5)
A[9, 6] = d(u4', q6)
A[9, 7] = d(u4', q7)
A[9, 8] = d(u4', q8)
A[9, 9] = d(u4', u4)
A[9, 10] = d(u4', u6)
A[9, 11] = d(u4', u7)

A[10, 1] = d(u6', q1)
A[10, 2] = d(u6', q2)
A[10, 3] = d(u6', q3)
A[10, 4] = d(u6', q4)
A[10, 5] = d(u6', q5)
A[10, 6] = d(u6', q6)
A[10, 7] = d(u6', q7)
A[10, 8] = d(u6', q8)
A[10, 9] = d(u6', u4)
A[10, 10] = d(u6', u6)
A[10, 11] = d(u6', u7)

A[11, 1] = d(u7', q1)
A[11, 2] = d(u7', q2)
A[11, 3] = d(u7', q3)
A[11, 4] = d(u7', q4)
A[11, 5] = d(u7', q5)
A[11, 6] = d(u7', q6)
A[11, 7] = d(u7', q7)
A[11, 8] = d(u7', q8)
A[11, 9] = d(u7', u4)
A[11, 10] = d(u7', u6)
A[11, 11] = d(u7', u7)

B[1, 1] = d(q1', T4)
B[1, 2] = d(q1', T6)
B[1, 3] = d(q1', T7)

B[2, 1] = d(q2', T4)
B[2, 2] = d(q2', T6)
B[2, 3] = d(q2', T7)

B[3, 1] = d(q3', T4)
B[3, 2] = d(q3', T6)
B[3, 3] = d(q3', T7)

B[4, 1] = d(q4', T4)
B[4, 2] = d(q4', T6)
B[4, 3] = d(q4', T7)

B[5, 1] = d(q5', T4)
B[5, 2] = d(q5', T6)
B[5, 3] = d(q5', T7)

B[6, 1] = d(q6', T4)
B[6, 2] = d(q6', T6)
B[6, 3] = d(q6', T7)

B[7, 1] = d(q7', T4)
B[7, 2] = d(q7', T6)
B[7, 3] = d(q7', T7)

B[8, 1] = d(q8', T4)
B[8, 2] = d(q8', T6)
B[8, 3] = d(q8', T7)

B[9, 1] = d(u4', T4)
B[9, 2] = d(u4', T6)
B[9, 3] = d(u4', T7)

B[10, 1] = d(u6', T4)
B[10, 2] = d(u6', T6)
B[10, 3] = d(u6', T7)

B[11, 1] = d(u7', T4)
B[11, 2] = d(u7', T6)
B[11, 3] = d(u7', T7)

C[1, 1] = d(q1, q1)
C[1, 2] = d(q1, q2)
C[1, 3] = d(q1, q3)
C[1, 4] = d(q1, q4)
C[1, 5] = d(q1, q5)
C[1, 6] = d(q1, q6)
C[1, 7] = d(q1, q7)
C[1, 8] = d(q1, q8)
C[1, 9] = d(q1, u4)
C[1, 10] = d(q1, u6)
C[1, 11] = d(q1, u7)

C[2, 1] = d(q2, q1)
C[2, 2] = d(q2, q2)
C[2, 3] = d(q2, q3)
C[2, 4] = d(q2, q4)
C[2, 5] = d(q2, q5)
C[2, 6] = d(q2, q6)
C[2, 7] = d(q2, q7)
C[2, 8] = d(q2, q8)
C[2, 9] = d(q2, u4)
C[2, 10] = d(q2, u6)
C[2, 11] = d(q2, u7)

C[3, 1] = d(q3, q1)
C[3, 2] = d(q3, q2)
C[3, 3] = d(q3, q3)
C[3, 4] = d(q3, q4)
C[3, 5] = d(q3, q5)
C[3, 6] = d(q3, q6)
C[3, 7] = d(q3, q7)
C[3, 8] = d(q3, q8)
C[3, 9] = d(q3, u4)
C[3, 10] = d(q3, u6)
C[3, 11] = d(q3, u7)

C[4, 1] = d(q4, q1)
C[4, 2] = d(q4, q2)
C[4, 3] = d(q4, q3)
C[4, 4] = d(q4, q4)
C[4, 5] = d(q4, q5)
C[4, 6] = d(q4, q6)
C[4, 7] = d(q4, q7)
C[4, 8] = d(q4, q8)
C[4, 9] = d(q4, u4)
C[4, 10] = d(q4, u6)
C[4, 11] = d(q4, u7)

C[5, 1] = d(q5, q1)
C[5, 2] = d(q5, q2)
C[5, 3] = d(q5, q3)
C[5, 4] = d(q5, q4)
C[5, 5] = d(q5, q5)
C[5, 6] = d(q5, q6)
C[5, 7] = d(q5, q7)
C[5, 8] = d(q5, q8)
C[5, 9] = d(q5, u4)
C[5, 10] = d(q5, u6)
C[5, 11] = d(q5, u7)

C[6, 1] = d(q6, q1)
C[6, 2] = d(q6, q2)
C[6, 3] = d(q6, q3)
C[6, 4] = d(q6, q4)
C[6, 5] = d(q6, q5)
C[6, 6] = d(q6, q6)
C[6, 7] = d(q6, q7)
C[6, 8] = d(q6, q8)
C[6, 9] = d(q6, u4)
C[6, 10] = d(q6, u6)
C[6, 11] = d(q6, u7)

C[7, 1] = d(q7, q1)
C[7, 2] = d(q7, q2)
C[7, 3] = d(q7, q3)
C[7, 4] = d(q7, q4)
C[7, 5] = d(q7, q5)
C[7, 6] = d(q7, q6)
C[7, 7] = d(q7, q7)
C[7, 8] = d(q7, q8)
C[7, 9] = d(q7, u4)
C[7, 10] = d(q7, u6)
C[7, 11] = d(q7, u7)

C[8, 1] = d(q8, q1)
C[8, 2] = d(q8, q2)
C[8, 3] = d(q8, q3)
C[8, 4] = d(q8, q4)
C[8, 5] = d(q8, q5)
C[8, 6] = d(q8, q6)
C[8, 7] = d(q8, q7)
C[8, 8] = d(q8, q8)
C[8, 9] = d(q8, u4)
C[8, 10] = d(q8, u6)
C[8, 11] = d(q8, u7)

C[9, 1] = d(u1, q1)
C[9, 2] = d(u1, q2)
C[9, 3] = d(u1, q3)
C[9, 4] = d(u1, q4)
C[9, 5] = d(u1, q5)
C[9, 6] = d(u1, q6)
C[9, 7] = d(u1, q7)
C[9, 8] = d(u1, q8)
C[9, 9] = d(u1, u4)
C[9, 10] = d(u1, u6)
C[9, 11] = d(u1, u7)

C[10, 1] = d(u2, q1)
C[10, 2] = d(u2, q2)
C[10, 3] = d(u2, q3)
C[10, 4] = d(u2, q4)
C[10, 5] = d(u2, q5)
C[10, 6] = d(u2, q6)
C[10, 7] = d(u2, q7)
C[10, 8] = d(u2, q8)
C[10, 9] = d(u2, u4)
C[10, 10] = d(u2, u6)
C[10, 11] = d(u2, u7)

C[11, 1] = d(u3, q1)
C[11, 2] = d(u3, q2)
C[11, 3] = d(u3, q3)
C[11, 4] = d(u3, q4)
C[11, 5] = d(u3, q5)
C[11, 6] = d(u3, q6)
C[11, 7] = d(u3, q7)
C[11, 8] = d(u3, q8)
C[11, 9] = d(u3, u4)
C[11, 10] = d(u3, u6)
C[11, 11] = d(u3, u7)

C[12, 1] = d(u4, q1)
C[12, 2] = d(u4, q2)
C[12, 3] = d(u4, q3)
C[12, 4] = d(u4, q4)
C[12, 5] = d(u4, q5)
C[12, 6] = d(u4, q6)
C[12, 7] = d(u4, q7)
C[12, 8] = d(u4, q8)
C[12, 9] = d(u4, u4)
C[12, 10] = d(u4, u6)
C[12, 11] = d(u4, u7)

C[13, 1] = d(u5, q1)
C[13, 2] = d(u5, q2)
C[13, 3] = d(u5, q3)
C[13, 4] = d(u5, q4)
C[13, 5] = d(u5, q5)
C[13, 6] = d(u5, q6)
C[13, 7] = d(u5, q7)
C[13, 8] = d(u5, q8)
C[13, 9] = d(u5, u4)
C[13, 10] = d(u5, u6)
C[13, 11] = d(u5, u7)

C[14, 1] = d(u6, q1)
C[14, 2] = d(u6, q2)
C[14, 3] = d(u6, q3)
C[14, 4] = d(u6, q4)
C[14, 5] = d(u6, q5)
C[14, 6] = d(u6, q6)
C[14, 7] = d(u6, q7)
C[14, 8] = d(u6, q8)
C[14, 9] = d(u6, u4)
C[14, 10] = d(u6, u6)
C[14, 11] = d(u6, u7)

C[15, 1] = d(u7, q1)
C[15, 2] = d(u7, q2)
C[15, 3] = d(u7, q3)
C[15, 4] = d(u7, q4)
C[15, 5] = d(u7, q5)
C[15, 6] = d(u7, q6)
C[15, 7] = d(u7, q7)
C[15, 8] = d(u7, q8)
C[15, 9] = d(u7, u4)
C[15, 10] = d(u7, u6)
C[15, 11] = d(u7, u7)

C[16, 1] = d(u8, q1)
C[16, 2] = d(u8, q2)
C[16, 3] = d(u8, q3)
C[16, 4] = d(u8, q4)
C[16, 5] = d(u8, q5)
C[16, 6] = d(u8, q6)
C[16, 7] = d(u8, q7)
C[16, 8] = d(u8, q8)
C[16, 9] = d(u8, u4)
C[16, 10] = d(u8, u6)
C[16, 11] = d(u8, u7)

C[17, 1] = d(u1', q1)
C[17, 2] = d(u1', q2)
C[17, 3] = d(u1', q3)
C[17, 4] = d(u1', q4)
C[17, 5] = d(u1', q5)
C[17, 6] = d(u1', q6)
C[17, 7] = d(u1', q7)
C[17, 8] = d(u1', q8)
C[17, 9] = d(u1', u4)
C[17, 10] = d(u1', u6)
C[17, 11] = d(u1', u7)

C[18, 1] = d(u2', q1)
C[18, 2] = d(u2', q2)
C[18, 3] = d(u2', q3)
C[18, 4] = d(u2', q4)
C[18, 5] = d(u2', q5)
C[18, 6] = d(u2', q6)
C[18, 7] = d(u2', q7)
C[18, 8] = d(u2', q8)
C[18, 9] = d(u2', u4)
C[18, 10] = d(u2', u6)
C[18, 11] = d(u2', u7)

C[19, 1] = d(u3', q1)
C[19, 2] = d(u3', q2)
C[19, 3] = d(u3', q3)
C[19, 4] = d(u3', q4)
C[19, 5] = d(u3', q5)
C[19, 6] = d(u3', q6)
C[19, 7] = d(u3', q7)
C[19, 8] = d(u3', q8)
C[19, 9] = d(u3', u4)
C[19, 10] = d(u3', u6)
C[19, 11] = d(u3', u7)

C[20, 1] = d(u4', q1)
C[20, 2] = d(u4', q2)
C[20, 3] = d(u4', q3)
C[20, 4] = d(u4', q4)
C[20, 5] = d(u4', q5)
C[20, 6] = d(u4', q6)
C[20, 7] = d(u4', q7)
C[20, 8] = d(u4', q8)
C[20, 9] = d(u4', u4)
C[20, 10] = d(u4', u6)
C[20, 11] = d(u4', u7)

C[21, 1] = d(u5', q1)
C[21, 2] = d(u5', q2)
C[21, 3] = d(u5', q3)
C[21, 4] = d(u5', q4)
C[21, 5] = d(u5', q5)
C[21, 6] = d(u5', q6)
C[21, 7] = d(u5', q7)
C[21, 8] = d(u5', q8)
C[21, 9] = d(u5', u4)
C[21, 10] = d(u5', u6)
C[21, 11] = d(u5', u7)

C[22, 1] = d(u6', q1)
C[22, 2] = d(u6', q2)
C[22, 3] = d(u6', q3)
C[22, 4] = d(u6', q4)
C[22, 5] = d(u6', q5)
C[22, 6] = d(u6', q6)
C[22, 7] = d(u6', q7)
C[22, 8] = d(u6', q8)
C[22, 9] = d(u6', u4)
C[22, 10] = d(u6', u6)
C[22, 11] = d(u6', u7)

C[23, 1] = d(u7', q1)
C[23, 2] = d(u7', q2)
C[23, 3] = d(u7', q3)
C[23, 4] = d(u7', q4)
C[23, 5] = d(u7', q5)
C[23, 6] = d(u7', q6)
C[23, 7] = d(u7', q7)
C[23, 8] = d(u7', q8)
C[23, 9] = d(u7', u4)
C[23, 10] = d(u7', u6)
C[23, 11] = d(u7', u7)

C[24, 1] = d(u8', q1)
C[24, 2] = d(u8', q2)
C[24, 3] = d(u8', q3)
C[24, 4] = d(u8', q4)
C[24, 5] = d(u8', q5)
C[24, 6] = d(u8', q6)
C[24, 7] = d(u8', q7)
C[24, 8] = d(u8', q8)
C[24, 9] = d(u8', u4)
C[24, 10] = d(u8', u6)
C[24, 11] = d(u8', u7)

D[1, 1] = d(q1, T4)
D[1, 2] = d(q1, T6)
D[1, 3] = d(q1, T7)

D[2, 1] = d(q2, T4)
D[2, 2] = d(q2, T6)
D[2, 3] = d(q2, T7)

D[3, 1] = d(q3, T4)
D[3, 2] = d(q3, T6)
D[3, 3] = d(q3, T7)

D[4, 1] = d(q4, T4)
D[4, 2] = d(q4, T6)
D[4, 3] = d(q4, T7)

D[5, 1] = d(q5, T4)
D[5, 2] = d(q5, T6)
D[5, 3] = d(q5, T7)

D[6, 1] = d(q6, T4)
D[6, 2] = d(q6, T6)
D[6, 3] = d(q6, T7)

D[7, 1] = d(q7, T4)
D[7, 2] = d(q7, T6)
D[7, 3] = d(q7, T7)

D[8, 1] = d(q8, T4)
D[8, 2] = d(q8, T6)
D[8, 3] = d(q8, T7)

D[9, 1] = d(u1, T4)
D[9, 2] = d(u1, T6)
D[9, 3] = d(u1, T7)

D[10, 1] = d(u2, T4)
D[10, 2] = d(u2, T6)
D[10, 3] = d(u2, T7)

D[11, 1] = d(u3, T4)
D[11, 2] = d(u3, T6)
D[11, 3] = d(u3, T7)

D[12, 1] = d(u4, T4)
D[12, 2] = d(u4, T6)
D[12, 3] = d(u4, T7)

D[13, 1] = d(u5, T4)
D[13, 2] = d(u5, T6)
D[13, 3] = d(u5, T7)

D[14, 1] = d(u6, T4)
D[14, 2] = d(u6, T6)
D[14, 3] = d(u6, T7)

D[15, 1] = d(u7, T4)
D[15, 2] = d(u7, T6)
D[15, 3] = d(u7, T7)

D[16, 1] = d(u8, T4)
D[16, 2] = d(u8, T6)
D[16, 3] = d(u8, T7)

D[17, 1] = d(u1', T4)
D[17, 2] = d(u1', T6)
D[17, 3] = d(u1', T7)

D[18, 1] = d(u2', T4)
D[18, 2] = d(u2', T6)
D[18, 3] = d(u2', T7)

D[19, 1] = d(u3', T4)
D[19, 2] = d(u3', T6)
D[19, 3] = d(u3', T7)

D[20, 1] = d(u4', T4)
D[20, 2] = d(u4', T6)
D[20, 3] = d(u4', T7)

D[21, 1] = d(u5', T4)
D[21, 2] = d(u5', T6)
D[21, 3] = d(u5', T7)

D[22, 1] = d(u6', T4)
D[22, 2] = d(u6', T6)
D[22, 3] = d(u6', T7)

D[23, 1] = d(u7', T4)
D[23, 2] = d(u7', T6)
D[23, 3] = d(u7', T7)

D[24, 1] = d(u8', T4)
D[24, 2] = d(u8', T6)
D[24, 3] = d(u8', T7)

encode A, B, C, D

unitsystem kg, meter, sec

input q1=0.0 m, q2=0.0 m, q3=0.0 rad, q4=0.0 rad, q5=0.0 rad, &
      q6=0.0 rad, q7=0.0 rad, q8=0.0 rad
input u4=0.0 rad/s, u6=0.0 rad/s, u7=0.0 rad/s

output q1 m, q2 m, q3 rad, q4 rad, q5 rad, q6 rad, q7 rad, q8 rad
output u1 m/s, u2 m/s, u3 rad/s, u4 rad/s, u5 rad/s, u6 rad/s, &
       u7 rad/s, u8 rad/s
output u1' m/s^2, u2' m/s^2, u3' rad/s^2, u4' rad/s^2, u5' rad/s^2, &
       u6' rad/s^2, u7' rad/s^2, u8' rad/s^2

code dynamics() WhippleDynamics.c

%---------------------------------------------------------------------%
%         save output
%---------------------------------------------------------------------%

save Whipple.all

%---------------------------------------------------------------------%
