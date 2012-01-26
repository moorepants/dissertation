function [dx, y] = total_ode(t, x, u, cb, tb, IHF, k, l, varargin)
% function [dx, y] = total_ode(t, x, u, cb, tb, IHF, k, l, varargin)
%
% Returns the state derivatives and the outputs of the handlebar, fork and
% front wheel assembly motion.
%
% Parameters
% ----------
% t : double
%   Current time [s].
% x : double, 2 x 1
%   Current state [deltal; omegal].
% u : double, 0 x 0
%   Empty matrix.
% cb : double
%   Viscous friction coefficient [N*m*s].
% tb : double
%   Coulomb friction coefficient [N*m].
% IHF : double
%   Handlebar, fork and front wheel  moment of inertia about the steer axis
%   [kg*m^2].
% k : double, 7 x 1
%   The spring stiffness [N/m].
% l : double, 7 x1
%   The lever arm [m].
% varargin : cell array
%   Optional arguments passed through the idnlgrey/pem calls.
%
% Returns
% -------
% dx : double, 2 x 1
%   The derivative of the states.
% y : double, 1 x 1
%   The output: steer angle [rad].

delta = x(1);
omega = x(2);

dx = zeros(2, 1);
dx(1) = omega;
dx(2) = (-cb * omega - tb * sign(omega) - 2 * k * l^2 * delta) / IHF;

y = delta;
