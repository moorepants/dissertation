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

Addition of rider arms
======================

It has been shown that the addition of the inertial effects of the arms can
potentially alter the open loop dynamics of the bicycle significantly
[Schwab2011]_. As described in Chapter :ref:`davisbicycle`, we rigidified the
rider's torso and legs with respect to the rear frame of the bicycle. The human
makes use of his arms to control the bicycle. The Whipple model does not take
into account the dynamic motion of the arms and certainly not the fact that
steer torque forces are acutally generated from the muscle contraction/flexion
in the riders arms.

Roll angle trailer
==================

.. todo:: I think I will cut this as I haven't built the complete model for
   this yet and we have been neglecting it in the system identification
   analysis.  I will talk about its design in the davis bicycle chapter.

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

A common assumption regarding how a person controls a bicycle with minimal or
no steer input is that the rider can lean their body relative to the bicycle
frame. This assumption is especially drawn for the no-hands riding case. A
simple leaning rider can be modeled by adding an additional rider lean degree
of freedom, :math:`q_9`, with an accompanying rider lean torque, :math:`T_9`.
[Sharp2008]_, [Schwab2008]_, [Peterson2008a]_, have all modeled this system
explicitly.

I define the upper body hinge as a horizontal line at a distance :math:`d_4`
below the rear wheel center when the bicycle is in the nominal configuration.
The direction cosine matrix relating the upper body to the rear frame is:

.. math::
   :label: EtoF

   ^C\mathbf{R}^G =
   \begin{bmatrix}
   c_\lambda & 0 & s_\lambda\\
   -s_\lambda s_9 & c_9 & c_\lambda s_9\\
   -s_\lambda c_9 & -s_9 & c_\lambda c_9
   \end{bmatrix}

A point on the hinge is then defined as

.. math::

   \bar{R}^{cg/do} = -d_4s_\lambda\hat{c}_1 + d_4c_\lambda\hat{c}_3

where :math:`\lambda` is the steer axis tilt and is a function of :math:`d_1`,
:math:`d_2`, and :math:`d_3` as described in :ref:`eom`.

The angular velocity and angular acceleration of the upper body in the bicycle
frame is defined as

.. math::

   ^C\bar{\omega}^G = u_9 \hat{g}_1

.. math::

   ^C\bar{\alpha}^G = \dot{u}_9 \hat{g}_1

with :math:`u_9=\dot{q}_9`. The linear velocities and accelerations of the
hinge point and the upper body center of mass are as follows:

.. math::
   :label: CgInN

   ^N\bar{v}^{c_g} = ^N\bar{v}^{d_o} + ^N\bar\omega^C\times\bar{r}^{c_g/d_o}

   ^N\bar\omega^C\times\bar{r}^{c_g/d_o} =
   &d_4c_\lambda(u_5+s_4u_3)\hat{c}_1 -\\
   &d_4(s_\lambda(s_5u_4+c_4c_5u_3)+c_\lambda(c_5u_4-s_5c_4u_3))\hat{c}_2 +\\
   &d_4s_\lambda(u_5+s_4u_3)\hat{c}_3

.. math::
   :label: GoInN

   ^N\bar{v}^{g_o} = ^N\bar{v}^{c_g} + ^N\bar\omega^G\times\bar{r}^{g_o/c_g}

   ^N\bar\omega^G\times\bar{r}^{g_o/c_g} =
   &-l_6(s_9s_{\lambda-5}u_4-c_9u_5-(s_4c_9+s_9c_4c_{\lambda-5})u_3)\hat{g}_1 +\\
   &(-l_6(u_9+c_{\lambda-5}u_4+c_4s_{\lambda-5}u_3)-l_5(s_9u_5+
   c_9s_{\lambda-5}u_4+(s_4s_9-c_4c_9c_{\lambda-5})u_3))\hat{g}_2 +\\
   &l_5(s_9s_{\lambda-5}u_4-c_9u_5-(s_4c_9+s_9c_4c_{\lambda-5})u_3)\hat{g}_3

