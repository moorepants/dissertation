.. _extensions:

===============================
Extensions of the Whipple Model
===============================

.. warning::

   This document is a draft which is updated regularly (Last updated |today|).
   Once I submit if for my doctoral degree at UC Davis, it will be done. So for
   now use at your own risk. The information may or may not be correct.
   Reviews, comments and suggestions are welcome.

Preface
=======

The Whipple model provides a nice platform of which to add more bodies,
and different constraints and explore their effects on the dynamics of the
system. Some extensions are easier than others, but almost always easier than
the kinematics of the Whipple model itself. I've been curious as to whether
if one already has the equations of motion of a base system, could one develop
a systematic way of adding additional bodies or change constraints without
having to re-derive the entire equations over again. Some numerical methods for
generating equations of motion may lend themselves to this, but its not
apparent if there could be a generalized analytical method.

Introduction
============

It has be shown that the linear Whipple model can reliably predict the motion
of a riderless uncontrolled bicycle [Kooijman2008]_, [Stevens2009]_,
[Escalona2011]_ for speeds between 4 and 6 m/s. But the Whipple model is may
certainly be limited in it's ability to predict the motion of the bicycle and
rider as a system whole. A person's body keeps it shape through passive joint
forces, unconscious active control and conscious active control. Assuming no
active control and lumping the unconscious control with the passive control one
can potentially model the rider as flexible assembly of many bodies. Secondly,
the rider's weight is typically 80 to 90 percent of the entire system,
potentially invalidates the knife edge wheel assumptions employed in the
Whipple model. Here I present several bicycle models that attempt to explain
some of the rider's passive dynamics and also a model with stability
augmentation device. The models are all based on of the basic formulation of
the Whipple model in Chapter :ref:`eom`. Various combinations of these model
extensions are used in the later Chapters for analysis of our more complicated
systems.

Lateral Force Input
===================

.. todo:: Roland1973 laterally perturbs a motorcycle model.

The Whipple model is typically defined with three input forces roll torque
:math:`T_4`, rear wheel torque :math:`T_6` and steer torque :math:`T_7`. Here I
add a fourth input, a lateral force :math:`F_{c_l}`, which acts on a point on
the bicycle frame, :math:`c_l`. The force is defined such that it is always in
the :math:`\hat{n}_2` direction and acts on the point located in the mid-plane
of the bicycle frame. I choose the global :math:`\hat{n}_2` direction instead
of the yaw frame's :math:`\hat{a}_2` direction because it correlated with
the impulsive forces applied in our experiments. One rationalization of the force
can be imagined if a person were to walk beside a bicycle and simply push
laterally on the rear frame. One can even think of it as a simplified version of
the resultant force from lateral wind gust. I utilized this input in the Davis
control task experiments in Chapter :ref:`control`, were we apply a lateral
impulsive force to the bicycle/rider system.

The vector from the rear wheel center to the lateral force point is

.. math::
   :label: eqLateralForcePoint

   \bar{r}^{c_l/d_o} = d_4\hat{c}_1 + d_5\hat{c}_3

The velocity of the point is

.. math::
   :label: eqClInN

   ^N\bar{v}^{c_l} = ^N\bar{v}^{d_o} + ^N\bar\omega^C\times\bar{r}^{c_l/d_o}

   ^N\bar\omega^C\times\bar{r}^{c_l/d_o} =
   d_5(u_5+s_4u_3)\hat{c}_1 +
   &(d_4(s_5u_4+c_4c_5u_3)-d_5(c_5u_4-s_5c_4u_3))\hat{c}_2 -
   d_4(u_5+s_4u_3)\hat{c}_3

To form the equations of motion the additional generalized active force dot
mutliplied with the partial velocities of the point. The force is simply

.. math::
   :label: eqLateralForce

   \bar{R}^{c_l} = F_{c_l}\hat{n}_2

The linear model is computed in the same fashion as described in Chapter
:ref:`eom`, with an additional column in both the input, :math:`\mathbf{B}`,
and feed-forward, :math:`\mathbf{D}`, matrices corresponding to the new input
force. Unlike roll torque this force can contribute to both the roll and steer
states. The location of the point determines the contribution to each state.

Figure :ref:`figLatForceImp` compares the impulse response for roll torque to
the response from a lateral force at the seat for a particular bicycle in
within its stable speed range. Notice that the lateral force input does not
excite the system with as large as amplitudes but that the response is similar.
This only a function of where the force is applied. If the force is applied
directly above the rear wheel contact at a height of unity from the ground,
the response will be identical.

.. _figLatForceImp:

.. figure:: figures/extensions/lat-force-impulse.*
   :align: center
   :width: 4in

   figLatForceImp

   The impulse reponse for the roll angle, :math:`q_4`, and steer angle,
   :math:`q_7`, for a roll torque input (blue) and the lateral force input at a
   point just below the seat (red). The parameter set used was for the Jason on
   the Davis instrumented bicycle and was linearized at a forward speed of7 m/s.

Figure :ref:`figLatForceBode` shows the frequency response in a similar fashion
as the impulse response. The responses for both input types is very similar for
this frequency spectrum, with the difference in magnitudes proportional to the
distance the lateral force is from the rear wheel contact point.

.. _figLatForceBode:

