.. _extensions:

================================================
Extensions and modifcations to the Whipple Model
================================================

Here I present several bicycle models based on of the basic formulation of the
Whipple model in Chapter :ref:`eom`. Various combinations of these model
extensions are used in the later Chapters for analysis.

Lateral Force Input
===================

The Whipple model typically has three input forces roll torque :math:`T_4`,
rear wheel torque :math:`T_6` and steer torque :math:`T_7`. Here I add a fourth
input, lateral force :math:`F_{c_l}`, which acts on a point on the bicycle
frame. The force is defined such that it is always in the :math:`n_2` direction
and acts on a point located in the midplane of the bicycle frame. One
rationlization of the force can be imagined if a person were to walk beside a
bicycle and simply push laterally on the rear frame. One can even think of it
as a simplfied version of the resultant force from lateral wind gust. I
utilized this input in the Davis control task experiments in Chapter
:ref:`control`, were we apply a lateral impulsive force to the bicycle/rider
system.

The vector from the rear wheel center to the point is:

.. math::
   :label: lateralForcePoint

   \bar{r}^{C_l/D_o} = d_4\hat{c}_1 + d_5\hat{c}_3

The velocity of the point is can be computed with the following relationship:

.. math::
   :label: ClInN

   ^N\bar{v}^{c_l} = ^N\bar{v}^{d_o} + ^N\bar\omega^C\times\bar{r}^{c_l/d_o}

   ^N\bar\omega^C\times\bar{r}^{c_l/d_o} =
   d_5(u_5+s_4u_3)\hat{c}_1 +
   &(d_4(s_5u_4+c_4c_5u_3)-d_5(c_5u_4-s_5c_4u_3))\hat{c}_2 -
   d_4(u_5+s_4u_3)\hat{c}_3

Finally, there is an additional generalized active force:

.. math::
   :label: lateralForce

   \bar{R}^{C_l} = F_{cl}\hat{n}_2

The linear model is computed in the same fashion as described, with an
additional column in both the input, :math:`\mathbf{B}`, and feedforward,
:math:`\mathbf{D}`, matrices.

.. todo:: Add an impulse response graph? Linear, nonlinear?

Flywheel in the front wheel
===========================

Another interesting model extension involves adding an additional rotating
wheel coicedent with the front wheel. It has been shown theorecially that
increasing the angular momentum of the front wheel via change in inertia
([Astrom2005]_, [Franke1990]_) or speed, has a strong effect on the stability
of the Whipple model. It is interesting to note that for the benchmark bicycle
independently increasing the moment of inertia of the front wheel, decreases
both the weave and capsize speeds. A low weave speed may give open loop
stability benefits to riders at low speed. Conversely, it has also be shown
that both a bicycle without gyroscopic effects can be stable [Kooijman2011]_
and that humans can ride them [Jones1970]_ with little difficulty. The idea
that gyroscopic action can stablize a moving two wheeled vehicle has been
demostrated as early as the dawn of the 20th century, with the invention of the
gyrocar and the gryo monorail. More recently several engineering students at
Dartmouth University applied this theory to a compact flywheel mounted within
the spokes of a childen's bicycle wheel [Ward2006]_. This has since become a
comercially avialable product, the GyroBike, that claims to allow children to
learn to ride quicker, due to the bicycle's increased stabilty at low speeds.

.. todo:: are their any gyro stablized two wheel vehicles earlier than the
   car?

.. todo:: Video I took of the gyrobike on the treadmill.

Using the Whipple model presented in Chapter :ref:`eom` as a base model, the
GyroBike can be modeled by adding an additional symmetric rigid body, :math:`G`
with mass :math:`m_G` to the system which rotates about the front wheel axis
though a new generilzed coordinate, :math:`q9`. The angular velocity and
acceleration of the new body are defined with the simple kinematical
differential equation:

.. math::

   ^F\omega^G = \dot{q}_9 \hat{e}_2 = u_9 \hat{e}_2

.. math::

   ^F\alpha^G = \dot{u}_9 \hat{e}_2

The location of the flywheel center of mass is at the same point as the front
wheel center of mass, thus the linear velocities and accelerations are the same
as the front wheel:

.. math::

   ^N\bar{v}^{go} = ^N\bar{V}^{fo}

.. math::

   ^N\bar{a}^{go} = ^N\bar{a}^{fo}

An additional torque, :math:`T_9`, is required to drive the flywheel relative
to the front wheel.

.. math::

   \bar{T}^F = -T_9\hat{e}_2

   \bar{T}^G = T_9\hat{e}_2

At this point, :math:`\tilde{F}_r`, can be formed with the addtional equation
for the new degree of freedom.

The generilized inertia force, :math:`\tilde{F}^*_r` is formed by taking into
account the mass, :math:`m_G`, and inertia of the new body:

.. math::
   :label: IG

   I_G =
   \begin{bmatrix}
     I_{G11} & 0 & 0\\
     0 & I_{G22} & 0\\
     0 & 0 & I_{G11}
   \end{bmatrix}

The equations of motion are formed and linearized with respect to the nominal
equilibrium point and a nominal angular velocity of the flywheel. The following
figures show how increasing the speed of the flywheel pushes the weave and
capsize critical speeds lower and lower, creating a stable speed range at
speeds in which a person may learn to ride a bicycle.

.. figure:: figures/extensions/gyrobike-flywheel-off.png

   figGyroOff

   The root loci with respect to the rear wheel angular speed when the flywheel
   is fixed to the front wheel (i.e. has the the same angular velocity.

.. figure:: figures/extensions/gyrobike-flywheel-medium.png

   figGyroMedium

   The root loci with respect to the rear wheel angular speed when the flywheel
   is spinning at 50 rad/s with respect to the front wheel.

.. figure:: figures/extensions/gyrobike-flywheel-fast.png

   figGyroFast

   The root loci with respect to the rear wheel angular speed when the flywheel
   is spinning at 100 rad/s with respect to the front wheel.

.. todo:: Clean up these graphs.

.. todo:: Plot these with the actual parameters of the gyrobike. These plots
   are of the benchmark parameters with an additional identical front wheel.

.. todo:: Other possible plots: weave and capsize speeds as a function of flywheel
   speed, 3D plot versus both parameters (u6 and u9), root loci wrt to u9 at a
   single low speed.

Leaning rider extension
=======================

A typical assumption is that a rider can control a bicycle by leaning their
body relative to the bicycle frame. This is especially drawn for the no-hands
riding case. A simple leaning rider can be modeled by adding an additional
rider lean degree of freedom.

Addition of rider arms
======================

Addition holonomic contraints
-----------------------------

Linearization
-------------

Comparison to Arend's model
---------------------------

Roll angle trailer
==================

David de Lorenzo extension (3 rider dof)
========================================


Flexible rider (hip rotation, back lean and twist)
==================================================

