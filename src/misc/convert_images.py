#!usr/bin/env python

import os

def convert_all(directory, inputExt, outputExt, dpi=300):
    allFiles = os.listdir(directory)
    inputFiles = [x for x in allFiles if x.endswith(inputExt)]
    outputFiles = [os.path.splitext(x)[0] + '.' +outputExt for x in inputFiles]
    for i, o in zip(inputFiles, outputFiles):
        convert_image(directory + i, directory + o, dpi=dpi)

def convert_image(inputFileName, outputFileName, dpi=300):

    os.system('convert -density ' + str(dpi) + ' "' + inputFileName +
            '" -density ' + str(dpi) + ' "' + outputFileName + '"')
