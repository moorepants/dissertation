.. _extensions:

===============================
Extensions of the Whipple Model
===============================

Preface
=======

After I had derived the Whipple model, it was natural to start thinking about
extending it to understand various other phenomena. It turned out that one of
Mont's former students, David de Lorenzo, had worked on adding rider
biomechanical degrees of freedom to the Whipple model in the early 90's,
submitted the work to Vehicle System Dynamics but never resubmitted after the
first round of reviews, and the work was still sitting dormant in Mont's files.
Luke and I had just finished our preliminary exams and decided to try to write
a paper for the 2007 International Symposium on Computer Simulation in
Biomechanics. de Lorenzo's work inspired us to explore a model with more
realistic rider motion, which we based on this dormant model. This was the
first of several model extensions I developed for various reasons over the
years. Others included variations on the rider biomechanics and models of
unusual bicycle products such as the Swing Bike and Gyro Bike. This chapter
details the findings from some of the models.

Introduction
============

The Whipple model is an ideal basic model and platform from which to explore
more realistic models of both the bicycle and the rider. It has been
demonstrated that the linear Whipple model can reliably predict the motion of a
riderless uncontrolled bicycle :cite:`Kooijman2006`, :cite:`Kooijman2008`,
:cite:`Kooijman2009`, :cite:`Stevens2009`, :cite:`Escalona2011` for speeds in
and around the stable speed range. But the Whipple model may certainly be
limited in it's ability to predict the motion of the bicycle and rider as an
integrated system. A person's body keeps its shape through passive joint
forces, unconscious active control and conscious active control. Assuming no
active control and lumping the unconscious control with the passive control one
can potentially model the rider as flexible assembly of many bodies. Secondly,
the rider's weight is typically 80 to 90 percent of the entire system, which
potentially invalidates the knife edge wheel assumptions employed in the
Whipple model. Here I present several bicycle models that attempt to explain
some of the rider's passive dynamics and also a model with a passive stability
augmentation device. The models are all based on the basic formulation of the
Whipple model in Chapter :ref:`eom` and make use of the variables defined
therein. Various combinations of these model extensions are used in the later
Chapters for analysis of more complicated systems.

Notation
========

Each model presented in this chapter makes use of the notation defined in
Chapter :ref:`eom` otherwise each model in each section is treated
independently and may use the same notation of the other models.

Lateral Force Input
===================

The Whipple model is typically defined with three inputs: roll torque
:math:`T_4`, rear wheel torque :math:`T_6`, and steer torque :math:`T_7`. These
ideal inputs are not necessarily easy to map to the actual inputs to the
system. In particular, it is generally not possible to execute a pure roll
torque, but a lateral force from the environment is much easier. This type of
input has long been used and modeled, e.g. :cite:`Roland1973b` uses a lateral
perturbation in modeling and experimentation of a motorcycle.

Here I add a fourth input, a lateral force :math:`F_{c_l}`, which acts at a
point on the rear frame, :math:`c_l`. The force is defined such that it is
always in the :math:`\hat{n}_2` direction and acts on the point located in the
mid-plane of the bicycle frame. The :math:`\hat{n}_2` direction is chosen
instead of the yaw frame's :math:`\hat{a}_2` direction because it better models
the impulsive forces applied in the experiments detailed in Chapter
:ref:`systemidentification`. The force can describe a person walking beside a
bicycle and simply pushing laterally on the rear frame. One can even think of
it as a simplified version of the resultant force from lateral wind gust,
although a gust would also apply a force to the front frame.

The vector from the rear wheel center to the lateral force point is

.. math::
   :label: eqLateralForcePoint

   \bar{r}^{c_l/d_o} = d_4\hat{c}_1 + d_5\hat{c}_3

The velocity of the point is

.. math::
   :label: eqClInN

   ^N\bar{v}^{c_l} = {}^N\bar{v}^{d_o} + {}^N\bar\omega^C\times\bar{r}^{c_l/d_o}

where

.. math::

   ^N\bar\omega^C\times\bar{r}^{c_l/d_o} =
   d_5(u_5+s_4u_3)\hat{c}_1 +
   &(d_4(s_5u_4+c_4c_5u_3)-d_5(c_5u_4-s_5c_4u_3))\hat{c}_2 -
   d_4(u_5+s_4u_3)\hat{c}_3

To form the equations of motion, an additional generalized active force dot
multiplied with the partial velocities of the point is required. The
generalized active force is simply

.. math::
   :label: eqLateralForce

   \bar{R}^{c_l} = F_{c_l}\hat{n}_2

The non-linear and linear models are computed in the same fashion as described
in Chapter :ref:`eom`, with an additional column in both the input,
:math:`\mathbf{B}`, and feed-forward, :math:`\mathbf{D}`, matrices
corresponding to the new input force. Unlike a pure roll torque this force can
effectively contribute to both the roll and steer torques. The location of the
point determines the contribution.

:ref:`Figure 4.1<figLatForceImp>` compares the impulse response for roll torque
to that of a lateral force at the seat for a particular bicycle
within its stable speed range. Notice that the lateral force input does not
excite the system with as large amplitudes but that the response is similar.
The amplitude is a function of where the force is applied. If the force is
applied directly above the rear wheel contact at a height of unity from the
ground, the response will be identical.

.. _figLatForceImp:

