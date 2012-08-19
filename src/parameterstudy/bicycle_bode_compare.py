#!/usr/bin/env python

import matplotlib.pyplot as plt
import bicycleparameters as bp

# compare the benchmark parameters to some of the bicycles I measured
pathToData = '/media/Data/Documents/School/UC Davis/Bicycle Mechanics/BicycleParameters/data'

browser = bp.Bicycle('Browser', pathToData=pathToData, forceRawCalc=True)
browser.add_rider('Jason')

goldenRatio = (5**0.5 - 1.0) / 2.0
fig_width = 5.0
fig_height = fig_width * goldenRatio
fig_size =  [fig_width,fig_height]
params = {'axes.labelsize': 10,
          'text.fontsize': 10,
          'legend.fontsize': 10,
          'xtick.labelsize': 8,
          'ytick.labelsize': 8,
          'text.usetex': True,
          'figure.figsize': fig_size}
plt.rcParams.update(params)

speedFig = plt.figure()

browser.compare_bode_speeds([0.5, 2.0, 6.0, 10.0], 1, 0, fig=speedFig)
#sixLine = speedFig.ax2.lines[2]
#sixLine.set_ydata(sixLine.get_ydata() + 360.)
speedFig.savefig('../../figures/parameterstudy/bode-speeds.pdf')
speedFig.savefig('../../figures/parameterstudy/bode-speeds.png', dpi=200)

# compare heavy bicycle to light bicycle
rigid = bp.Bicycle('Rigid', pathToData=pathToData, forceRawCalc=True)
rigid.add_rider('Jason', reCalc=True)

# add the rider from the rigid configuration to the pista, this normalizes the
# rider inertial influence between bicycles
pista = bp.Bicycle('Pista', pathToData=pathToData, forceRawCalc=True)
pista.parameters['Benchmark'] = bp.rider.combine_bike_rider(pista.parameters['Benchmark'],
        rigid.riderPar['Benchmark'])

weightFig = plt.figure()
bp.compare_bode_bicycles([rigid, pista], 5.0, 1, 0, fig=weightFig)
weightFig.savefig('../../figures/parameterstudy/bode-weight.pdf')
weightFig.savefig('../../figures/parameterstudy/bode-weight.png', dpi=200)
