===========================
Bicycle Equations Of Motion
===========================

Introduction
============

Attempting to derive the equations of motion of the Whipple model is pretty
much what got me hooked into bicycle dynamics. I attempted it for my class
project in Mont Hubbard's winter 2006 multi-body dynamics class and struggle
with it well into the summer before finally getting a mostly correct answer.
After the fact, I realized much of my pain was cause by a single missing
apostrophe in my Autolev computer code[#]_. Another student, Thomas Englehardt,
in the class also derived the equations and helped me debug by sharing his code
and going over his methods. It turned out that my orignial equations weren't
"exactly" correct and it wasn't until Luke Peterson joined our lab and got the
bicycle dynamics itch did I get the bugs sorted out in my derivation.
Conversations and collaboration with Luke have improved the derivation
significantly and influence much of what follows. Luke has also continued to
improve the derivation with the goal of printing the first compact symbolic
result.

Derivation of the Non-linear Equations of Motion
================================================

The Whipple Model will be the foundation for any extensions we develop. This
section details derivation of the non-linear equatios of motion using Kane's
method [KaneLevinson1985]_. The equations of motion are algrebracally unwieldy
and no one so far has publicly shown them in a form compact enough to print for
analytical understanding[#]_. My methodology relies heavily on computer aided
algebra to do the bookkeeping in the deviration, so I will only describe the
necessary details to derive the equations, leaving the algebra and derivatives
to the computer. The symbolic equations of motion herin were developed within
the frame work of Autolev.

Model
-----

The definition of the Whipple Bicycle Model that I use includes these requirements:

* The Whipple model is made up of four rigid bodies (frame/rider,
  fork/handlebar and two wheels)
* The bodies are connected to each other by frictionless revolute joints.
* The wheels contact the ground under pure rolling and no sideslip conditions.
* The bicycle is assumed to be laterally symmetric.
* Flat ground?.

Unfortunately the word "model" will be use in varying contexts when speaking. I
consider a model to be the same if the minimal equation of motion are the same.
This means that the Whipple Bicycle Model linearized about the nominal
configuation is a different model than thet non-linear Whipple Bicycle Model. I
will try to be explicit when refering to the various models.

.. todo::
   Figure of the bicycle geometry with caption: The bicycle in the upright no
   steer configuration. The rigid bodies are the rear wheel, C, frame/rider, D,
   fork/handlebar, F and front wheel, G. The geometric parameters are also
   shown.

Geometry
--------

The geometry of the whipple model can be parameterized in an infinite amount of
ways. It is typical and natural to define the geometry with respect to the modern
descriptions of bicycle geometry that is used in the bicyle fabrication world,
such as wheel diameter/radius, head tube angle, trail and or rake. These
parameterizations pose a problem when developing the non-linear equations of
motion because they are typically defined with respect to a nominal
configuration of the bicycle. The benchmark derivation of the linear whipple
model about the nominal configuration uses a set of non-minimal parameters to
to parameterize the model. These are a bad choice of parameters when looking at
the model from a non-linear perspective, as they vary with time. These
parameters have also been minimized by [Sharp2008]_ by making use of gyrostats.
This formulation helps to simplify the model, but also does not simplify the
non-linear formulation. The motorcycle treatement of geometry is a good
reference [xxxx]_.

.. todo::
   Find the reference to the paper on motorcycle geometry by a italian guy.

With that in mind after using various parameterizations, Luke and I have
settled on the geometric formulation presented by [Psiaki]_. The wheels are
described by their radius (> = 0) and the remaining geometry is defined by
three distances which are time invariant. The distance :math:`d_1` is the
offset to the center of the rear wheel from the steer axis and :math:`d_3` is
the offset of the front wheel from the steering axis. :math:`d_2` is then the
distance along the steer axis from the point of perpendicular intersection to
the rear and front offset lines.

Generalized Coordinates
-----------------------

I use eight generalized coordinates to develop the bicycle configuration. This
is not the miminal set in terms of holonomic constraints or in terms of
ignorable coordinates, but is useful none-the-less primarily due to the nature of
deriving the equations with a CAS.

Orientation
-----------

Before time, there first was the Newtonian reference frame. We chose the
coordiates to fit the ____ standard as in [Meijaard2007]_. I start with
locating the rear wheel contact point in the ground plane of the Newtonian
reference frame, :math:`N`, longitudinal and lateral coordinates :math:`q_1`
and :math:`q_2`, which turn out to be ignorable coordinates. I then orient the
bicycle rear frame reference frame, :math:`C`, with respect to the newtonian
reference frame through a body fixed 3-1-2 rotation defining the yaw angle,
:math:`q_3`, the roll angle, :math:`q_4`, and the pitch angle, :math:`q_5`. The
intermediate frames yaw, :math:`A` and roll, :math:`B`, are implicitly
generated along the way. The rotation matrix of :math:`C` relative to :math:`N`
is then:

.. math::
   :label: NtoC

   ^NR^C =
   \begin{bmatrix}
   -s_3s_4s_5 + c_5c_3 & -s_3c_4 & s_3s_4c_5 + s_5c_3\\
   c_3s_4s_5 + c5s_3 & c_3c_4 & -c_3s_4c_5 + s_5s_4\\
   -c_4s_5 & s_4 & c_4c_5
   \end{bmatrix}

The rear wheel reference frame, :math:`D`, rotates with repect to the bicycle
frame about the :math:`\hat{c}_2` axis through :math:`q_6`.

.. math::
   :label: CtoD

   ^CR^D =
   \begin{bmatrix}
   c_6 & 0 & -s_6\\
   0 & 1 & 0\\
   s_6 & 0 & c_6
   \end{bmatrix}

The fork/handlebar reference frame, :math:`E`, rotates with respect to the
bicycle reference frame about the :math:`\hat{c}_3` axis through :math:`q_7`.

.. math::
   :label: CtoE

   ^CR^E =
   \begin{bmatrix}
   c_7 & s_7 & 0\\
   -s_7 & c_7 & 0\\
   0 & 0 & 1
   \end{bmatrix}

Finally, the front wheel, :math:`F`, rotates with respect to the fork/handlebar
through :math:`q_8` about the :math:`\hat{e}_2` axis.

.. math::
   :label: EtoF

   ^ER^F =
   \begin{bmatrix}
   c_8 & 0 & -s_8\\
   0 & 1 & 0\\
   s_8 & 0 & c_8
   \end{bmatrix}

The first two coordinates locate the the system in the Newtownian reference
frame and the remaing six coordinates orient the four rigid bodies within the
Newtonian reference frame.

.. todo::
   Diagram of the bicycle showing each generalized coordinate.

Position
--------

The positions of the various points on the bicycle must be defined with respect
to the Newtonian reference frame. There are six primary points of interest: the
four mass centers and the two ground contact points.

The point of contact for the bicyle wheels are one of techincally abstract
points in dynamics. There are four distinct points of concern. The first being
the point in the ground plane that instanteously contacts the wheel at any
given time, the point in the ground plane that tracks the contact point, the
point on the wheel that instataneously contacts the ground at any given time,
and the point on the wheel ...

.. todo::
   Contact points need better explanations.

The location of the contact point in the newtonian frame is defined by:

.. math::
   :label: rearWheelContact

   \bar{r}^{D_n/N_o} = q_1\hat{n}_1 + q_2\hat{n}_2

This encompasses a holonomic constraint (the contact point can't move in the n3
direction.

The mass center of the rear wheel, :math:`D_o`, is assumed to be at the center of the wheel:

.. math::
   :label: rearWheelMassCenter

   \bar{r}^{D_o/D_n} = -r_F\hat{b}_3

The mass center of the front wheel, :math:`F_o`, is located by the frame and
fork dimensions:

.. math::
   :label: frontWheelMassCenter

   \bar{r}^{F_o/D_o} = d_1\hat{c}_1 + d_2\hat{c}_3 + d_3\hat{e}_1

It is useful to define a point on the steer axis, :math:`C_e`, such that:

.. math::
   :label: DoToCe

   \bar{r}^{C_e/D_o} = d_1\hat{c}_1

The bicycle frame mass center, :math:`C_o`, is located by two additional
parameters:

.. math::
   :label: frameMassCenter

   \bar{r}^{C_o/D_o} = l_1\hat{c}_1 + l_2\hat{c}_3

Similarly the fork mass center, :math:`E_o`, is located by two more additional
parameters.

.. math::
   :label: forkMassCenter

   \bar{r}^{E_o/F_o} = l_3\hat{e}_1 + l_4\hat{e}_3

The location of the front wheel contact point is less trivial. The vector from
the front wheel center to the contact point is defined as:

.. math::
   :label: frontWheelContact

   \bar{r}^{F_n/F_o} = r_F(\hat{e}_2\times\hat{n}_3)\times\hat{e}_2

   \bar{r}^{F_n/F_o} = r_F(s_4s_7-s_5c_4c_7)\hat{e}_1 + r_Fc_4c_5\hat{e}_3

Where the triple cross product represents the unit vector pointing from the
front wheel center to the front wheel contact. [Basu-Mandal2007]_ give an
explanation and diagram. The equation can also be though of in terms of dot
products such that you subtract the :math:`\hat{n}_3` component of
:math:`\hat{e}_2` from :math:`\hat{n}_3` to get a vector that points from the
front wheel center to the contact point, :math:`\bar{x}`. The vector of
interest can then be formed by multiplying :math:`r_F` by the unit vector in
the direction of :math:`\bar{x}`:

.. math::
   :label: frontWheelContactDot

   \bar{x} = (\hat{a}_3 - (\hat{e}_2 \cdot\hat{a}_3)\hat{e}_2)

   \bar{r}^{F_n/F_o} = r_F\frac{\bar{x}}{||\bar{x}||}

Holonomic Constraints
---------------------

Two holonomic configuration constraints, arising from the fact that both wheels
must touch the ground, complicates the model derivation. The first holonomic
equation is encompassed in the definition of the rear wheel contact point
:eq:`rearWheelContact`. This constraint enforces that the contact point cannot
have an displacement in the :math:`\hat{n}_3` direction[#]_. The second
holonomic constraint is enforced by requiring the front wheel to touch the
ground plane.  The constraint is characterized by a nonlinear relationship
between the roll angle :math:`q_4`, steer angle :math:`q_7` and pitch angle
:math:`q_5`.

.. math::
   :label: holonomicConstraint

   \bar{r}^{G_n/D_n}\cdot\hat{a}_3 =
   d_2c_4c_5 + d_3(s_4s_7-s_5s_4s_7) + r_F(1-(s_4s_7+s_5s_7s_4)^2)^{1/2} -
   r_Rs_4 - d_1s_5s_4 = 0

I choose pitch, :math:`q_6`, as the dependent coordinate. This choice of pitch
has some to do with the fact that in "normal" bicycle configurations, pitch is
constant to the first order. This is not universal and it may be smart to
choose the dependent coordinate differently for other cases.  The constraint
equation can be formulated into a quartic in the sine of the pitch
[Psiaki1979]_, [Peterson2007]_ which is theorectically analytically solveable.
But I do not do this, instead I make us of a new velocity contraint described
in :ref:`nonholonomic`.

Kinematical Differential Equations
----------------------------------

The choice of generalized speeds can significantly reduce the length of the
equations of motion [Mitiguy1996]. This is benefical for both working with the
analytical forms of the equations of motion and the efficiency in computing
them. This is true, but I took the easy way out and chose to not attempt to
select optimum kinematical differerntial equations and select the generalized
speeds to simply be equal to the derivatives of the generalized coordinates. My
only excuse is that computers are fast these days and this may or may not
matter much.

.. math::
   :label: generlizedSpeeds

   u_i = \dot{q}_i

Velocities
----------

The angular and linear velocities of each rigid body are required as usual.
Also the velocities of the points on the wheel at the ground contact points are
required for the developement of the nonholomic constraints. The angular
velocity of the bicycle frame, :math:`C`, in :math:`N` is:

.. math::
   :label: omegaCinN

   ^N\omega^C = (c_5u_4-s_5c_4u_3)\hat{c}_1 + (u_5+s_4u_3)\hat{c}_2 +
   (s_5u_4+c_4c_5u_3)\hat{c}_3

Both the fork and the rear wheel are connected to the bicycle frame by simple revolute joints.

.. math::
   :label: omegaDinC

   ^C\omega^D = u_6\hat{c}_2

.. math::
   :label: omegaEinC

   ^C\omega^E = u_7\hat{c}_3

The front wheel has simple rotation relative to the fork.

.. math::
   :label: omegaFinE

   ^E\omega^F = u_8\hat{e}_2

The angular velocity of any of the bodies can now be computed with respect to
the newtonian reference frame. For example:

.. math::
   :label: omegaFinN

   ^F\omega^N = ^N\omega^C + ^C\omega^E + ^E\omega^F

Using the angular velocities and the position vectors the velocities of the
mass centers can be computed. Starting with mass center of the rear wheel:

.. math::
   :label: DoInN

   ^N\bar{v}^{D_o} = u_1\hat{n}_1 + u_2\hat{n}_2 -
   r_Rs_4u_3\hat{b}_1 + r_Ru_4\hat{b}_2

The mass center of the rear wheel, :math:`D_o` and the mass center of bicycle
frame, :math:`C_o`,  both lie on the bicycle frame so the velocity can easily
be computed:

.. math::
   :label: CoInN

   ^N\bar{v}^{C_o} = ^N\bar{v}^{D_o} + ^N\bar\omega^C\times\bar{r}^{C_o/D_o}

   ^N\bar\omega^C\times\bar{r}^{C_o/D_o} = l_2(u_5+s_4u_3)\hat{c}_1 +
   (l_1(s_5u_4+c_4c_5u_3)-l_2(c_5u_4-s_5c_4u_3))\hat{c}_2
   - l_1(u_5+s_4u_3)\hat{c}_3

The velocity of the steer axis point is computed in the same fashion:

.. math::
   :label: test

   ^N\bar{v}^{C_e} = ^N\bar{v}^{D_o} + ^N\bar\omega^C\times\bar{r}^{C_e/D_o}

   ^N\bar\omega^C\times\bar{r}^{C_e/D_o} = d_1(s_5u_4+c_4c_5u_3)\hat{c}_2 -
   d_1(u_5+s_4u_3)\hat{c}_3

The velocity of the front wheel center is:

.. math::
   :label: test

   ^N\bar{v}^{F_o} = ^N\bar{v}^{C_e} + ^N\bar\omega^E\times\bar{r}^{F_o/C_e}

   ^N\bar\omega^E\times\bar{r}^{F_o/C_e} =
   &-d_2(s_7c_5u_4-c_7u_5-(s_4c_7+s_5s_7c_4)u_3)\hat{e}_1 +\\
   &(d_3(u_7+s_5u_4+c_4c_5u_3)-d_2(s_7u_5+c_5c_7u_4+(s_4s_7-s_5c_4c_7)u_3))\hat{e}_2 +\\
   &d_3(s_7c_5u_4-c_7u_5-(s_4c_7+s_5s_7c_4)u_3)\hat{e}_3

Then the velocity of the fork mass center can be defined as:

.. math::
   :label: EoInN

   ^N\bar{v}^{E_o} = ^N\bar{v}^{F_o} + ^N\omega^E\times\bar{r}^{E_o/F_o}

   ^N\omega^E\times\bar{r}^{E_o/F_o} =
   &-l4(s_7c_5u_4-c_7u_5-(s_4c_7+s_5s_7c_4)u_3)\hat{e}_1 +\\
   &(l3(u_7+s_5u_4+c_4c_5u_3)-l4(s_7u_5+c_5c_7u_4+(s_4s_7-s_5c_4c_7)u_3))\hat{e}_2 +\\
   &l3(s_7c_5u_4-c_7u_5-(s_4c_7+s_5s_7c_4)u_3)\hat{e}_3

The velocity of the contact points on the wheel are needed to enforce the
no-slip condition.

.. math::
   :label: DnInN

   ^N\bar{v}^{D_n} = ^N\bar{v}^{D_o} + ^N\omega^D\times\bar{r}^{D_n/D_o}

   ^N\omega^D\times\bar{r}^{D_n/D_o} = r_R(u_5+u_6+s_4u_3)\hat{b}_1 - r_Ru_4\hat{b}_2

   ^N\bar{v}^{D_n} = r_R(u_5+u_6)\hat{b}_1 + u_1\hat{n}_1 + u_2\hat{n}_2

The front wheel contact velocity:

.. math::
   :label: FnInN

   ^N\bar{v}^{F_n} = ^N\bar{v}^{F_o} + ^N\omega^F\times\bar{r}^{F_n/F_o}

   ^N\omega^F\times\bar{r}^{F_n/F_o} =&
   -r_Fc_4c_5(s_7c_5u_4-u_8-c_7u_5-(s_4c_7+s_5s_7c_4)u_3)\hat{e}_1 -\\
   &r_F(c_4c_7u_4+s_7c_4c_5u_5-s_4s_5s_7u_4-(s_4s_7-s_5c_4c_7)u_7)\hat{e}_2 +\\
   &r_F(s_4s_7-s_5c_4c_7)(s_7c_5u_4-u_8-c_7u_5-(s_4c_7+s_5s_7c_4)u_3)\hat{e}_3

Acceleration
------------

The angular acceleration of each body along with the linear acceleration of
each mass center are required to form :math:`F_r^*`. The angular acceleration
of the bicycle reference frame in :math:`N` is:

.. math::
   :label: alphaCinN

   ^N\bar{\alpha}^C =
   &(s_4s_5u_3u_4+c_5\dot{u}_4-s_5u_4u_5-c_4c_5u_3u_5-s_5c_4\dot{u}_3)\hat{c}_1 +
   (c_4u_3u_4+\dot{u}_5+s_4\dot{u}_3)\hat{c}_2 +\\
   &(c_5u_4u_5+s_5\dot{u}_4+c_4c_5\dot{u}_3-s_4c_5u_3u_4-s_5c_4u_3u_5)\hat{c}_3

.. math::
   :label: alphaDinC

   ^C\bar{\alpha}^D = \dot{u}_6\hat{c}_2

.. math::
   :label: alphaEinC

   ^C\bar{\alpha}^E = \dot{u}_7\hat{c}_3

.. math::
   :label: alphaFinE

   ^E\bar{\alpha}^F = \dot{u}_8\hat{e}_2

The linear acceleration of each mass center can then be computed.

The acceleration of the rear wheel center of mass.

.. math::
   :label: aDoInN

   ^N\bar{a}^{D_o} = \dot{u}_1\hat{n}_1 + \dot{u}_2\hat{n}_2 -
   r_Rs_4u_3^2\hat{a}_2 - r_R(2c_4u_3u_4+s_4\dot{u}_3)\hat{b}_1 +
   r_R\dot{u}_4\hat{b}_2 + r_Ru_4^2\hat{b}_3

The acceleration of the biycle frame center of mass.

.. math::
   :label: aCoinN

   ^N\bar{a}^{C_o} = ^N\bar{a}^{D_o} + ^N\omega^C\times(^N\omega^C\times\bar{r}^{C_o/D_o}) + ^N\bar{\alpha}^C\times\bar{r}^{C_o/D_o}

   ^N\omega^C\times(^N\omega^C\times\bar{r}^{C_o/D_o}) =
    &(-l_1(u_5+s_4u_3)^2-(s_5u_4+c_4c_5u_3)(l_1(s_5u_4+c_4c_5u_3)-l_2(c_5u_4-s_5c_4u_3)))\hat{c}_1 +\\
    &(u_5+s_4u_3)(l_2(s_5u_4+c_4c_5u_3)+l_1(c_5u_4-s_5c_4u_3))\hat{c}_2\\
    &+ ((c_5u_4-s_5c_4u_3)(l_1(s_5u_4+c_4c_5u_3)-l_2(c_5u_4-s_5c_4u_3))-l_2(u_5+s_4u_3)^2)\hat{c}_3

   ^N\bar{\alpha}^C\times\bar{r}^{C_o/D_o} =
   &l_2(c_4u_3u_4+\dot{u}_5+s_4\dot{u}_3)\hat{c}_1 +\\
   &(-l_1(s_4c_5u_3u_4+s_5c_4u_3u_5-c_5u_4u_5-s_5\dot{u}_4-c_4c_5\dot{u}_3)-l_2(s_4s_5u_3u_4+c_5\dot{u}_4-s_5u_4u_5-c_4c_5u_3u_5-s_5c_4\dot{u}_3))\hat{c}_2 -\\
   &l_1(c_4u_3u_4+\dot{u}_5+s_4\dot{u}_3)\hat{c}_3

The acceleration of the steer axis point.

.. math::
   :label: aCeInN

   ^N\bar{a}^{C_e} = ^N\bar{a}^{D_o} + ^N\omega^C\times(^N\omega^C\times\bar{r}^{C_e/D_o}) + ^N\bar{\alpha}^C\times\bar{r}^{C_e/D_o}

   ^N\omega^C\times(^N\omega^C\times\bar{r}^{C_e/D_o}) =
    &-d_1((u_5+s_4u_3)^2+(s_5u_4+c_4c_5u_3)^2)\hat{c}_1 +\\
    &d_1(u_5+s_4u_3)(c_5u_4-s_5c_4u_3)\hat{c}_2 +\\
    &d_1(s_5u_4+c_4c_5u_3)(c_5u_4-s_5c_4u_3)\hat{c}_3

   ^N\bar{\alpha}^C\times\bar{r}^{C_e/D_o} =
   &-d_1(s_4c_5u_3u_4+s_5c_4u_3u_5-c_5u_4u_5-s_5\dot{u}_4-c_4c_5\dot{u}_3)\hat{c}_2 -\\
   &d_1(c_4u_3u_4+\dot{u}_5+s_4\dot{u}_3)\hat{c}_3

The acceleration of the front wheel center of mass.

.. math::
   :label: aFoInN

   ^N\bar{a}^{F_o} = ^N\bar{a}^{C_e} + ^N\omega^E\times(^N\omega^E\times\bar{r}^{F_o/C_e}) + ^N\bar{\alpha}^E\times\bar{r}^{F_o/C_e}

   ^N\omega^E\times(^N\omega^E\times\bar{r}^{F_o/C_e}) =
    &(-d_3(s_7c_5u_4-c_7u_5-(s_4c_7+s_5s_7
    c_4)u_3)^2-(u_7+s_5u_4+c_4c_5u_3)(d_3(u_7+s_5u_4+c_4
    c_5u_3)-d_2(s_7u_5+c_5c_7u_4+(s_4s_7-s_5c_4c_7)u_3)))\hat{e}_1 -\\
    &(s_7c_5u_4-c_7u_5-(s_4c_7+s_5s_7
    c_4)u_3)(d_2(u_7+s_5u_4+c_4c_5u_3)+d_3(s_7u_5+c_5
    c_7u_4+(s_4s_7-s_5c_4c_7)u_3))\hat{e}_2 +\\
    &((s_7u_5+c_5c_7u_4+(s_4s_7-s_5c_4c_7)u_3)(d_3(u_7+s_5u_4+c_4c_5u_3)-
    d_2(s_7u_5+c_5c_7u_4+(s_4s_7-s_5c_4c_7)u_3))-d_2(s_7c_5u_4-c_7u_5-(s_4c_7+s_5s_7c_4)u_3)^2)\hat{e}_3

   ^N\bar{\alpha}^E\times\bar{r}^{F_o/C_e} =
    &-d_2(s_7u_5u_7+c_5c_7u_4u_7+u_3(s_4s_7u_7+s_4s_5s_7u_4-c_4c_7u_4-s_5c_4c_7u_7-s_7c_4c_5u_5)+s_7c_5\dot{u}_4-s_5s_7u_4u_5-c_7\dot{u}_5-(s_4c_7+s_5s_7c_4)\dot{u}_3)\hat{e}_1 +\\
    &(d_2(s_5c_7u_4u_5+s_7c_5u_4u_7-c_7u_5u_7-u_3(s_4c_7u_7+s_7c_4u_4+s_4s_5c_7u_4+s_5s_7c_4u_7-c_4c_5c_7u_5)-s_7\dot{u}_5
    -c_5c_7\dot{u}_4-(s_4s_7-s_5c_4c_7)\dot{u}_3)-d_3(s_4
    c_5u_3u_4+s_5c_4u_3u_5-c_5u_4u_5-\dot{u}_7-s_5\dot{u}_4-c_4c_5\dot{u}_3))\hat{e}_2 +\\
    &d_3(s_7u_5u_7+c_5c_7u_4u_7+u_3(s_4s_7u_7+
    s_4s_5s_7u_4-c_4c_7u_4-s_5c_4c_7u_7-s_7c_4c_5u_5)+s_7c_5\dot{u}_4-s_5s_7u_4u_5-c_7\dot{u}_5-(s_4
    c_7+s_5s_7c_4)\dot{u}_3)\hat{e}_3

The acceleration of the fork center of mass.

.. math::
   :label: aEoInN

   ^N\bar{a}^{E_o} = ^N\bar{a}^{F_o} + ^N\omega^E\times(^N\omega^E\times\bar{r}^{E_o/F_o}) + ^N\bar{\alpha}^E\times\bar{r}^{E_o/F_o}

   ^N\omega^E\times(^N\omega^E\times\bar{r}^{E_o/F_o}) =
   &(-l_3(s_7c_5u_4-c_7u_5-(s_4c_7+s_5s_7c_4)u_3)^2-(u_7+s_5u_4+c_4c_5u_3)(l_3(u_7+s_5u_4+c_4c_5u_3)-
   l_4(s_7u_5+c_5c_7u_4+(s_4s_7-s_5c_4c_7)u_3)))\hat{e}_1 -\\
   &(s_7c_5u_4-c_7u_5-(s_4c_7+s_5s_7c_4)u_3)(l_4(u_7+s_5u_4+c_4c_5u_3)+l_3(s_7u_5+c_5c_7u_4+(s_4s_7-s_5c_4c_7)u_3))\hat{e}_2 +\\
   &((s_7u_5+c_5c_7u_4+(s_4s_7-s_5c_4c_7)u_3)(l_3(u_7+s_5u_4+c_4c_5u_3)-
   l_4(s_7u_5+c_5c_7u_4+(s_4s_7-s_5c_4c_7)u_3))-l_4(s_7c_5u_4-c_7u_5-(s_4c_7+s_5s_7c_4)u_3)^2)\hat{e}_3

   ^N\bar{\alpha}^E\times\bar{r}^{E_o/F_o} =
   &-l_4(s_7u_5u_7+c_5c_7u_4u_7+u_3(s_4s_7u_7+s_4s_5s_7u_4-c_4c_7u_4-
   s_5c_4c_7u_7-s_7c_4c_5u_5)+s_7c_5\dot{u}_4-s_5s_7u_4u_5-c_7\dot{u}_5-
   (s_4c_7+s_5s_7c_4)\dot{u}_3)\hat{e}_1 +\\
   &(l_4(s_5c_7u_4u_5+s_7c_5u_4u_7-c_7u_5u_7-u_3(s_4c_7u_7+s_7c_4u_4+
   s_4s_5c_7u_4+s_5s_7c_4u_7-c_4c_5c_7u_5)-s_7\dot{u}_5
   -c_5c_7\dot{u}_4-(s_4s_7-s_5c_4c_7)\dot{u}_3)-l_3(s_4
   c_5u_3u_4+s_5c_4u_3u_5-c_5u_4u_5-\dot{u}_7-s_5\dot{u}_4-c_4c_5\dot{u}_3))\hat{e}_2 +\\
   &l_3(s_7u_5u_7+c_5c_7u_4u_7+u_3(s_4s_7u_7+s_4s_5s_7u_4-c_4c_7u_4-
   s_5c_4c_7u_7-s_7c_4c_5u_5)+s_7c_5\dot{u}_4-s_5s_7u_4u_5-c_7\dot{u}_5-(s_4
   c_7+s_5s_7c_4)\dot{u}_3)\hat{e}_3

Mass
----

The mass of each rigid body is defined as a constant: :math:`m_C`, :math:`m_D`,
:math:`m_E` and :math:`m_F`.

Inertia
-------

The inertia for each body is defined with respect to the mass center and the
body's local reference frame. The bicycle wheels are assumed to be symmetric
about their 1-3 plane and the 1-2 plane.

.. math::
   :label: ID

   I_D =
   \begin{bmatrix}
   I_{D11} & 0 & 0\\
   0 & I_{D22} & 0\\
   0 & 0 & I_{D11}
   \end{bmatrix}

.. math::
   :label: IF

   I_F =
   \begin{bmatrix}
   I_{F11} & 0 & 0\\
   0 & I_{F22} & 0\\
   0 & 0 & I_{F11}
   \end{bmatrix}

The bicycle frame and fork are assumed to be symmetric about their 1-3 planes.

.. math::
   :label: IC

   I_C =
   \begin{bmatrix}
   I_{C11} & 0 & I_{C13}\\
   0 & I_{C22} & 0\\
   I_{C13} & 0 & I_{C33}
   \end{bmatrix}

.. math::
   :label: IE

   I_E =
   \begin{bmatrix}
   I_{E11} & 0 & I_{E13}\\
   0 & I_{E22} & 0\\
   I_{E13} & 0 & I_{E33}
   \end{bmatrix}

.. todo:: Should I show these as inertia dyadics instead?

Generalized Active Forces
-------------------------

We assume that the only force acting on the system is the gravitational force,
:math:g. Thus:

.. math::

  F_{C_o} = m_Cg\hat{n}_3

  F_{D_o} = m_Dg\hat{n}_3

  F_{E_o} = m_Eg\hat{n}_3

  F_{F_o} = m_Fg\hat{n}_3

We assume that there are three generalized active torques acting the system
which will correspond to the three independent generalized speeds found in
:ref:`nonholonomic`.

The roll torque, :math:`T_4`, acts between the bicycle frame and the newtonian
frame about :math:`\hat{a}_1`. The rear wheel torque, :math:`T_6`, acts between the bicycle
frame and the rear wheel about :math:`\hat{c}_2` and the steer torque, :math:`T_7`, acts
between the bicycle frame and the fork about :math:`\hat{c}_3`.

.. _nonholonomic:

Non-holonomic Constraints
-------------------------

I make use of five non-holonomic constraints to reduce the locally achievable
configuration space from eight degrees of freedom to three. The first four
constraints are introduced to enforce the pure rolling, no side-slip, contact
of the knife-edge wheels with the ground plane. This requires that there are no
components of velocity of the wheel contact points in the
:math:`{\mathbf{a}}_1` and :math:`{\mathbf{a}}_2` directions producing the
following relationships:

.. math::

   ^N\bar{v}^{D_n}\cdot\hat{a}_1 = s_3u_2 + c_3u_1 + r_R(u_5+u_6) = 0

   ^N\bar{v}^{D_n}\cdot\hat{a}_2 = c_3u_2 - s_3u_1 = 0

   ^N\bar{v}^{F_n}\cdot\hat{a}_1 =
   &s_3u_2 + c_3u_1 + d_2c_5u_5 + d_2s_4c_5u_3 + r_Fc_4c_7(u_8+c_7u_5+(s_4c_7+s_5s_7c_4)u_3) -\\
   &r_Rs_4u_3 - d_3s_7c_4u_3 - d_1s_5(u_5+s_4u_3) - s_7c_5(d_3u_7-r_F(s_7c_4c_5u_5-(s_4s_7-s_5c_4c_7)u_7))\\
   &- s_5(d_3c_7(u_5+s_4u_3)+rFs_4s_7(u_8+c_7u_5+(s_4c_7+s_5s_7c_4)u_3)) = 0

   ^N\bar{v}^{F_n}\cdot\hat{a}_2 =
   &c_3u_2 + d_1c_5u_3 + r_Rc_4u_4 + d_1s_4c_5u_5 + d_1s_5c_4u_4 + (c_4c_7-s_4s_5s_7)(d_3(u_7+s_5u_4+c_4c_5u_3)-\\
   &d_2(s_7u_5+c_5c_7u_4+(s_4s_7-s_5c_4c_7)u_3)-r_F(c_4c_7u_4+s_7c_4c_5u_5-s_4s_5s_7u_4-(s_4s_7-s_5c_4c_7)u_7)) -\\
   &s_3u_1 - (s_7c_4+s_4s_5c_7)(d_2(s_7c_5u_4-c_7u_5-(s_4c_7+s_5s_7c_4)u_3)+\\
   &r_Fc_4c_5(s_7c_5u_4-u_8-c_7u_5-(s_4c_7+s_5s_7c_4)u_3)) - s_4c_5(d_3(s_7c_5u_4-c_7u_5-(s_4c_7+s_5s_7c_4)u_3)+\\
   &r_F(s_4s_7-s_5c_4c_7)(s_7c_5u_4-u_8-c_7u_5-(s_4c_7+s_5s_7c_4)u_3))

The fifth non-holonomic velocity constraint is not a necessary one but can be
used to manage the second holonomic constraint :eq:`something` and is a method
to avoid having to solve the quartic algebraically. By differentiating the
holonomic cosntraint equation we arrive at velocity equation that is linear in
the speeds and can be treated as a non-holonomic constrain even though it is
not one.

.. math::

   \frac{d}{dt}(\bar{r}^{G_n/D_n}\cdot\hat{a}_3) =
   &r_Rs_4u_4 + d_1s_4s_5u_4 + d_3(s_4c_7u_7+s_7c_4u_4+s_4s_5c_7u_4+s_5s_7c_4u_7-c_4c_5c_7u_5) +\\
   &2r_F(s_4s_7-s_5c_4c_7)(s_4c_7u_7+s_7c_4u_4+s_4s_5c_7u_4+s_5s_7c_4u_7-c_4c_5c_7u_5) -\\
   &d_1c_4c_5u_5 -d_2s_5c_4u_5 - 2r_Fs_5c_5c_4^2u_5 -s_4c_5(d_2+2r_Fc_4c_5)u_4 = 0

These five equations are linear in the generalized speeds. I chose the roll
rate, :math:`u_4`, the rear wheel rate, :math:`u_6`, and the steer rate,
:math:`u_7`, as my independent generalized speeds following convention.

At this point, you can find the solution for the dependent speeds as a function
of the independent speeds but it  becomes analytically long and it is not
necessarily trivial to reduce their length. A smarter choice of generalized
speeds could certainly help, but I did not spend great effort to search for an
optimum set. From this point on, I will not show the analytical results of the
equations of motion, but will only walk through the remainder of the theory, as
all of the building blocks are in place to derive the equations with Kane's
method (or any other method). I highly recommend the use of computer aided
algebra to continue on, but for the diehard you certainly could write them by
hand.

The dependent speeds take this form:

.. math::
   u_1 = f(u_4, u_6, u_7, q_1, \ldots, q_8)

   u_2 = f(u_4, u_6, u_7, q_1, \ldots, q_8)

   u_3 = f(u_4, u_6, u_7, q_1, \ldots, q_8)

   u_5 = f(u_4, u_7, q_1, \ldots, q_8)

   u_8 = f(u_4, u_6, u_7, q_1, \ldots, q_8)


Fr
--

Eight generalized coordinates, one of which is dependent, and three
independent generalized speeds (:math:`u_i=\dot{q}_i` where
:math:`i = 4,5,7`) describe the system. Five of these are
ignorable coordinates (:math:`q_i`, :math:`i = 1,2,3,5,8`),
that is they do not occur in the dynamical equations of motion. The
nonminimal set of dynamic equations of motion (Eqs. eq:accels
and eq:speeds) were formed by Kane's method. They are nonminimal
because pitch angle, :math:`q_6`, was not solved for explicitly.
With this set of equations one must calculate the pitch angle
numerically for its initial condition when simulating and for the
fixed point when linearizing.

.. math::
   \dot{u}_i=f\left(u_4,u_5,u_7,q_4,q_6,q_7\right)\textrm{ where }i=4,5,7
   :label: {eq:accels}

.. math::
   \dot{q}_i=u_i\textrm{ where }i=4,5,6,7
   :label: {eq:speeds}

Ignorable Coordinates
---------------------

The equations of motion indicate that the location of the rear wheel contact,
yaw angle, and both wheel angles are ignorable.

Simulation
----------
.. todo:: Show the same simulation with regards to Meijaard2007 and a step/impulse response.

Validation
----------
.. todo:: Compare to Basu-Mandall2007 and Meijaard2007

Linearized Equations of Motion
==============================

The equations of motion can then be linearized by calculating the
Jacobian of the system of equations. The partial derivatives were
evaluated at the following fixed point: :math:`q_i=0` where
:math:`i=4,6,7`, :math:`u_i=0` where :math:`i=4,7`, and
:math:`u_5=-v/R_r` where :math:`v` is the constant forward
speed of the bicycle. This reduces the system to four linear first
order differential equations in the form:

.. math::
   \frac{d}{dt}
    \left[
    \begin{array}{c}
        q_4\\q_5\\q_6\\q_7\\u_4\\u_5\\u_7
    \end{array}
    \right]
    =
    \mathbf{A}
    \left[
    \begin{array}{c}
        q_4\\q_5\\q_6\\q_7\\u_4\\u_5\\u_7
    \end{array}
    \right]
    \label{eq:linearEq}

Validation
----------

The linearized model was checked for accuracy against
the benchmark bicycle in two ways. First the linearized equations
of motion (Eq. eq:linearEq) were formulated into two second order
differential equations in the more familiar canonical form
(Eq. eq:canonical) used in [MeijaardPapadopoulosRuinaSchwab2007]_.
They present the values for the coefficient matrices
(:math:`\mathbf{M}`, :math:`\mathbf{C}_1`,
:math:`\mathbf{K}_0` and :math:`\mathbf{K}_2`) for the
benchmark parameter set at least 15 significant figures and my
model matched all of the significant figures.

.. math::
   \mathbf{M\dot{u}}+v\mathbf{C}_1\mathbf{u}+\left[g\mathbf{K}_0+v^2\mathbf{K}_2\right]\mathbf{q}=0
   :label: {eq:canonical}

The eigenvalues of the system of linear equations can be calculated
and are typically plotted versus forward speed for the linear
upright constant speed configuration (Fig. fig:eigenvalues).
[MeijaardPapadopoulosRuinaSchwab2007]_also provided eigenvalue
calculations at various speeds of the benchmark bicycle for model
comparison. The eigenvalues for my model matched to at least 15
significant figures.

.. todo::
   Eigenvalues versus speed for an example bicycle. The four modes of
   motion are identified. \\emph[Caster]_ is stable and real for all positive
   values of speed. It describes the tendency for the front wheel to right
   itself in forward motion. \\emph[Capsize]_ is always real, stable at low speeds
   and becomes marginally unstable at a higher speed. It describes the roll of
   the rear frame. \\emph[Weave]_ is real at very low speeds and describes an
   inverted pendulum-like motion i.e. the bicycle falls over. As speed increases
   the eigenvalues coalesce into a complex conjugate pair that describes a
   sinusoidal motion of the roll and steer, with steer lagging the roll. This
   mode becomes stable at a higher speed. The weave and capsize critical speeds
   bound a stable speed range.

.. rubric:: Footnotes

.. [#] My colleague, Dale L. Peterson, has made significant progress
       formulating the equations of motion in a readable and compact form, which will
       most likely be published soon.
.. [#] Luke and I have dreamed of developing an open source version of Autolev
       for years and that has finally culminated through primarily Luke and Gilber
       Gede's efforts in the creation of sympy.physics.mechanics.
.. [#] This contraint can readily be modified to support a non-flat ground.
