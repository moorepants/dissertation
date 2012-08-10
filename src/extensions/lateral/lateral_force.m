% This script generates both an impulse and frequency response plot for a
% bicycle with respect to a lateral force applied to the bicycle frame.

addpath('/media/Data/Documents/School/UC Davis/Bicycle Mechanics/HumanControl')

pathToFile = ['/media/Data/Documents/School/UC Davis/Bicycle Mechanics/' ...
    'HumanControl/parameters/RigidJasonPar.txt'];

par = par_text_to_struct(pathToFile);

% set the height of the force point such that 1 newton of lateral force
% gives 1 n-m of torque about the wheel contact point line
par.zcl = -1.0;
%par.xcl = 0.0;

speed = 7.0;
[A, B, C, D] = whipple_pull_force_abcd(par, speed);

bicycle = ss(A, B, C, D);

[y, t] = impulse(bicycle);

fig1 = figure();
figWidth = 4.0;
goldenRatio = (1 + sqrt(5)) / 2;
figHeight = figWidth / goldenRatio;
set(fig1, ...
    'Color', [1, 1, 1], ...
    'PaperOrientation', 'portrait', ...
    'PaperUnits', 'inches', ...
    'PaperPositionMode', 'manual', ...
    'PaperPosition', [0, 0, figWidth, figHeight], ...
    'PaperSize', [figWidth, figHeight])
    %'OuterPosition', [424, 305 - 50, 518, 465], ...

lines = plot(t, y(:, 4, 1), 'b-', ...
     t, y(:, 7, 1), 'b--', ...
     t, y(:, 4, 3), 'r-', ...
     t, y(:, 7, 3), 'r--');

set(lines, 'linewidth', 2.0)
set(gca, 'TickDir', 'out', ...
    'Box', 'off')
title('Impulse Response')
xlabel('Time [s]')
ylabel('Angle [rad]')
legend({'$q_4$ $(T_4)$', '$q_7$ $(T_4)$', '$q_4$ $(F_{cl})$', '$q_7$ $(F_{cl})$'}, 'interpreter', 'latex')

print(fig1, '-dpng', '-r300', '../../../figures/extensions/lat-force-impulse.png')
saveas(fig1, '../../../figures/extensions/lat-force-impulse.pdf')

[num, den] = ss2tf(A, B, C, D, 1);
rollFromTorque = tf(num(4, :), den);
steerFromTorque = tf(num(7, :), den);
[num, den] = ss2tf(A, B, C, D, 3);
rollFromForce = tf(num(4, :), den);
steerFromForce = tf(num(7, :), den);

fig2 = figure();
figWidth = 5.0;
goldenRatio = (1 + sqrt(5)) / 2;
figHeight = figWidth / goldenRatio;
set(fig2, ...
    'Color', [1, 1, 1], ...
    'PaperOrientation', 'portrait', ...
    'PaperUnits', 'inches', ...
    'PaperPositionMode', 'manual', ...
    'OuterPosition', [424, 305 - 50, 518, 465], ...
    'PaperPosition', [0, 0, figWidth, figHeight], ...
    'PaperSize', [figWidth, figHeight])
hold all
b = bodeplot(rollFromTorque, 'b-', ...
    steerFromTorque, 'b--', ...
    rollFromForce, 'r-', ...
    steerFromForce, 'r--', ...
    {1, 20});
hold off
bodeOpts = getoptions(b);
bodeOpts.PhaseMatching = 'on';
bodeOpts.PhaseMatchingFreq = 1;
bodeOpts.PhaseMatchingValue = 0;
bodeOpts.Title.String = '';
setoptions(b,bodeOpts);

plotAxes = findobj(fig2, 'type', 'axes');

% there seems to be a bug such that the xlabel is too low, this is a hack to
% get it to work
raise = 0.05;
set(plotAxes, 'XColor', 'k', 'YColor', 'k', 'Fontsize', 8)
curPos1 = get(plotAxes(1), 'Position');
curPos2 = get(plotAxes(2), 'Position');
set(plotAxes(1), 'Position', curPos1 + [0, raise, 0, 0])
set(plotAxes(2), 'Position', curPos2 + [0, raise, 0, 0])
xLab = get(plotAxes(1), 'Xlabel');
set(xLab, 'Units', 'normalized')

legend({'$q_4$ $(T_4)$', '$q_7$ $(T_4)$', '$q_4$ $(F_{cl})$', '$q_7$ $(F_{cl})$'}, 'interpreter', 'latex')
% find all the lines in the current figure
lines = findobj(fig2, 'type', 'line');
for i = 3:length(lines)
    set(lines, 'LineWidth', 2.0)
end

set(xLab, 'Position', get(xLab, 'Position') + [0, raise + 0.1, 0])
print(fig2, '-dpng', '-r300', '../../../figures/extensions/lat-force-bode.png')

% matlab sucks, the position is different in the pdf and the png and I can't
% move it for the pdf in the correct position, the following two lines don't
% seem to do anything
xLab = get(plotAxes(1), 'Xlabel');
set(xLab, 'Position', get(xLab, 'Position') + [0, -0.5, 0])
saveas(fig2, '../../../figures/extensions/lat-force-bode.pdf')
