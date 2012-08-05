PATH_TO_BICYCLE_SYSTEM_ID = '/media/Data/Documents/School/UC Davis/Bicycle Mechanics/BicycleSystemID';
addpath([PATH_TO_BICYCLE_SYSTEM_ID '/src/matlab'])
dataDir = [PATH_TO_BICYCLE_SYSTEM_ID filesep 'data' filesep 'riderid' ...
    filesep 'disturbance-runs'];

% Luke on the pavilion floor @ 4 m/s
runID = '00657';
runIDvalid = '00658';

% Charlie on the treadmill @ 4 m/s
%runID = '00315';
%runIDvalid = '00316';

% Load the SISO data.
inputs = {'fB'};
outputs = {'delta'};

[data, meta] = build_id_data([runID '.mat'], outputs, inputs, ...
    dataDir, true);

display(sprintf('The speed of the identification data is %1.2f', meta.speed))

% Load the initial guess.
results = load([PATH_TO_BICYCLE_SYSTEM_ID filesep 'data' filesep ...
    'riderid' filesep 'bestControllerIdResults.mat']);
parameters = results.parameters(strcmp([runID '.mat'], results.matFiles), :);
gainGuess = parameters(1:5);
neuroGuess = parameters(6:7);

% Construct the bicycle state space.
whipple = bicycle_state_space(['Rigid' meta.rider], meta.speed);
% This is the model identified from Luke's pavilion runs.
M = [129.3615, 2.5592;
     2.5592, 0.2505];
C1 = [ 0,   33.5263;
      -0.5486,    2.0997];
K0 = [-115.7074, -4.5261;
      -4.5261,   -0.4889];
K2 = [0, 103.9425;
      0, 2.6034];
H = [0.9017;
     0.0111];
augmented = replace_essential(whipple, M, C1, K0, K2, H, meta.speed, 9.81);

% Construct the entire system.
grey = bicycle_grey('lateral', augmented, meta.speed, outputs, ...
    gainGuess, neuroGuess);

pemArgs = {'Maxiter', 100, ...
           'SearchMethod', 'auto', ...
           'Focus', 'Stability', ...
           'Display', 'on', ...
           'FixedParameter', {'zetanm'}, ...
          };

% Find the SISO solution.
sisoid = pem(data, grey, pemArgs{:});

% Load the multi-output data.
outputs = {'psi', 'phi', 'delta', 'psiDot', 'phiDot', 'deltaDot', 'tDelta'};
[data, meta] = build_id_data([runID '.mat'], outputs, inputs, ...
    dataDir, true);
% Construct the SIMO system.
grey = bicycle_grey('lateral', augmented, meta.speed, outputs, ...
    gainGuess, neuroGuess);
% Set the initial parameter guess to that found in the SISO model.
grey.ParameterVector = sisoid.ParameterVector;

% Find the SIMO solution
simoid = pem(data, grey, pemArgs{:});

% Load the validation data.
[validationData, validationMeta] = build_id_data([runIDvalid '.mat'], ...
    outputs, inputs, dataDir, true);

display(sprintf('The speed of the identifciation data is %1.2f', ...
    validationMeta.speed))

[YH, FIT, X0] = compare(validationData, sisoid, simoid);

sisoY = YH{1}.OutputData;
simoY = YH{2}.OutputData;
outputData = validationData.OutputData;
inputData = validationData.InputData;
outputNames = validationData.OutputName;
fit = FIT;

%save('../../data/systemidentification/riderIdTreadmill.mat', 'sisoY', ...
    %'simoY', 'outputData', 'inputData', 'outputNames', 'runIDvalid', 'fit')
save('../../data/systemidentification/riderIdPavilion.mat', 'sisoY', ...
    'simoY', 'outputData', 'inputData', 'outputNames', 'runIDvalid', 'fit')

