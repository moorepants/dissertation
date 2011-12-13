function h = left_arm_constraint(qd, qi, p)
% function h = left_arm_constraint(qd, qi, p)
%
% Returns the value of the holonomic constraints for the left arm given the
% configuration and parameters.
%
% Parameters
% ----------
% qd : double, size(4, 1)
%   The vector of configuration variables.
%   q13, q14, q15, q16
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
q13 = qd(1);
q14 = qd(2);
q15 = qd(3);
q16 = qd(4);

h = zeros(4, 1);

h(1) = p.d6 + p.d12 * sin(q14) + p.d13 * (sin(q14) * cos(q16)+sin(q16) * ...
    cos(q14) * cos(q15)) - p.d1 - p.d10 * sin(q7) - (p.d3+p.d9) * cos(q7);

h(2) = p.d10 * cos(q7) - p.d7 - (p.d3+p.d9) * sin(q7) - p.d12 * sin(q13) * ...
    cos(q14) - p.d13 * (sin(q13) * cos(q14) * cos(q16)-sin(q16) * ...
    (sin(q15) * cos(q13)+sin(q13) * sin(q14) * cos(q15)));

h(3) = p.d8 + p.d12 * cos(q13) * cos(q14) + p.d13 * (cos(q13) * cos(q14) * ...
    cos(q16)+sin(q16) * (sin(q13) * sin(q15)-sin(q14) * cos(q13) * ...
    cos(q15))) - p.d11 - p.d2;

h(4) = sin(q15) * sin(q5) * cos(q14) + cos(q5) * (sin(q13) * cos(q15) + ...
    sin(q14) * sin(q15) * cos(q13));
