HUMAN_CONTROL_DIR = '/media/Data/Documents/School/UC Davis/Bicycle Mechanics/HumanControl';
addpath(HUMAN_CONTROL_DIR)

% figure options
figWidth = 4.0;
goldenRatio = (1 + sqrt(5)) / 2;
figHeight = figWidth / goldenRatio;

figOptions.Color = [1, 1, 1];
figOptions.PaperOrientation = 'portrait';
figOptions.PaperUnits = 'inches';
figOptions.PaperPositionMode = 'manual';
figOptions.PaperPosition = [0, 0, figWidth, figHeight];
figOptions.PaperSize = [figWidth, figHeight];

% The stable speed range for Charlie on the Rigidcl is 5.70 to 9.67 m/s
% The weave bifurcation is at 0.9 m/s.

% Here are some test speeds to use in the following analysis.
speeds.pendulum = 0.8;
speeds.weave = 5.0;
speeds.stable = 7.0;
speeds.capsize = 10.0;
speedNames = fieldnames(speeds);

% create the neuromuscular block
wnm = 30;
zetanm = 0.717;
neuromuscular = tf(wnm^2, [1, 2 * zetanm * wnm, wnm^2]);

%% Step response of the stable Whipple model

% system description
[Ab, Bb, Cb, Db] = whipple_pull_force_abcd(par, speeds.stable);
bicycle = ss(Ab, Bb, Cb, Db);
bicycleTF = tf(bicycle);

% roll torque transfer functions

phiOverTphi = bicycleTF(4, 1);
display('Phi over Tphi @ 7 m/s')
zpk(phiOverTphi)

deltaOverTphi = bicycleTF(7, 1);
display('Delta over Tphi @ 7 m/s')
zpk(deltaOverTphi)

% steer torque transfer functions

phiOverTdelta = bicycleTF(4, 2);
display('Phi over Tdelta @ 7 m/s')
zpk(phiOverTdelta)

deltaOverTdelta = bicycleTF(7, 2);
display('Delta over Tdelta @ 7 m/s')
zpk(deltaOverTdelta)

% step responses
time = linspace(0, 5, 200);
[yPhiTphi, ~] = step(phiOverTphi, time);
[yDeltaTphi, ~] = step(deltaOverTphi, time);
[yPhiTdelta, ~] = step(phiOverTdelta, time);
[yDeltaTdelta, ~] = step(deltaOverTdelta, time);

% plot
stableStep = figure();
set(stableStep, figOptions)

subplot(2, 1, 1)
plot(time, rad2deg(yPhiTphi), time, rad2deg(yDeltaTphi))
ylim([-0.2, 1])
grid
legend('\phi', '\delta')
xlabel('Time [s]')
ylabel('Angle [deg]')

subplot(2, 1, 2)
set(stableStep, figOptions)
plot(time, rad2deg(yPhiTdelta), time, rad2deg(yDeltaTdelta))
ylim([-50, 5])
grid
legend('\phi', '\delta')
xlabel('Time [s]')
ylabel('Angle [deg]')
saveas(stableStep, '../../figures/control/stable-step-response.png')

%% Find suitable gains for roll angle feedback with steer torque control.

%for i = 1:length(speedNames)
    %[Ab, Bb, Cb, Db] = whipple_pull_force_abcd(par, speeds.(speedNames{i}));
    %bicycle = ss(Ab, Bb, Cb, Db);
    %bicycleTF = tf(bicycle);
%
    %phiOverTdelta = bicycleTF(4, 2);
    %phidotOverTdelta = bicycleTF(12, 2);
%
    %figure()
    %rlocus(phiOverTdelta)
    %rlocus(phidotOverTdelta)
%
    %figure()
    %rlocus(phiOverTdelta, linspace(-100, 0))
    %rlocus(phidotOverTdelta, linspace(-100, 0))
%end

% These are only valid for the speeds 0.8, 5.0, 7.0, 10.0
kPhi.pendulum = nan;
kPhi.weave = 1.92;
kPhi.stable = 0;
kPhi.capsize = -10.1;

