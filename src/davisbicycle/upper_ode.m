function [dx, y] = upper_ode(t, x, u, cu, tu, IG, k, l, varargin)
% function [dx, y] = upper_ode(t, x, u, cu, tu, IG, k, l, varargin)
%
% Returns the state derivatives and the outputs of the handlebar motion as a
% function of time.
%
% Parameters
% ----------
% t : double
%   Current time [s].
% x : double, 2 x 1
%   Current state [deltau; omegau].
% u : double
%   Current input, Tm [Nm].
% cu : double
%   Viscous friction coefficient [N*m*s].
% tu : double
%   Coulomb friction coefficient [N*m].
% IG : double
%   Handlebar moment of inertia about the steer axis [kg*m^2].
% k : double
%   Spring stiffness [N/m].
% l : double
%   Lever arm [m].
% varargin : cell array
%   Optional arguments passed through the idnlgrey/pem calls.
%
% Returns
% -------
% dx : double, 2 x 1
%   The derivative of the states.
% y : double
%   The output, steer rate [rad/s].

deltau = x(1);
omegau = x(2);

Tm = u;

dx = zeros(2, 1);
dx(1) = omegau;
dx(2) = (-cu * omegau - tu * sign(omegau) - 2 * k * l^2 * deltau - Tm) / IG;

y = omegau;