.. figure:: figures/extensions/lat-force-impulse.*
   :align: center
   :width: 4in
   :target: _images/lat-force-impulse.png

   Impulse responses for the roll angle, :math:`q_4`, and steer angle,
   :math:`q_7`, for a roll torque input (blue) and the lateral force input at a
   point just below the seat (red). The numerical parameters were generated
   from the data of Jason on the Davis instrumented bicycle and the equations
   were linearized at a forward speed of 7 m/s. Plot generated by
   `src/extensions/lateral/lateral_force.m``.

:ref:`Figure 4.2<figLatForceBode>` shows the frequency response in a similar
fashion as the impulse response. The responses for both input types are very
similar for this frequency range, with the difference in magnitudes a function
of the distance the lateral force is from the rear wheel contact point.

.. _figLatForceBode:

.. figure:: figures/extensions/lat-force-bode.*
   :align: center
   :width: 5in
   :target: _images/lat-force-bode.png

   Frequency responses for the roll angle, :math:`q_4`, and steer angle,
   :math:`q_7`, for a roll torque input (blue) and the lateral force input at a
   point just below the seat (red). The numerical parameters were generated
   from the data of Jason on the Davis instrumented bicycle and the equations
   were linearized at a forward speed of 7 m/s. Plot generated by
   ``src/extensions/lateral/lateral_force.m``.

This model is used extensively in the later chapters for modeling and
simulation of lateral perturbation experiments.

Notation
--------

:math:`c_l`
   The point at which the lateral force is applied.
:math:`d_4,d_5`
   The distances which locate the lateral force point :math:`c_l`.
:math:`F_{cl}`
   The magnitude of the lateral force.

.. _secRiderArms:

Rider Arms
==========

:cite:`Schwab2010` and :cite:`Schwab2012` has shown that the addition of the
inertial effects of the arms can significantly alter the open loop dynamics of
the bicycle-rider system, and most importantly, that a typical bicycle and
rider may not have a stable speed range. As will be described in Chapter
:ref:`davisbicycle`, we rigidified the rider's torso and legs with respect to
the rear frame of the bicycle. The rider was then only able to make use of
their arms to control the bicycle. The Whipple model does not take into account
the dynamic motion of the arms and certainly not the fact that steer torques
are actually generated from the muscle contraction and flexion in the riders
arms. Being that our riders were able to move their arms and the motion can
have significant effect on the open loop dynamics, we developed a similar model
as the upright flexed arm model found in :cite:`Schwab2010` and
:cite:`Schwab2012`.

.. _figArmModel:

.. figure:: figures/extensions/arm-model-diagram.*
   :align: center
   :width: 3.56in
   :target: _images/arm-model-diagram.png

   Diagram of the additional arm bodies. Only the upper portion of the system
   is shown. The rider's torso, neck, and head are assumed to be part of the
   rear frame rigid body, :math:`C`.

In most bicycle models, the front frame is externally forced to move with
respect to the rear frame through a torque applied between the rear frame and
the front frame. A more realistic model with arms would force the front frame
motion through joint torques in the arms. For simplicity's sake and without
loss of generality we keep the steer torque, :math:`T_4`, as the driving torque
but retain the associated motion of the arms. The inertial effects of the arms
can then be captured by adding four additional rigid bodies to the Whipple
model for the left and right upper and lower arm segments and introducing
enough constraints such that the additional degrees of freedom are removed
:ref:`Figure 4.3<figArmModel>`. The arms are assumed to symmetric with respect
to the sagittal plane when in the nominal configuration. The four new bodies
are defined as:

:math:`G`:
   right upper arm
:math:`H`:
   right lower arm
:math:`I`:
   left upper arm
:math:`J`:
   left lower arm

The right and left upper arms are each oriented through body fixed 1-2-3
rotations through the abduction, elevation and rotation angles :math:`q_9`,
:math:`q_{10}`, :math:`q_{11}` and :math:`q_{13}`, :math:`q_{14}`,
:math:`q_{15}` for the right and left arms respectively.

.. math::
   :label: eqRightShoulder

   ^C\mathbf{R}^G =
   \begin{bmatrix}
   c_{10}c_{11} & -c_{10}s_{11} & s_{10}\\
   s_9s_{10}c_{11} + s_{11}c_9 & -s_9s_{10}s_{11} + c_{11}c_9 & -s_9c_{10}\\
   -c_9s_{10}c_{11} + s_{11}s_9 & c_9s_{10}s_{11} + c_{11}s_9 & c_9c_{10}
   \end{bmatrix}

.. math::
   :label: eqLeftShoulder

   ^C\mathbf{R}^I =
   \begin{bmatrix}
   c_{14}c_{15} & -c_{14}s_{15} & s_{14}\\
   s_{13}s_{14}c_{15} + s_{15}c_{13} & -s_{13}s_{14}s_{15} + c_{15}c_{13} & -s_{13}c_{14}\\
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

This definition differs from :cite:`Schwab2010` and will allow full non-linear
unlocked motion of the arms. Schwab's joint configuration limits the model to
be valid only in and around the linear equilibrium point presented therein.

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

   \bar{r}^{g_r/f_o} = d_9 \hat{e}_1 + d_{10} \hat{e}_2 + d_{11} \hat{e}_3

   \bar{r}^{g_l/f_o} = d_9 \hat{e}_1 - d_{10} \hat{e}_2 + d_{11} \hat{e}_3

To enforce that the hands remain on the grips, I first introduce six holonomic
constraints embodied in

.. math::
   :label: eqHandsOnGrips

   \bar{r}^{h_r/s_r} - \bar{r}^{g_r/s_r} = 0

   \bar{r}^{h_l/s_l} - \bar{r}^{g_l/s_l} = 0

After forcing the hands to be at the grips this leaves two degrees of freedom,
one for each arm. The free motion is such that the arms can rotate about the
lines connecting the shoulders to the grips. I choose to eliminate these two
degrees of freedom by forcing the arms to always "hang down" relative to the rear
frame, i.e. that the vector aligned with the elbow has no component in the
downward direction of the roll frame, :math:`B`.

.. math::
   :label: eqArmsDown

   \hat{g}_2 \cdot \hat{b}_3 = 0

   \hat{i}_2 \cdot \hat{b}_3 = 0

This assumption is limited in validity to small pitch angles, as a large pitch
angles would cause the riders arms to rotate in odd positions. A better
constraint would be to dot with a vector in the :math:`C` frame which is
aligned with :math:`\hat{b}_3` when the bicycle is not pitched, but this
definition would require a new geometric parameter so I chose the former, i.e.
Equation :eq:`eqArmsDown`.

With these eight holonomic constraints, the model now has three degrees of
freedom which are the same number as the Whipple model, but with the added
inertial effects of the arms. The expressions for the velocities and
accelerations of the mass centers of the four new bodies needed to form the
equations of motion are lengthy and they are omitted here. Please refer to the
source code for the equations: ``src/extensions/arms/Arms.al``.

The generalized active forces remain the same as described in Chapter
:ref:`eom` with the addition of the lateral force described in the previous
section. The generalized inertia forces must be modified to include the
accelerations of the mass centers along with the mass and inertia of the new
bodies. The masses are simply defined as :math:`m_g`, :math:`m_h`, :math:`m_i`
and :math:`m_j`. The arms segments are assumed to be symmetric about their
associated :math:`3` axes, thus :math:`I_{11} = I_{22}`.

.. math::
   :label: eqIUpperArm

   \mathbf{I}_G =
   \begin{bmatrix}
     I_{G11} & 0 & 0\\
     0 & I_{G11} & 0\\
     0 & 0 & I_{G33}
   \end{bmatrix}
   =
   \mathbf{I}_I =
   \begin{bmatrix}
     I_{I11} & 0 & 0\\
     0 & I_{I11} & 0\\
     0 & 0 & I_{I33}
   \end{bmatrix}

.. math::
   :label: eqILowerArm

   \mathbf{I}_H =
   \begin{bmatrix}
     I_{H11} & 0 & 0\\
     0 & I_{H11} & 0\\
     0 & 0 & I_{H33}
   \end{bmatrix}
   =
   \mathbf{I}_J =
   \begin{bmatrix}
     I_{J11} & 0 & 0\\
     0 & I_{J11} & 0\\
     0 & 0 & I_{J33}
   \end{bmatrix}

With this information the equations of motion can be formed with Kane's method
as described in Chapter :ref:`eom`. Special care must be taken when linearizing
the equations of motion due to the eight holonomic constraints. The additional
generalized coordinates, :math:`q_9` through :math:`q_{16}`, are dependent
coordinates and are ultimately functions of the pitch and steer angles. The
chain rule must be properly applied or the independent coordinates must be
solved for when expanding the Taylor series and forming the Jacobian matrices.

Figures :ref:`4.4<figArmsRootLocus>` and :ref:`4.5<figArmsEig>` show how the
eigenvalues vary with speed with respect to the nominal configuration
equilibrium point. There are three distinct modes for all speeds shown, two of
which are real and one that is complex. The oscillatory mode is always stable,
unlike the weave mode in the Whipple model. Secondly, one real mode is always
unstable and the other is always stable. The addition of the arms' inertial
effects causes the system to not have a stable speed range unlike the
prediction of the Whipple model.

.. _figArmsRootLocus:

.. figure:: figures/extensions/arms-root-locus.*
   :width: 4in
   :align: center
   :target: _images/arms-root-locus.png

   The root locus with respect to speed of the Whipple model with arms for the
   parameter set associated with Jason seated on the Davis instrumented bicycle
   calculated with the Yeadon method. Generated with
   ``src/extensions/arms/plot_eig.py``.

.. _figArmsEig:

.. figure:: figures/extensions/arms-eig.*
   :width: 4in
   :align: center
   :target: _images/arms-eig.png

   The components of the eigenvalues with respect to speed of the Whipple model
   with arms for the parameter set associated with Jason seated on the Davis
   instrumented bicycle calculated with the Yeadon method. This plot shares
   similar characteristics as the one presented in :cite:`Schwab2010`. Generated
   with ``src/extensions/arms/plot_eig.py``.

One may be quick to parallel the three modes of motion to the weave, capsize,
and caster modes of the Whipple model, but closer examination of the
eigenvectors reveals that the motions are not quite the same. Figures
:ref:`4.6<figArmsPhasorHalf>`, :ref:`4.7<figArmsPhasorThree>`,
:ref:`4.8<figArmsPhasorFive>`, and :ref:`4.9<figArmsPhasorEight>` are phasor
plots of the eigenvector components at various speeds which correspond to the
ones given in previous chapter for the Whipple model.

The phasor diagrams show that the most negative real eigenmode is not as nearly
as fast as the caster mode and it is no longer dominated by steer angle. The
mode decays in both roll and steer with roll dominant at low speeds and steer
at high speeds. The unstable real eigenmode is dominant in roll angle and slows
with increasing speed like the Whipple model, but is unstable for the given
speeds. The stable oscillatory mode is dominant in steer at low speeds and
roll at high speeds. The 0.5 m/s case is interesting in that the mode is
primarily a stable oscillation in steer angle around 0.3 hertz. As the speed
increases the larger roll angle magnitude is different in behavior than the
Whipple weave mode.

.. _figArmsPhasorHalf:

.. figure:: figures/extensions/arms-phasor-half.*
   :width: 6in
   :align: center
   :target: _images/arms-phasor-half.png

   Normalized eigenvector components plotted in the real/imaginary plane for
   each mode at a forward speed of 0.5 m/s. Only the roll angle, :math:`q_4`,
   and steer angle, :math:`q_7`, components are shown. Generated with
   ``src/extensions/arms/plot_eig.py``.

.. _figArmsPhasorThree:

.. figure:: figures/extensions/arms-phasor-three.*
   :width: 6in
   :align: center
   :target: _images/arms-phasor-three.png

   Normalized eigenvector components plotted in the real/imaginary plane for
   each mode at a forward speed of 3.0 m/s. Only the roll angle, :math:`q_4`,
   and steer angle, :math:`q_7`, components are shown. Generated with
   ``src/extensions/arms/plot_eig.py``.

.. _figArmsPhasorFive:

.. figure:: figures/extensions/arms-phasor-five.*
   :width: 6in
   :align: center
   :target: _images/arms-phasor-five.png

   Normalized eigenvector components plotted in the real/imaginary plane for
   each mode at a forward speed of 5.0 m/s. Only the roll angle, :math:`q_4`,
   and steer angle, :math:`q_7`, components are shown. Generated with
   ``src/extensions/arms/plot_eig.py``.

.. _figArmsPhasorEight:

.. figure:: figures/extensions/arms-phasor-eight.*
   :width: 6in
   :align: center
   :target: _images/arms-phasor-eight.png

   Normalized eigenvector components plotted in the real/imaginary plane for
   each mode at a forward speed of 8.0 m/s. Only the roll angle, :math:`q_4`,
   and steer angle, :math:`q_7`, components are shown. Generated with
   ``src/extensions/arms/plot_eig.py``.

Notation
--------

:math:`G,J,I,J`
   The arm rigid bodies.
:math:`d_6`-:math:`d_{13}`
   Geometric distances to locate the arm joints.
:math:`s_r,e_r,h_r,g_r,s_l,e_l,h_l,g_l`
   Points on the arms and handlebars: (s)houlder, (e)lbow, (h)and, and (g)rip.
   Subscripts: (l)eft and (r)ight.
:math:`m_g,m_h,m_i,m_j`
   The masses of the arm rigid bodies.
:math:`\mathbf{I}_G,\mathbf{I}_H,\mathbf{I}_I,\mathbf{I}_J`
   The inertia tensors of the arm rigid bodies defined about the mass center
   and with respect to the local reference frame.

Front wheel flywheel
====================

Another model extension of interest involves addition of an extra rotating
wheel coincident with the front wheel. It is well known that that increasing
the angular momentum of the front wheel via change in inertia
(:cite:`Astrom2005`, :cite:`Franke1990`) or rotational speed, has a strong
effect on the stability of the Whipple model. For the benchmark bicycle
:cite:`Meijaard2007`, independently increasing the moment of inertia of the
front wheel, decreases both the weave and capsize speeds. A low weave speed may
provide open loop stability advantages to riders at low speed, with the
reasoning that a stable bicycle may require less rider control. Conversely, it
has also been shown both that a bicycle without gyroscopic effects can be
stable :cite:`Kooijman2011` and that humans can ride them :cite:`Jones1970`
with little difficulty. The idea that gyroscopic action can stabilize a moving
two wheeled vehicle has been demonstrated as early as the dawn of the 20th
century, with the invention of the gyro monorail and the gyro car
(:cite:`WikipediaGyromonorail2012`, :cite:`WikipediaGyroCar2012`) which made
use of control servos to gyros to applied roll righting torques to the single
track vehicles. Of more recent interest, several engineering students at
Dartmouth University applied this theory to a compact flywheel mounted within
the spokes of a children's bicycle wheel :cite:`Ward2006` taking advantage of
the fact that the flywheel imparts torques such that the bicycle steers into
the fall. This has since been developed into a commercially available product,
the GyroBike, that claims to allow children to learn to ride more easily, due
to the bicycle's increased stability at low speeds. I was given an article
about the bicycle from the Dartmouth alumni magazine, subsequently met the
woman who created the startup company around the idea in San Francisco, was
able to test ride the full scale prototype, and eventually purchased a 12"
version of the bicycle. The bicycle alone stays very stable even to extremely
low speeds, but when I, as an experienced rider, tried to ride and control it
the steering felt less responsive than one would generally prefer.

.. raw:: html

   <p>The following video demonstrates that the gyrobike without a rider is
   stabilized at 2 m/s when the flywheel is at full speed.</p>

   <center>
     <iframe width="420" height="315"
       src="http://www.youtube.com/embed/YmtPNIu4WI0"
       frameborder="0" allowfullscreen>
     </iframe>
   </center>

Using the Whipple model presented in Chapter :ref:`eom` as a base, the
flywheel's effect can be modeled by adding an additional symmetric rigid body,
:math:`G` with mass :math:`m_g` to the system which rotates about the front
wheel axis though a new generalized coordinate, :math:`q_9`. The angular
velocity and acceleration of the new body are defined with the simple
kinematical differential equation

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

   ^N\bar{v}^{g_o} = {}^N\bar{v}^{f_o}

.. math::
   :label: eqAGo

   ^N\bar{a}^{g_o} = {}^N\bar{a}^{f_o}

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

   \mathbf{I}_G =
   \begin{bmatrix}
     I_{G11} & 0 & 0\\
     0 & I_{G22} & 0\\
     0 & 0 & I_{G11}
   \end{bmatrix}

The equations of motion are formed and linearized with respect to the nominal
equilibrium point and a nominal angular velocity of the flywheel. Figures
:ref:`4.10<figGyroOff>`, :ref:`4.11<figGyroVary>`,
:ref:`4.12<figGyroOffRider>`, and :ref:`4.13<figGyroVaryRider>` show how
adjusting the flywheel angular velocity can affect the stability of the bicycle
which may be beneficial for people learning to ride a bicycle. All of the plots
were generated using parameters measured from a production GyroBike and the
rider's parameters were generated by scaling the Yeadon geometry of an adult,
Charlie, to child-size proportions which are detailed in Chapter
:ref:`physicalparameters`.

.. _figGyroOff:

.. figure:: figures/extensions/gyrobike-flywheel-off.*
   :width: 4in
   :align: center
   :target: _images/gyrobike-flywheel-off.png

   The magnitudes of the eigenvalue components with respect to the forward speed
   when the flywheel is fixed to the front wheel (i.e. has the same angular
   velocity as the front wheel). The solid lines show the real parts and the
   dotted lines show the imaginary parts, with color matching the parts for a
   given eigenvalue. Generated by ``src/extensions/gyro/gyrobike_linear.py``.

.. _figGyroVary:

.. figure:: figures/extensions/gyrobike-vary-flywheel.*
   :width: 4in
   :align: center
   :target: _images/gyrobike-vary-flywheel.png

   The magnitudes of the eigenvalue components with respect to the flywheel
   angular speed when the forward velocity is 0.5 m/s. The solid lines show the
   real parts and the dotted lines show the imaginary parts, with color
   matching the parts for a given eigenvalue. Generated by
   ``src/extensions/gyro/gyrobike_linear.py``.

:ref:`Figure 4.10<figGyroOff>` depicts similar dynamics as one would expect from
a riderless bicycle with a relatively low weave critical speed (~2.25 m/s).
:ref:`Figure 4.11<figGyroVary>` then shows that the very unstable system at low
speeds can certainly be made stable by increasing the angular velocity of the
flywheel. In particular the bicycle becomes stable around 1000 rpm but it is
also interesting to note that increasing the velocity too much (> 3500 rpm)
results in an unstable system. The actual Gyrobike flywheel spins at speeds up
to 2000 rpm and riderless stability can clearly be observed.

.. _figGyroOffRider:

.. figure:: figures/extensions/gyrobike-flywheel-off-rider.*
   :width: 4in
   :align: center
   :target: _images/gyrobike-flywheel-off-rider.png

   The magnitudes of the eigenvalue components with respect to the forward
   speed when the flywheel is fixed to the front wheel (i.e. has the same
   angular velocity as the front wheel) and a rigid child is seated on the
   bicycle. The solid lines show the real parts and the dotted lines show the
   imaginary parts, with color matching the parts for a given eigenvalue.
   Generated by ``src/extensions/gyro/gyrobike_linear.py``.

.. _figGyroVaryRider:

.. figure:: figures/extensions/gyrobike-vary-flywheel-rider.*
   :width: 4in
   :align: center
   :target: _images/gyrobike-vary-flywheel-rider.png

   The magnitudes of the eigenvalue components with respect to the flywheel
   angular speed when the forward velocity is 0.5 m/s and a rigid child is
   seated on the bicycle. The solid lines show the real parts and the dotted
   lines show the imaginary parts, with color matching the parts for a given
   eigenvalue. Generated by ``src/extensions/gyro/gyrobike_linear.py``.

:ref:`Figure 4.12<figGyroOffRider>` shows that the weave critical speed with a
rider is only about 1 m/s greater than without a rider. :ref:`Figure
4.13<figGyroOffRider>` shows that if a child-sized rider is rigidly added to
the rear frame that the flywheel must spin up to 3500 rpm for the system to be
stable and the time constant of the unstable eigenvalue does not decrease
significantly until the flywheel spins at 2000 rpm. Also as with the riderless
case, the system can be destabilized if the wheel spins at a high enough rate;
in this case about 7000 rpm.

.. _figGyroNonLin:

.. figure:: figures/extensions/gyro-nonlin-sim.*
   :width: 5in
   :align: center
   :target: _images/gyro-nonlin-sim.png

   The open loop non-linear simulation of the gyro bicycle given the initial
   conditions: :math:`u_4=0.5` rad/s, :math:`u_6=-v/r_R` where :math:`v=0.5`
   m/s, :math:`u_9=-5000` rpm.

:ref:`Figure 4.14<figGyroNonLin>` shows the resulting time history of the
non-linear model traveling at a very slow speed with the flywheel spinning fast
enough to stabilize the bicycle. The gyroscopic torques cause the steer angle
to decay rapidly in a steer into the fall. The conservative nature of the system
causes the forward speed to increase slightly. This is reflected as a decrease
in the flywheel rotational speed because it is defined with respect to the
front wheel.

This model and these examples give credence to the effectiveness of increasing
the angular momentum of the front wheel in stabilizing the bicycle. The
gyroscopic forces may not be necessary for stability but they have great power
in stabilizing even very unstable systems. This assistance does come a cost
though, both in the flywheel weight and the need to spin the flywheel at high
speeds. When the child rider's inertia is accounted for, very high spin speeds
are needed to stabilize the system. And interestingly, increasing the flywheel
speed too much can destabilize the system, albeit only marginally.

Notation
--------

:math:`G`
   The flywheel rigid body.
:math:`m_g`
   Mass of the flywheel.
:math:`q_9`
   Angle of the flywheel with respect to the front wheel.
:math:`u_9`
   Angular rate of the flywheel with respect to the front wheel.
:math:`g_o`
   Flywheel mass center.
:math:`T_9`
   Torque acting between the front wheel and the flywheel.
:math:`\mathbf{I}_G`
   Inertia tensor of the flywheel.
:math:`v`
   The forward speed of the bicycle: :math:`v = - r_R u_6`.

Leaning rider extension
=======================

A common assumption regarding how a person biomechanically controls a bicycle
with minimal or no input via the handlebars is that the rider can lean their
body relative to the bicycle rear frame. This assumption is more often than not
drawn from observing no-hands riding during which the rider seems to lean
relative to the bicycle frame. A simple leaning rider can be modeled by adding
an additional rider upper body as an inverted pendulum atop the bicycle. This
introduces an additional lean degree of freedom, :math:`q_9`, and can be
accompanied by a rider lean torque, :math:`T_9` which models the rider's
ability to apply forces between the upper torso and the rear frame.

Many have created variations of this model in the past including
:cite:`Lunteren1967`, :cite:`Roland1972`, :cite:`Weir1972`,
:cite:`Zytveld1975`, :cite:`Nagai1983`, etc. but, as :cite:`Roland1972` points
out, the roll torque is the more realistic control input as opposed to roll
angle as many of the other authors tend to prefer. Weir et al. notes the fact
that lean control has much less authority than steer control, and that the
rider more or less leans equal and opposite to the vehicles roll angle
:cite:`Weir1979a`. The inverted pendulum with a roll torque has now been widely
adopted and more recent works focus on understanding these types of models
(:cite:`Sharp2007`, :cite:`Sharp2008a`, :cite:`Schwab2008`,
:cite:`Peterson2008a`, etc.), with the hypothesis that control by roll torque
is much less effective than steer torque being confirmed in all these studies.

To build the same model, we define the upper body hinge as a horizontal line at
a distance :math:`d_4` below the rear wheel center when the bicycle is in the
nominal configuration. The direction cosine matrix relating the upper body to
the rear frame is

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

The mass center is located by

.. math::
   :label: eqLocGo

   \bar{R}^{g_o/c_g} = l_5 \hat{g}_1 + l_6 \hat{g}_3

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

   ^N\bar{v}^{c_g} = {}^N\bar{v}^{d_o} + {}^N\bar\omega^C\times\bar{r}^{c_g/d_o}

where

.. math::

   ^N\bar\omega^C\times\bar{r}^{c_g/d_o} =
   &d_4c_\lambda(u_5+s_4u_3)\hat{c}_1 -\\
   &d_4(s_\lambda(s_5u_4+c_4c_5u_3)+c_\lambda(c_5u_4-s_5c_4u_3))\hat{c}_2 +\\
   &d_4s_\lambda(u_5+s_4u_3)\hat{c}_3

and

.. math::
   :label: eqVGoInN

   ^N\bar{v}^{g_o} = {}^N\bar{v}^{c_g} + {}^N\bar\omega^G\times\bar{r}^{g_o/c_g}

where

.. math::

   ^N\bar\omega^G\times\bar{r}^{g_o/c_g} =
   &-l_6(s_9s_{\lambda-5}u_4-c_9u_5-(s_4c_9+s_9c_4c_{\lambda-5})u_3)\hat{g}_1 +\\
   &(-l_6(u_9+c_{\lambda-5}u_4+c_4s_{\lambda-5}u_3)-l_5(s_9u_5+
   c_9s_{\lambda-5}u_4+(s_4s_9-c_4c_9c_{\lambda-5})u_3))\hat{g}_2 +\\
   &l_5(s_9s_{\lambda-5}u_4-c_9u_5-(s_4c_9+s_9c_4c_{\lambda-5})u_3)\hat{g}_3

The linear accelerations of the hinge point and the upper body center of mass
are as follows

.. math::
   :label: eqACginN

   ^N\bar{a}^{c_g} = {}^N\bar{a}^{d_o} +
   {}^N\omega^C\times(^N\omega^C\times\bar{r}^{c_g/d_o}) +
   {}^N\bar{\alpha}^C\times\bar{r}^{c_g/d_o}

where

.. math::

   ^N\omega^C\times(^N\omega^C\times\bar{r}^{c_g/d_o}) =
   &d_4(s_\lambda(u_5+s_4u_3)^2+(s_5u_4+c_4c_5u_3)(s_\lambda(s_5u_4+
   c_4c_5u_3)+\\
   &c_\lambda(c_5u_4-s_5c_4u_3)))\hat{c}_1 +\\
   &d_4(u_5+s_4u_3)(c_\lambda(s_5u_4+c_4c_5u_3)-s_\lambda(c_5u_4-
   s_5c_4u_3))\hat{c}_2 -\\
   &d_4(c_\lambda(u_5+s_4u_3)^2+(c_5u_4-s_5c_4u_3)(s_\lambda(s_5u_4+
   c_4c_5u_3)+\\
   &c_\lambda(c_5u_4-s_5c_4u_3)))\hat{c}_3

and

.. math::

   ^N\bar{\alpha}^C\times\bar{r}^{c_g/d_o} =
   &d_4c_\lambda(c_4u_3u_4+\dot{u}_5+s_4\dot{u}_3)\hat{c}_1 +\\
   &d_4(s_\lambda(s_4c_5u_3u_4+s_5c_4u_3u_5-c_5u_4u_5-s_5\dot{u}_4-
   c_4c_5\dot{u}_3)-\\
   &c_\lambda(s_4s_5u_3u_4+c_5\dot{u}_4-s_5u_4u_5-
   c_4c_5u_3u_5-s_5c_4\dot{u}_3))\hat{c}_2 +\\
   &d_4s_\lambda(c_4u_3u_4+\dot{u}_5+s_4\dot{u}_3)\hat{c}_3

and

.. math::
   :label: eqAGoinN

   ^N\bar{a}^{g_o} = {}^N\bar{a}^{c_g} +
   {}^N\omega^G\times(^N\omega^G\times\bar{r}^{g_o/c_g}) +
   {}^N\bar{\alpha}^G\times\bar{r}^{g_o/c_g}

where

.. math::

   ^N\omega^G\times(^N\omega^G\times\bar{r}^{g_o/c_g}) =
   &(-l_5(s_9s_{\lambda-5}u_4-c_9u_5-(s_4c_9+s_9c_4c_{\lambda-5})u_3)^2-\\
   &(s_9u_5+c_9s_{\lambda-5}u_4+(s_4s_9-\\
   &c_4c_9c_{\lambda-5})u_3)(l_6(u_9+
   c_{\lambda-5}u_4+c_4s_{\lambda-5}u_3)+\\
   &l_5(s_9u_5+c_9s_{\lambda-5}u_4+
   (s_4s_9-c_4c_9c_{\lambda-5})u_3)))\hat{g}_1 -\\
   &(s_9s_{\lambda-5}u_4-c_9u_5-(s_4c_9+s_9c_4c_{\lambda-5})u_3)(l_5(u_9+
   c_{\lambda-5}u_4+c_4s_{\lambda-5}u_3)-\\
   &l_6(s_9u_5+c_9s_{\lambda-5}u_4+(s_4s_9-c_4c_9c_{\lambda-5})u_3))\hat{g}_2+\\
   &(-l_6(s_9s_{\lambda-5}u_4-c_9u_5-(s_4c_9+s_9c_4c_{\lambda-5})u_3)^2-\\
   &(u_9+c_{\lambda-5}u_4+c_4s_{\lambda-5}u_3)(l_6(u_9+c_{\lambda-5}u_4+\\
   &c_4s_{\lambda-5}u_3)+l_5(s_9u_5+c_9s_{\lambda-5}u_4+(s_4s_9-
   c_4c_9c_{\lambda-5})u_3)))\hat{g}_3

where

.. math::

   ^N\bar{\alpha}^G\times\bar{r}^{g_o/c_g} =
   &-l_6(s_9u_5u_9+c_9s_{\lambda-5}u_4u_9+u_3(s_4s_9u_9+s_4s_9c_{\lambda-5}u_4-
   c_4c_9u_4-s_9c_4s_{\lambda-5}u_5-\\
   &c_4c_9c_{\lambda-5}u_9)+s_9s_{\lambda-5}\dot{u}_4-s_9c_{\lambda-5}u_4u_5-c_9\dot{u}_5-
   (s_4c_9+s_9c_4c_{\lambda-5})\dot{u}_3)\hat{g}_1 +\\
   &(l_6(s_4s_{\lambda-5}u_3u_4+c_4c_{\lambda-5}u_3u_5-s_{\lambda-5}u_4u_5-
   \dot{u}_9-c_{\lambda-5}\dot{u}_4-c_4s_{\lambda-5}\dot{u}_3)+\\
   &l_5(s_9s_{\lambda-5}u_4u_9+c_9c_{\lambda-5}u_4u_5-
   c_9u_5u_9-u_3(s_4c_9u_9+s_9c_4u_4+s_4c_9c_{\lambda-5}u_4+\\
   &s_9c_4c_{\lambda-5}u_9-c_4c_9s_{\lambda-5}u_5)-
   s_9\dot{u}_5-c_9s_{\lambda-5}\dot{u}_4-
   (s_4s_9-c_4c_9c_{\lambda-5})\dot{u}_3))\hat{g}_2 +\\
   &l_5(s_9u_5u_9+c_9s_{\lambda-5}u_4u_9+u_3(s_4s_9u_9+s_4s_9c_{\lambda-5}u_4-
   c_4c_9u_4-s_9c_4s_{\lambda-5}u_5-\\
   &c_4c_9c_{\lambda-5}u_9)+s_9s_{\lambda-5}\dot{u}_4-
   s_9c_{\lambda-5}u_4u_5-c_9\dot{u}_5-(s_4c_9+
   s_9c_4c_{\lambda-5})\dot{u}_3)\hat{g}_3

We introduce two additional torques. The first is an input torque between the
rear frame and the rider's upper body, :math:`T_9`. This can be considered as
the active torque contribution which the rider's control system would provide.
The second torque is defined as

.. math::
   :label: eqPassiveTorque

   T_9^p = -c_9 u_9 - k_9 q_9

where :math:`c_9` and :math:`k_9` are damping and stiffness coefficients which
are provided as way to characterize the passive torques generated by the
tissue, ligament, tendon, and bone structures. A free lean joint without this
passive torque is far from realistic as large active torques would be required
to keep the body upright. These are equivalent to simple proportional and
derivative negative feedback on the roll angle and could be defined as such
equivalently.

The additional generalized force is

.. math::
   :label: eqGravity

   \bar{R}^{g_o} = m_Gg\hat{n}_3

and the generalized torques are modified to include the new torques

.. math::
   :label: eqGenTorques

   \bar{T}^C = T_4\hat{a}_1 - T_6\hat{c}_2 - T_7\hat{c}_3 +
   (k_9q_9+c_9u_9-T_9)\hat{g}_1

   \bar{T}^G = -(k_9q_9+c_9u_9-T_9)\hat{g}_1

The mass of the upper body is :math:`m_g` and it is assumed to by
symmetric about its sagittal plane

.. math::
   :label: eqIG2

   \mathbf{I}_G =
   \begin{bmatrix}
     I_{G11} & 0 & I_{G13}\\
     0 & I_{G22} & 0\\
     I_{G13} & 0 & I_{G33}
   \end{bmatrix}

The equations of motion are again formed using Kane's method and linearized as
described in Chapter :ref:`eom`. This linear model has been explicitly explored
by both :cite:`Schwab2008` and :cite:`Peterson2008a` with parameter values
estimated by proportioning the benchmark parameter set from
:cite:`Meijaard2007`. The following plot, :ref:`Figure 4.15<figRiderLean>`,
uses more realistic rider parameters which are generated with methods described
in Chapter :ref:`physicalparameters` and the passive lean torque coefficients
are set to zero to demonstrate the nature of the system with no passive
stiffness and damping. Notice that the largest eigenvalue is much larger than
those reported in Schwab and Peterson with a time to double of about a tenth of
a second. We found that root difficult to stabilize when employing a manual
control model based on the one presented in Chapter :ref:`control`, which
suggests the need and existence for some additional passive stabilization.

.. _figRiderLean:

.. figure:: figures/extensions/rider-lean.*
   :width: 5in
   :align: center
   :target: _images/rider-lean.png

   The magnitudes of the eigenvalue components with respect to the forward
   speed for the leaning rider model. The solid lines show the real parts and
   the dotted lines show the imaginary parts, with color matching the parts for
   a given eigenvalue. Generated by ``src/extensions/lean/riderlean.py``.

The damping and stiffness coefficients can be selected such that the highly
unstable rider mode is stabilized and the stable speed range observed in the
Whipple model is restored, :ref:`Figure 4.16<figRiderLeanPassive>`. It is likely
that control strategies that work with the Whipple model can be applied to this
model with appropriate stiffness and damping selections. The parameters used
are taken from :cite:`Lorenzo1996`, which he estimated to be, :math:`k_9=128`
N-m/rad and :math:`c_9=50` N-m/rad/s.

.. _figRiderLeanPassive:

.. figure:: figures/extensions/rider-lean-damp-stiff.*
   :width: 5in
   :align: center
   :target: _images/rider-lean-damp-stiff.png

   The magnitudes of the eigenvalue components with respect to the forward speed for
   the leaning rider model. The solid lines show the real parts and the dotted
   lines show the imaginary parts, with color matching the parts for a given
   eigenvalue. Generated by ``src/extensions/lean/riderlean.py``.

The leaning rider model exhibits a very fast, unstable eigenmode which is
constant with respect to speed when the upper body is treated as a simple
inverted pendulum. In general, rider lean degrees of freedom have a
de-stabilizing effect to the Whipple model. A combination of the rider's active
and passive postural control most likely stabilizes this mode in the real
system, but it is debatable whether the passive control alone completely
stabilizes the mode.

Notation
--------

:math:`d_4`
   The distance to the torso hinge.
:math:`l_5,l_6`
   Distances to locate the upper body mass center.
:math:`s_{\lambda-5}`, :math:`c_{\lambda-5}`
   Shorthand for :math:`\operatorname{sin}(\lambda-q_5)` and
   :math:`\operatorname{sin}(\lambda-q_5)`.
:math:`c_g`
   Rider hinge point.
:math:`c_9,k_9`
   The passive stiffness and damping coefficients.
:math:`m_g`
   Mass of the upper body (torso, arms, neck, and head).
:math:`\mathbf{I}_g`
   Inertia of the upper body.
:math:`T_9`
   The active torque acting between the rider's upper body and the rear frame.
:math:`T_9^p`
   The passive torque acting between the rider's upper body and the rear frame.

David de Lorenzo extension
==========================

Preface
-------

To expand on the ideas presented in the previous section, I'd like to share
some findings from a short conference paper that Luke Peterson and I put
together for the 11th International Symposium on Computer Simulation in
Biomechanics :cite:`Moore2007`. I have included it here almost verbatim but have
updated the writings to tie it better into the dissertation and make it less
dated. I have not updated the derivation of the equations of motion to reflect
the parameters and methodology presented in this dissertation, so I will leave
those out but they can be found in the source code. Nonetheless the model can
be systematically derived in the same fashion as the previous sections. The
initial interest in this model was based on an unpublished paper by de Lorenzo
and Hubbard :cite:`Lorenzo1996` which explored parameter studies of a model similar
to the one that is presented. Here we pursue the effects that passive springs
and dampers at the biomechanical joints have on the stability of the bicycle,
in much the same way as in the previous section but with a more complex rider
model.

Introduction
------------

We build on the Whipple model by adding biomechanical degrees of freedom that
capture the dominant rider's motion and the flexible coupling to the rear
frame. The rationale for doing so is that the mass and inertia of a rider is
much larger than that of the bicycle, and the coupling between the rider and
the bicycle is certainly not rigid. Rider modeling has been approached in the
motorcycle literature :cite:`Limebeer2006` but typically does not address the
smaller vehicle inertial properties and the possible difference in the coupling
constants. For example, when riding a bicycle, it is easy to observe that the
frame yaw and roll motions differ from the rider yaw and roll motions.
Modeling the rider and frame as a single rigid body ignores this flexible
coupling. In this analysis, we seek to understand the effect of the addition of
these new degrees of freedom on the stable speed ranges of the bicycle. We
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
also in parallel. These rider degrees of freedom are detailed in :ref:`Figure
4.17<figLorenzoConfiguration>` and are similar to the motorcycle rider model
constructed by Katayama, et al. :cite:`Katayama1988` with the exception of the rider
twist. The lateral linear spring and damper represents the connection between
the rider’s crotch and the seat\ [#crotch]_. The spring and damper constants are
influenced by the seat and the properties of the skeletal muscle tissue of the
inner thighs and/or buttocks. The torsional springs and dampers represent the
musculoskeletal stiffness and damping at the hips.

.. _figLorenzoConfiguration:

.. figure:: figures/extensions/lorenzo-configuration.*
   :width: 5 in
   :align: center
   :target: _images/lorenzo-configuration.*

   Pictorial description of (a) the additional rider degrees of freedom and (b)
   the six rigid bodies.

This six-rigid-body model has eleven generalized coordinates. One generalized
coordinate (frame pitch) is eliminated by the holonomic configuration
constraints requiring that both wheels touch the ground. This leaves ten
generalized speeds, of which four are eliminated due to the nonholonomic
constraints for the purely rolling wheels. The nonlinear equations of motion
were linearized numerically about the nominal upright, constant velocity
configuration using a central differencing method with an optimum perturbation
size. The linear system is tenth order in frame roll, steer, lower body lean,
upper body lean, and upper body twist.

The physical parameters are adapted from :cite:`Meijaard2007` with exception of the
rider pivot point locations and the spring and damper constants. The pivot
point locations were measured and the spring and damper constants were taken
from :cite:`Lorenzo1996`, which he estimated. All of the physical parameters were
chosen in such a way that, if the rider degrees of freedom are locked, the
model reduces to the benchmark Whipple model, similar to the later work done by
:cite:`Peterson2008a` and :cite:`Schwab2008`.

Results and Discussion
----------------------

In order to understand how the eigenvalues impact each state variable of our
system, it is essential to examine the components of each eigenvector
corresponding to each generalized coordinate. By detailed examination, we are
able to determine how each eigenvalue contributes to each generalized
coordinate, across the range of speeds examined.

:ref:`Figure 4.18<figLorenzoEig>` shows the real parts of the identified
eigenvalues of the flexible rider model and :ref:`Figure
4.19<figLorenzoComplex>`. By comparison to the Whipple model, it can be seen
that the modes are greatly affected by the additional rider states. The weave
mode has become unstable for all velocities and no stable speed range is
present. Additionally, the rider modes are all complex at all speeds.

.. _figLorenzoEig:

.. figure:: figures/extensions/lorenzo-eig.*
   :align: center
   :width: 4in
   :target: _images/lorenzo-eig.jpg

   Real parts of the eigenvalues as a function of forward speed with the
   stiffness and damping terms set to realistic values.

.. _figLorenzoComplex:

.. figure:: figures/extensions/lorenzo-plane.*
   :width: 2 in
   :align: center
   :target: _images/lorenzo-plane.png

   Root locus of the eigenvalues with respect to speed, a different view of
   :ref:`Figure 4.18<figLorenzoEig>`.

Examining the eigenvector of the weave mode at different velocities, we find
that at low speeds the weave mode is dominated by frame roll and steer, while
at high speeds the weave is dominated by upper body lean and twist about the
body's long axis, :ref:`Figure 20<figLorenzoEigVec>`. This phenomenon was also
observed by Limebeer and Sharp :cite:`Limebeer2006`. Furthermore, another unstable
oscillatory eigenvalue pair is present at velocities below about 4 m/s for this
parameter set.

.. _figLorenzoEigVec:

.. figure:: figures/extensions/lorenzo-eigvec.png
   :width: 5 in
   :align: center

   Weave mode eigenvector components for the Whipple model (left) and the
   de Lorenzo model (right) at 5.0 m/s.

As the stiffness and damping coefficients for the rider/frame coupling are
increased (by factors of about :math:`10^3` and :math:`30` respectively), the
eigenvalues begin to match those of the Whipple model, and a stable speed range
reappears. However, the values of stiffness and damping for which a stable
speed range did exist are unrealistically high :ref:`Figure
21<figLorenzoHigh>`.

.. _figLorenzoHigh:

.. figure:: figures/extensions/lorenzo-high.jpg
   :width: 4 in
   :align: center

   Real parts of the eigenvalues as a function of forward speed with the
   stiffness and damping terms set to unrealistically high values.

Conclusion
----------

The notion that the bicycle-rider system can be stable during hands-free riding
with no active control from the rider seems to be not necessarily true when the
rider's biomechanics are modeled more realistically. For the particular set of
estimated parameters, the weave mode is unstable for the entire range of speeds
investigated when realistic flexible rider dynamics are included. While the
Whipple model provides many insights into the dynamics and control of the
bicycle, it lacks the complexity to capture the essential dynamics that are
present in open-loop hands-free riding. In particular, it is highly likely that
bicycle rider must always use active control to keep the bicycle upright and
self-stabilization is not guaranteed. Parameters studies that show the
dependence of stability across a range of speeds for ranges of stiffness and
damping at the biomechanical joints can shed more light on the system for more
conclusive results.

.. _secFlexibleRider:

No Hands
========

I've ended up thinking a great deal about the actual biomechanical motion one
uses to balance a bicycle when riding no handed and I've learned much about it
by talking with colleagues such as Jim Papadopoulos, Jodi Kooijman, Arend
Schwab, and others. For the final studies in this dissertation I had intended
to do a thorough study of the dynamics of balancing with no hands by more
carefully modeling the actual biomechanics we employ during the task.
Understanding hands free balancing can also shed light into how we use our body
when we also have our hands on the bars, albeit with much smaller body motions
because steer is almost always the optimal control input to the bicycle. Steer
provides much more control authority.

It is relatively easy to learn to ride without using ones hands and many people
that know how to ride a bicycle can do so. Some can even navigate roads and
obstacles reasonably well. Without being able to directly affect the steering
angle for control purposes, one must somehow affect the roll angle, which in
turn is coupled to steering. Driving the roll angle drives the steer angle
which points the bicycle in the desired direction. In the purely mechanical
sense one can imagine that a rider could "lean" relative to the rear frame,
thus inducing the counter reaction causing the frame to roll the opposite
direction of the lean. Models are often the chosen with this theory in mind
:cite:`Zytveld1975`, :cite:`Peterson2008a`, :cite:`Schwab2008`,
:cite:`Sharp2008a`, etc. They are the most intuitive and simple model but the
idea of leaning may in fact be too simplistic to describe the actual
biomechanical coupling a rider has with a bicycle\ [#motorcyclelean]_.

The rider's upper body is typically more than three times the mass of the
bicycle and it takes proportionally more force to move it. The studies that
will be presented in Chapters :ref:`delftbicycle` and :ref:`motioncapture` show
that the rider's upper body both moves little relative to the rear frame and
leans little with  with respect to inertial space\ [#weir]_. In contrast the
bicycle can quickly roll relative to the relatively inertially "fixed" rider.
With that in mind, it is possible to imagine rolling the bicycle frame
underneath the body using leg and buttock muscles. The fact that during
hands-free riding one feels the seat moving back and forth under between one's
legs, gives some evidence that the coupling at the seat is important. Another
interesting thing to note is that it is virtually impossible to control a
bicycle without both hands *and* both feet placed on the grips and pedals,
respectively. Removing ones feet from the pedals removes the ability to apply
forces from the rider's body to the bicycle frame, which can contribute to
control of the bicycle roll angle. Secondly, it is also noteworthy that the
roll angle of the bicycle can be commanded much easier when the rider is up off
the seat (i.e. the rider contacts the bicycle only with hands and feet). This
leads me to hypothesize that no-hand-control is dependent on the rider's
ability to roll the bicycle frame using the lower extremity muscles which are
critically dependent on the leg.

If that is true, then there is may be a simple model that can capture the
relative motion of the bicycle rear frame with respect to the lower extremities
and pelvis. To help confirm this I examined the data from the motion capture
experiments (Chapter :ref:`motioncapture`) of a no-hand run with the rider
pedaling. :ref:`Figure 22<figHipTrace>` plots the motion of the coccyx and
pelvis markers in the rear frame reference frame from the perspective of
looking at the rider's torso from the front for a single run. This plot was
shows that the coccyx moves laterally with respect to bike frame, but more
prevalent are the curves that the pelvis follows. This gives indication that
the pelvis basically rotates about an axis just below the seat that runs
longitudinally with respect to the bicycle.

.. raw:: html

   <p>The following video shows a rider balancing at 10 km/h without using his
   hands.</p>

   <center>
     <iframe width="480" height="360"
       src="http://www.youtube.com/embed/7KXQPUsA3ds"
       frameborder="0" allowfullscreen>
     </iframe>
   </center>

.. _figHipTrace:

.. figure:: figures/extensions/hip-trace.*
   :width: 4in
   :align: center
   :target: _images/hip-trace.png

   The hip trace from run # 3104. This plots the position of the two hip
   markers and the coccyx marker relative to the bicycle's rear frame in space
   over time. `View the video <http://www.youtube.com/7KXQPUsA3ds>`_.