.. figure:: figures/extensions/lat-force-bode.*
   :align: center
   :width: 5in

   figLatForceBode

   The frequency response for the roll angle, :math:`q_4`, and steer angle,
   :math:`q_7`, for a roll torque input (blue) and the lateral force input at a
   point just below the seat (red). The parameter set used was for the Jason on
   the Davis instrumented bicycle and was linearized at a forward speed of 7 m/s.

.. todo::  I don't know how interesting these graphs are. Showing the
   relationship for magnitude of the outputs with respect to the location of the
   lateral force point might be more interesting.

Rider Arms
==========

[Schwab2010]_ has shown that the addition of the inertial effects of the arms
can significantly alter the open loop dynamics of the bicycle. Most importantly
that a typical bicycle and rider may not have a stable speed range. As will be
described in Chapter :ref:`davisbicycle`, we rigidified the rider's torso and
legs with respect to the rear frame of the bicycle. The rider was only able to
make use of their arms to control the bicycle. The Whipple model does not take
into account the dynamic motion of the arms and certainly not the fact that
steer torque forces are actually generated from the muscle contraction/flexion
in the riders arms. Being that our riders were able to move their arms and the
motion can have significant effect on the open loop dynamics, we employ a
similar more complete model as did [Schwab2010]_.

In bicycle models, the front frame is typically externally forced to move with
respect to the rear frame through a torque applied between the rear frame and
the front frame. A more realistic model with arms would force the front frame
motion through joint torques in the arms. For simplicity's sake and without
loss of generality I keep the steer torque, :math:`T_4`, as the driving torque
letting the arms follow letting the arms follow suit. The inertial effects of
the arms can then be captured by adding four additional rigid bodies to the
Whipple model for the left and right upper and lower arm segments and
introducing enough constraints such that the no additional degrees of freedom
are introduced. I assume that the arms are symmetric with respect to the
sagittal plane. The four new bodies are defined as:

- :math:`G`: right upper arm
- :math:`H`: right lower arm
- :math:`I`: left upper arm
- :math:`J`: left lower arm

The right and left upper arms are each oriented through body fixed 1-2-3
rotations through the abduction, elevation and rotation angles :math:`q_9`,
:math:`q_{10}`, :math:`q_{11}` and :math:`q_{13}`, :math:`q_{14}`,
:math:`q_{15}` for the right and left arms respectively.

.. math::
   :label: eqRightShoulder

   ^N\mathbf{R}^G =
   \begin{bmatrix}
   c_{10}c_{11} & -c_{10}s_{11} & s_{10}\\
   s_9s_{10}c_{11} + s_{11}c_9 & -s_9s_{10}s_{11} + c_{11}c_9 & -s_9c{10}\\
   -c_9s_{10}c_{11} + s_{11}s_9 & c_9s_{10}s_{11} + c_{11}s_9 & c_9c_{10}
   \end{bmatrix}

.. math::
   :label: eqLeftShoulder

   ^N\mathbf{R}^I =
   \begin{bmatrix}
   c_{14}c_{15} & -c_{14}s_{15} & s_{14}\\
   s_{13}s_{14}c_{15} + s_{15}c_{13} & -s_{13}s_{14}s_{15} + c_{15}c_{13} & -s_{13}c{14}\\
   -c_{13}s_{14}c_{15} + s_{15}s_{13} & c_{13}s_{14}s_{15} + c_{15}s_{13} & c_{13}c_{14}
   \end{bmatrix}

The right and left lower arms are oriented through simple rotations through
:math:`q_{12}` and :math:`q_{16}` with respect to the upper arms at the elbow
joint.

.. math::
   :label: eqGtoH

   ^G\mathbf{R}^H =
   \begin{bmatrix}
     c_{12} & 0 & -s_{12}\\
     0 & 1 & 0\\
     s_{12} & 0 & c_{12}
   \end{bmatrix}

.. math::
   :label: eqItoJ

   ^I\mathbf{R}^J =
   \begin{bmatrix}
     c_{16} & 0 & -s_{16}\\
     0 & 1 & 0\\
     s_{16} & 0 & c_{16}
   \end{bmatrix}

This definition differs from [Schwab2010]_ and will allow full non-linear
unlocked motion of the arms. Schwab's joint configuration limits the model to
only be valid in around the linear equilibrium point presented therein.

The right and left shoulders are located in the rear frame by

.. math::
   :label: eqShoulders

   \bar{r}^{s_r/d_o} = d_6 \hat{c}_1 + d_7 \hat{c}_2 + d_8 \hat{c}_3

   \bar{r}^{s_l/d_o} = d_6 \hat{c}_1 - d_7 \hat{c}_2 + d_8 \hat{c}_3

The right and left elbows are located by

.. math::
   :label: eqElbows

   \bar{r}^{e_r/s_r} = d_{12} \hat{g}_3

   \bar{r}^{e_l/s_l} = d_{12} \hat{i}_3

The upper and lower arm mass centers are located by

.. math::
   :label: eqArmCoM

   \bar{r}^{g_o/s_r} = l_5 \hat{g}_3

   \bar{r}^{h_o/e_r} = l_6 \hat{i}_3

   \bar{r}^{i_o/s_l} = l_5 \hat{i}_3

   \bar{r}^{j_o/e_l} = l_6 \hat{j}_3

The hands are located by

