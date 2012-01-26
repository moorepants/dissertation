function [data, delta0, omega0] = steer_dynamics_iddata(fileName, outputs, input)
% function [data, delta0, omega0] = steer_dynamics_iddata(fileName, outputs,
%   input)
%
% Returns an iddata object with either no input or the steer tube torque as
% the input and either or both the steer angle and steer rate measurements
% as outputs.
%
% Parameters
% ----------
% fileName : char
%   The mat file name of the run (e.g. '00217.mat').
% outputs : cell array of chars
%   The desired outputs. Options are 'SteerAngle' and 'SteerRate'.
% input : boolean
%   True if you want the steer tube torque as the input and false if not
%   (i.e. no input.
%
% Returns
% -------
% data : iddata
%   The input/output data.
% delta0 : double
%   The initial value of the steer angle.
% omega0 : double
%   The initial value of the steer rate.

pathToData = '/media/Data/Documents/School/UC Davis/Bicycle Mechanics/BicycleDataProcessor/exports/mat';

runData = load([pathToData filesep fileName]);

if ~strcmp(runData.Maneuver, 'Steer Dynamics Test')
    error([fileName ' is not a Steer Dynamics Test.'])
end

if ismember(fileName, {'00224.mat', '00225.mat', '00226.mat'})
    acceleration = runData.AccelerometerAccelerationZ;
    data = iddata(acceleration, [], 1 / 200);
    set(data, 'TimeUnit', 's')
    set(data, 'OutputName', 'Acceleration', 'OutputUnit', 'm/s^2')
    data = detrend(data);
    if data.OutputData(1) < 0
        start = find(data.OutputData > 0, 1);
    else
        start = find(data.OutputData < 0, 1);
    end
    data = data(start:end);
    delta0 = nan;
    omega0 = nan;
else
    inchlb2Nm = 25.4 / 1000.0 * 4.44822162;
    Tm = inchlb2Nm * runData.SteerTubeTorque; % N*m

    delta = deg2rad(runData.SteerAngle);
    omega= runData.ForkRate; % rad/s

    y = [];

    if ismember('SteerRate', outputs)
        y = omega; % rad/s
    end

    if ismember('SteerAngle', outputs)
        y = [y, delta]; % rad
    end

    % the kinetic and potential energy of the system
    k = 912.77; % individual spring stiffness, N/m
    l = 0.231; % lever arm length, m
    % moment of inertia of wheel, fork and handlebar about steer axis, kg*m^2
    IH = 0.12974383;
    % differentiate the steer angle (this give a smoother signal than the using
    % the rate gyro, due to some time offset??)
    deltad = gradient(delta, 1 / 200);
    ke = 1 / 2 * IH * deltad.^2;
    pe = k * l^2 * delta.^2;
    energy = ke + pe;
    % use the data from 70% of max energy to 1% of max
    [maxE, ~] = max(energy);
    start = length(energy) - find(energy(end:-1:1) > maxE * 0.7, 1);
    stop = find(energy < maxE * 0.01, 1);

    if input
        data = iddata(y, Tm, 1 / 200);
        set(data, 'TimeUnit', 's')
        set(data, 'InputName', 'SteerTubeTorque', 'InputUnit', 'N*m')
    else
        data = iddata(y, [], 1 / 200);
    end

    unitMap.SteerAngle = 'rad';
    unitMap.SteerRate = 'rad/s';
    units = {};
    for i = 1:length(outputs)
        units{i} = unitMap.(outputs{i});
    end

    set(data, 'OutputName', outputs, 'OutputUnit', units)

    data = detrend(data(start:stop));

    delta0 = delta(start);
    omega0 = omega(start);
end
