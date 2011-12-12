%---------------------------------------------------------------------%
% File: Arms.al
% Creation Date: December 9, 2011
% Author: Jason K. Moore
% Description: Generates the nonlinear and linear equations of motion
% for an extended Whipple bicycle model with four inputs: roll torque,
% rear wheel torque, steer torque and a lateral force at a point on the
% bicycle frame. The extension includes four rigid bodies that model
% the upper and lower arms of the rider and their motion with respect
% to the steer angle.

%---------------------------------------------------------------------%
%         default settings
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

% declare the four bicycle bodies
% c: rear frame
% d: rear wheel
% e: front frame
% f: front wheel

bodies c, d, e, f

% declare the four rider bodies
% g: right upper arm
% h: right lower arm
% i: left upper arm
% j: left lower arm

bodies g, h, i, j

%---------------------------------------------------------------------%
%         points
%---------------------------------------------------------------------%

% declare two points for the wheel contacts
% dn: rear contact point
% fn: front contact point

points dn, fn

% ce: steer axis point
% cl : lateral force point

points ce, cl

% declare points to locate the rider's arms
% sr: right shoulder
% sl: left shoulder
% er: right elbow
% el: left elbow
% hr: right hand
% hl: left hand
% gr: right handlebar grip
% gl: left handlebar grip

points sr, sl, er, el, hr, hl, gr, gl

%---------------------------------------------------------------------%
%         constants and variables
%---------------------------------------------------------------------%

% rf: radius of front wheel
% rr: radius of rear wheel
% d1: the perpendicular distance from the steer axis to the center
%     of the rear wheel (rear offset)
% d2: the distance between the wheels along the steer axis
% d3: the perpendicular distance from the steer axis to the center
%     of the front wheel (fork offset)
% d4: the c1> distance from the rear wheel center to the lateral force point
% d5: the c3> distance from the rear wheel center to the lateral force point
% d6: locates the shoulders relative to the rear wheel center
% d7: locates the shoulders relative to the rear wheel center
% d8: locates the shoulders relative to the rear wheel center
% d9: locates the grips relative to the front wheel center
% d10: locates the grips relative to the front wheel center
% d11: locates the grips relative to the front wheel center
% d12: length of the upper arms
% d13: length of the lower arms
% l1: the distance in the c1> direction from the center of the rear
%     wheel to the frame center of mass
% l2: the distance in the c3> direction from the center of the rear
%     wheel to the frame center of mass
% l3: the distance in the e1> direction from the front wheel center to
%     the center of mass of the fork
% l4: the distance in the e3> direction from the front wheel center to
%     the center of mass of the fork
% l5: the distance from the shoulder to the upper arm center of mass
% l6: the distance from the elbow to the lower arm center of mass

constants rf, rr, d{1:15}, l{1:8}

% gravity
constants g

% bicycle masses
constants mc, md, me, mf

% arm masses
constants mg, mh, mi, mj

% inertia
constants ic11, ic22, ic33, ic31
constants id11, id22
constants ie11, ie22, ie33, ie31
constants if11, if22

% arm inertia
constants ig11, ig33
constants ih11, ih33
constants ii11, ii33
constants ij11, ij33

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
% q9:  right shoulder abduction
% q10: right shoulder elevation
% q11: right shoulder rotation
% q12: right elbow elevation
% q13: left shoulder abduction
% q14: left shoulder elevation
% q15: left shoulder rotation
% q16: left elbow elevation

variables q{16}'

%---------------------------------------------------------------------%
%         generalized speeds
%---------------------------------------------------------------------%

motionvariables' u{16}'

%---------------------------------------------------------------------%
%         mass and inertia properties
%---------------------------------------------------------------------%

mass c=mc, d=md, e=me, f=mf, g=mg, h=mh, i=mi, j=mj
inertia c, ic11, ic22, ic33, 0, 0, ic31
inertia d, id11, id22, id11
inertia e, ie11, ie22, ie33, 0, 0, ie31
inertia f, if11, if22, if11
inertia g, ig11, ig11, ig33
inertia h, ih11, ih11, ih33
inertia i, ii11, ii11, ii33
inertia j, ij11, ij11, ij33

%---------------------------------------------------------------------%
%         angular relationships                                       %
%---------------------------------------------------------------------%

% rear frame yaw
simprot(n, a, 3, q3)

% rear frame roll
simprot(a, b, 1, q4)

% rear frame pitch
simprot(b, c, 2, q5)

% rear wheel rotation
simprot(c, d, 2, q6)

% steering angle
simprot(c, e, 3, q7)

% front wheel rotation
simprot(e, f, 2, q8)

% right shoulder
dircos(c, g, body123, q9, q10, q11)

% right elbow
simprot(g, h, 2, q12)

% left shoulder
dircos(c, i, body123, q13, q14, q15)

% left elbow
simprot(i, j, 2, q16)

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

% locate the shoulders
p_do_sr> = d6 * c1> + d7 * c2> + d8 * c3>
p_do_sl> = d6 * c1> - d7 * c2> + d8 * c3>

% locate the elbows
p_sr_er> = d12 * g3>
p_sl_el> = d12 * i3>

% locate the hands
p_er_hr> = d13 * h3>
p_el_hl> = d13 * j3>

% locate the centers of mass of the arms
p_sr_go> = l5 * g3>
p_sl_io> = l5 * i3>

p_er_ho> = l6 * h3>
p_el_jo> = l6 * j3>

% steer axis point to the front wheel center
p_ce_fo> = d2 * c3> + d3 * e1>