%%%time = data.SamplingInstants;
%%%
%%%fig = figure('Visible', 'off');
%%%goldenRatio = (1 + sqrt(5)) / 2;
%%%figWidth = 5;
%%%figHeight = figWidth * 1.25;
%%%set(gcf, ...
    %%%'Color', [1, 1, 1], ...
    %%%'PaperOrientation', 'portrait', ...
    %%%'PaperUnits', 'inches', ...
    %%%'PaperPositionMode', 'manual', ...
    %%%'OuterPosition', [424, 305 - 50, 518, 465], ...
    %%%'PaperPosition', [0, 0, figWidth, figHeight], ...
    %%%'PaperSize', [figWidth, figHeight])
%%%
%%%leftMargin = 0.16;
%%%% [gapHeight, gapWidth], [lowerMargin, upperMargin], [leftMargin, rigthMargin]
%%%axesHandles = tight_subplot(6, 1, [0.05, 0.0], [0.1, 0.05], [0.17, leftMargin]);
%%%
%%%% steer torque
%%%ax = axesHandles(1);
%%%% TODO: this title doesn't seem to want to show up
%%%title(ax, sprintf('Run # %s at %1.1f m/s', runID, v))
%%%lh = plot(ax, time, data.InputData(:, 1), 'k');
%%%ylabel(ax, '\(T_\delta\) [N-m]', 'Interpreter', 'Latex')
%%%xlim(ax, [0, 7])
%%%%set(ax, 'XTick', [])
%%%
%%%ax = axesHandles(2);
%%%lh = plot(ax, time, data.InputData(:, 2), 'k');
%%%ylabel(ax, '\(F_{c_l}\) [N]', 'Interpreter', 'Latex')
%%%ylim(ax, [-250, 250])
%%%xlim(ax, [0, 7])
%%%%set(ax, 'XTick', [])
%%%
%%%ylabels = {'\(\phi\) [rad]', '\(\delta\) [rad]',
           %%%'$\dot{\phi}$ [rad/s]', '$\dot{\delta}$ [rad/s]'};
%%%
%%%f = squeeze(FIT);
%%%for i = 1:4
    %%%ax = axesHandles(i + 2);
    %%%lh = plot(ax, ...
              %%%time, data.OutputData(:, i), 'k', ...
              %%%time, YH{1}.OutputData(:, i), 'b', ...
              %%%time, YH{2}.OutputData(:, i), 'g', ...
              %%%time, YH{3}.OutputData(:, i), 'r');
    %%%ylabel(ax, ylabels{i}, 'Interpreter', 'Latex')
    %%%idLeg = sprintf('I (%1.0f%%)', f(1, i));
    %%%whipLeg = sprintf('W (%1.0f%%)', f(2, i));
    %%%armLeg = sprintf('A (%1.0f%%)', f(3, i));
    %%%leg = legend(ax, 'M', idLeg, whipLeg, armLeg);
    %%%% I can't figure out how to change the legend line length!! the
    %%%% following doesn't seem to work
    %%%legLines = findobj(leg, 'type', 'line');
    %%%for i = 2:2:length(legLines)
        %%%lim = get(legLines(i), 'XData');
        %%%set(legLines(i), 'XData', [lim(1), lim(2) / 3])
    %%%end
    %%%set(leg, 'FontSize', 4)
    %%%% TODO: I can't figure out how to tell the legend box to go exactly
    %%%% where I want it to. It seems to be resized depending on what font size
    %%%% is in the box and the space for the lines.
    %%%axPos = get(ax, 'Position');
    %%%pos = get(leg, 'Position');
    %%%% left, bottom, width, height
    %%%set(leg, 'OuterPosition',[0.86, axPos(2) + 0.05,  0.05, 0.01])
    %%%%get(leg)
%%%
    %%%xlim(ax, [0, 7])
    %%%%if i ~= 4
        %%%%set(ax, 'XTick', [])
    %%%%end
%%%end
%%%
%%%% add the the time axis to the last bottom plot
%%%xlabel('Time [s]')
%%%
%%%saveas(fig, '../../figures/systemidentification/example-fit.png')
%%%saveas(fig, '../../figures/systemidentification/example-fit.pdf')
