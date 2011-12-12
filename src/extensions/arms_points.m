function points = arms_points(q, p)
% function points = arms_points(q, p)
%
% Returns the coordinates for various points in the Whipple model with arms.
%
% Parameters
% ----------
% q : double, size(16, 1)
%   All of the configuration variables in order from 1 to 16.

% define the direction cosine matrices for each of the bodies
% A vector, a, can be expressed in the N frame, n, by pre-multiplying by n_a.
% n = n_a * a
n_a = [cos(q(3)) -sin(q(3)) 0
       sin(q(3)),  cos(q(3)),  0
       0,  0,   1,];

a_b= [1, 0, 0
      0,  cos(q(4)), -sin(q(4))
      0, sin(q(4)), cos(q(4))];

b_c = [cos(q(5)), 0, sin(q(5))
       0, 1, 0
       -sin(q(5)), 0, cos(q(5))];

c_d = [cos(q(6)), 0, sin(q(6))
       0, 1, 0
       -sin(q(6)), 0, cos(q(6))];

c_e = [cos(q(7)), -sin(q(7)), 0
       sin(q(7)), cos(q(7)), 0
       0, 0, 1];

e_f = [cos(q(8)), 0, sin(q(8))
       0, 1, 0
       -sin(q(8)), 0, cos(q(8))];

c_g = [cos(q(10))*cos(q(11)), -sin(q(11))*cos(q(10)), sin(q(10))
       sin(q(11))*cos(q(9)) + sin(q(10))*sin(q(9))*cos(q(11)), cos(q(11))*cos(q(9)) - sin(q(10))*sin(q(11))*sin(q(9)), -sin(q(9))*cos(q(10))
       sin(q(11))*sin(q(9)) - sin(q(10))*cos(q(11))*cos(q(9)), sin(q(9))*cos(q(11)) + sin(q(10))*sin(q(11))*cos(q(9)), cos(q(10))*cos(q(9))];

g_h = [cos(q(12)), 0, sin(q(12))
       0, 1, 0
       -sin(q(12)), 0, cos(q(12))];

c_i = [cos(q(14))*cos(q(15)), -sin(q(15))*cos(q(14)), sin(q(14))
       sin(q(15))*cos(q(13)) + sin(q(13))*sin(q(14))*cos(q(15)), cos(q(13))*cos(q(15)) - sin(q(13))*sin(q(14))*sin(q(15)), -sin(q(13))*cos(q(14))
       sin(q(13))*sin(q(15)) - sin(q(14))*cos(q(13))*cos(q(15)), sin(q(13))*cos(q(15)) + sin(q(14))*sin(q(15))*cos(q(13)), cos(q(13))*cos(q(14))];

i_j = [cos(q(16)), 0, sin(q(16))
       0, 1, 0
       -sin(q(16)), 0, cos(q(16))];

%% create unit vectors for each reference frame

% to express a vector in frame A in frame N: aInN * v
aInN = n_a;
bInN = n_a * a_b;
cInN = n_a * a_b * b_c;
dInN = n_a * a_b * b_c * c_d;
eInN = n_a * a_b * b_c * c_e;
fInN = n_a * a_b * b_c * c_e;
gInN = n_a * a_b * b_c * c_g;
iInN = n_a * a_b * b_c * c_i;
hInN = n_a * a_b * b_c * c_g * g_h;
jInN = n_a * a_b * b_c * c_i * i_j;

% create the unit vectors
% for example d is the d set of dextral vectors in N
n = eye(3);
a = aInN * n;
b = bInN * n;
c = cInN * n;
d = dInN * n;
e = eInN * n;
f = fInN * n;
g = gInN * n;
h = hInN * n;
i = iInN * n;
j = jInN * n;

%% calculate the vector to each point
% newtonian origin to rear wheel center
p_no_do = q(1) * n(:, 1) + q(2) * n(:, 2) - p.rr * b(:, 3);

% rear wheel center to steer axis point
p_do_ce = p.d1 * c(:, 1);

% steer axis point to the front wheel center
p_ce_ex = p.d2 * c(:, 3);
p_ex_fo = p.d3 * e(:, 1);

% right arm
% locate the shoulders
p_do_sr = p.d6 * c(:, 1) + p.d7 * c(:, 2) + p.d8 * c(:, 3);
% locate the elbows
p_sr_er = p.d12 * g(:, 3);
% locate the hands
p_er_hr = p.d13 * h(:, 3);

% left arm
% locate the shoulders
p_do_sl = p.d6 * c(:, 1) - p.d7 * c(:, 2) + p.d8 * c(:, 3);
% locate the elbows
p_sl_el = p.d12 * i(:, 3);
% locate the hands
p_el_hl = p.d13 * j(:, 3);

% rear wheel center to bicycle frame center
p_do_co = p.l1 * c(:, 1) + p.l2 * c(:, 3);

% locate the centers of mass of the arms
p_sr_go = p.l5 * g(:, 3);
p_sl_io = p.l5 * i(:, 3);

p_er_ho = p.l6 * h(:, 3);
p_el_jo = p.l6 * j(:, 3);

% front wheel center to fork/handlebar center
p_fo_eo = p.l3 * e(:, 1) + p.l4 * e(:, 3);

% locate the grips
p_fo_gr = p.d9 * e(:, 1) + p.d10 * e(:, 2) + p.d11 * e(:, 3);
p_fo_gl = p.d9 * e(:, 1) - p.d10 * e(:, 2) + p.d11 * e(:, 3);

% locate the lateral force point
p_do_cl = p.d4 * c(:, 1) + p.d5 * c(:, 3);

% locate the ground contact points
p_do_dn = p.rr * b(:, 3);
v = cross(cross(e(:, 2), a(:, 3)), e(:, 2));
p_fo_fn = p.rf * v ./ norm(v);

points = zeros(3, 20);

points(:, 1) = p_no_do + p_do_dn;
points(:, 2) = [nan;, nan; nan];
% these make up the bicycle frame
points(:, 3) = p_no_do;
points(:, 4) = p_no_do + p_do_ce;
points(:, 5) = p_no_do + p_do_ce + p_ce_ex;
points(:, 6) = p_no_do + p_do_ce + p_ce_ex + p_ex_fo;
points(:, 7) = [nan;, nan; nan];
points(:, 8) = p_no_do + p_do_ce + p_ce_ex + p_ex_fo + p_fo_fn;
points(:, 9) = [nan;, nan; nan];
% the right arm
points(:, 10) = p_no_do + p_do_sr; % right shoulder
points(:, 11) = p_no_do + p_do_sr + p_sr_er; % right elbow
points(:, 12) = p_no_do + p_do_sr + p_sr_er + p_er_hr;
points(:, 13) = [nan;, nan; nan];
% left arm
points(:, 14) = p_no_do + p_do_sl; % left shoulder
points(:, 15) = p_no_do + p_do_sl + p_sl_el; % left elbow
points(:, 16) = p_no_do + p_do_sl + p_sl_el + p_el_hl;
points(:, 17) = [nan;, nan; nan];
points(:, 18) = p_no_do + p_do_ce + p_ce_ex + p_ex_fo + p_fo_gr; % right grip
points(:, 19) = [nan;, nan; nan];
points(:, 20) = p_no_do + p_do_ce + p_ce_ex + p_ex_fo + p_fo_gl; % left grip
