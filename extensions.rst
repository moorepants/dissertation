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

   \bar{r}^{c_l/d_o} = d_4\hat{c}_1 + d_5\hat{c}_3

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

   \bar{R}^{c_l} = F_{c_l}\hat{n}_2

The linear model is computed in the same fashion as described, with an
additional column in both the input, :math:`\mathbf{B}`, and feedforward,
:math:`\mathbf{D}`, matrices.

.. todo:: Add an impulse response graph? Linear, nonlinear?

Addition of rider arms
======================

It has been shown that the addition of the inertial effects of the arms can
ignificantly alter the open loop dynamics of the bicycle [Schwab2011]_. As
described in Chapter :ref:`davisbicycle`, we rigidified the rider's torso and
legs with respect to the rear frame of the bicycle. The human makes use of his
arms to control the bicycle. The Whipple model does not take into account the
dynamic motion of the arms and certainly not the fact that steer torque forces
are acutally generated from the muscle contraction/flexion in the riders arms.

The steer torque is a function of the joint torques in the arms and for
simplicity, is kept as the driving torque. The inertial effects of the arms can
be captured by adding four additional rigid bodies to the Whipple model for the
left and right upper and lower arm segments and constrainig the bodies to the
the shoulder and handle bar points. The four bodies are defined as:

- :math:`G`: right upper arm
- :math:`H`: right lower arm
- :math:`I`: left upper arm
- :math:`J`: left lower arm

The right and left upper arms are oriented through body fixed 1-2-3 rotations
through the abduction, elevation and rotation angles :math:`q_9`,
:math:`q_{10}`, :math:`q_{11}` and :math:`q_{13}`, :math:`q_{14}`,
:math:`q_{15}` for the right and left arms respectively.

.. math::

   ^N\mathbf{R}^G =
   \begin{bmatrix}
   c_{10}c_{11} & -c_{10}s_{11} & s_{10}\\
   s_9s_{10}c_{11} + s_{11}c_9 & -s_9s_{10}s_{11} + c_{11}c_9 & -s_9c{10}\\
   -c_9s_{10}c_{11} + s_{11}s_9 & c_9s_{10}s_{11} + c_{11}s_9 & c_9c_{10}
   \end{bmatrix}

.. math::

   ^N\mathbf{R}^I =
   \begin{bmatrix}
   c_{14}c_{15} & -c_{14}s_{15} & s_{14}\\
   s_{13}s_{14}c_{15} + s_{15}c_{13} & -s_{13}s_{14}s_{15} + c_{15}c_{13} & -s_{13}c{14}\\
   -c_{13}s_{14}c_{15} + s_{15}s_{13} & c_{13}s_{14}s_{15} + c_{15}s_{13} & c_{13}c_{14}
   \end{bmatrix}

The right and left lower arms are oriented through simple rotations through
:math:`q_{12}` and :math:`q_{16}` with respect to the upper arms.

.. math::
   :label: CtoD

   ^G\mathbf{R}^H =
   \begin{bmatrix}
     c_{12} & 0 & -s_{12}\\
     0 & 1 & 0\\
     s_{12} & 0 & c_{12}
   \end{bmatrix}

.. math::
   :label: CtoD

   ^I\mathbf{R}^J =
   \begin{bmatrix}
     c_{16} & 0 & -s_{16}\\
     0 & 1 & 0\\
     s_{16} & 0 & c_{16}
   \end{bmatrix}

This definition differs from [Schwab2011]_ and will acutally allow full
non-linear unlocked motion of the arms. Schwab's model is only valid in around
the linear equilibrium point presented.

The right and left shoulders are located by:

.. math::

   \bar{r}^{s_r/d_o} = d_4 \hat{c}_1 + d_5 \hat{c}_2 + d_6 \hat{c}_3

   \bar{r}^{s_l/d_o} = d_4 \hat{c}_1 - d_5 \hat{c}_2 + d_6 \hat{c}_3

The right and left elbows are located by:

.. math::

   \bar{r}^{e_r/d_o} = d_{10} \hat{g}_3

   \bar{r}^{e_l/d_o} = d_{12} \hat{i}_3

The upper and lower arm mass centers are located by:

.. math::

   \bar{r}^{g_o/s_r} = l_5 \hat{g}_3

   \bar{r}^{h_o/e_r} = l_6 \hat{i}_3

   \bar{r}^{i_o/s_l} = l_7 \hat{g}_3

   \bar{r}^{j_o/e_l} = l_8 \hat{i}_3

The hands must then be constrained to connect to the handlebars. The handlebar
grip locations are:

