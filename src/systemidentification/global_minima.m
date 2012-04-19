% This is an attempt to compare the identification as an output error model
% and when estimating the Kalman gain matrix. It currently doesn't really
% work well.
PATH_TO_BICYCLE_SYSTEM_ID = '/media/Data/Documents/School/UC Davis/Bicycle Mechanics/BicycleSystemID';
addpath([PATH_TO_BICYCLE_SYSTEM_ID '/src/matlab'])
dataDir = [PATH_TO_BICYCLE_SYSTEM_ID filesep 'scripts' filesep 'statespaceid' filesep 'exports'];

inputs = {'tDelta', 'fB'};
states = {'phi', 'delta', 'phiDot', 'deltaDot'};
outputs = {'phi', 'delta', 'phiDot', 'deltaDot'};
outputs = {'delta', 'phiDot'};

runID = '00700';
[data, v, rider] = build_id_data([runID '.mat'], outputs, inputs, ...
    dataDir, true);

whippleModel = bicycle_structured(['Rigid' rider], v, 'states', states, ...
    'inputs', inputs, 'outputs', outputs);

pemArgs = {'Maxiter', 100, ...
           'SearchMethod', 'auto', ...
           'Focus', 'Prediction', ...
           'DisturbanceModel', 'none', ...
           'InitialState', 'Estimate', ...
           'Display', 'on', ...
          };

identifiedModel = pem(data, whippleModel, pemArgs{:});

pemArgs = {'Maxiter', 1000, ...
           'SearchMethod', 'auto', ...
           'Focus', 'Prediction', ...
           'InitialState', 'Estimate', ...
           'Display', 'on', ...
          };

noiseStructured = whippleModel;
noiseStructured.A = identifiedModel.A;
noiseStructured.B = identifiedModel.B;
% this doesn't seem to force the estimation of only the bottom two rows of
% the K matrix, I'm not sure how to enforce it
%noiseStructured.Ks = [0, 0, 0, 0;
                      %0, 0, 0, 0;
                      %nan, nan, nan, nan;
                      %nan, nan, nan, nan];
noiseStructured.Ks = [0, 0;
                      0, 0;
                      nan, nan;
                      nan, nan];

% this currently runs to the 1000th iteration
noiseModel = pem(data, noiseStructured, pemArgs{:});

[YH, FIT, X0] = compare(data, identifiedModel, noiseModel);

time = data.SamplingInstants;

fig = figure('Visible', 'off');
goldenRatio = (1 + sqrt(5)) / 2;
figWidth = 5;
figHeight = figWidth * 1.25;
set(gcf, ...
    'Color', [1, 1, 1], ...
    'PaperOrientation', 'portrait', ...
    'PaperUnits', 'inches', ...
    'PaperPositionMode', 'manual', ...
    'OuterPosition', [424, 305 - 50, 518, 465], ...
    'PaperPosition', [0, 0, figWidth, figHeight], ...
    'PaperSize', [figWidth, figHeight])

leftMargin = 0.16;
% [gapHeight, gapWidth], [lowerMargin, upperMargin], [leftMargin, rigthMargin]
axesHandles = tight_subplot(6, 1, [0.05, 0.0], [0.1, 0.05], [0.17, leftMargin]);

% steer torque
ax = axesHandles(1);
% TODO: this title doesn't seem to want to show up
title(ax, sprintf('Run # %s at %1.1f m/s', runID, v))
lh = plot(ax, time, data.InputData(:, 1), 'k');
ylabel(ax, '\(T_\delta\) [N-m]', 'Interpreter', 'Latex')
xlim(ax, [0, 7])
%set(ax, 'XTick', [])

ax = axesHandles(2);
lh = plot(ax, time, data.InputData(:, 2), 'k');
ylabel(ax, '\(F_{c_l}\) [N]', 'Interpreter', 'Latex')
ylim(ax, [-250, 250])
xlim(ax, [0, 7])
%set(ax, 'XTick', [])

ylabels = {'\(\phi\) [rad]', '\(\delta\) [rad]',
           '$\dot{\phi}$ [rad/s]', '$\dot{\delta}$ [rad/s]'};

f = squeeze(FIT);
for i = 1:length(outputs)
    ax = axesHandles(i + 2);
    lh = plot(ax, ...
              time, data.OutputData(:, i), 'k', ...
              time, YH{1}.OutputData(:, i), 'b', ...
              time, YH{2}.OutputData(:, i), 'r');
    ylabel(ax, ylabels{i}, 'Interpreter', 'Latex')
    idLeg = sprintf('I (%1.0f%%)', f(1, i));
    noiseLeg = sprintf('N (%1.0f%%)', f(2, i));
    leg = legend(ax, 'M', idLeg, noiseLeg);
    % I can't figure out how to change the legend line length!! the
    % following doesn't seem to work
    legLines = findobj(leg, 'type', 'line');
    for i = 2:2:length(legLines)
        lim = get(legLines(i), 'XData');
        set(legLines(i), 'XData', [lim(1), lim(2) / 3])
    end
    set(leg, 'FontSize', 4)
    % TODO: I can't figure out how to tell the legend box to go exactly
    % where I want it to. It seems to be resized depending on what font size
    % is in the box and the space for the lines.
    axPos = get(ax, 'Position');
    pos = get(leg, 'Position');
    % left, bottom, width, height
    set(leg, 'OuterPosition',[0.86, axPos(2) + 0.05,  0.05, 0.01])
    %get(leg)

    xlim(ax, [0, 7])
    %if i ~= 4
        %set(ax, 'XTick', [])
    %end
end

% add the the time axis to the last bottom plot
xlabel('Time [s]')

saveas(fig, '../../figures/systemidentification/global-minima.png')
saveas(fig, '../../figures/systemidentification/global-minima.pdf')