.. math::
   :label: aCginN

   ^N\bar{a}^{c_g} = ^N\bar{a}^{d_o} +
   ^N\omega^C\times(^N\omega^C\times\bar{r}^{c_g/d_o}) +
   ^N\bar{\alpha}^C\times\bar{r}^{c_g/d_o}

   ^N\omega^C\times(^N\omega^C\times\bar{r}^{c_g/d_o}) =
   &d_4(s_\lambda(u_5+s_4u_3)^2+(s_5u_4+c_4c_5u_3)(s_\lambda(s_5u_4+
   c_4c_5u_3)+c_\lambda(c_5u_4-s_5c_4u_3)))\hat{c}_1 +\\
   &d_4(u_5+s_4u_3)(c_\lambda(s_5u_4+c_4c_5u_3)-s_\lambda(c_5u_4-
   s_5c_4u_3))\hat{c}_2 -\\
   &d_4(c_\lambda(u_5+s_4u_3)^2+(c_5u_4-s_5c_4u_3)(s_\lambda(s_5u_4+
   c_4c_5u_3)+c_\lambda(c_5u_4-s_5c_4u_3)))\hat{c}_3

   ^N\bar{\alpha}^C\times\bar{r}^{c_g/d_o} =
   &d_4c_\lambda(c_4u_3u_4+\dot{u}_5+s_4\dot{u}_3)\hat{c}_1 +\\
   &d_4(s_\lambda(s_4c_5u_3u_4+s_5c_4u_3u_5-c_5u_4u_5-s_5\dot{u}_4-
   c_4c_5\dot{u}_3)-\\
   &c_\lambda(s_4s_5u_3u_4+c_5\dot{u}_4-s_5u_4u_5-
   c_4c_5u_3u_5-s_5c_4\dot{u}_3))\hat{c}_2 +\\
   &d_4s_\lambda(c_4u_3u_4+\dot{u}_5+s_4\dot{u}_3)\hat{c}_3

.. math::
   :label: aGoinN

   ^N\bar{a}^{g_o} = ^N\bar{a}^{c_g} +
   ^N\omega^G\times(^N\omega^G\times\bar{r}^{g_o/c_g}) +
   ^N\bar{\alpha}^G\times\bar{r}^{g_o/c_g}

   ^N\omega^G\times(^N\omega^G\times\bar{r}^{g_o/c_g}) =
   &(-l_5(s_9s_{\lambda-5}u_4-c_9u_5-(s_4c_9+s_9c_4c_{\lambda-5})u_3)^2-
   (s_9u_5+c_9s_{\lambda-5}u_4+(s_4s_9-\\
   &c_4c_9c_{\lambda-5})u_3)(l_6(u_9+
   c_{\lambda-5}u_4+c_4s_{\lambda-5}u_3)+l_5(s_9u_5+c_9s_{\lambda-5}u_4+
   (s_4s_9-c_4c_9c_{\lambda-5})u_3)))\hat{g}_1 -\\
   &(s_9s_{\lambda-5}u_4-c_9u_5-(s_4c_9+s_9c_4c_{\lambda-5})u_3)(l_5(u_9+
   c_{\lambda-5}u_4+c_4s_{\lambda-5}u_3)-l_6(s_9u_5+c_9s_{\lambda-5}u_4+\\
   &(s_4s_9-c_4c_9c_{\lambda-5})u_3))\hat{g}_2+\\
   &(-l_6(s_9s_{\lambda-5}u_4-c_9u_5-(s_4c_9+s_9c_4c_{\lambda-5})u_3)^2-
   (u_9+c_{\lambda-5}u_4+c_4s_{\lambda-5}u_3)(l_6(u_9+c_{\lambda-5}u_4+\\
   &c_4s_{\lambda-5}u_3)+l_5(s_9u_5+c_9s_{\lambda-5}u_4+(s_4s_9-
   c_4c_9c_{\lambda-5})u_3)))\hat{g}_3

   ^N\bar{\alpha}^G\times\bar{r}^{g_o/c_g} =
   &-l_6(s_9u_5u_9+c_9s_{\lambda-5}u_4u_9+u_3(s_4s_9u_9+s_4s_9c_{\lambda-5}u_4-
   c_4c_9u_4-s_9c_4s_{\lambda-5}u_5-c_4c_9c_{\lambda-5}u_9)+\\
   &s_9s_{\lambda-5}\dot{u}_4-s_9c_{\lambda-5}u_4u_5-c_9\dot{u}_5-
   (s_4c_9+s_9c_4c_{\lambda-5})\dot{u}_3)\hat{g}_1 +\\
   &(l_6(s_4s_{\lambda-5}u_3u_4+c_4c_{\lambda-5}u_3u_5-s_{\lambda-5}u_4u_5-
   \dot{u}_9-c_{\lambda-5}\dot{u}_4-c_4s_{\lambda-5}\dot{u}_3)+
   l_5(s_9s_{\lambda-5}u_4u_9+c_9c_{\lambda-5}u_4u_5-\\
   &c_9u_5u_9-u_3(s_4c_9u_9+s_9c_4u_4+s_4c_9c_{\lambda-5}u_4+
   s_9c_4c_{\lambda-5}u_9-c_4c_9s_{\lambda-5}u_5)-
   s_9\dot{u}_5-c_9s_{\lambda-5}\dot{u}_4-
   (s_4s_9-c_4c_9c_{\lambda-5})\dot{u}_3))\hat{g}_2 +\\
   &l_5(s_9u_5u_9+c_9s_{\lambda-5}u_4u_9+u_3(s_4s_9u_9+s_4s_9c_{\lambda-5}u_4-
   c_4c_9u_4-s_9c_4s_{\lambda-5}u_5-c_4c_9c_{\lambda-5}u_9)+
   s_9s_{\lambda-5}\dot{u}_4-\\
   &s_9c_{\lambda-5}u_4u_5-c_9\dot{u}_5-(s_4c_9+
   s_9c_4c_{\lambda-5})\dot{u}_3)\hat{g}_3