.. math::

   \bar{r}^{h_r/e_r} = d_{13} \hat{h}_3

   \bar{r}^{h_l/e_l} = d_{13} \hat{j}_3

The handlebar grips are located by

.. math::
   :label: eqGrips

   \bar{r}^{g_r/f_o} = d_9 \hat{e}_1 + d_10 \hat{e}_2 + d_11 \hat{e}_3

   \bar{r}^{g_l/f_o} = d_9 \hat{e}_1 - d_10 \hat{e}_2 + d_11 \hat{e}_3

To enforce that the hands remain on the grips, I first introduce six holonomic
constraints embodied in

.. math::
   :label: eqHandsOnGrips

   \bar{r}^{h_r/s_r} - \bar{r}^{g_r/s_r} = 0

   \bar{r}^{h_l/s_l} - \bar{r}^{g_l/s_l} = 0

After forcing the hands to be at the grips this leaves two degrees of freedom,
one for each arm.  The free motion is such that the arms can rotate about the
lines connecting the shoulders to the grips. I choose to eliminate these two
degrees of freedom by forcing the arms to always "hang down" relative to the rear
frame, i.e. that the vector aligned with the elbow has no component in the
downward direction of the roll frame, :math:`B`.

.. math::
   :label: eqArmsDown

   \hat{g}_2 \cdot \hat{b}_3 = 0

   \hat{i}_2 \cdot \hat{b}_3 = 0

This assumption is limited in validity around small pitch angles, as a large
pitch angles would cause the riders arms to rotate in odd positions. A better
constraint would be to dot with a vector in the :math:`C` frame which is
aligned with the :math:`\hat{b}_3` when the bicycle is not pitched, but due to
our choice of geometric parameters, a new parameter would have to be
introduced, so I choose the former.

With these eight holonomic constraints, the model now has three degrees of
freedom which are the same as the Whipple model, but with the added inertial
effects of the arms. The expressions for the velocities and accelerations of
the mass centers of the four new bodies needed to form the equations of motion
are lengthy and I will spare this section with their mess. Please refer to the
source code for the equations.

The generalized active forces remain the same as described in Chapter
:ref:`eom` with the addition of the lateral force described in the previous
section. The generalized inertia forces must be modified to include the
accelerations of the mass centers along with the mass and inertia of the new
bodies. The masses are simply defined as :math:`m_g`, :math:`m_h`, :math:`m_i`
and :math:`m_j`. The arms segments are assumed to be symmetric about their
associated :math:`2` axes, thus :math:`I_{11} = I_{22}`.

.. todo:: I could reduce the number of parameters due to the symmetry of the
   problem, i.e. m_g = m_h and the left and right inertias are equivalent.
   Right now my code doesn't do that, but I could change it.

.. math::
   :label: eqIUpperArm

   I_G =
   \begin{bmatrix}
   I_{G11} & 0 & 0\\
   0 & I_{G11} & 0\\
   0 & 0 & I_{G33}
   \end{bmatrix}
   =
   I_I =
   \begin{bmatrix}
   I_{I11} & 0 & 0\\
   0 & I_{I11} & 0\\
   0 & 0 & I_{I33}
   \end{bmatrix}

.. math::
   :label: eqILowerArm

   I_H =
   \begin{bmatrix}
   I_{H11} & 0 & 0\\
   0 & I_{H11} & 0\\
   0 & 0 & I_{H33}
   \end{bmatrix}
   =
   I_J =
   \begin{bmatrix}
   I_{J11} & 0 & 0\\
   0 & I_{J11} & 0\\
   0 & 0 & I_{J33}
   \end{bmatrix}

With this information the equations of motion can be formed with Kane's method
as described in Chapter :ref:`eom`. Special care must be taken when linearizing
the equations of motion due to the eight holonomic constraints. The additional
generalized coordinates, :math:`q_9` through :math:`q_{16}`, are all dependent
coordinates and are ultimately functions of the pitch and steer angles. The
chain rule must be properly applied or the independent coordinates must be
solved for when forming the Jacobian.

Figure :ref:`figArmsEig` shows how the eigenvalues vary with speed with respect
to the nominal equilibrium point. Notice that the oscillatory mode spans the
entire speed range and is always stable. Their is a real mode which is stable
at every given speed. Finally, a highly stable real mode is also shown.

.. _figArmsEig:

.. figure:: figures/extensions/arms-eig.png
   :align: center

   figArmsEig

   The root loci with respect to speed of the Whipple model with arms for the
   parameter set associated with Jason seated on the Davis instrumented bicycle
   calculated with the Yeadon method. This plot shares similar characteristics
   as the one presented in [Schwab2010]_.

.. todo:: Eigenvector component plots could help describe the motion.

.. todo:: Compare transfer function from steer torque to roll angle for the
   Whipple model and the arms model.

Flywheel in the front wheel
===========================

