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

roll = ['Mpd', 'C1pd']
steer = ['Mdd', 'C1dp', 'C1dd']

tableData = cbi.table_data(roll, steer, idMat, covMat)

cbi.create_rst_table(tableData, roll, steer,
        fileName='../../tables/systemidentification/canonical-id-table-one.rst')

roll = ['K0pd']
steer = ['K0dd', 'K2dd', 'HdF']

tableData = cbi.table_data(roll, steer, idMat, covMat)

cbi.create_rst_table(tableData, roll, steer,
        fileName='../../tables/systemidentification/canonical-id-table-two.rst')
