#!/usr/bin/env python
import os
import cPickle
from canonicalbicycleid import canonical_bicycle_id as cbi

# Specify the data files
dataDir = '/media/Data/Documents/School/UC Davis/Bicycle Mechanics/CanonicalBicycleID/data'
pathToIDMat = os.path.join(dataDir, 'idMatrices.p')
pathToCovar = os.path.join(dataDir, 'covarMatrices.p')

with open(pathToIDMat) as f:
    idMat = cPickle.load(f)

with open(pathToCovar) as f:
    covMat = cPickle.load(f)
fNames = ['one', 'two', 'three']

roll = [['Mpd', 'C1pd', 'K0pd'], [], []]
steer = [[], ['Mdd', 'C1dp', 'C1dd'], ['K0dd', 'K2dd', 'HdF']]

for n, r, s in zip(fNames, roll, steer):
    tableData = cbi.table_data(r, s, idMat, covMat)
    cbi.create_rst_table(tableData, r, s,
            fileName='../../tables/systemidentification/canonical-id-table-' +
            n + '.rst')

# this computes the trail given the identified C1dp parameter
rigid = cbi.bp.Bicycle('Rigid', '/media/Data/Documents/School/UC Davis/Bicycle Mechanics/BicycleParameters/data')
p = cbi.bp.io.remove_uncertainties(rigid.parameters['Benchmark'])
SF = p['IFyy'] / p['rF']
SR = p['IRyy'] / p['rR']
ST = SR + SF
for k, v in idMat.items():
    C1dp = v[1][1, 0]
    c = -p['w'] * (C1dp + SF * cbi.np.cos(p['lam'])) / ST / cbi.np.cos(p['lam'])
    print k, c