Another model extension that perked my interest involves adding an additional
rotating wheel coincident with the front wheel. It has been shown theoretically
that increasing the angular momentum of the front wheel via change in inertia
([Astrom2005]_, [Franke1990]_) or rotational speed, has a strong effect on the
stability of the Whipple model. For the benchmark bicycle [Meijaard2007]_
independently increasing the moment of inertia of the front wheel, decreases
both the weave and capsize speeds. A low weave speed may provide open loop
stability advantages to riders at low speed, with the reasoning that a stable
bicycle may require less rider control. Conversely, it has also be shown that
both a bicycle without gyroscopic effects can be stable [Kooijman2011]_ and
that humans can ride them [Jones1970]_ with little difficulty. The idea that
gyroscopic action can stabilize a moving two wheeled vehicle has been
demonstrated as early as the dawn of the 20th century, with the invention of
the gyro car and the gyro monorail [Wikipedia?]_. Of more recent interest,
several engineering students at Dartmouth University applied this theory to a
compact flywheel mounted within the spokes of a children's bicycle wheel
[Ward2006]_. This has since been developed into a commercially available
product, the GyroBike, that claims to allow children to learn to ride easier,
due to the bicycle's increased stability at low speeds [GyroBike2011]_. I was
given an article about the bicycle from the Dartmouth alumni magazine and
subsequently met the woman who was creating the startup company around the idea
in San Francisco and was able to ride the full scale prototype and eventually
purchased a 16" version. The bicycle alone stays very stable even to extremely
low speeds, but when I as an experienced rider tried ride and control it the
steering felt less responsive than I'd prefer.

.. todo:: are their any gyro stablized two wheel vehicles earlier than the
   car? Find a good citation.

.. todo:: Add citation to the gyrobike website.

.. todo:: Check size of gyrobike wheel.

.. raw:: html

   <p>The following video demonstrates that the gyrobike without a rider is
   stabilized at 2 m/s when the flywheel is at full speed.</p>

   <center>
     <iframe width="420" height="315"
       src="http://www.youtube.com/embed/YmtPNIu4WI0"
       frameborder="0" allowfullscreen>
     </iframe>
   </center>

Using the Whipple model presented in Chapter :ref:`eom` as a base model, the
GyroBike can be modeled by adding an additional symmetric rigid body, :math:`G`
with mass :math:`m_g` to the system which rotates about the front wheel axis
though a new generalized coordinate, :math:`q_9`. The angular velocity and
acceleration of the new body are defined with respect to the simple kinematical
differential equation

.. math::
   :label: eqQ9

   ^F\omega^G = \dot{q}_9 \hat{e}_2 = u_9 \hat{e}_2

where

.. math::
   :label: eqU9

   ^F\alpha^G = \dot{u}_9 \hat{e}_2

The location of the flywheel center of mass is at the same point as the front
wheel center of mass, making the linear velocities and accelerations the
same as the front wheel

.. math::
   :label: eqVGo

   ^N\bar{v}^{go} = ^N\bar{V}^{fo}

.. math::
   :label: eqAGo

   ^N\bar{a}^{go} = ^N\bar{a}^{fo}

An additional torque, :math:`T_9`, is required to drive the flywheel relative
to the front wheel

.. math::
   :label: eqT9

   \bar{T}^F = -T_9\hat{e}_2

   \bar{T}^G = T_9\hat{e}_2

At this point, :math:`\tilde{F}_r`, can be formed with an additional equation
for the new degree of freedom.

The generalized inertia force, :math:`\tilde{F}^*_r` is formed by taking into
account the mass, :math:`m_g`, and inertia of the new body

.. math::
   :label: eqIG

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
   :width: 4in
   :align: center

   figGyroOff

   The root loci with respect to the rear wheel angular speed when the flywheel
   is fixed to the front wheel (i.e. has the the same angular velocity as the
   front wheel).

.. figure:: figures/extensions/gyrobike-vary-flywheel.png
   :width: 4in
   :align: center

   figGyroVary

   The root loci with respect to the flywheel angular velocity when the the
   forward velocity is 0.5 m/s. It shows that the system can certainly be made
   stable by increasing the angular velocity of the flywheel, but it is also
   interesting to note that increasing the velocity too much results in an
   unstable system.

.. figure:: figures/extensions/gyrobike-flywheel-off-rider.png
   :width: 4in
   :align: center

   figGyroOffRider

   The root loci with respect to the rear wheel angular speed when the flywheel
   is fixed to the front wheel (i.e. has the the same angular velocity as the
   front wheel) and a rigid child is seated on the bicycle.

Notice that if a child sized rider is rigidly added to the rear frame that the
flywheel must spin at almost 4000 rpm for the system to be stable and the time
constant of the unstable eigenvalue doesn't decrease decrease much until you at
least have the flywheel spinning at 200 rpm.

.. todo:: It would be interesting to know how fast the gyro wheel does spin. It
   it has three speed settings.

.. figure:: figures/extensions/gyrobike-vary-flywheel-rider.png
   :width: 4in
   :align: center

   figGyroVaryRider

   The root loci with respect to the flywheel angular velocity when the the
   forward velocity is 0.5 m/s when a rigid child is seated on the bicycle. It
   shows that the system can certainly be made stable by increasing the angular
   velocity of the flywheel, but it is also interesting to note that increasing
   the velocity too much results in an unstable system.

.. figure:: figures/extensions/gyro-nonlin-sim.png
   :width: 4in
   :align: center

   figGyroNonLin

   The non-linear simulation of bicycle traveling at 4.6 m/s with the flywheel
   spining at.

.. todo:: Plot the flywheel rate on this plot too.

.. todo:: Other possible plots: weave and capsize speeds as a function of flywheel
   speed, 3D plot versus both parameters (u6 and u9)

