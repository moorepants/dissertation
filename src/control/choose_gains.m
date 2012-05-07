% This is an example of choosing the gains for the bicycle-rider system.

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

% create the bicycle block
par = par_text_to_struct([HUMAN_CONTROL_DIR filesep 'parameters/RigidCharliePar.txt']);
v = 9.0;
bicycle = whipple_pull_force_abcd(par, v);

% Now change the model to the one identified from Luke's pavilion runs.
load('../../../Bicycle Mechanics/CanonicalBicycleID/data/cid-L-P.mat')
invM = inv(M);
Aid = [-invM * [K0 * 9.81 + K2 * v^2], -invM * C1 * v];
Bid = [invM(:, 2), invM * H];
bicycle.A([9, 11], [4, 7, 9, 11]) = Aid;
bicycle.B([9, 11], [2, 3]) = Bid;

bicycleTF = tf(bicycle);

% create the neuromuscular block
wnm = 30;
zetanm = 0.707;
neuromuscular = tf(wnm^2, [1, 2 * zetanm * wnm, wnm^2]);

%% delta loop
deltaOpen = neuromuscular * bicycleTF('delta', 'tDelta');
display('The open steer loop.')
zpk(deltaOpen)

% plot the root locus for the negative feedback system
deltaLocus = figure();
set(deltaLocus, figOptions)
set(deltaLocus, 'PaperPosition', [0, 0, 4, 4], 'PaperSize', [4, 4])
rlocus(deltaOpen)
xlim([-30 5])
ylim([-30 30])
sgrid(0.15:0.1:0.95, 5:5:40)
saveas(deltaLocus, '../../figures/control/delta-locus.png')

% calculate the damping ratio of the closed loop system
gainVec = [0.01:0.01:20 20:1:60];
zetaMat = zeros(6, length(gainVec));
polesMat = zeros(6, length(gainVec));
for i = 1:length(gainVec)
    deltaClosed = feedback(gainVec(i) * deltaOpen, 1);
    [~, z, p] = damp(deltaClosed);
    zetaMat(:, i) = z;
    polesMat(:, i) = p;
end

