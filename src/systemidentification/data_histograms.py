import numpy as np
import matplotlib.pyplot as plt
import bicycledataprocessor as bdp

dataset = bdp.DataSet()
dataset.open()

rawMeta = dataset.database.root.runTable

dates = []

for d in rawMeta.cols.DateTime[:]:
    try:
        dates.append(bdp.main.matlab_date_to_object(d))
    except ValueError:
        pass

runs = []

sets = {}
sets['Rider'] = set(rawMeta.cols.Rider)
sets['Maneuver'] = set(rawMeta.cols.Maneuver)
sets['Environment'] = set(rawMeta.cols.Environment)
allSpeeds = set(rawMeta.cols.Speed)
sets['Speed'] = []
for speed in allSpeeds:
    if not np.isnan(speed):
        sets['Speed'].append(speed)

num = {}
for k, v in sets.items():
    num[k] = {}
    for unique in v:
        num[k][unique] = 0

for row in rawMeta.iterrows():
    # this limits it to all the runs that are potentially valid for analyses
    con = []
    con.append(row['Rider'] in ['Jason', 'Charlie', 'Luke'])
    con.append(row['Maneuver'] == 'Balance' or
               row['Maneuver'] == 'Track Straight Line' or
               row['Maneuver'] == 'Balance With Disturbance' or
               row['Maneuver'] == 'Track Straight Line With Disturbance')
    con.append(row['corrupt'] is not True)
    con.append(int(row['RunID']) > 100)
    if False not in con:
        runs.append(row['RunID'])
        num['Rider'][row['Rider']] += 1
        num['Maneuver'][row['Maneuver']] += 1
        num['Environment'][row['Environment']] += 1
        num['Speed'][row['Speed']] += 1

dataset.close()

speeds = num['Speed']
num['Speed'] = {}
for k, v in speeds.items():
    num['Speed']['%1.2f' % k] = v

fig_width = 4.0
goldenRatio = (5**0.5 - 1.0) / 2.0
fig_height = fig_width * goldenRatio
fig_height = fig_width
fig_size =  [fig_width, fig_height]
params = {'axes.labelsize': 8,
          'axes.titlesize': 10,
          'text.fontsize': 8,
          'legend.fontsize': 8,
          'xtick.labelsize': 6,
          'ytick.labelsize': 6,
          'text.usetex': True,
          'figure.figsize': fig_size,
          'figure.subplot.hspace': 0.3,
          'figure.subplot.wspace': 0.2,
          'figure.subplot.bottom': 0.1,
          'figure.subplot.left': 0.1,
          'figure.dpi': 200}

plt.rcParams.update(params)

fig = plt.figure()

ax = fig.add_subplot(2, 2, 1)
riders = ['Charlie', 'Jason', 'Luke']
x = np.arange(len(riders))
ax.bar(x, [num['Rider'][r] for r in riders], width=0.5)
ax.set_xlim((x[0] - 0.5, x[-1] + 1.0))
ax.set_ylabel(r'\# Runs')
ax.set_title('Riders')
plt.xticks(x + 0.25, riders)

ax = fig.add_subplot(2, 2, 2)
maneuvers = ['Balance', 'Balance With Disturbance',
             'Track Straight Line', 'Track Straight Line With Disturbance']
x = np.arange(len(maneuvers))
ax.bar(x,[num['Maneuver'][m] for m in maneuvers], width=0.5)
maneuvers = ['Balance', 'Balance\nWith Disturbance',
             'Track\nStraight Line', 'Track Straight\nLine With Disturbance']
ax.set_xlim((x[0] - 0.5, x[-1] + 1.0))
ax.set_title('Maneuvers')
plt.xticks(x + 0.25, maneuvers)

ax = fig.add_subplot(2, 2, 3)
environments = ['Horse Treadmill', 'Pavillion Floor']
x = np.arange(len(environments))
ax.bar(x, [num['Environment'][e] for e in environments], width=0.5)
ax.set_xlim((x[0] - 0.5, x[-1] + 1.0))
ax.set_ylabel(r'\# Runs')
ax.set_title('Environments')
plt.xticks(x + 0.25, environments)

ax = fig.add_subplot(2, 2, 4)
speeds = ['1.40', '2.00', '3.00', '4.00', '4.92', '5.80', '7.00', '9.00']
x = np.arange(len(speeds))
ax.bar(x, [num['Speed'][s] for s in speeds], width=0.5)
ax.set_xlim((x[0] - 0.5, x[-1] + 1.0))
ax.set_title('Speeds')
plt.xticks(x + 0.25, speeds, rotation=-20)

fig.savefig('../../figures/systemidentification/raw-data-bar-plot.png')