Leaning rider extension
=======================

A common assumption regarding how a person controls a bicycle with minimal or
no steer input is that the rider can lean their body relative to the bicycle
frame. This assumption is more often than not drawn for no-hands riding. A
simple leaning rider can be modeled by adding an additional rider lean degree
of freedom, :math:`q_9`, with an accompanying rider lean torque, :math:`T_9`.
[Sharp2008]_, [Schwab2008]_, [Peterson2008a]_, have all modeled this system
explicitly.

.. todo:: talk a bit more about the conclusions in those papers.

I define the upper body hinge as a horizontal line at a distance :math:`d_4`
below the rear wheel center when the bicycle is in the nominal configuration.
The direction cosine matrix relating the upper body to the rear frame is

.. math::
   :label: eqDCMGtoC

   ^C\mathbf{R}^G =
   \begin{bmatrix}
   c_\lambda & 0 & s_\lambda\\
   -s_\lambda s_9 & c_9 & c_\lambda s_9\\
   -s_\lambda c_9 & -s_9 & c_\lambda c_9
   \end{bmatrix}

A point, :math:`c_g`, on the hinge is then defined as

.. math::
   :label: eqLocCg

   \bar{R}^{c_g/d_o} = -d_4s_\lambda\hat{c}_1 + d_4c_\lambda\hat{c}_3

where :math:`\lambda` is the steer axis tilt and is a function of :math:`d_1`,
:math:`d_2`, and :math:`d_3` as described in :ref:`eom`.

The angular velocity and angular acceleration of the upper body in the bicycle
frame is defined as

.. math::
   :label: eqOmegaCinG

   ^C\bar{\omega}^G = u_9 \hat{g}_1

.. math::
   :label: eqAlphaCinG

   ^C\bar{\alpha}^G = \dot{u}_9 \hat{g}_1

with :math:`u_9=\dot{q}_9`. The linear velocities of the hinge point and the
upper body center of mass are

.. math::
   :label: eqVCgInN

   ^N\bar{v}^{c_g} = ^N\bar{v}^{d_o} + ^N\bar\omega^C\times\bar{r}^{c_g/d_o}

   ^N\bar\omega^C\times\bar{r}^{c_g/d_o} =
   &d_4c_\lambda(u_5+s_4u_3)\hat{c}_1 -\\
   &d_4(s_\lambda(s_5u_4+c_4c_5u_3)+c_\lambda(c_5u_4-s_5c_4u_3))\hat{c}_2 +\\
   &d_4s_\lambda(u_5+s_4u_3)\hat{c}_3

.. math::
   :label: eqVGoInN

   ^N\bar{v}^{g_o} = ^N\bar{v}^{c_g} + ^N\bar\omega^G\times\bar{r}^{g_o/c_g}

   ^N\bar\omega^G\times\bar{r}^{g_o/c_g} =
   &-l_6(s_9s_{\lambda-5}u_4-c_9u_5-(s_4c_9+s_9c_4c_{\lambda-5})u_3)\hat{g}_1 +\\
   &(-l_6(u_9+c_{\lambda-5}u_4+c_4s_{\lambda-5}u_3)-l_5(s_9u_5+
   c_9s_{\lambda-5}u_4+(s_4s_9-c_4c_9c_{\lambda-5})u_3))\hat{g}_2 +\\
   &l_5(s_9s_{\lambda-5}u_4-c_9u_5-(s_4c_9+s_9c_4c_{\lambda-5})u_3)\hat{g}_3

The linear accelerations of the hinge point and the upper body center of mass
are as follows

.. math::
   :label: eqACginN

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
   :label: eqAGoinN

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

I introduce two additional torques. The first is the input torque between the
rear frame and the rider's upper body, :math:`T_9`. This can be considered as
the active torque contribution of which the rider's control system would
provide. The second torque is defined as

.. math::
   :label: eqPassiveTorque

   T_9^p = -c_9 * u_9 - k_9 * q_9

where :math:`c_9` and :math:`k_9` are damping and stiffness coefficients which
are introduced as way to characterize the passive torques generated by the
tissue, ligament, tendon and bone structure. A free lean joint is far from
realistic as large active torques would be required to keep the body upright.
These equivalent to simple proportional and derivative negative feedback on the
roll angle and could be defined as such also.

The additional generalized force is

.. math::
   :label: eqGravity

  \bar{R}^{g_o} = m_Gg\hat{n}_3

and the generalized torques modified to include the new torques

.. math::
   :label: eqGenTorques

   \bar{T}^C = T_4\hat{a}_1 - T_6\hat{c}_2 - T_7\hat{c}_3 +
   (k_9q_9+c_9u_9-T_9)\hat{g}_1

   \bar{T}^G = -(k_9q_9+c_9u_9-T_9)\hat{g}_1

The mass of the upper body is :math:`m_g` and it is assumed to by
symmetric about the sagital plane

.. math::
   :label: eqIG

   I_G =
   \begin{bmatrix}
   I_{G11} & 0 & I_{G13}\\
   0 & I_{G22} & 0\\
   I_{G13} & 0 & I_{G33}
   \end{bmatrix}

