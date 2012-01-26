function [cb, tb, IHF, k, l] = total_bearing_friction(varargin)
% function [cb, tb, IHF, k, l] = total_bearing_friction(varargin)
%
% Returns estimated parameters for the upper bearing friction in the steer
% column.
%
% Parameters
% ----------
% varargin : cell array of booleans, 1 x 5, optional
%   Specify true or false for each parameters. True will fix the parameter
%   and false will allow it to be estimated.
%
% Returns
% -------
% cb : double, 15 x 1
%   The viscous friction coefficient [N*m*s].
% tb : double, 15 x 1
%   The Coulomb friction torque [N*m].
% IHF : double, 15 x 1
%   The moment of inertia of the handlebar, fork and front wheel about the
%   steer axis [kg*m^2].
% k : double, 15 x 1
%   The spring stiffness [N/m].
% l : double, 15 x 1
%   The lever arm [m].

% set the initial guesses and bounds on the parameters
par(1, 1).Name = 'cb';
par(1, 1).Unit = '';
par(1, 1).Value = 0.4327;
par(1, 1).Minimum = 0;
par(1, 1).Maximum = Inf;
par(1, 1).Fixed = 0;

par(2, 1).Name = 'tb';
par(2, 1).Unit = '';
par(2, 1).Value = 0.0349;
par(2, 1).Minimum = 0;
par(2, 1).Maximum = Inf;
par(2, 1).Fixed = 0;

% handlebar, fork and front wheel inertia about the steer axis
par(3, 1).Name = 'IHF';
par(3, 1).Unit = 'kg*m^2';
par(3, 1).Value = 0.12974383;
par(3, 1).Minimum = 0;
par(3, 1).Maximum = Inf;
par(3, 1).Fixed = 1;

% spring stiffness, N/m
par(4, 1).Name = 'k';
par(4, 1).Unit = 'N/m';
par(4, 1).Value = 904.7;
par(4, 1).Minimum = 0;
par(4, 1).Maximum = Inf;
par(4, 1).Fixed = 1;

% spring lever arm, m
par(5, 1).Name = 'l';
par(5, 1).Unit = 'm';
par(5, 1).Value = 0.231;
par(5, 1).Minimum = 0;
par(5, 1).Maximum = Inf;
par(5, 1).Fixed = 1;

% set the initial conditions
init(1, 1).Name = 'delta';
init(1, 1).Value = 0;
init(1, 1).Unit = '';
init(1, 1).Minimum = -Inf;
init(1, 1).Maximum = Inf;
init(1, 1).Fixed = 0;

init(2, 1).Name = 'omega';
init(2, 1).Value = 0;
init(2, 1).Unit = '';
init(2, 1).Minimum = -Inf;
init(2, 1).Maximum = Inf;
init(2, 1).Fixed = 0;

% build the nonlinear grey box model
order = [1, 0, 2]; % outputs, inputs, states
sampleTime = 0; % zero means it is defined as a continous model
grey = idnlgrey('total_ode', order, par, init, sampleTime);
set(grey, 'OutputName', 'SteerAngle')

% all of the steer tests
runs = 209:223;

cb = zeros(length(runs), 1);
tb = zeros(length(runs), 1);
IHF = zeros(length(runs), 1);
k = zeros(length(runs), 1);
l = zeros(length(runs), 1);

for i = 1:length(runs)
    display(['Run 00' num2str(runs(i))])

    [data, delta0, omega0] = steer_dynamics_iddata(['00' num2str(runs(i)) ...
        '.mat'], {'SteerAngle'}, false);

    % if fixed is supplied apply it
    if size(varargin, 2) > 0
        if size(varargin{1}, 2) ~= 5
            error('You must supply five booleans.')
        else
            setpar(grey, 'Fixed', varargin{1})
        end
    end

    % update the initial condition guesses
    setinit(grey, 'Value',  {delta0, omega0})

    % find the best fit
    fit = pem(data, grey, 'InitialState', 'Estimate');

    % store the results
    cb(i) = fit.Par(1).Value;
    tb(i) = fit.Par(2).Value;
    IHF(i) = fit.Par(3).Value;
    k(i) = fit.Par(4).Value;
    l(i) = fit.Par(5).Value;

    % show the plots
    figure(i)
    % you have to give a finite prediction horizon for time series models (no input)
    compare(data, grey, fit, 1);
end
