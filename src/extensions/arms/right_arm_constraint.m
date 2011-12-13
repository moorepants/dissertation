function h = right_arm_constraint(qd, qi, p)
% function h = right_arm_constraint(qd, qi, p)
%
% Returns the value of the holonomic constraints for the right arm given the
% configuration and parameters.
%
% Parameters
% ----------
% qd : double, size(4, 1)
%   The vector of configuration variables.
%   q9, q10, q11, q12
% qi : double, size(2, 1)
%   q5, q7
% p : structure
%   The geometric parameters of the model.
%
% Returns
% -------
% h : double, size(4, 1)
%   The value of the holonomic constraints.

q5 = qi(1);
q7 = qi(2);
q9 = qd(1);
q10 = qd(2);
q11 = qd(3);
q12 = qd(4);

h = zeros(4, 1);

h(1) = p.d6 + p.d10 * sin(q7) + p.d12 * sin(q10) + p.d13 * (sin(q10) * ...
    cos(q12)+sin(q12) * cos(q10) * cos(q11)) - p.d1 - (p.d3 + p.d9) * cos(q7);

h(2) = p.d7 - p.d10 * cos(q7) - (p.d3+p.d9) * sin(q7) - p.d12 * sin(q9) * ...
    cos(q10) - p.d13 * (sin(q9) * cos(q10) * cos(q12) - sin(q12) * ...
    (sin(q11) * cos(q9)+sin(q10) * sin(q9) * cos(q11)));

h(3) = p.d8 + p.d12 * cos(q10) * cos(q9) + p.d13 * (cos(q10) * cos(q12) * ...
    cos(q9)+sin(q12) * (sin(q11) * sin(q9)-sin(q10) * cos(q11) * ...
    cos(q9))) - p.d11 - p.d2;

h(4) = sin(q11) * sin(q5) * cos(q10) + cos(q5) * (sin(q9) * cos(q11) + ...
    sin(q10) * sin(q11) * cos(q9));
