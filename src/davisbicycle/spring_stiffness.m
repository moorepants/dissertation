function [k, sigk] = spring_stiffness()
% function [k, sigk] = spring_stiffness()
%
% Returns the estimated spring stiffness.
%
% Returns
% -------
% k : double
%   Mean stiffness [N/m].
% sigk : double
%   The standard deviation in stiffness [N/m].

runs = {'24', '25', '26'};
stiffness = zeros(length(runs), 1);

for i = 1:length(runs)
    [data, ~, ~] = steer_dynamics_iddata(['002' runs{i} '.mat'], [], []);
    % stiffness guess from Peter's static spring stiffness measurements
    k = 913; % N/m
    m = 11.4; % kg (the measured mass, not including any of the spring mass)
    grey = idgrey('spring_ode', k, 'c', m);
    set(grey, 'OutputName', data.OutputName)
    % this does not estimate the Kalman gain matrix (note that the stiffness
    % estimation will change from ~905 to ~901 if you do estimate K).
    fit = pem(data, grey, 'InitialState', 'Estimate');
    %figure(i)
    %compare(data, grey, fit, 1)
    stiffness(i) = fit.par;
end

k = mean(stiffness);
sigk = std(stiffness);