deltaDamp = figure();
set(deltaDamp, figOptions)
plot(gainVec, zetaMat', 'k.', [gainVec(1), gainVec(end)], [0.15, 0.15], 'k--')
xlabel('k_\delta')
ylabel('\zeta')
title('Steer Angle Closed Loop')
saveas(deltaDamp, '../../figures/control/delta-damp.png')
saveas(deltaDamp, '../../figures/control/delta-damp.pdf')

% show how the bode plot looks for various gains
bodeGains = linspace(1, 100, 5);
%[3.278, 7, 12, 30, 45.9];
bodeLeg = cell(1, 5);
for i = 1:length(bodeGains)
    bodeLeg{i} = sprintf('%1.1f', bodeGains(i));
end

deltaBode = figure();
hold all
for k = bodeGains
    deltaClosed = feedback(k * deltaOpen, 1);
    bode(deltaClosed, {0.1, 100})
end
hold off
legend(bodeLeg)
set(deltaBode, figOptions)
saveas(deltaBode, '../../figures/control/delta-bode.png')

% Here should be some magic to pick the right gain based on the damping
% ratio and the eigenvalues of the closed delta loop, but for now I'll set
% the gain manually based off of viewing the plot. Refer to generate_data to
% see how we automate it with the Bode design criteria.
kDelta = input('Choose kDelta.\n');

% delta / deltac
deltaClosed = feedback(kDelta * deltaOpen, 1);
display('The closed steer loop')
zpk(deltaClosed)

% tDelta / deltac
tDeltaDeltac = feedback(kDelta * neuromuscular, bicycleTF('delta', 'tDelta'));

%% phiDot / deltac
gainVec = -10:0.01:1;
gainVec(find(gainVec == 0)) = [];
zetaMat = zeros(6, length(gainVec));
polesMat = zeros(6, length(gainVec));
for i = 1:length(gainVec)
    phiDotOpen = gainVec(i) * tDeltaDeltac * bicycleTF('phiDot', 'tDelta');
    phiDotClosed = minreal(feedback(phiDotOpen, 1));
    [~, z, p] = damp(phiDotClosed);
    zetaMat(:, i) = z;
    polesMat(:, i) = p;
end

phiDotDamp = figure();
set(phiDotDamp, figOptions)
plot(gainVec, zetaMat', 'k.', ...
    [gainVec(1), gainVec(end)], [0.15, 0.15], 'k--')
xlabel('k_\dot{\phi}')
ylabel('\zeta')
title('Roll Rate Closed Loop')
saveas(phiDotDamp, '../../figures/control/phiDot-damp.png')
saveas(phiDotDamp, '../../figures/control/phiDot-damp.pdf')

phiDotLocus = figure();
set(phiDotLocus, figOptions)
set(phiDotLocus, 'PaperPosition', [0, 0, 4, 4], 'PaperSize', [4, 4])
rlocus(minreal(tDeltaDeltac * bicycleTF('phiDot', 'tDelta')), gainVec)
xlim([-30 5])
ylim([-30 30])
sgrid(0.15:0.1:0.95, 5:5:40)
saveas(phiDotLocus, '../../figures/control/phiDot-locus.png')

% choose the gain manually
kPhiDot = input('Choose kPhiDot.\n');

phiDotOpen = kPhiDot * tDeltaDeltac * bicycleTF('phiDot', 'tDelta');
phiDotClosed = minreal(feedback(phiDotOpen, 1));
display('Closed roll rate loop.')
zpk(phiDotClosed)

phiDotBode = figure();
bode(phiDotClosed, {1, 20})
set(phiDotBode, figOptions)
saveas(phiDotBode, '../../figures/control/phiDot-bode.png')
saveas(phiDotBode, '../../figures/control/phiDot-bode.pdf')

% cross over frequencies
cross.phi = 2;
cross.psi = cross.phi / 2;
cross.yQ = cross.psi / 2;

%% roll loop
tDeltaPhiDotc = feedback(kPhiDot * tDeltaDeltac, bicycleTF('phiDot', 'tDelta'));
phiOpen = tDeltaPhiDotc * bicycleTF('phi', 'tDelta');

w = logspace(-1, 2, 1000);
[mag, ~] = bode(phiOpen, w);
kPhi = 1 / interp1(w, mag(:)', cross.phi);

phiClosed = feedback(kPhi * phiOpen, 1);
display('Roll angle loop closed.')
zpk(minreal(phiClosed))

phiBode = figure();
hold all
bode(phiOpen, {0.1, 20})
bode(kPhi * phiOpen, {0.1, 20})
hold off
set(phiBode, figOptions)
saveas(phiBode, '../../figures/control/phi-bode.png')
saveas(phiBode, '../../figures/control/phi-bode.pdf')

%% Step response to a commanded roll angle.
tdeltaOverPhic = phiClosed / bicycleTF('phi', 'tDelta');
deltaOverPhic = tdeltaOverPhic * bicycle('delta', 'tDelta');

time = linspace(0, 5, 200);
u = deg2rad(10) * ones(length(time), 1);
[yPhi, ~] = lsim(phiClosed, u, time);
[yDelta, ~] = lsim(deltaOverPhic, u, time);
[yTdelta, ~] = lsim(tdeltaOverPhic, u, time);

comRollAngle = figure();
set(comRollAngle, figOptions)
[ax, h1, h2] = plotyy(time, rad2deg([yPhi, yDelta]), time, yTdelta);
grid
xlabel('Time [s]')
ylabel('Angle [deg]')
legend('\phi', '\delta', 'T_\delta')
saveas(comRollAngle, '../../figures/control/commanded-roll-angle-human.png')

%% heading loop
tDeltaPhic = feedback(kPhi * tDeltaPhiDotc, bicycleTF('phi', 'tDelta'));
psiOpen = tDeltaPhic * bicycleTF('psi', 'tDelta');

[mag, ~] = bode(psiOpen, w);
kPsi = 1 / interp1(w, mag(:)', cross.psi);

psiClosed = feedback(kPsi * psiOpen, 1);

psiBode = figure();
hold all
bode(psiOpen, {0.1, 20})
bode(kPsi * psiOpen, {0.1, 20});
hold off
set(psiBode, figOptions)
saveas(psiBode, '../../figures/control/psi-bode.png')
saveas(psiBode, '../../figures/control/psi-bode.pdf')

%% lateral deviation loop
tDeltaPsic = feedback(kPsi * tDeltaPhic, bicycleTF('psi', 'tDelta'));
yqOpen = tDeltaPsic * bicycleTF('yQ', 'tDelta');

[mag, phase] = bode(yqOpen, w);
kYq = 1 / interp1(w, mag(:)', cross.yQ);

yqClosed = feedback(kYq * yqOpen, 1);

yqBode = figure();
hold all
bode(yqOpen, {0.1, 20})
bode(kYq * yqOpen, {0.1, 20})
hold off
set(yqBode, figOptions)
saveas(yqBode, '../../figures/control/yq-bode.png')
saveas(yqBode, '../../figures/control/yq-bode.pdf')

% Show a step response to lateral deviation
tdeltaOverYqc = yqClosed / bicycleTF('yQ', 'tDelta');
phiOverYqc = tdeltaOverYqc * bicycle('phi', 'tDelta');
deltaOverYqc = tdeltaOverYqc * bicycle('delta', 'tDelta');

time = linspace(0, 10, 200);
[yYq, ~] = step(yqClosed, time);
[yPhi, ~] = step(phiOverYqc, time);
[yDelta, ~] = step(deltaOverYqc, time);
[yTdelta, ~] = step(tdeltaOverYqc, time);

comLateral = figure();
set(comLateral, figOptions)
subplot(3, 1, 1)
plot(time, yYq)
grid
ylabel('y_q [m]', 'rot', 0)
subplot(3, 1, 2)
plot(time, rad2deg([yPhi, yDelta]))
ylabel('Angle [deg]', 'rot', 0)
legend('\phi', '\delta')
grid
subplot(3, 1, 3)
plot(time, yTdelta)
ylabel('T_\delta [n-m]', 'Rotation', 0)
grid
xlabel('Time [s]')
saveas(comLateral, '../../figures/control/commanded-lateral-human.png')
