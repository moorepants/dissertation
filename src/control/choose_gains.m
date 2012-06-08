function choose_gains()
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

% bode options
bodeOpts = bodeoptions;
bodeOpts.Title.String = '';

% create the bicycle block
par = par_text_to_struct([HUMAN_CONTROL_DIR filesep 'parameters/RigidCharliePar.txt']);
v = 5.0;
bicycle = whipple_pull_force_abcd(par, v);

% Now change the model to the one identified from Luke's pavilion runs.
%load('../../../Bicycle Mechanics/CanonicalBicycleID/data/cid-L-P.mat')
%invM = inv(M);
%Aid = [-invM * [K0 * 9.81 + K2 * v^2], -invM * C1 * v];
%Bid = [invM(:, 2), invM * H];
%bicycle.A([9, 11], [4, 7, 9, 11]) = Aid;
%bicycle.B([9, 11], [2, 3]) = Bid;

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
print(deltaLocus, '-dpng', '-r200', '../../figures/control/delta-locus.png')
saveas(deltaLocus, '../../figures/control/delta-locus.pdf')

% calculate the damping ratio of the closed loop system
%gainVec = [0.01:0.01:20 20:1:60];
%gainVec = [0.01:0.01:30];
%zetaMat = zeros(6, length(gainVec));
%polesMat = zeros(6, length(gainVec));
%for i = 1:length(gainVec)
    %deltaClosed = feedback(gainVec(i) * deltaOpen, 1);
    %[~, z, p] = damp(deltaClosed);
    %zetaMat(:, i) = z;
    %polesMat(:, i) = p;
