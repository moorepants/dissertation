from altk import alutils

matrices = ('A', 'B', 'C', 'D')
states = ['q' + str(i + 1) for i in range(8)] + ['u4', 'u6', 'u7']
inputs = ['Fcl', 'T4', 'T6', 'T7']
outputs = ['q' + str(i + 1) for i in range(8)] + ['u' + str(i + 1) for i in range(8)]

alutils.write_linearization(matrices, states, inputs, outputs,
        filename='lin.al')
