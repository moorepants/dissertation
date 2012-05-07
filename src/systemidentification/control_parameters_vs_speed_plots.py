import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

from load_rider_id_results import df

# Plot parameters for Latex output
params = {'backend': 'ps',
          'axes.labelsize': 10,
          'text.fontsize': 10,
          'legend.fontsize': 8,
          'xtick.labelsize': 8,
          'ytick.labelsize': 8,
          'text.usetex': True,
          'figure.dpi': 200,
          }
plt.rcParams.update(params)

# Create a histogram of the speeds
fig, ax = plt.subplots(1, 1, squeeze=True)
fig.set_size_inches(5, 5)
ax.hist(df['speed'], bins=40, range=(0, 10), align='mid')
ax.set_xlabel('Speed m/s')
ax.set_ylabel('Runs')
ax.set_xticks(np.linspace(0, 10, 21))
fig.savefig('../../figures/systemidentification/speed-hist-all.png')
fig.savefig('../../figures/systemidentification/speed-hist-all.pdf')

fig, ax = plt.subplots(6, 1, sharex=True)
fig.set_size_inches(4, 6)

parameters = ['kDelta', 'kPhiDot', 'kPhi', 'kPsi', 'kYQ', 'wnm']

speedBins = np.linspace(0.0, 10.0, num=41)
plotData = {k : [] for k in parameters}
nums = []
meanFits = []
for v in speedBins:
    sbin = df[(v - 0.25 < df['speed']) & (df['speed'] < v + 0.25)]
    nums.append(len(sbin))
    meanFits.append(sbin['fit'].mean())
    for par in parameters:
        plotData[par].append(sbin[par])

widths = 0.25 * (np.sqrt(nums) / np.max(np.sqrt(nums)))
line = lambda x, m, b: m * x + b
constant = lambda x, c: c
ylims = [(0, 100), (-8, 1), (1, 12), (-0.5, 3), (-0.5, 2), (0, 80)]
for i, par in enumerate(parameters):
    # Fit a weight line through the medians.
    y = np.array([sbin.median() for sbin in plotData[par]])
    x = speedBins
    weight = np.array([sbin.std() for sbin in plotData[par]])
    if par == 'wnm':
         b, cov = curve_fit(constant, x[~np.isnan(y)], y[~np.isnan(y)],
                sigma=widths[~np.isnan(y)])
         m = 0.0
    else:
        (m, b), cov = curve_fit(line, x[~np.isnan(y)], y[~np.isnan(y)],
                sigma=1. / widths[~np.isnan(y)])
    ax[i].plot(np.linspace(0, 10), m * np.linspace(0, 10) + b, '-g')
    ax[i].boxplot(plotData[par], positions=speedBins, widths=widths)
    ax[i].set_ylim(ylims[i])
    ax[i].set_ylabel(par)
    #xts = ax[i].get_xticks()
    xticks = np.linspace(0.0, 10.0, num=21)
    ax[i].set_xticks(xticks)
    #ax[i].set_xticks(xts - 0.25)
    #ax[i].set_xticklabels(speedBins)
ax[-1].set_xlabel('Speed m/s')

fig.savefig('../../figures/systemidentification/par-vs-speed-box-all.png')
fig.savefig('../../figures/systemidentification/par-vs-speed-box-all.pdf')
#top = ax[0].twiny()
#top.set_xticks(ax[0].get_xticks() - 1.5)
#top.set_xticklabels([''] + ['{}'.format(n) for n in nums])
