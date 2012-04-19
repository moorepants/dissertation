import sys
sys.path.append('..')
from load_paths import read

import os
import cPickle
import numpy as np
import pandas
import bicycledataprocessor as bdp

# load in the raw results
with open(read('pathToGoodRuns')) as f:
    goodRuns = cPickle.load(f)

with open('rollFitPercent.p') as f:
    rollFit = cPickle.load(f)

with open('steerFitPercent.p') as f:
    steerFit = cPickle.load(f)

# get the rider, environment, maneuver, duration so we can sort by them
dataset = bdp.DataSet()
dataset.open()

runTable = dataset.database.root.runTable
taskTable = dataset.database.root.taskTable

runIds = [bdp.database.run_id_string(r) for r in goodRuns]

rider = []
environment = []
maneuver = []
duration = []

for rid in runIds:
    rowNum = bdp.database.get_row_num(rid, runTable)
    row = runTable[rowNum]
    rider.append(row['Rider'])
    environment.append(row['Environment'])
    maneuver.append(row['Maneuver'])

    rowNum = bdp.database.get_row_num(rid, taskTable)
    row = taskTable[rowNum]
    duration.append(row['Duration'])

dataset.close()

# build up a dictionary and data frame with all of the results
dataDict = {}

for k, v in rollFit.items():
    dataDict['roll-' + k] = v

for k, v in steerFit.items():
    dataDict['steer-' + k] = v

dataDict['duration'] = duration
dataDict['environment'] = environment
dataDict['rider'] = rider
dataDict['maneuver'] = maneuver

df = pandas.DataFrame(dataDict, index=runIds)

# Create an integer weighting from 0 to 100 based on the duration of the runs.
# The percent variance for long runs should be weighted more than those of
# short runs because it is harder to get a good fit percentage for longer
# duration runs.
df['weights'] = np.int32(100 * df['duration'] / df['duration'].max())

def compare(data, riders, environments, weighted=False):
    # subset the data frame based on riders and environments
    df2 = data[data['rider'].isin(riders)]
    df3 = df2[df2['environment'].isin(environments)]
    weights = df3['weights']

    steercols = [x for x in df3.columns if x.startswith('steer')]
    rollcols = [x for x in df3.columns if x.startswith('roll')]
    # now remove all but the steer values
    steerNumerics = df3.reindex(columns=steercols)
    rollNumerics = df3.reindex(columns=rollcols)

    def median(data, weighted):
        ans = {}
        for k, v in data.iteritems():
            if weighted is True:
                tot = []
                for i, fit in enumerate(v):
                    tot += weights[i] * [fit]
            else:
                tot = v
            ans[k] = np.median(tot)
        return ans

    steerMedian = median(steerNumerics, weighted)
    rollMedian = median(rollNumerics, weighted)

    #def print_col(ans):
        #ans.sort(key=lambda x: x[1], reverse=True)
        #for a in ans:
            #print('{}: {:.1%}'.format(a[0], a[1]))

    #print_col(steerMedian)
    #print_col(rollMedian)

    return steerMedian, rollMedian

sets = ['-'.join(x.split('-')[1:]) for x in df.columns
        if x.startswith('steer')]
sets.remove('Whipple')
sets.remove('Arm')

rMap = {'J': ['Jason'],
        'C': ['Charlie'],
        'L': ['Luke'],
        'A': ['Charlie', 'Jason', 'Luke']}
eMap = {'P': ['Pavillion Floor'],
        'H': ['Horse Treadmill'],
        'A': ['Pavillion Floor', 'Horse Treadmill']}

steerdf = {}
rolldf = {}
for s in sets:
    r, e = s.split('-')
    sMed, rMed = compare(df, rMap[r], eMap[e])
    sInd = sorted(sMed.keys())
    sInd.remove('steer-Whipple')
    sInd.remove('steer-Arm')
    sInd.append('steer-Whipple')
    sInd.append('steer-Arm')
    steerdf[s] = []
    for model in sInd:
        steerdf[s].append(sMed[model])
    rInd = sorted(rMed.keys())
    rInd.remove('roll-Whipple')
    rInd.remove('roll-Arm')
    rInd.append('roll-Whipple')
    rInd.append('roll-Arm')
    rolldf[s] = []
    for model in rInd:
        rolldf[s].append(rMed[model])

sdf = pandas.DataFrame(steerdf, index=[x[6:] for x in sInd])
rdf = pandas.DataFrame(rolldf, index=[x[5:] for x in rInd])

# Create an restructuredtext table for each of the input measures.
per = lambda x: '{:.1%}'.format(x)

shtml = sdf.to_html(float_format=per)
with open('steer.html', 'w') as f:
    f.write(shtml)
os.system('pandoc -f html -t rst -o median-steer.rst steer.html')
os.system('mv median-steer.rst ../../tables/systemidentification/')

rhtml = rdf.to_html(float_format=per)
with open('roll.html', 'w') as f:
    f.write(rhtml)
os.system('pandoc -f html -t rst -o median-roll.rst roll.html')
os.system('mv median-roll.rst ../../tables/systemidentification/')