Gilbert Gede and I began devising a harness that would both constrain the
rider's motion to the motion observed in :ref:`Figure 22<figHipTrace>` and
allows us to measure the forces and the kinematics involved. We created a
`video <http://www.youtube.com/embed/FcAp-DbHp9M>`_ shot from behind and shows
me balancing no-handed on a treadmill. We taped three sticks to my back: one
across the shoulders, the second to the upper portion of my spine, and the
third to the lower portion of my spine to visualize the dominant motion of the
rider with respect to the bicycle frame and how the spine moved. I chose the
stick locations based on the motion capture studies we did. This video
confirmed that the spine bend could probably be described by a single joint in
the middle of the spine and that the pelvis rolls about the seat (i.e. a
longitudinal axis just below the seat).

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
these motions and limit the rider to the observed motions.

.. _figTestRiderHarness:

.. figure:: figures/extensions/test-rider-harness.*
   :width: 3in
   :align: center
   :target: _images/test-rider-harness.png

   A mock-up of a harness to measure the dominant motions of the rider's pelvis
   roll angle relative to the bicycle rear frame and the lean angle relative to
   the pelvis. The lower brace (green) is affixed the rider's pelvis and
   rotates relative to the bicycle frame. The second joint allows the rider's
   torso to lean relative to the pelvis.