%end
%
%deltaDamp = figure();
%set(deltaDamp, figOptions)
%plot(gainVec, zetaMat', 'k.', [gainVec(1), gainVec(end)], [0.55, 0.55], 'k--')
%xlabel('k_\delta')
%ylabel('\zeta')
%title('Steer Angle Closed Loop')
%print(deltaDamp, '-dpng', '-r200', '../../figures/control/delta-damp.png')
%saveas(deltaDamp, '../../figures/control/delta-damp.pdf')

% show how the bode plot looks for various gains
bodeGains = [4.05, 8, 13, 17.48];
bodeLeg = cell(1, length(bodeGains));
for i = 1:length(bodeGains)
    bodeLeg{i} = sprintf('%1.1f', bodeGains(i));
end

deltaBode = figure();
hold all
for k = bodeGains
    deltaClosed = feedback(k * deltaOpen, 1);
    bode(deltaClosed, {0.1, 100}, bodeOpts)
end
hold off

% this code seems to do absolutley fucking nothing! wtf? I hate matlab
% sometimes. It is so convafuckingluted to manipulate graphics. Why is the
% xlabel hanging off the bottom in the first place?
raise = 0.2;
plotAxes = findobj(deltaBode, 'type', 'axes');
for i = 1:length(plotAxes)
    curPos = get(plotAxes(i), 'Position')
    set(plotAxes(i), 'Position', curPos + [0, raise, 0, 0])
    get(plotAxes(i), 'Position')
end
xLab = get(plotAxes(1), 'Xlabel');
set(xLab, 'Units', 'normalized')
set(xLab, 'Position', get(xLab, 'Position') + [0, raise + 0.05, 0])

legend(bodeLeg)

set(deltaBode, figOptions)

remove_io_label(deltaBode)

print(deltaBode, '-dpng', '-r200', '../../figures/control/delta-bode.png')
saveas(deltaBode, '../../figures/control/delta-bode.pdf')

% Here should be some magic to pick the right gain based on the damping
% ratio and the eigenvalues of the closed delta loop, but for now I'll set
% the gain manually based off of viewing the plot. Refer to generate_data to
% see how we automate it with the Bode design criteria.
%kDelta = input('Choose kDelta.\n');
kDelta = 17.48;

% delta / deltac
deltaClosed = feedback(kDelta * deltaOpen, 1);
display('The closed steer loop')
zpk(deltaClosed)

% tDelta / deltac
tDeltaDeltac = feedback(kDelta * neuromuscular, bicycleTF('delta', 'tDelta'));

%% phiDot / deltac
gainVec = -4:0.01:2;
gainVec(find(gainVec == 0)) = [];
%zetaMat = zeros(6, length(gainVec));
%polesMat = zeros(6, length(gainVec));
%for i = 1:length(gainVec)
    %phiDotOpen = gainVec(i) * tDeltaDeltac * bicycleTF('phiDot', 'tDelta');
    %phiDotClosed = minreal(feedback(phiDotOpen, 1));
    %[~, z, p] = damp(phiDotClosed);
    %zetaMat(:, i) = z;
    %polesMat(:, i) = p;
%end
%
%phiDotDamp = figure();
%set(phiDotDamp, figOptions)
%plot(gainVec, zetaMat', 'k.', ...
    %[gainVec(1), gainVec(end)], [0.15, 0.15], 'k--')
%xlabel('k_\dot{\phi}')
%ylabel('\zeta')
%title('Roll Rate Closed Loop')
%print(phiDotDamp, '-dpng', '-r200', '../../figures/control/phiDot-damp.png')
%saveas(phiDotDamp, '../../figures/control/phiDot-damp.pdf')

phiDotLocus = figure();
set(phiDotLocus, figOptions)
set(phiDotLocus, 'PaperPosition', [0, 0, 4, 4], 'PaperSize', [4, 4])
rlocus(minreal(tDeltaDeltac * bicycleTF('phiDot', 'tDelta')), gainVec)
xlim([-30 5])
ylim([-30 30])
sgrid(0.15:0.1:0.95, 5:5:40)
print(phiDotLocus, '-dpng', '-r200', '../../figures/control/phiDot-locus.png')
saveas(phiDotLocus, '../../figures/control/phiDot-locus.pdf')

% choose the gain manually
%kPhiDot = input('Choose kPhiDot.\n');
kPhiDot = -0.44;

phiDotOpen = kPhiDot * tDeltaDeltac * bicycleTF('phiDot', 'tDelta');
phiDotClosed = minreal(feedback(phiDotOpen, 1));
display('Closed roll rate loop.')
zpk(phiDotClosed)

phiDotBode = figure();
bode(phiDotClosed, {1, 20}, bodeOpts)
set(phiDotBode, figOptions)
remove_io_label(phiDotBode)
print(phiDotBode, '-dpng', '-r200', '../../figures/control/phiDot-bode.png')
saveas(phiDotBode, '../../figures/control/phiDot-bode.pdf')

% cross over frequencies
cross.phi = 2;
cross.psi = cross.phi / 2;
cross.yQ = cross.psi / 2;

%% roll loop
tDeltaPhiDotc = feedback(kPhiDot * tDeltaDeltac, bicycleTF('phiDot', 'tDelta'));
phiOpen = tDeltaPhiDotc * bicycleTF('phi', 'tDelta');

w = logspace(-1, 2, 1000);
[mag, ~] = bode(phiOpen, w, bodeOpts);
kPhi = 1 / interp1(w, mag(:)', cross.phi);

phiClosed = feedback(kPhi * phiOpen, 1);
display('Roll angle loop closed.')
zpk(minreal(phiClosed))

phiBode = figure();
hold all
bode(phiOpen, {0.1, 20}, bodeOpts)
bode(kPhi * phiOpen, {0.1, 20})
hold off
set(phiBode, figOptions)
remove_io_label(phiBode)
print(phiBode, '-dpng', '-r200', '../../figures/control/phi-bode.png')
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
set(ax(2),'YColor', 'k')
set(get(ax(2),'Ylabel'),'String','Torque [Nm]')
xlabel('Time [s]')
ylabel('Angle [deg]')
pos = get(gca(), 'Position');
set(gca(), 'Position', pos + [0, 0.1, -0.075, -0.1])
legend('\phi', '\delta', 'T_\delta')
print(comRollAngle, '-dpng', '-r200', '../../figures/control/commanded-roll-angle-human.png')
saveas(comRollAngle, '../../figures/control/commanded-roll-angle-human.pdf')

%% heading loop
tDeltaPhic = feedback(kPhi * tDeltaPhiDotc, bicycleTF('phi', 'tDelta'));
psiOpen = tDeltaPhic * bicycleTF('psi', 'tDelta');

[mag, ~] = bode(psiOpen, w, bodeOpts);
kPsi = 1 / interp1(w, mag(:)', cross.psi);

psiClosed = feedback(kPsi * psiOpen, 1);

psiBode = figure();
hold all
bode(psiOpen, {0.1, 20}, bodeOpts)
bode(kPsi * psiOpen, {0.1, 20}, bodeOpts);
hold off
remove_io_label(psiBode)
set(psiBode, figOptions)
print(psiBode, '-dpng', '-r200', '../../figures/control/psi-bode.png')
saveas(psiBode, '../../figures/control/psi-bode.pdf')

%% lateral deviation loop
tDeltaPsic = feedback(kPsi * tDeltaPhic, bicycleTF('psi', 'tDelta'));
yqOpen = tDeltaPsic * bicycleTF('yQ', 'tDelta');

[mag, phase] = bode(yqOpen, w, bodeOpts);
kYq = 1 / interp1(w, mag(:)', cross.yQ);

yqClosed = feedback(kYq * yqOpen, 1);

yqBode = figure();
hold all
bode(yqOpen, {0.1, 20}, bodeOpts)
bode(kYq * yqOpen, {0.1, 20})
hold off
remove_io_label(yqBode)
set(yqBode, figOptions)
print(yqBode, '-dpng', '-r200', '../../figures/control/yq-bode.png')
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
figOptions.PaperPosition = [0, 0, 5, 4];
figOptions.PaperSize = [5, 4];
set(comLateral, figOptions)
subplot(3, 1, 1)
plot(time, yYq)
grid
ylabel('y_q [m]')
subplot(3, 1, 2)
plot(time, rad2deg([yPhi, yDelta]))
ylabel('Angle [deg]')
legend('\phi', '\delta')
grid
subplot(3, 1, 3)
plot(time, yTdelta)
ylabel('T_\delta [n-m]')
grid
xlabel('Time [s]')
print(comLateral, '-dpng', '-r200', '../../figures/control/commanded-lateral-human.png')
saveas(comLateral, '../../figures/control/commanded-lateral-human.pdf')

function remove_io_label(bodeGraph)
    texts = findall(bodeGraph, 'Type', 'text');
    for i = 1:length(texts)
        s = get(texts(i), 'String');
        if length(s) > 3
            if strcmp(s(1:4), 'From')
                set(texts(i), 'String', '')
            end
        end
    end

