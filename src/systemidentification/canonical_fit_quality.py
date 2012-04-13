import sys
sys.path.append('..')
from load_paths import read
import cPickle
import numpy as np
import matplotlib.pyplot as plt
import bicycledataprocessor as bdp
from canonicalbicycleid import canonical_bicycle_id as cbi

with open(read('pathToGoodRuns')) as f:
    goodRuns = cPickle.load(f)

with open(read('pathToIdMat')) as f:
    idMat = cPickle.load(f)

dataset = bdp.DataSet()

roll = {k : [] for k in idMat.keys() + ['Whipple', 'Arm']}
steer = {k : [] for k in idMat.keys() + ['Whipple', 'Arm']}

allH = cbi.lateral_force_contribution(['Charlie', 'Jason', 'Luke'])

for runNum in goodRuns:
    trial = bdp.Run(runNum, dataset, filterFreq=15.)
    rider = trial.metadata['Rider']
    timeseries = cbi.benchmark_time_series(trial, subtractMean=True)
    for k, model in idMat.items():
        rollrsq, steerrsq, fig = cbi.input_prediction(timeseries, model)
        roll[k].append(rollrsq)
        steer[k].append(steerrsq)
        fig.savefig('plots/' + str(runNum) + '-' + k + '.png')
        plt.close(fig)
        del fig

    M, C1, K0, K2 = trial.bicycle.canonical(nominal=True)
    rollrsq, steerrsq, fig = cbi.input_prediction(timeseries, (M, C1, K0, K2,
            allH[rider]))
    roll['Whipple'].append(rollrsq)
    steer['Whipple'].append(steerrsq)
    fig.savefig('plots/' + str(runNum) + '-whipple.png')
    plt.close(fig)
    del fig

    v = timeseries['v'].mean()
    A, B, speeds = cbi.mean_arm([rider])
    M = np.linalg.inv(B[round(v * 10)][2:, [0, 1]])
    C = -np.dot(M, A[round(v * 10)][2:, [2, 3]])
    K = -np.dot(M, A[round(v * 10)][2:, [0, 1]])
    rollrsq, steerrsq, fig = cbi.input_prediction(timeseries, (M, C, K,
            allH[rider]))
    roll['Arm'].append(rollrsq)
    steer['Arm'].append(steerrsq)
    fig.savefig('plots/' + str(runNum) + '-arm.png')
    plt.close(fig)
    del fig