kPhiDot.pendulum = -111;
kPhiDot.weave = -5;
kPhiDot.stable = 0;
kPhiDot.capsize = nan;

%% Negative feedback of rollrate to control steer torque.

% This sets the system to minimize the error in the commanded torque with
% respect to a gain times roll rate. Notice the system requires positive
% feedback for stability.

% create the bicycle block
par = par_text_to_struct([HUMAN_CONTROL_DIR filesep 'parameters/RigidCharliePar.txt']);
[Ab, Bb, Cb, Db] = whipple_pull_force_abcd(par, speeds.weave);
bicycle = ss(Ab, Bb, Cb, Db);
bicycleTF = tf(bicycle);

% this is a commanded steer torque setup
rollRateClosed = feedback(bicycleTF, kPhiDot.weave, 2, 12);
[y, t] = step(rollRateClosed([4, 7], 2), time);
tDeltaOverTc = feedback(1, -3.74 * bicycleTF(12, 2));
[yTdelta, t] = step(tDeltaOverTc, time);

% plot
comSteerTorque = figure();
set(comSteerTorque, figOptions)
plotyy(t, rad2deg(y), t, yTdelta)
grid
xlabel('Time [s]')
ylabel('Angle [deg]')
legend('\phi', '\delta', 'T_\delta')
saveas(comSteerTorque, '../../figures/control/commanded-steer-torque.png')

%% Roll angle feedback to stablize the capsize mode.

% create the bicycle block
[Ab, Bb, Cb, Db] = whipple_pull_force_abcd(par, speeds.capsize);
bicycle = ss(Ab, Bb, Cb, Db);
bicycleTF = tf(bicycle);

phiOverTdelta = bicycleTF(4, 2);
phiOverPhic = feedback(kPhi.capsize * phiOverTdelta, 1);
tdeltaOverPhic = feedback(kPhi.capsize, phiOverTdelta);
deltaOverPhic = tdeltaOverPhic * bicycleTF(7, 2);

[yPhi, ~] = step(phiOverPhic, time);
[yDelta, ~] = step(deltaOverPhic, time);
[yTdelta, ~] = step(tdeltaOverPhic, time);

comRollAngle = figure();
set(comRollAngle, figOptions)
[ax, h1, h2] = plotyy(time, rad2deg([yPhi, yDelta]), time, yTdelta);
grid
xlabel('Time [s]')
ylabel('Angle [deg]')
legend('\phi', '\delta', 'T_\delta')
saveas(comRollAngle, '../../figures/control/commanded-roll-angle.png')

%%%% this is a commanded roll rate, which doesn't make much sense explicitly
%%%% now look at phidot feedback
%%%
%%%phidotOverTdelta = bicycleTF(12, 2);
%%%
%%%k = -3.74;
%%%phidotOverPhidotc = feedback(k * phidotOverTdelta, 1);
%%%tdeltaOverPhidotc = feedback(k, phidotOverTdelta);
%%%phiOverPhidotc = tdeltaOverPhidotc * bicycleTF(4, 2);
%%%deltaOverPhidotc = tdeltaOverPhidotc * bicycleTF(7, 2);
%%%
%%%time = linspace(0, 10, 200);
%%%[yPhi, ~] = impulse(phiOverPhidotc, time);
%%%[yDelta, ~] = impulse(deltaOverPhidotc, time);
%%%[yTdelta, ~] = impulse(tdeltaOverPhidotc, time);
%%%[yPhidot, ~] = impulse(phidotOverPhidotc, time);
%%%
%%%figure()
%%%subplot(3, 1, 1)
%%%plot(time, rad2deg(yPhidot))
%%%ylabel('$\dot{\phi}$ [deg/s]', 'Interpreter', 'latex')
%%%subplot(3, 1, 2)
%%%plot(time, rad2deg(yPhi), time, rad2deg(yDelta))
%%%legend('\phi', '\delta')
%%%ylabel('Angle [deg]')
%%%subplot(3, 1, 3)
%%%plot(time, yTdelta)
%%%ylabel('T_\delta [n-m]')