The equations of motion are formed with Kane's method and linearized as
described in :ref:`eom`. This linear model has been explicitly explored by both
[Schwab2008]_ and [Peterson2008a]_ with parameter values estimated from the by
spliting the values of the benchmark parameter set. The following plot uses
more realistic rider parameters which are generated with methods described in
Chapter :ref:`physicalparameters` and the passive lean torque coefficients are
set to zero. Notice that the largest eigenvalue is much larger than reported in
Schwab and Peterson with a time to double of about a tenth of a second. We
found that root difficult to stabilize when employing a manual control model
based on the one presented in Chapter :ref:`control`, which suggests the need
for some additional passive stabilization.

.. figure:: figures/extensions/rider-lean.png
   :width: 5in
   :align: center

   figRiderLean

   Needs a caption.

The damping stiffness coefficient can be selected to such that the highly
unstable rider mode is stablized and the stable speed range observed in the
Whipple model is restored and thus setting the model up for similar control.
The parameters used are taken from [Lorenzo1996]_, which he estimated,
:math:`k_9=128` N-m/rad and :math:`c_9=50` N-m/rad/s.

.. figure:: figures/extensions/rider-lean-damp-stiff.png
   :width: 5in
   :align: center

   figRiderLeanPassive

   Needs a caption.

.. todo:: These plots were generated with rider parameters based on my original
   method, it wouldn't take much to update the parameters to reflect the yeadon
   method.

David de Lorenzo extension
==========================

Preface
-------

To expand on the ideas presented in the previous section, I'd like to share
some findings from a short conference paper that Luke Peterson and I put
together for the 11th International Symposium on Computer Simulation in
Biomechanics [Moore2007]_. I have included it here almost verbatim but have
updated the writings to tie it into the dissertation and make it less dated. I
also have not updated the derivation of the equations of motion to reflect the
parameters and methodolgy presented in this dissertation, so I will leave those
out but they can be found in the source code. None-the-less the model can be
systematically derived in the same fashion as the previous sections. The
initial interest in this model was an unpublished paper by David de Lorenzo
[Lorenzo1996]_ and Mont Hubbard which explored parameter studies of a model
similar to the one that is presented. I have a inclination to try to get it
published as a heavy review stopped it in its tracks in 1996, but that will
have to wait. Here I pursue the effects that passive springs and dampers at the
biomechanical joints have on the stability of the bicycle, much in the same way
as the previous section but with a more complex rider model.

Introduction
------------

We build on the Whipple model by adding biomechanical degrees of freedom that
capture the dominant rider's motion and the flexible coupling to the rear
frame. The rationale for doing so is that the mass and inertia of a rider is
much larger than that of the bicycle, and the coupling between the rider and
the bicycle is certainly not rigid. Rider modeling has been approached in the
motorcycle literature [Limebeer2006]_ but typically does not address the
smaller vehicle inertial properties and the possible difference in the coupling
constants. For example, when riding a bicycle, it is easy to observe that the
frame yaw and roll motions are differ from the rider yaw and roll motions.
Modeling the rider and frame as a single rigid body ignores this flexible
coupling. In this analysis, we seek to understand the effect of the addition of
these new degrees of freedom on the stable speed range of the bicycle. We
examine the additional modes associated with the new degrees of freedom and how
they impact the weave, capsize, and caster modes seen in the Whipple model.

Methods
-------

