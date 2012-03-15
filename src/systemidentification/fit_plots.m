PATH_TO_BICYCLE_SYSTEM_ID = '/media/Data/Documents/School/UC Davis/Bicycle Mechanics/BicycleSystemID';
addpath(PATH_TO_BICYCLE_SYSTEM_ID)
dataDir = [PATH_TO_BICYCLE_SYSTEM_ID filesep 'scripts' filesep 'exports'];

inputs = {'tDelta', 'fB'};
states = {'phi', 'delta', 'phiDot', 'deltaDot'};
outputs = {'phi', 'delta', 'phiDot', 'deltaDot'};

[data, v, rider] = build_id_data('00588.mat', outputs, inputs, ...
    dataDir, true);

whippleModel = bicycle_structured(['Rigid' rider], v, 'states', states, ...
    'inputs', inputs, 'outputs', outputs);

armModel = whippleModel;
armModel.A = [0, 0, 1, 0
              0, 0, 0, 1
              8.4999, -3.1591, -0.0199, -0.5753
              7.1271, 9.7078, 1.2806, -3.7027];
armModel.B = [0, 0
              0, 0
              -0.0314, 0.0072
               2.0233, -0.0056];

pemArgs = {'Maxiter', 100, ...
           'SearchMethod', 'auto', ...
           'Focus', 'Prediction', ...
           'Weighting', [0.75, 0, 0, 0;
                         0, 1, 0, 0;
                         0, 0, 1, 0;
                         0, 0, 0, 1], ...
           'DisturbanceModel', 'none', ...
           'InitialState', 'zero', ...
           'Display', 'on', ...
          };

identifiedModel = pem(data, whippleModel, pemArgs{:});

pemArgs = {'Maxiter', 500, ...
           'SearchMethod', 'lsqnonlin', ...
           'Focus', 'Prediction', ...
           'Weighting', [1, 0, 0, 0;
                         0, 1, 0, 0;
                         0, 0, 1, 0;
                         0, 0, 0, 1], ...
           'DisturbanceModel', 'Estimate', ...
           'InitialState', 'Estimate', ...
           'Display', 'on', ...
          };
noise = pem(data, identifiedModel, pemArgs{:});

[YH, FIT, X0] = compare(data, whippleModel, armModel, identifiedModel);

time = data.SamplingInstants;

fig = figure('Visible', 'off');
goldenRatio = (1 + sqrt(5)) / 2;
figWidth = 4.0;
figHeight = figWidth * 1.25;
set(gcf, ...
    'Color', [1, 1, 1], ...
    'PaperOrientation', 'portrait', ...
    'PaperUnits', 'inches', ...
    'PaperPositionMode', 'manual', ...
    'OuterPosition', [424, 305 - 50, 518, 465], ...
    'PaperPosition', [0, 0, figWidth, figHeight], ...
    'PaperSize', [figWidth, figHeight])

axesHandles = tight_subplot(6, 1, [0.05, 0.0], [0.1, 0.01], [0.15, 0.05]);

ax = axesHandles(1);
lh = plot(ax, time, data.InputData(:, 1), 'k');
ylabel(ax, '\(T_\delta\) [N-m]', 'Interpreter', 'Latex')
xlim(ax, [0, 12])
set(ax, 'XTick', [])

ax = axesHandles(2);
lh = plot(ax, time, data.InputData(:, 2), 'k');
ylabel(ax, '\(F_{c_l}\) [N]', 'Interpreter', 'Latex')
xlim(ax, [0, 12])
set(ax, 'XTick', [])

ylabels = {'\(\phi\) [rad]', '\(\delta\) [rad]',
           '$\dot{\phi}$ [rad/s]', '$\dot{\delta}$ [rad/s]'};

f = squeeze(FIT);
for i = 1:4
    ax = axesHandles(i + 2);
    lh = plot(ax, ...
              time, data.OutputData(:, i), 'k', ...
              time, YH{1}.OutputData(:, i), 'b', ...
              time, YH{2}.OutputData(:, i), 'g', ...
              time, YH{3}.OutputData(:, i), 'r');
    ylabel(ax, ylabels{i}, 'Interpreter', 'Latex')
    whipLeg = sprintf('W %1.0f%%', f(1, i));
    armLeg = sprintf('A %1.0f%%', f(2, i));
    idLeg = sprintf('I %1.0f%%', f(3, i));
    leg = legend(ax, 'M', whipLeg, armLeg, idLeg);
    %pos = get(leg, 'Position');
    %set(leg, 'Position', pos + [0, 0, 0, 0])
    set(leg, 'FontSize', 5)
    % I can't figure out how to change the legend line length!! the
    % following doesn't seem to work
    legLines = findobj(leg, 'type', 'line');
    for i = 2:2:length(legLines)
        lim = get(legLines(i), 'XData');
        set(legLines(i), 'XData', [lim(1), lim(2) / 3])
    end
    xlim(ax, [0, 12])
    if i ~= 4
        set(ax, 'XTick', [])
    end
end

% add the the time axis to the last bottom plot
xlabel('Time [s]')

saveas(fig, '../../figures/systemidentification/example-fit.png')
