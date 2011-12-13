# so Yeadon defines his shoulder angles one way and I define mine another, how
# can I map his angles to my angles?
import sympy as sy
import sympy.physics.mechanics as me

alpha, beta, gamma, delta = sy.symbols('alpha beta gamma delta')
lam, q13, q14, q15 = sy.symbols('lambda q13 q14 q15')

newton = me.ReferenceFrame('N', indices=('1', '2', '3'))
bicycle = me.ReferenceFrame('C', indices=('1', '2', '3'))
yeadon = me.ReferenceFrame('Y', indices=('1', '2', '3'))
torso = me.ReferenceFrame('T', indices=('1', '2', '3'))

bicycle.orient(newton, 'Axis', (lam, newton['2']))
yeadon.orient(newton, 'Body', (3 * sy.pi / 2, sy.pi, 0), '312')
torso.orient(yeadon, 'Axis', (delta, yeadon['1']))

mooreArm = me.ReferenceFrame('I', indices=('1', '2', '3'))
mooreArm.orient(bicycle, 'Body', (q13, q14, q15), '123')
yeadonArm = me.ReferenceFrame('A', indices=('1', '2', '3'))
yeadonArm.orient(torso, 'Body', (alpha, beta, gamma), '213')
