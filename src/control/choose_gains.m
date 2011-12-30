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
[Ab, Bb, Cb, Db] = whipple_pull_force_abcd(par, 5.0); % 5 m/s
bicycle = ss(Ab, Bb, Cb, Db);
bicycleTF = tf(bicycle);

% create the neuromuscular block
wnm = 30;
zetanm = 0.717;
neuromuscular = tf(wnm^2, [1, 2 * zetanm * wnm, wnm^2]);

%% delta loop
deltaOpen = neuromuscular * bicycleTF(7, 2);

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
gainVec = [0.01:0.01:20 20:1:120];
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
bodeGains = [3.278, 7, 12, 30, 45.9];
deltaBode = figure();
hold all
for k = bodeGains
    deltaClosed = feedback(k * deltaOpen, 1);
    bode(deltaClosed, {0.1, 100})
end
hold off
legend({'3.278', '7.0', '12.0', '30.0', '45.9'})
set(deltaBode, figOptions)
saveas(deltaBode, '../../figures/control/delta-bode.png')

% Here should be some magic to pick the right gain based on the damping
% ratio and the eigenvalues of the closed delta loop, but for now I'll set
% the gain manually based off of viewing the plot. Refer to generate_data to
% see how we automate it with the Bode design criteria.
kDelta = 45.9;

% delta / deltac
deltaClosed = feedback(kDelta * deltaOpen, 1);

% tDelta / deltac
tDeltaDeltac = feedback(kDelta * neuromuscular, bicycleTF(7, 2));

%% phiDot / deltac
gainVec = -2:0.005:1;
gainVec(find(gainVec == 0)) = [];
zetaMat = zeros(6, length(gainVec));
polesMat = zeros(6, length(gainVec));
for i = 1:length(gainVec)
    phiDotOpen = gainVec(i) * tDeltaDeltac * bicycleTF(12, 2);
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

phiDotLocus = figure()
set(phiDotLocus, figOptions)
set(phiDotLocus, 'PaperPosition', [0, 0, 4, 4], 'PaperSize', [4, 4])
rlocus(minreal(tDeltaDeltac * bicycleTF(12, 2)), gainVec)
xlim([-30 5])
ylim([-30 30])
sgrid(0.15:0.1:0.95, 5:5:40)
saveas(phiDotLocus, '../../figures/control/phiDot-locus.png')

% choose the gain manually
kPhiDot = -0.062;
phiDotOpen = kPhiDot * tDeltaDeltac * bicycleTF(12, 2);
phiDotClosed = minreal(feedback(phiDotOpen, 1));

phiDotBode = figure();
bode(phiDotClosed, {1, 20})
set(phiDotBode, figOptions)
saveas(phiDotBode, '../../figures/control/phiDot-bode.png')
saveas(phiDotBode, '../../figures/control/phiDot-bode.pdf')

%% roll loop
tDeltaPhiDotc = feedback(kPhiDot * tDeltaDeltac, bicycleTF(12, 2));
phiOpen = tDeltaPhiDotc * bicycleTF(4, 2);

w = logspace(-1, 2, 1000);
[mag, ~] = bode(phiOpen, w);
kPhi = 1 / interp1(w, mag(:)', 2);

phiClosed = feedback(kPhi * phiOpen, 1);

phiBode = figure();
hold all
bode(phiOpen, {0.1, 20})
bode(kPhi * phiOpen, {0.1, 20})
hold off
set(phiBode, figOptions)
saveas(phiBode, '../../figures/control/phi-bode.png')
saveas(phiBode, '../../figures/control/phi-bode.pdf')

%% heading loop
tDeltaPhic = feedback(kPhi * tDeltaPhiDotc, bicycleTF(4, 2));
psiOpen = tDeltaPhic * bicycleTF(3, 2);

[mag, ~] = bode(psiOpen, w);
kPsi = 1 / interp1(w, mag(:)', 1);

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
tDeltaPsic = feedback(kPsi * tDeltaPhic, bicycleTF(3, 2));
yqOpen = tDeltaPsic * bicycleTF(18, 2);

[mag, phase] = bode(yqOpen, w);
kYq = 1 / interp1(w, mag(:)', 0.5);

yqClosed = feedback(kYq * yqOpen, 1);

yqBode = figure();
hold all
bode(yqOpen, {0.1, 20})
bode(kYq * yqOpen, {0.1, 20})
hold off
set(yqBode, figOptions)
saveas(yqBode, '../../figures/control/yq-bode.png')
saveas(yqBode, '../../figures/control/yq-bode.pdf')
