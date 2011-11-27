#!/usr/bin/env python

# built in imports
import sys

# dependencies
import numpy as np
import bicycleparameters as bp
from dtk import bicycle

# local dependencies
sys.path.append('/media/Data/Documents/School/UC Davis/Bicycle Mechanics/bicycle/alparse')
from models.WhippleMoorePar.WhippleMoorePar import LinearWhippleMoorePar

# create the Whipple model (with my parameters)
whip = LinearWhippleMoorePar()

# load the benchmark parameters
pathToData='/media/Data/Documents/School/UC Davis/Bicycle Mechanics/BicycleParameters/data/'
benchmark = bp.Bicycle('Benchmark', pathToData)
benchmarkPar = bp.io.remove_uncertainties(benchmark.parameters['Benchmark'])
# convert to my parameter set
moorePar = bicycle.benchmark_to_moore(benchmarkPar, oldMassCenter=False)
whip.set_parameters(moorePar)

# set the initial conditions to match Meijaard2007
speedNaught = 4.6
u6Naught = -speedNaught / moorePar['rR']
rollRateNaught = 0.5
pitchAngle = bicycle.pitch_from_roll_and_steer(0., 0., moorePar['rF'], moorePar['rR'],
        moorePar['d1'], moorePar['d2'], moorePar['d3'])

# linearize about the nominal configuration
equilibrium = np.zeros(len(whip.stateNames))
equilibrium[whip.stateNames.index('q5')] = pitchAngle
equilibrium[whip.stateNames.index('u6')] = u6Naught
whip.linear(equilibrium)

# set up the simulation
whip.set_initial_conditions('q5', pitchAngle, 'u4', rollRateNaught, 'u6', u6Naught)

# integration settings
ts = 0.01 # step size
tf = 5. # final time
whip.intOpts['ts'] = ts
whip.intOpts['tf'] = tf

whip.simulate()

# plot figure 4 from Meijaard2007 using my model
rollRate = whip.simResults['y'][:, whip.outputNames.index('u4')]
speed = -whip.simResults['y'][:, whip.outputNames.index('u6')] * whip.parameters['rR']
steerRate = whip.simResults['y'][:, whip.outputNames.index('u7')]
time = whip.simResults['t']
newFig = bicycle.meijaard_figure_four(time, rollRate, steerRate, speed)
newFig.savefig('../../figures/eom/meijaard2007-figure-four-linear.png', dpi=300)

# plot the eigenvalues vs speed
start = 0.0
stop = -10.0 / moorePar['rR']
rootLoci = whip.plot_root_loci('u6', start, stop, num=100, axes='parameter')
ax = rootLoci.axes[0]
ax.set_xlim(ax.get_xlim()[::-1])
rootLoci.savefig('../../figures/eom/root-loci.png', dpi=300)

# now find the eigenvalues
equilibrium[whip.stateNames.index('u6')] = -5.0 / moorePar['rR']
whip.linear(equilibrium)
e = whip.eig()[0]
r = e.real
r.sort()
i = e.imag
i.sort()
mooreEig = np.array([r[0], r[1], r[3], i[-1]])
mooreEig.sort()
meijaardEig = np.array([-14.07838969279822, # caster
                        -0.77534188219585, # weave real
                        -0.32286642900409, # capsize
                        4.46486771378823]) # weave imag
sigFigs = [16, 14, 14, 15]

table = """.. list-table:: Linear Whipple Model Comparision
   :header-rows: 1

   * - Model
     - Caster
     - Weave Real
     - Capsize
     - Weave Imaginary\n"""

for model, eigs in zip(['Meijaard', 'Moore'], [meijaardEig, mooreEig]):
    table += ' ' * 3 + '* - ' + model + '\n'
    for i, e in enumerate(eigs):
        sig = '%1.' + str(sigFigs[i] - 1) + 'e'
        table += ' ' * 5 + '- ' + sig % e + '\n'

print table

with open('../../tables/eom/linear-compare.rst', 'w') as f:
    f.write(table)