% front wheel center to fork/handlebar center
p_fo_eo> = l3 * e1> + l4 * e3>

% locate the grips
p_fo_gr> = d9 * e1> + d10 * e2> + d11 * e3>
p_fo_gl> = d9 * e1> - d10 * e2> + d11 * e3>

% locate the lateral force point
p_do_cl> = d4 * c1> + d5 * c3>

% locate the ground contact points
p_do_dn> = rr * b3>
p_fo_fn> = rf * unitvec(cross(cross(e2>, a3>), e2>))

%---------------------------------------------------------------------%
%         define the pitch configuration constraint
%---------------------------------------------------------------------%

% set the a3> component of p_dn_fn> equal to zero
holonomic1 = dot(p_dn_fn>, a3>)

% hands must touch the grips
hrzero> = p_sr_hr> - p_sr_gr>
holonomic2 = dot(hrzero>, c1>)
holonomic3 = dot(hrzero>, c2>)
holonomic4 = dot(hrzero>, c3>)

hlzero> = p_sl_hl> - p_sl_gl>
holonomic5 = dot(hlzero>, c1>)
holonomic6 = dot(hlzero>, c2>)
holonomic7 = dot(hlzero>, c3>)

% arms must always hang down
holonomic8 = dot(g2>, b3>)
holonomic9 = dot(i2>, b3>)

%output holonomic1, holonomic2, holonomic3, holonomic4, holonomic5, &
       %holonomic6, holonomic7, holonomic8, holonomic9
%code algebraic() ArmsHolonomic.m
%pause

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
q9' = u9
q10' = u10
q11' = u11
q12' = u12
q13' = u13
q14' = u14
q15' = u15
q16' = u16

%---------------------------------------------------------------------%
%         angular velocities
%---------------------------------------------------------------------%

angvel(n, a)
angvel(n, b)
angvel(n, c)
angvel(n, d)
angvel(n, e)
angvel(n, f)
angvel(n, g)
angvel(n, h)
angvel(n, i)
angvel(n, j)

%---------------------------------------------------------------------%
%         velocities
%---------------------------------------------------------------------%

v_do_n> = dt(p_no_do>, n)
v2pts(n, c, do, co)
v2pts(n, c, do, ce)
v2pts(n, e, ce, fo)
v2pts(n, e, fo, eo)

v2pts(n, c, do, sr)
v2pts(n, c, do, sl)

v2pts(n, g, sr, go)
v2pts(n, i, sl, io)

v2pts(n, g, sr, er)
v2pts(n, i, sl, el)

v2pts(n, h, er, ho)
v2pts(n, j, el, jo)

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
alf_g_n> = dt(w_g_n>, n)
alf_h_n> = dt(w_h_n>, n)
alf_i_n> = dt(w_i_n>, n)
alf_j_n> = dt(w_j_n>, n)

%---------------------------------------------------------------------%
%         accelerations
%---------------------------------------------------------------------%

a_do_n> = dt(v_do_n>, n)
a2pts(n, c, do, co)
a2pts(n, c, do, ce)
a2pts(n, e, ce, fo)
a2pts(n, e, fo, eo)

a2pts(n, c, do, sr)
a2pts(n, c, do, sl)

a2pts(n, g, sr, go)
a2pts(n, i, sl, io)

a2pts(n, g, sr, er)
a2pts(n, i, sl, el)

a2pts(n, h, er, ho)
a2pts(n, j, el, jo)

%---------------------------------------------------------------------%
%         forces and torques
%---------------------------------------------------------------------%

gravity(g * n3>, c, d, e, f, g, h, i, j)
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

% declare the derivative of each configuration constraint (holonomic)
dependent[5] = dt(holonomic1)
dependent[6] = dt(holonomic2)
dependent[7] = dt(holonomic3)
dependent[8] = dt(holonomic4)
dependent[9] = dt(holonomic5)
dependent[10] = dt(holonomic6)
dependent[11] = dt(holonomic7)
dependent[12] = dt(holonomic8)
dependent[13] = dt(holonomic9)

% the rear wheel angular speed, u6, the roll rate, u4, and the steering rate,
% u7, are taken to be the independent generalized speeds

constrain(dependent[u1, u2, u3, u5, u8, u9, u10, u11, u12, u13, u14, u15, u16])

%---------------------------------------------------------------------%
%         equations of motion
%---------------------------------------------------------------------%

zero = fr() + frstar()

%---------------------------------------------------------------------%
%       some extra outputs
%---------------------------------------------------------------------%

% front wheel contact location
q17 = dot(p_no_fn>, n1>)
q18 = dot(p_no_fn>, n2>)

unitsystem kg, meter, sec

output q1 m, q2 m, q3 rad, q4 rad, q5 rad, q6 rad, q7 rad, q8 rad
output q9 rad, q10 rad, q11 rad, q12 rad, q13 rad, q14 rad, q15 rad, q16 rad
output q17 m, q18 m

output u1 m/s, u2 m/s, u3 rad/s, u4 rad/s, u5 rad/s, u6 rad/s, u7 rad/s, u8 rad/s
output u9 rad/s, u10 rad/s, u11 rad/s, u12 rad/s, u13 rad/s, u14 rad/s, u15 rad/s, u16 rad/s

code dynamics() ArmsDynamics.c
code dynamics() ArmsDynamics.m

%---------------------------------------------------------------------%
%         save output
%---------------------------------------------------------------------%

save Arms.all

%---------------------------------------------------------------------%