.. todo:: I'm not sure how useful it is to print out these long equations.
   Maybe I shouldn't do it and refer to the code.

I introduce two additional forces. The first is the input torque between the
rear frame and the rider's upper body, :math:`T_9`. This is considered the
active torque of which the rider's control system would provide. The second
torque is defined as

.. math:: T_9^p = -c_9 * u_9 - k_9 * q_9

where :math:`c_9` and :math:`k_9` are damping and stiffness coeficients which
are a way to characterize the passive torque which keeps our back upright. It
is not realistic that the lean joint is a free joint and active control is
always required to keep our body upright. A human torso has some inherent
stiffness.

The additional generalized force is:

.. math::

  \bar{R}^{g_o} = m_Gg\hat{n}_3

and the generalized torques are also modified:


.. math::

   \bar{T}^C = T_4\hat{a}_1 - T_6\hat{c}_2 - T_7\hat{c}_3 + (k_9q_9+c_9u_9-T_9)\hat{g}_1

   \bar{T}^G = -(k_9q_9+c_9u_9-T_9)\hat{g}_1

The mass of the upper body is :math:`m_g` and the upper body is assumed to by
symmetric about the sagital plane:

.. math::
   :label: IG

   I_G =
   \begin{bmatrix}
   I_{G11} & 0 & I_{G13}\\
   0 & I_{G22} & 0\\
   I_{G13} & 0 & I_{G33}
   \end{bmatrix}

The equations of motion are formed and linearized as described in :ref:`eom`.
This model has been explicitly explored by both [Schwab2008]_ and
[Peterson2008a]_ with parameter values estimated from the Benchmark parameter
set, which is not necessarily that realisitic. The following plot uses more
realistic rider parameters which are generated it following chapter
:ref:`physicalparameters` and the passive lean torque set to zero. Notice that
the largest eigenvalue is much larger than the ones reported in Schwab and
Peterson with a time to double of about a tenth of a second.

.. figure:: figures/extensions/rider-lean.png

The damping stiffness coefficient can be selected to such that the highly
unstable rider mode is only marginally stable, thus making it easier to
control.

David de Lorenzo extension (3 rider dof)
========================================

.. todo:: Just paste in some of the work done in Moore2007

Flexible rider (hip rotation, back lean and twist)
==================================================

.. todo:: Talk a bit about this model and show the video we made of the no hand
   riding on the treadmill. Also show the graph of the hip markers relative to the
   seat.
