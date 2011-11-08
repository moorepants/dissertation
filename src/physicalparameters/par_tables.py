import os
import bicycleparameters as bp
from bicycleparameters.tables import Table

pathToData = '/media/Data/Documents/School/UC Davis/Bicycle Mechanics/BicycleParameters/data'
pathToTables = '../../tables/physicalparameters'

def create_tables(bikeNames, groupName):
    batavusBikes = []
    for bike in bikeNames:
        batavusBikes.append(bp.Bicycle(bike, pathToData=pathToData, forceRawCalc=True))

    for typ in ['Measured', 'Benchmark']:
        tab = Table('Measured', True, batavusBikes)
        pathToTableFile = os.path.join(pathToTables, groupName + typ + '.rst')
        tab.create_rst_table(fileName=pathToTableFile)
    print('Tables created for', bikeNames)

# make a tables for the batavus bikes
batavusNames = ['Browser', 'Browserins', 'Stratos', 'Crescendo']
delftNames = ['Fisher', 'Pista', 'Yellow', 'Yellowrev']
davisNames = ['Rigid', 'Rigidcl']
groupNames = ['batavus', 'delft', 'davis']

for pair in zip([batavusNames, delftNames, davisNames], groupNames):
    create_tables(pair[0], pair[1])
