function h = arms_holonomic(qd, qi, p)
% function h = arms_holonomic(qd, qi, p)
%
% Returns the value of the holonomic constraints for the Whipple model with
% rider arms given the configuration and parameters.
%
% Parameters
% ----------
% qd : double, size(8, 1)
%   The vector of dependent configuration variables.
%   q9, q10, q11, q12, q13, q14, q15, q16
% q : double, size(11, 1)
%   The vector of independent configuration variables.
%   q4, q5, q7
% p : structure
%   The geometric parameters of the model.
%
% Returns
% -------
% h : double, size(9, 1)
%   The value of the holonomic constraints.

q4 = qi(1); % roll angle
q5 = qi(2); % pitch angle
q7 = qi(3); % steer angle

q9 = qd(1);
q10 = qd(2);
q11 = qd(3);
q12 = qd(4);
q13 = qd(5);
q14 = qd(6);
q15 = qd(7);
q16 = qd(8);

z = zeros(88,1);

z(3) = cos(q4);
z(4) = sin(q4);
z(5) = cos(q5);
z(6) = sin(q5);
z(9) = cos(q7);
z(10) = sin(q7);
z(13) = cos(q10);
z(14) = cos(q11);
z(15) = z(13)*z(14);
z(16) = sin(q11);
z(17) = z(13)*z(16);
z(18) = sin(q10);
z(19) = cos(q9);
z(20) = sin(q9);
z(21) = z(16)*z(19) + z(14)*z(18)*z(20);
z(23) = z(13)*z(20);
z(24) = z(16)*z(20) - z(14)*z(18)*z(19);
z(25) = z(14)*z(20) + z(16)*z(18)*z(19);
z(26) = z(13)*z(19);
z(27) = cos(q12);
z(28) = sin(q12);
z(29) = cos(q14);
z(30) = cos(q15);
z(31) = z(29)*z(30);
z(32) = sin(q15);
z(33) = z(29)*z(32);
z(34) = sin(q14);
z(35) = cos(q13);
z(36) = sin(q13);
z(37) = z(32)*z(35) + z(30)*z(34)*z(36);
z(39) = z(29)*z(36);
z(40) = z(32)*z(36) - z(30)*z(34)*z(35);
z(41) = z(30)*z(36) + z(32)*z(34)*z(35);
z(42) = z(29)*z(35);
z(43) = cos(q16);
z(44) = sin(q16);
z(45) = z(5)*z(9);
z(46) = z(6)*z(9);
z(47) = z(5)*z(10);
z(48) = z(6)*z(10);
z(49) = z(3)*z(10) + z(4)*z(46);
z(50) = z(4)*z(10) - z(3)*z(46);
z(51) = z(3)*z(9) - z(4)*z(48);
z(53) = z(4)*z(5);
z(54) = z(3)*z(5);
z(55) = z(47)*z(53) - z(6)*z(51);
z(56) = z(45)*z(51) + z(47)*z(49);
z(57) = z(55)^2 + z(56)^2;
z(58) = z(57)^0.5;
z(59) = z(55)/z(58);
z(60) = z(56)/z(58);
z(61) = p.rf*z(59);
z(62) = p.rf*z(60);
z(64) = z(3)*z(6);
z(68) = z(15)*z(28) + z(18)*z(27);
z(69) = z(21)*z(28) - z(23)*z(27);
z(70) = z(24)*z(28) + z(26)*z(27);
z(74) = z(31)*z(44) + z(34)*z(43);
z(75) = z(37)*z(44) - z(39)*z(43);
z(76) = z(40)*z(44) + z(42)*z(43);
z(80) = z(5)*z(25) + z(6)*z(17);
z(86) = z(5)*z(41) + z(6)*z(33);

h = zeros(9, 1);

% this is the roll, pitch, steer constraint
h(1) = p.d2*z(54) + z(54)*z(62) + z(50)*(p.d3+z(61)) - p.d1*z(64) - p.rr*z(3);
% these set of equations are the constraints which force the hands on the
% grips and the arms to hang downward
h(2) = p.d6 + p.d10*z(10) + p.d12*z(18) + p.d13*z(68) - p.d1 - (p.d3+p.d9)*z(9);
h(3) = p.d7 + p.d13*z(69) - p.d10*z(9) - p.d12*z(23) - (p.d3+p.d9)*z(10);
h(4) = p.d8 + p.d12*z(26) + p.d13*z(70) - p.d11 - p.d2;
h(5) = p.d6 + p.d12*z(34) + p.d13*z(74) - p.d1 - p.d10*z(10) - (p.d3+p.d9)*z(9);
h(6) = p.d10*z(9) + p.d13*z(75) - p.d7 - p.d12*z(39) - (p.d3+p.d9)*z(10);
h(7) = p.d8 + p.d12*z(42) + p.d13*z(76) - p.d11 - p.d2;
h(8) = z(80);
h(9) = z(86);