Beginning with the Whipple model, the bicycle/rider rigid body is divided into
three separate bodies; the bicycle rear frame, the rider lower body and the
rider upper body. The lower body includes the legs and hips while the upper
body includes the torso, arms, and head. Three additional generalized
coordinates are used to configure the rider rigid bodies with respect to the
frame and to each other. The first two are the lateral rotation of the lower
body about a pivot point at the feet and lateral rotation of the upper body
with respect to the lower body, both about horizontal axes parallel to the
forward axis of the bicycle frame. The lower body is connected to the frame at
the foot pivot by a revolute joint and at the seat by a linear spring and
damper in parallel. The third coordinate is the twist of the upper body
relative to the lower body about a nominally vertical axis. Both upper body
lean and twist motions are resisted by linear torsional springs and dampers,
also in parallel. These rider degrees of freedom are detailed in
:ref:`figLorenzoConfiguration` and are similar to the motorcycle rider model
constructed by Katayama, et al. [Katayama1988]_ with the exception of the rider
twist. The lateral linear spring and damper represents the connection between
the rider’s crotch and the seat [#]_. The spring and damper constants are
influenced by the seat and the properties of the skeletal muscle tissue of
thighs and/or buttocks. The torsional springs and dampers represent the
musculoskeletal stiffness and damping at the hips.

.. _figLorenzoConfiguration:

.. figure:: figures/extensions/lorenzo-configuration.png
   :width: 5 in
   :align: center

   figLorenzoConfiguration

   Pictorial description of (a) the additional rider degrees of freedom and (b)
   the six rigid bodies.

This six rigid body model has eleven generalized coordinates. One generalized
coordinate (frame pitch) is eliminated by the holonomic configuration
constraints requiring that both wheels touch the ground. This leaves ten
generalized speeds, of which four are eliminated due to the nonholonomic
constraints for the purely rolling wheels. The nonlinear equations of motion
were linearized numerically about the nominal upright, constant velocity
configuration using a central differencing method with an optimum perturbation
size. The linear system about the nominal configuration and constant speed is
tenth order in frame roll, steer, lower body lean, upper body lean and upper
body twist.

The physical parameters are adapted from [Meijaard2007]_ with exception of the
rider pivot point locations and the spring and damper constants. The pivot
point locations were measured and the spring and damper constants were taken
from [Lorenzo1996]_ which he estimated. All of the physical parameters were
chosen in such a way that, if the rider degrees of freedom are locked, the
model reduces to the benchmark Whipple model, similar to the later work done by
[Peterson2008a]_ and [Schwab2008]_.

Results and Discussion
----------------------

In order to understand how the eigenvalues impact each state variable of our
system, it is essential to examine the components of each eigenvector
corresponding to each generalized coordinate.  By detailed examination, we are
able to determine how each eigenvalue contributes to each generalized
coordinate, across the range of speeds examined.

Figure :ref:`figLorenzoEig` shows the real parts of the identified eigenvalues
of the flexible rider model. By comparison to the Whipple model, it can be seen
that the modes are greatly affected by the additional rider states. The weave
mode has become unstable for all velocities due and no stable speed range is
present.

.. _figLorenzoEig:

.. figure:: figures/extensions/lorenzo-eig.jpg
   :align: center
   :width: 5in

   figLorenzoEig

   The eigenvalues as a function of forward speed.

.. _figLorenzoComplex:

.. figure:: figures/extensions/lorenzo-plane.png
   :width: 3 in
   :align: center

   figLorenzoComplex

   The root loci with respect to speed.

Examining the eigenvector of the weave mode at different velocities we find
that at low speeds the weave mode is dominated by frame roll and steer, while
at high speeds the weave is dominated by upper body lean and twist. This
phenomenon was also observed by Limebeer and Sharp [Limebeer2006]_.
Furthermore, another unstable oscillatory eigenvalue pair is present at
velocities below about 4 m/s for this parameter set.

.. _figLorenzoEigVec:

.. figure:: figures/extensions/lorenzo-eigvec.png
   :width: 6 in
   :align: center

   figLorenzoEigVec

   The eigenvector components.

As the stiffness and damping coefficients for the rider/frame coupling are
increased (by factors of about :math:`10^3` and :math:`30` respectively), the
eigenvalues begin to match those of the Whipple model, and a stable speed range
reappears. However, the values of stiffness and damping for which a stable
speed range did exist are unrealistically high.

.. figure:: figures/extensions/lorenzo-high.jpg
   :width: 5 in
   :align: center

   figLorenzoHigh

   The eigen fucking values.

Conclusion
----------

The notion that the bicycle-rider system can be stable during hands-free riding
and with no active control from the rider is not necessarily true when the
rider's biomechanics are modeled more realistically. For the particular set of
estimated parameters the weave mode is unstable for the entire range of speeds
investigated when realistic flexible rider dynamics are included. While the
Whipple model provides many insights into the dynamics and control of the
bicycle, it lacks the complexity to capture the essential dynamics that are
present in passive hands-free riding. In particular, it is highly likely that
bicycle rider must always use active control to keep the bicycle upright and
self-stabilization is not guaranteed. Parameters studies that show the
dependence on stability across a range of speeds for ranges of stiffness and
damping at the biomechanical joints can shed more light on the system for more
conclusive results.

Flexible rider (hip rotation, back lean and twist)
==================================================

I've ended up thinking a great deal about the actual biomechanical motion one
uses to balance a bicycle when riding no-handed and I've learned much about it
by talking with colleagues such as Jim P., Jodi and Arend. For the final
studies in this dissertation I had intended to do a thorough study of the
dynamics of balancing with no hands based around the structure of the actual
biomechanics we employ. This no-hand biomechanical model also relates to
what we may do even when we have our hands on the bars, albeit with much
smaller magnitudes as steer is almost always the optimal control input to the
bicycle which gives much more bang for the buck.

It is relatively easy to learn to ride without using your hands and many people
that know how to ride a bicycle can do so. Some can navigate roads and
obstacles very well too. Without being able to directly affect the steering
angle for control purposes, one must somehow affect the roll angle, which in
turn is coupled to steering. Driving the roll angle, drives the steer angle
which points you in the direction you want to go. In the purely mechanical
sense one can imagine that a rider could "lean" relative to the rear frame,
thus inducing the counter reaction causing the frame to roll the opposite
direction you lean. This is often the chosen model [Peterson2008a]_,
[Schwab2008]_,... others, and is most intuitive and simple model but I think
the idea of leaning may in fact be too simplistic to describe what is really
going on in a bicycle [#]_ . The rider's upper body is typically more than
three times the mass of the bicycle and it takes much more force to move in
inertial space than the low mass bicycle. The studies that are presented in
:ref:`delftbicycle` and :ref:`motioncapture` show that the rider's upper body
moves little relative to the rear frame and even inertially with respect to
upper body roll or lean in inertial space, but that the bicycle frame can
quickly roll relative to the inertially "fixed" rider. With that in mind, one can
imagine rolling the bicycle frame underneath your body by using your leg and
butt muscles. It is clearly evident when riding no hands as you feel the seat
moving back and forth under your butt. Another interesting thing to note is
that it is virtually impossible to control a bicycle without your hands and
*your feet* placed on the grips and pedals. Removing your feet from the pedals
takes away the ability to apply forces from the rider's body to the bicycle
frame which can contribute to change in the bicycle roll angle. This leads me to
believe that no hand control is dependent on the rider's ability to roll the
bicycle frame using the lower extremity muscles which are critically dependent
on the leg.

If that is true, then there is a most likely a simple model that can capture
the relative motion of the bicycle rear frame with respect to the lower
extremities and hips. This lead me to examine the data from the motion capture
experiments of a no-hand run with the rider pedaling. I plotted the motion of
tail bone and hip markers in the rear frame reference frame from the
perspective of looking at the rider's butt from behind. This plot was shows
that the butt moves laterally with respect to bike frame a bit, but more
prevalent is the curves that the hips follow. One can then visualize the hips
rotating about a line just below the seat that runs fore to aft.

.. figure:: figures/extensions/hip-trace.png
   :width: 5in
   :align: center

   figHipTrace

   The hip trace from run # 3104.

.. todo:: improve this plot and draw the arc of the hip motion

Gilbert and I worked on exploring this motion and theorizing a harness of some
sort that would both constrain the rider's motion to these key motions and
allows us to measure the forces and the kinematics involved. We created two
videos of the rider. The first video is shot from behind and shows me balancing
no-handed on a treadmill. I taped three sticks to my back: one across the
shoulders, the second to the upper portion of my spine and the third to the
lower portion. The idea was to visualize the dominant motion of the rider with
respect to the bicycle frame and how the spine moved. I chose these sticks
based on the motion capture studies we did. We observed that the spine bend can
probably be described by a single joint in the middle of the spine and that the
butt and hips roll about the seat.

.. raw:: html
   <p>The following video demonstrates that the bicycle frame does roll
   relative to the somewhat inertially fixed rider, that the hips rotate about
   the seat and also that the spine may only need one laterally rotational
   degree of freedom to capture the dominate spine motions.</p>

   <center>
     <iframe width="420" height="315"
       src="http://www.youtube.com/embed/FcAp-DbHp9M"
       frameborder="0" allowfullscreen>
     </iframe>
   </center>

At this point, we constructed a mock-up of a harness that would both measure
these motions and limit the rider to those motions.

.. _figTestRiderHarness:

.. figure:: figures/extensions/test-rider-harness.jpg
   :width: 3in
   :align: center

   figTestRiderHarness

   A mock-up of a harness to measure the dominant motions of the rider, which
   also constrains the rider to some degree to the prescribed  motion.

The model to described this motion would have a revolute joint just below the
seat such that the riders hips can roll about the seat. The legs would be
constrained such that the feet met the foot pegs and the knee angles would be
dependent on the hip angle. Finally, the spine would be stiffened with a back
brace and a single revolute joint for back lean relative to the hips would be
measured. I also considered measuring the rider's torso twist angle relative to
the hips.

.. todo:: Add the Autodesk Inventor drawing of this model, or even an
   animation.

We intended to develop a harness and pair it with a force measuring seat post
and foot pegs which measure the downward force applied by the feet to the
bicycle with the goal to characterize the force interaction between the rider
and the bicycle which causes the bicycle to roll.

.. todo:: mention how changing the roll angle when you off the seat is very
   easy

Conclusions
===========

I've presented several of the extensions to the Whipple model that I've made
use of and talked some about there characteristics. It surely isn't exhaustive
on any but provides some useful conclusions for the coming chapters.

I showed that the lateral force input we used in the control experiments must
be properly accounted for and not simply assumed to be characterized by a roll
torque.

Adding a flywheel to the front wheel of a bicycle can radically change it's
stability regime and can make the model stable as very low speeds, slower than
average walking. But if the inertial effects of the rider are taken into
account, the flywheel may have to spin at very high speeds for any significant
change in dynamics.

The addition of the inertial affects of the arms change the system dynamics
significantly. In particular by eliminating the stable speed range and the
capsize mode becomes very unstable.

Adding various rider degrees of freedom create an unstable system, but passive
forces acting on the new joints can potentially stabilize the new modes. The
rider must use a combination of passive and active control on his body to keep
the bicycle/rider system stable.

Finally, I've shown some ideas of developing a slightly different biomechanical
model of the rider that may be a more realistic way of characterizing the
motion used for non-steer related control of the bicycle.

Notation
========

Each section in this Chapter uses its own notation and I use variable names for
different quantities in each section, except for the arms model section as it
subsumes the lateral force input. Also each model makes use of the parameters
defined in Chapter :ref:`eom` as a base.

:math:`c_l`
   The point at which the lateral force is applied.
:math:`d_4,d_5`
   The distances which locate :math:`c_l`.
:math:`G,J,I,J`
   Rigid bodies.
:math:`d6-d13`
   Geometric distances.
:math:`s_r,e_r,h_r,g_r,s_l,e_l,h_l,g_l`
   Points on the arms.
:math:`c_g`
   Rider hinge point.
:math:`c_9,k_9`
   The passive stiffness and damping coefficients.

.. rubric:: Footnotes

.. [#] We got a kick out of "crotch stiffness" i.e. the stiffness of the
   crotch spring, and tried to encourage Mont to use the terminology when he
   presented this for us in Taiwan.

.. [#] Leaning on a motorcycle makes more sense as the mass of the motorcycle
   is comparable or more than the mass of the riders upper body.