The model to describe this motion would have a revolute joint just below the
seat such that the riders pelvis can roll about a longitudinal revolute joint
just below the seat. The legs would be constrained such that the feet locked
into the foot pegs and the knee angles would be dependent on the pelvis roll
angle. Finally, the spine would be stiffened with a back brace and a single
revolute joint for back lean relative to the pelvis would be measured.

We intended to develop a harness and pair it with a force measuring seat post
and foot pegs which measure the downward force applied by the feet to the
bicycle. The goal would have been to characterize the both the kinematic and
kinetic coupling between the rider and the bicycle which causes the bicycle to
roll. I included this section to simply document the thoughts and effort, but
none of this was ever executed in a proper experiment.

Conclusions
===========

Several extensions to the Whipple model have been presented. The details are
not exhaustive but provide some useful conclusions for the coming chapters. I
showed that the lateral force input we used in the control experiments must be
properly accounted for and not simply assumed to be characterized by a pure
roll torque. This force contributes to both the roll and steer degrees of
freedom which is a function of the location of the force application. Secondly,
the addition of the inertial affects of the arms change the bicycle system
dynamics significantly. In this particular case, it eliminates any possibility
for stability and the capsize mode becomes very unstable. This model will play
a role in the data analysis presented in Chapter :ref:`systemidentification`
because it more realistically models our test subjects' motion. In the third
section, I show how adding a flywheel to the front wheel of a bicycle can
radically change it's stable speed regime and can make the model stable at very
low speeds, even slower than average walking. But if the inertial effects of
the rider are taken into account, the flywheel may have to spin at very high
speeds for any significant change in dynamics. Next, I show that adding various
rider degrees of freedom generally creates an unstable system, but passive
forces acting on the new joints can potentially stabilize the new modes. It is
likely that the rider must make use of a combination of both passive and active
control to keep the bicycle/rider system stable. Finally, I've presented some
ideas and thoughts on developing a slightly different biomechanical model of
the rider that may be a more realistic way of characterizing the motion used
for hands-free control of the bicycle.

.. rubric:: Footnotes

.. [#crotch] We got a kick out of "crotch stiffness" i.e. the stiffness of the
   crotch spring, and tried to encourage Mont to use the terminology when he
   presented this for us in Taiwan.

.. [#motorcyclelean] A model for leaning on a motorcycle makes more sense as
   the mass of the motorcycle is comparable to or more than the mass of the
   riders upper body.

.. [#weir] :cite:`Weir1979a` points out this with respect to motorcycles, in
   that the rider's upper body mostly stays still and rider's lean angle is
   nearly equal and opposite to the motorcycle.
