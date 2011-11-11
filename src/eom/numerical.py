import re
from scipy.integrate import ode
from numpy import zeros
from matplotlib.pyplot import plot, show
from math import pi

def simulate_chaos_pendulum():
    args = [9.81, 0.075, 0.01, 5E-6, 0.2, 0.1, 50e-6, 250e-6, 200e-6]
    initial = [0.785398163, 0.00872664626, 0.0, 0.0]
    ti = 0.0
    tf = 10.0
    dt = 0.01

    from chaos import f

    r = ode(f).set_integrator('vode')
    r.set_initial_value(initial, ti).set_f_params(args)

    x = zeros((int((tf - ti) / dt), len(initial)))
    t = zeros(int((tf - ti) / dt))
    i = 0
    while r.successful() and r.t < (tf - dt):
        x[i, :] = r.y
        t[i] = r.t
        r.integrate(r.t + dt)
        i += 1

    plot(t, x * 180. / pi)
    show()
    return t, x

def output_scipy(kane, filename):
    """Writes a python module which includes code for numerically integrating a
    system derived with sympy.physics.mechanics.

    Parameters
    ----------
    kane : Kane
    filename : string

    """

    stateNames = [cleanse(x) for x in (kane._q + kane._u)]
    allPar = [cleanse(x) for x in (kane._find_othersymbols(kane._fr) +
        kane._find_othersymbols(kane._frstar))]

    # remove duplicates and sort
    parameterNames = sorted(list(set(allPar)),
        key=lambda x: x.lower())
    parameterNames.remove('t')

    m = kane.mass_matrix_full
    f = kane.forcing_full

    indent = ' ' * 4
    content = "from numpy import zeros, sin, cos\n"
    content += "from numpy.linalg import solve\n\n"
    content += "def f(t, x, args):\n    # unpack the states\n\n"

    for i, state in enumerate(stateNames):
        content += indent + state + ' = x[' + str(i) + ']\n'

    content += '\n    # unpack the parameters\n\n'
    for i, parameter in enumerate(parameterNames):
        content += indent + parameter + ' = args[' + str(i) + ']\n'

    content += '\n    # mass matrix\n\n'
    content += indent + 'm = zeros((' + str(m.shape[0]) + ', ' + str(m.shape[1]) + '))\n'
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            content += indent + 'm[' + str(i) + ', ' + str(j) + '] = ' + cleanse(m[i, j]) + '\n'

    content += '\n    # forcing vector\n\n'
    content += indent + 'f = zeros(' + str(len(f)) + ')\n'
    for i in range(len(f)):
        content += indent + 'f[' + str(i) + '] = ' + cleanse(f[i]) + '\n'

    content += '\n' + indent + 'return solve(m, f)'

    modFile = open(filename, 'w')
    modFile.write(content)
    modFile.close()

def cleanse(exp):
    noqDots = re.sub(r'Derivative\(q(\d)\(t\), t\)\)', r'u\1', str(exp))
    return noqDots.replace('(t)', '')
