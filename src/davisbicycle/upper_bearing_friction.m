function [cu, tu, IG, k, l] = upper_bearing_friction(varargin)
% function [cu, tu, IG, k, l] = upper_bearing_friction(varargin)
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
% cu : double, 7 x 1
%   The viscous friction coefficient in N*m*s.
% tu : double, 7 x 1
%   The Coulomb friction torque in N*m.
% IG : double, 7 x 1
%   The moment of inertia of the handlebar (above the steer torque sensor)
%   about the steer axis in kg*m^2.
% k : double, 7 x 1
%   The spring stiffness.
% l : double, 7 x1
%   The lever arm.

% set the initial guesses and bounds on the parameters
par(1, 1).Name = 'cu';
par(1, 1).Unit = '';
par(1, 1).Value = 0.4327;
par(1, 1).Minimum = 0;
par(1, 1).Maximum = Inf;
par(1, 1).Fixed = 0;

par(2, 1).Name = 'tu';
par(2, 1).Unit = '';
par(2, 1).Value = 0.0349;
par(2, 1).Minimum = 0;
par(2, 1).Maximum = Inf;
par(2, 1).Fixed = 0;

% handlebar moment of inertia about steer axis
% the inertia is from the bicycle parameters measurements
par(3, 1).Name = 'IG';
par(3, 1).Unit = 'kg*m^2';
par(3, 1).Value = 0.06569374;
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
init(1, 1).Name = 'deltau';
init(1, 1).Value = 0;
init(1, 1).Unit = '';
init(1, 1).Minimum = -Inf;
init(1, 1).Maximum = Inf;
init(1, 1).Fixed = 0;

init(2, 1).Name = 'omegau';
init(2, 1).Value = 0;
init(2, 1).Unit = '';
init(2, 1).Minimum = -Inf;
init(2, 1).Maximum = Inf;
init(2, 1).Fixed = 0;

% build the nonlinear grey box model
% I did have upper_ode as a nested function here and called idnlgrey
% with @upper_ode, but got some kind of error that wouldn't let it
% simulate. Then I moved upper_ode to another function and it worked
% fine. This seems like a bug as the docs say you can use function handles.
grey = idnlgrey('upper_ode', [1, 1, 2], par, init, 0);
set(grey, 'InputName', 'SteerTubeTorque')
set(grey, 'OutputName', 'SteerRate')

% runs 217-223 have the rate gyro mounted to the top of the steer tube
runs = 217:223;

cu = zeros(length(runs), 1);
tu = zeros(length(runs), 1);
IG = zeros(length(runs), 1);
k = zeros(length(runs), 1);
l = zeros(length(runs), 1);

for i = 1:length(runs)
    % Only fit to the rate gyro output as it was attached to the top of the
    % handlebar. This tries to eliminate any flexibility issues in the steer
    % column by not using the steer angle sensor which is further away.
    [data, deltaNaught] = steer_dynamics_iddata(['00' num2str(runs(i)) ...
        '.mat'], {'SteerRate'}, true);

    % if fixed is supplied apply it
    if size(varargin, 2) > 0
        if size(varargin{1}, 2) ~= 5
            error('You must supply five booleans.')
        else
            setpar(grey, 'Fixed', varargin{1})
        end
    end

    % update the initial condition guesses
    setinit(grey, 'Value',  {deltaNaught, data.OutputData(1)})

    % find the best fit
    fit = pem(data, grey, 'InitialState', 'Estimate');

    % store the results
    cu(i) = fit.Par(1).Value;
    tu(i) = fit.Par(2).Value;
    IG(i) = fit.Par(3).Value;
    k(i) = fit.Par(4).Value;
    l(i) = fit.Par(5).Value;

    % show the plots
    figure(i)
    compare(data, grey, fit);
end
