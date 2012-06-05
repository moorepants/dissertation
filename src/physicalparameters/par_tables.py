import os
import bicycleparameters as bp
from bicycleparameters.tables import Table

pathToData = '/media/Data/Documents/School/UC Davis/Bicycle Mechanics/BicycleParameters/data'
pathToTables = '../../tables/physicalparameters'

def create_tables(bikeNames, groupName):
    bikes = []
    for bike in bikeNames:
        bikes.append(bp.Bicycle(bike, pathToData=pathToData,
            forceRawCalc=True))

    for typ in ['Measured', 'Benchmark']:
        tab = Table(typ, True, bikes)
        pathToTableFile = os.path.join(pathToTables, groupName + typ + '.rst')
        tab.create_rst_table(fileName=pathToTableFile)
    print('Tables created for', bikeNames)

# make a tables for the batavus bikes
batavusNames = ['Browser', 'Browserins', 'Stratos']
delftNames = ['Crescendo', 'Fisher', 'Pista']
yellowNames = ['Yellow', 'Yellowrev']
davisNames = ['Rigid', 'Rigidcl', 'Gyro']
groupNames = ['batavus', 'delft', 'yellow', 'davis']

for pair in zip([batavusNames, delftNames, yellowNames, davisNames],
        groupNames):
    create_tables(pair[0], pair[1])
