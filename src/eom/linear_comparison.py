#!/usr/bin/env python

# dependencies
import numpy as np
import bicycleparameters as bp
from dtk import bicycle

# local dependencies
try:
    f = open('Whipple.py', 'r')
except IOError:
    from altk import alparse
    alparse.alparse('Whipple', 'Whipple', code='Python')
else:
    f.close()
    del f

from Whipple import LinearWhipple

# create the Whipple model (with my parameters)
whip = LinearWhipple()

# load the benchmark parameters
pathToData='/media/Data/Documents/School/UC Davis/Bicycle Mechanics/BicycleParameters/data/'
benchmark = bp.Bicycle('Benchmark', pathToData)
benchmarkPar = bp.io.remove_uncertainties(benchmark.parameters['Benchmark'])
# convert to my parameter set
moorePar = bicycle.benchmark_to_moore(benchmarkPar, oldMassCenter=False)
whip.set_parameters(moorePar)

# set the initial conditions to match Meijaard2007
speedNaught = 4.6
u6Naught = -speedNaught / moorePar['rr']
rollRateNaught = 0.5
pitchAngle = bicycle.pitch_from_roll_and_steer(0., 0., moorePar['rf'], moorePar['rr'],
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
rollRate = whip.get_sim_output('u4')
speed = -whip.get_sim_output('u6') * whip.parameters['rr']
steerrate = whip.get_sim_output('u7')
time = whip.simResults['t']
newFig = bicycle.meijaard_figure_four(time, rollRate, steerrate, speed)
newFig.savefig('../../figures/eom/meijaard2007-figure-four-linear.png', dpi=300)
newFig.savefig('../../figures/eom/meijaard2007-figure-four-linear.pdf')

# plot the eigenvalues vs speed
settings = {'num':100,
            'axes':'complex',
            'pub':True,
            'width':5.0}
start = 0.0
stop = -10.0 / moorePar['rr']
rootLocus = whip.plot_root_locus('u6', start, stop, factor=('v',
    -moorePar['rr']), units='m/s', **settings)
rootLocus.savefig('../../figures/eom/root-locus-complex.png', dpi=300)
rootLocus.savefig('../../figures/eom/root-locus-complex.pdf')

settings['axes'] = 'parameter'
settings['ylim'] = (-10, 10)
rootLocus = whip.plot_root_locus('u6', start, stop, factor=('v',
    -moorePar['rr']), units='m/s', **settings)
ax = rootLocus.axes[0]
# find the lines
firstVals = np.array([line.get_ydata()[0] for line in ax.lines])

casterLine = ax.lines[np.argmin(firstVals)]
capsizeLine = ax.lines[np.nonzero((firstVals > casterLine.get_ydata()[0]) &
    (firstVals < 0))[0]]
upperWeaveLine = ax.lines[np.argmax(firstVals)]
lowerWeaveLine = ax.lines[np.nonzero((firstVals < upperWeaveLine.get_ydata()[0]) &
        (firstVals > 0))[0]]

for i, val in enumerate(firstVals):
    if np.abs(val - 0.) < 1e-10:
        ax.lines[i].set_color(upperWeaveLine.get_color())

lowerWeaveLine.set_color(upperWeaveLine.get_color())

ax.annotate('Caster',
        casterLine.get_xydata()[np.argmin(np.abs(casterLine.get_xdata() -
            1.0))], xytext=(2.5, -7.0), color=casterLine.get_color(),
        arrowprops={'arrowstyle':"->", 'color':casterLine.get_color()})
ax.annotate('Capsize',
        capsizeLine.get_xydata()[np.argmin(np.abs(capsizeLine.get_xdata() -
            7.0))], xytext=(8.25, 2.5), color=capsizeLine.get_color(),
        arrowprops={'arrowstyle':"->", 'color':capsizeLine.get_color()})
ax.annotate('Weave',
        upperWeaveLine.get_xydata()[np.argmin(np.abs(upperWeaveLine.get_xdata() -
            2.0))], xytext=(2.5, 6.0), color=upperWeaveLine.get_color(),
        arrowprops={'arrowstyle':"->", 'color':upperWeaveLine.get_color()})

weaveSpeed = upperWeaveLine.get_xdata()[upperWeaveLine.get_ydata() > 0.0][-1]
capsizeSpeed = capsizeLine.get_xdata()[capsizeLine.get_ydata() >= 0.0][0]

ax.plot([weaveSpeed, weaveSpeed], [-11.0, 0.], 'k-')
ax.plot([weaveSpeed, weaveSpeed], [-11.0, 0.], 'ko')
ax.plot([capsizeSpeed, capsizeSpeed], [-11.0, 0.], 'k-')
ax.plot([capsizeSpeed, capsizeSpeed], [-11.0, 0.], 'ko')
ax.text(4.5, -9.0, 'Stable')
ax.arrow(weaveSpeed, -7.0, capsizeSpeed - weaveSpeed, 0.0, shape='full')

rootLocus.savefig('../../figures/eom/root-locus.png', dpi=300)
rootLocus.savefig('../../figures/eom/root-locus.pdf')

# now find the eigenvalues
equilibrium[whip.stateNames.index('u6')] = -5.0 / moorePar['rr']
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
