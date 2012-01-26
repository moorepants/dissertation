function [dx, y] = lower_ode(t, x, u, cl, tl, ISF, varargin)
% function [dx, y] = lower_ode(t, x, u, cl, tl, ISF, varargin)
%
% Returns the state derivatives and the outputs of the fork and front wheel
% (below torque sensor) motion.
%
% Parameters
% ----------
% t : double
%   Current time [s].
% x : double, 2 x 1
%   Current state [deltal; omegal].
% u : double
%   Current input, Tm [Nm].
% cl : double
%   Viscous friction coefficient [N*m*s].
% tl : double
%   Coulomb friction coefficient [N*m].
% ISF : double
%   Fork and front wheel moment of inertia about the steer axis [kg*m^2].
% varargin : cell array
%   Optional arguments passed through the idnlgrey/pem calls.
%
% Returns
% -------
% dx : double, 2 x 1
%   The derivative of the states.
% y : double, 1 x 1
%   The output: steer angle [rad].

deltal = x(1);
omegal = x(2);

Tm = u;

dx = zeros(2, 1);
dx(1) = omegal;
dx(2) = (Tm - cl * omegal - tl * sign(omegal)) / ISF;

y = deltal;