.. math::

   \bar{r}^{g_r/f_o} = d_7 \hat{e}_1 + d_8 \hat{e}_2 + d_9 \hat{e}_3

   \bar{r}^{g_l/f_o} = d_7 \hat{e}_1 - d_8 \hat{e}_2 + d_9 \hat{e}_3

The hands are located by:

.. math::

   \bar{r}^{h_r/e_r} = d_{11} \hat{h}_3

   \bar{r}^{h_l/e_l} = d_{13} \hat{j}_3

To enforce that the hands remain on the grips, I entroduce six holonomic
constraints embodied in the following two vector eqations:

.. math::

   \bar{r}^{e_r/s_r} + \bar{r}^{h_r/e_r} = \bar{r}^{g_r/s_r}

   \bar{r}^{e_l/s_l} + \bar{r}^{h_l/e_l} = \bar{r}^{g_l/s_l}

This leaves a two degrees of freedom such that the arms can rotate about the
line from the shoulder to the grips. I choose to eliminate these two degrees of
freedom by forcing the arms to always hang down relative to the rear frame,
i.e. that the vector aligned with the elbow has no component in the downward
direction of the roll frame, :math:`B`.

.. math::

   \hat{g}_2 \cdot \hat{b}_3 = 0

   \hat{i}_2 \cdot \hat{b}_3 = 0

With these eight holonomic constraints, the model is now back to the three
degrees of freedom in of the Whipple model, but with the added inertial effects
of the arms. The expressions for the velocities and accelerations of the mass
centers of the four new bodies are lengthy and I will spare this section with
their mess. Please refer to the source code for the equations.

The generalized active forces remain the same as described in Chapter
:ref:`eom`, but the generalized ineritia forces must be modified to include the
accelerations of the of the mass centers and the mass and inertia of the new
bodies. The masses are simply defined as :math:`m_g`, :math:`m_h`, :math:`m_i`
and :math:`m_j`. The arms segments are assumed to be symmetric about their
assciated :math:`2` axes, thus :math:`I_{11} = I_{22}`.

.. math::
   :label: IG

   I_G =
   \begin{bmatrix}
   I_{G11} & 0 & 0\\
   0 & I_{G11} & 0\\
   0 & 0 & I_{G33}
   \end{bmatrix}

.. math::
   :label: IH

   I_H =
   \begin{bmatrix}
   I_{H11} & 0 & 0\\
   0 & I_{H11} & 0\\
   0 & 0 & I_{H33}
   \end{bmatrix}

.. math::
   :label: II

   I_I =
   \begin{bmatrix}
   I_{I11} & 0 & 0\\
   0 & I_{I11} & 0\\
   0 & 0 & I_{I33}
   \end{bmatrix}

.. math::
   :label: IJ

   I_J =
   \begin{bmatrix}
   I_{J11} & 0 & 0\\
   0 & I_{J11} & 0\\
   0 & 0 & I_{J33}
   \end{bmatrix}

With this information the equations of motion can be formed with Kane's method
as described in Chapter :ref:`eom`. Special care must be taken when linearizing
the equations of motion due to the eight holonomic constraints. The addtional
generalized cooridnates, :math:`q_9` through :math:`q_{16}`, are all dependent
coordinates and are ultimately functions of the steer angle, :math:`q_7`, and
the chain rule must be applied when forming the Jacobian of the equations of
motion as they are functions of all of the non-ignorable coordinates.

.. todo:: Show some graphs. I need to get the numerical linearization working
   for this model so that I can plot the eigenvalues plot. I assume it will
   look similar to Arend's.

Roll angle trailer
==================

.. todo:: I think I will cut this as I've only built an independent kinematic
   model for this and we have been neglecting it in the system identification
   analysis. I will talk about its design in the davis bicycle chapter.

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

.. figure:: figures/extensions/gyrobike-vary-flywheel.png

   figGyroFast

   The root loci with respect to the flywheel angular velocity when the the
   forward velocity is 0.5 m/s. It shows that the system can certainly be made
   stable by increasing the angular velocity of the flywheel, but it is also
   interesting to note that increasing the velocity too much results in an
   unstable system.

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

.. figure:: figures/extensions/rider-lean-damp-stiff.png

David de Lorenzo extension (3 rider dof)
========================================

.. todo:: Just paste in some of the work done in Moore2007

Flexible rider (hip rotation, back lean and twist)
==================================================

.. todo:: Talk a bit about this model and show the video we made of the no hand
   riding on the treadmill. Also show the graph of the hip markers relative to the
   seat.
