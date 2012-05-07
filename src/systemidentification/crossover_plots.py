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

fig = plt.figure()
fig.set_size_inches(3, 3)
df[['wcPhi', 'wcPsi', 'wcYQ']].boxplot()
fig.savefig('../../figures/systemidentification/crossover-all.png')
fig.savefig('../../figures/systemidentification/crossover-all.pdf')
