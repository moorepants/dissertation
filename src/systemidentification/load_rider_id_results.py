#!/usr/bin/env python

import os
from scipy.io import loadmat
import pandas
import bicycledataprocessor as bdp

# Load in the Matlab data
pathToBicycleID = '/media/Data/Documents/School/UC Davis/Bicycle Mechanics/BicycleSystemID'
results = loadmat(pathToBicycleID +
    '/data/riderid/bestControllerIdResults.mat', squeeze_me=True)
crossover = loadmat(pathToBicycleID +
    '/data/riderid/crossoverFrequencies.mat', squeeze_me=True)

# Build a dictionary of all the data
dataDict = {}
dataDict['speed'] = results['speeds']
dataDict['fit'] = results['fits']
dataDict['kDelta'] = results['parameters'][:, 0]
dataDict['kPhiDot'] = results['parameters'][:, 1]
dataDict['kPhi'] = results['parameters'][:, 2]
dataDict['kPsi'] = results['parameters'][:, 3]
dataDict['kYQ'] = results['parameters'][:, 4]
dataDict['wnm'] = results['parameters'][:, 5]
dataDict['zetanm'] = results['parameters'][:, 6]
dataDict['runid'] = [os.path.splitext(str(x))[0] for x in results['matFiles']]
dataDict['wcPhi'] = crossover['phi']
dataDict['wcPsi'] = crossover['psi']
dataDict['wcYQ'] = crossover['yQ']

dataset = bdp.DataSet()
dataset.open()
runTable = dataset.database.root.runTable
taskTable = dataset.database.root.taskTable

dataDict['speedbin'] = []
dataDict['maneuver'] = []
dataDict['rider'] = []
dataDict['duration'] = []
dataDict['environment'] = []

for runID in dataDict['runid']:
    rTabNum = bdp.database.get_row_num(runID, runTable)
    rRow = runTable[rTabNum]
    dataDict['maneuver'].append(rRow['Maneuver'])
    dataDict['rider'].append(rRow['Rider'])
    dataDict['environment'].append(rRow['Environment'])
    dataDict['speedbin'].append(rRow['Speed'])
    tTabNum = bdp.database.get_row_num(runID, taskTable)
    tRow = taskTable[tTabNum]
    dataDict['duration'].append(tRow['Duration'])

dataset.close()

# Create a pandas DataFrame
df = pandas.DataFrame(dataDict)
print(len(df))
df = df.dropna(axis=0)
print(len(df))
df = df[(df['wnm'] < 100.0) & (df['fit'] > 10.0)]
print(len(df))
