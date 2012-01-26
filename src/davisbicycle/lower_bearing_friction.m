function [cl, tl, ISF] = lower_bearing_friction(varargin)
% function [cl, tl, ISF] = lower_bearing_friction(varargin)
%
% Returns estimated parameters for the lower bearing friction in the steer
% column.
%
% Parameters
% ----------
% varargin : cell array of booleans, 1 x 3, optional
%   Specify true or false for each parameter. True will fix the parameter
%   and false will allow it to be estimated. Parameters are cl, tl, and ISF.
%
% Returns
% -------
% cl : double, 7 x 1
%   The viscous friction coefficient in N*m*s.
% tl : double, 7 x 1
%   The Coulomb friction torque in N*m.
% ISF : double, 7 x 1
%   The moment of inertia of the fork and front wheel (everything below the
%   torque sensor) about the steer axis in kg*m^2.

% set the initial guesses and bounds on the parameters
par(1, 1).Name = 'cl';
par(1, 1).Unit = '';
par(1, 1).Value = 0.2;
par(1, 1).Minimum = 0;
par(1, 1).Maximum = Inf;
par(1, 1).Fixed = 0;

par(2, 1).Name = 'tl';
par(2, 1).Unit = '';
par(2, 1).Value = 0.0349;
par(2, 1).Minimum = 0;
par(2, 1).Maximum = Inf;
par(2, 1).Fixed = 0;

% fork and front wheel moment of inertia about steer axis
% the inertia is from the bicycle parameters measurements
par(3, 1).Name = 'ISF';
par(3, 1).Unit = 'kg*m^2';
par(3, 1).Value = 0.06405009;
par(3, 1).Minimum = 0;
par(3, 1).Maximum = Inf;
par(3, 1).Fixed = 1;

% set the initial conditions
init(1, 1).Name = 'deltal';
init(1, 1).Value = 0;
init(1, 1).Unit = '';
init(1, 1).Minimum = -Inf;
init(1, 1).Maximum = Inf;
init(1, 1).Fixed = 0;

init(2, 1).Name = 'omegal';
init(2, 1).Value = 0;
init(2, 1).Unit = '';
init(2, 1).Minimum = -Inf;
init(2, 1).Maximum = Inf;
init(2, 1).Fixed = 0;

% build the nonlinear grey box model
order = [1, 1, 2]; % [outputs, inputs, states]
grey = idnlgrey('lower_ode', order, par, init, 0);
set(grey, 'InputName', 'SteerTubeTorque')
set(grey, 'OutputName', {'SteerAngle'})

% runs 205-216 have the rate gyro mounted in the normal position (i.e. steer
% angle and steer rate are measured at the same place)
%runs = 211:216;
runs = 216;

cl = zeros(length(runs), 1);
tl = zeros(length(runs), 1);
ISF = zeros(length(runs), 1);

for i = 1:length(runs)
    [data, delta0, omega0] = steer_dynamics_iddata(['00' num2str(runs(i)) ...
        '.mat'], {'SteerAngle'}, true);

    % if fixed is supplied, apply it
    if size(varargin, 2) > 0
        if size(varargin{1}, 2) ~= 3
            error('You must supply three booleans.')
        else
            setpar(grey, 'Fixed', varargin{1})
        end
    end

    % update the initial condition guesses
    setinit(grey, 'Value',  {delta0, omega0})

    % find the best fit
    fit = pem(data, grey);

    % store the results
    cl(i) = fit.Par(1).Value;
    tl(i) = fit.Par(2).Value;
    ISF(i) = fit.Par(3).Value;

    % show the plots
    figure(i)
    compare(data, grey, fit);
end
