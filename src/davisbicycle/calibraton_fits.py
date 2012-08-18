from numpy import array, sqrt
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from dtk.process import fit_goodness

# matplotlib settings
golden_mean = (sqrt(5) - 1.0) / 2.0
fig_width = 3.0
fig_height = fig_width * golden_mean
params = {'backend': 'ps',
          'axes.labelsize': 8,
          'ytick.labelsize': 6,
          'axes.titlesize': 8,
          'text.fontsize': 8,
          'legend.fontsize': 6,
          'xtick.labelsize': 6,
          'text.usetex': True,
          'figure.figsize': [fig_width,fig_height],
          'figure.dpi' : 300,
          'figure.title.fontsize': 8,
          }
plt.rcParams.update(params)

# The wheel speed motor regression.
rpm = array([42.5, 62.0, 89.0, 132.0, 185.0, 271.5, 391.0, 569.0, 855.0, 1243.0,
        1785.0, 2588.0])

voltage = array([0.094, 0.1385, 0.199, 0.291, 0.406, 0.595, 0.857, 1.252, 1.879,
        2.738, 3.91, 5.67])

line = lambda x, m, b: m * x + b

(m, b), pcov = curve_fit(line, voltage, rpm)


rsq, SSE, SST, SSR = fit_goodness(rpm, line(voltage, m, b))

fig, ax = plt.subplots()

ax.scatter(voltage, rpm, label='Measured')
ax.plot(voltage, line(voltage, m, b), 'g', label='Best Fit')
ax.set_xlabel('Motor Voltage [V]')
ax.set_ylabel('Rotational Speed [rpm]')
ax.annotate(r'$r^2={:1.3f}$\\$m={:1.0f}$\\$b={:1.2f}$'.format(rsq, m, b), (0.0,
    1000.0), fontsize=8)
ax.legend(loc=4)

fig.tight_layout()

fig.savefig('../../figures/davisbicycle/speed-calibration.png', dpi=300)
fig.savefig('../../figures/davisbicycle/speed-calibration.pdf')

# The steer torque sensor regression.

load = array([0, 30, 60, 90, 120, 150, 0, -0, -30, -60, -90, -120, -150, -0])

voltage = array([0.000, 1.998, 3.993, 5.997, 7.994, 9.997, 0.002, 0.000,
    -1.995, -3.994, -5.989, -7.986, -9.986, 0.002])

(m, b), pcov = curve_fit(line, voltage, load)

rsq, SSE, SST, SSR = fit_goodness(load, line(voltage, m, b))

fig, ax = plt.subplots()

ax.scatter(voltage, load, label='Measured')
ax.plot(voltage, line(voltage, m, b), 'g', label='Best Fit')
ax.set_xlabel('Sensor Voltage [V]')
ax.set_ylabel('Load [in-lb]')
ax.annotate(r'$r^2={:1.3f}$\\$m={:1.0f}$\\$b={:1.2f}$'.format(rsq, m, b),
        (-10.0, 0.0), fontsize=8)
ax.legend(loc=4)

fig.tight_layout()

fig.savefig('../../figures/davisbicycle/torque-calibration.png', dpi=300)
fig.savefig('../../figures/davisbicycle/torque-calibration.pdf')
