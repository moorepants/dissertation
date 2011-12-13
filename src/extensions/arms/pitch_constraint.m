function h = pitch_constraint(qd, qi, p)
% function h = pitch_constraint(qd, qi, p)
%
% Paramters
% ---------
% qd : double
%   The dependent coordinate, pitch angle.
% qi : double, size(2, 1)
%   The independent cooridnates, roll angle and steer angle.
% p : structure
%   The parameters, must include rf, rr, d1, 2, d3.
%
% Returns
% -------
% h : double
%   The constraint evaluated at the given points.

q5 = qd;
q4 = qi(1);
q7 = qi(2);

h = p.d2 * cos(q4) * cos(q5) + p.rf * cos(q4)^2 * cos(q5)^2 / (cos(q4)^2 * ...
    cos(q5)^2+(sin(q4) * sin(q7)-sin(q5) * cos(q4) * cos(q7))^2)^0.5 + ...
    (sin(q4) * sin(q7)-sin(q5) * cos(q4) * cos(q7)) * (p.d3 + p.rf * ...
    (sin(q4) * sin(q7)-sin(q5) * cos(q4) * cos(q7))/(cos(q4)^2 * ...
    cos(q5)^2+(sin(q4) * sin(q7) - sin(q5) * cos(q4) * cos(q7))^2)^0.5) - ...
    p.rr * cos(q4) - p.d1 * sin(q5) * cos(q4);
