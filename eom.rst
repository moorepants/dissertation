.. _eom:

===========================
Bicycle Equations Of Motion
===========================

Introduction
============

Attempting to derive the equations of motion of the Whipple bicycle model was
the trigger which solidified my graduate research topic. I attempted the
derivation for my class project in Mont Hubbard's winter 2006 multi-body
dynamics class and struggled with it well into the summer before finally
getting a mostly correct answer. After the fact, I realized much of my pain was
caused by a single missing apostrophe in my Autolev source code [#]_. But
regardless of that another student in the class, Thomas Englehardt, also
derived the equations and helped me debug by sharing his code and going over
his methods. Even then, it turned out that my original equations weren't
"exactly" correct and it wasn't until Luke Peterson joined our lab and got the
bicycle dynamics itch did I get the bugs sorted out in my derivation.
Conversations and collaboration with Luke have improved the derivation
significantly and influence much of what follows. Luke has also continued to
improve the derivation with the goal of printing the first compact symbolic
result.

Derivation of the Non-linear Equations of Motion
================================================

The Whipple Model is the foundation of all the models presented in this
dissertation. This section details derivation of the non-linear equations of
motion using Kane's method [KaneLevinson1985]_. The equations of motion are
algebraically unwieldy and no one so far has publicly printed them in a form
compact enough to print on reasonably sized paper and certainly not in a form
suitable for any in depth analytical understanding [#]_. My methodology relies
heavily on computer aided algebra to do the bookkeeping in the derivation, so I
will only describe the necessary details to derive the equations, leaving the
algebra, trigonometry and calculus to the computer. The symbolic equations of
motion herein were originally developed using Autolev, a proprietary and now
defunct software package for symbolically deriving equations of motion for
multi-body systems. I've since used the open source software `SymPy
<http://sympy.org>`_ to derive the equations with the help of the included
``mechanics`` package which was developed in our lab to provide a software
package suitable of academia with similar capabilities as Autolev. The input
code for both software packages are available in the ``src/eom`` directory of
the dissertation source files.

.. todo:: add the autolev code to the src/eom directory, i.e. make alparse
   installable

Model Description
-----------------

The *Whipple Bicycle Model* [Whipple1899]_ is typically defined by these set of
assumptions:

* The Whipple model is made up of four rigid bodies: the main frame (may or may
  not include a rigid rider), the fork and handlebar assembly and two wheels.
* The bodies are connected to each other by frictionless revolute joints.
* The wheels have knife edges and contact the ground under pure rolling with no
  side-slip.
* The complete bicycle is assumed to be laterally symmetric.
* The bicycle rolls on flat ground.

Unfortunately the word "model" will be used in varying contexts and with
different meanings throughout this dissertation. I will attempt to be precise
with my wording. For this chapter, I consider a dynamic model, such as the
*Whipple Bicycle Model*, to be the equivalent to another dynamic model if at
least the minimal set of equation of motions are the same (i.e. give the same
result when evaluated at a particular state). This implies that the Whipple
Bicycle Model linearized about the nominal configuration is a different model
than the non-linear *Whipple Bicycle Model*. I will try to be explicit when
referring to the various models.

.. todo:: What about when a model is invalid at some configuration? I suspect
   that a derivation with euler angles might very well give different results
   as the same model derived with quaternions at a point where the euler angle
   derivation has a divide by zero.

I will use this terminology for the four rigid bodies, see Figure
:ref:`figBicycleGeometry <1>`:

Rear Frame, :math:`C`
   The main bicycle frame which may include parts or all of the rider.
Rear Wheel, :math:`D`
   The rear wheel of the bicycle.
Front Frame, :math:`E`
   The fork and handlebar assembly. May include things such front racks and
   panniers.
Front Wheel, :math:`F`
   The front wheel of the bicycle.

Parameterization
----------------

The benchmark derivation of the linear Whipple model [Meijaard2007]_ about the
nominal configuration uses a set of non-minimal parameters based on typical
geometric parameters and inertia definitions with respect to the global
reference frame. The *nominal configuration* is defined as the configuration
when the steering angle is zero and the bicycle is upright with respect to
gravity and the ground plane. The parameters presented in [Meijaard2007]_ are
not necessarily the best choice of parameters, especially when looking at the
model from a non-linear perspective, as they not the simplest nor a minimal set
of parameters. For example, the benchmark parameters can been reduced in number
by making use of gyrostats, see [Sharp2008]_. Choosing a minimum, constant set
of parameters can certainly reduce the complexity of the resulting non-linear
equations. In this derivation, I use a parameterization with different geometry
and inertial definitions to facilitate a more intuitive non-linear derivation,
but do not make use of gyrostats to reduce the number of parameters.

Conversion
~~~~~~~~~~

This section details the conversion from the benchmark parameter set to my
parameter set. When the bicycle is in the nominal configuration the parameters
can be converted with the following relationships. The wheel radii are defined
the same, but the remaining geometry is calculated with:

.. math::
   :label: eqGeometryConversion

   d_1 = \operatorname{cos}(\lambda) (c + w - r_R \operatorname{tan}(\lambda))

   d_3 = -\operatorname{cos}(\lambda) (c - r_F \operatorname{tan}(\lambda))

   d_2 = \frac{(r_R + d_1 \operatorname{sin}(\lambda) - r_F + d_3
   \operatorname{sin}(\lambda))}{\operatorname{cos}(\lambda)}

The mass center locations are as follows:

.. math::
   :label: eqMassCenterConversion

   l_1 = x_B  \operatorname{cos}(\lambda) - z_B  \operatorname{sin}(\lambda) -
   r_R  \operatorname{sin}(\lambda)

   l_2 = x_B  \operatorname{sin}(\lambda) + z_B  \operatorname{cos}(\lambda) +
   r_R \operatorname{cos}(\lambda)

   l_4 = (z_H + r_F)  \operatorname{cos}(\lambda) + (x_H - w)
   \operatorname{sin}(\lambda)

   l_3 = \frac{x_H - w - l_4  \operatorname{sin}(\lambda)}
   {\operatorname{cos}(\lambda)}

The masses are equivalently defined. The left are my variable names and the
right are the Benchmark names:

.. math::
   :label: eqMassConversion

   m_C = m_B

   m_D = m_R

   m_E = m_H

   m_F = m_F

The moments of inertia of the wheels are also equivalently defined:

.. math::
   :label: eqWheelInertiaConversion

     \mathbf{I}_D =
     \begin{bmatrix}
       I_{D11} & 0 & 0\\
       0 & I_{D22} & 0\\
       0 & 0 & I_{D11}
     \end{bmatrix}
     = \mathbf{I}_R =
     \begin{bmatrix}
       I_{Rxx} & 0 & 0\\
       0 & I_{Ryy} & 0\\
       0 & 0 & I_{Rxx}
     \end{bmatrix}

     \mathbf{I}_F =
     \begin{bmatrix}
       I_{F11} & 0 & 0\\
       0 & I_{F22} & 0\\
       0 & 0 & I_{F11}
     \end{bmatrix}
     = \mathbf{I}_F =
     \begin{bmatrix}
       I_{Fxx} & 0 & 0\\
       0 & I_{Fyy} & 0\\
       0 & 0 & I_{Fxx}
     \end{bmatrix}

The moments and products of inertia for the frame and fork require the
direction cosine matrix with respect to rotation through :math:`\lambda`.

.. math::
   :label: eqConversionRotation

   \mathbf{R} =
   \begin{bmatrix}
     c_\lambda & 0. & -s_\lambda\\
     0. & 1. & 0.\\
     s_\lambda & 0. & c_\lambda
   \end{bmatrix}

.. math::
   :label: eqFrameInertiaConversion

    \mathbf{I}_B =
    \begin{bmatrix}
      I_{Bxx} & 0 & I_{Bxz}\\
      0 & I_{Byy} & 0\\
      I_{Bxz} & 0 & I_{Bzz}
    \end{bmatrix}

    \mathbf{I}_C =  \mathbf{R} \mathbf{I}_B \mathbf{R}^T

.. math::
   :label: eqForkInertiaConversion

   \mathbf{I}_H =
   \begin{bmatrix}
     I_{Hxx} & 0 & I_{Hxz}\\
     0 & I_{Hyy} & 0\\
     I_{Hxz} & 0 & I_{Hzz}
   \end{bmatrix}

   \mathbf{I}_E =  \mathbf{R} \mathbf{I}_H \mathbf{R}^T

.. _geometry:

Geometry
--------

The geometry of the Whipple model can be parameterized in an infinite amount of
ways. It is typical and often natural to define the geometry with respect to
the descriptions of bicycle geometry used in the bicycle fabrication industry
such as wheel diameter, head tube angle, trail and or rake. Choices of
parameterizations like these create unnecessary complications when developing
the non-linear equations of motion because they are typically defined with
respect to only the nominal configuration of the bicycle and are not constant
with respect to the system configuration.

.. todo:: Should I include a diagram of the traditional geometry definitions?

With that in mind and after trying various parameterizations, I settled on the
geometric formulation presented by [Psiaki1979]_. The wheels are described by
their radius (:math:`\left(r\geq0\right)`) and the remaining geometry is
defined by three distances, all of which are configuration invariant. The
distance :math:`d_1` is the offset to the center of the rear wheel from the
steer axis and :math:`d_3` is the offset of the front wheel from the steering
axis. :math:`d_2` is then the distance between the wheel centers as measured
along the steer axis. :ref:`Figure 1 <figBicycleGeometry>` gives a complete
visual description.

.. _figBicycleGeometry:

.. figure:: figures/eom/bicycle-geometry.png
   :align: center
   :width: 3.75in

   The bicycle in the nominal configuration. The rigid bodies are the
   rear frame, C, rear wheel, D, front frame, E and front wheel, F. The
   geometric parameters and important points are also shown.

Generalized Coordinates
-----------------------

The bicycle is completely configured in a Newtonian reference frame by eight
generalized coordinates. I chose the SAE vehicle dynamics coordinates standard
as in [Meijaard2007]_ [#]_ and all rotations are are defined as positive
right-handed. I define rotation matrices such that:

.. math::

   \bar{a} = ^N\mathbf{R}^A \bar{n}

where :math:`\bar{n}` is a vector expressed in the :math:`N` frame and
:math:`\bar{a}` is the same vector expressed in the :math:`A` frame.

.. figure:: figures/eom/bicycle-coordinates.png
   :width: 3.6in
   :align: center

   figBicycleCoordinates

   The bicycle in a general configuration showing each of the eight generalized
   coordinates.

I start with locating the point that follows the rear wheel contact in the
ground plane of the Newtonian reference frame, :math:`N`, with the longitudinal
and lateral coordinates :math:`q_1` and :math:`q_2`, respectively. I then
orient the rear frame, :math:`C`, with respect to the Newtonian reference frame
through a body fixed 3-1-2 rotation defining the yaw angle, :math:`q_3`, the
roll angle, :math:`q_4`, and the pitch angle, :math:`q_5`. The intermediate
frames yaw, :math:`A` and roll, :math:`B`, are implicitly generated. The
rotation matrix of :math:`C` relative to :math:`N` is then:

.. math::
   :label: NtoC

   ^N\mathbf{R}^C =
   \begin{bmatrix}
   c_3c_5 - s_3s_4s_5 & s_4s_5c_3 + s_3c_5 & -s_5c_4\\
   -s_3c_4 & c_3c_4  & s_4\\
   s_5c_3 + s_3s_4c_5 & s_3s_5 - s_4c_3c_5 & c_4c_5
   \end{bmatrix}

The rear wheel, :math:`D`, rotates with respect to the rear frame about the
:math:`\hat{c}_2` axis through :math:`q_6`.

.. math::
   :label: CtoD

   ^C\mathbf{R}^D =
   \begin{bmatrix}
   c_6 & 0 & -s_6\\
   0 & 1 & 0\\
   s_6 & 0 & c_6
   \end{bmatrix}

The front frame, :math:`E`, rotates with respect to the rear frame about the
:math:`\hat{c}_3` axis through the steering angle, :math:`q_7`.

.. math::
   :label: CtoE

   ^C\mathbf{R}^E =
   \begin{bmatrix}
   c_7 & s_7 & 0\\
   -s_7 & c_7 & 0\\
   0 & 0 & 1
   \end{bmatrix}

Finally, the front wheel, :math:`F`, rotates with respect to the front frame
through :math:`q_8` about the :math:`\hat{e}_2` axis.

.. math::
   :label: EtoF

   ^E\mathbf{R}^F =
   \begin{bmatrix}
   c_8 & 0 & -s_8\\
   0 & 1 & 0\\
   s_8 & 0 & c_8
   \end{bmatrix}

The first two coordinates locate the system in the Newtonian reference frame
and the remaining six coordinates orient the four rigid bodies within the
Newtonian reference frame.

The positions of the various points on the bicycle must be defined with respect
to the Newtonian reference frame. There are six primary points of interest: the
four mass centers, :math:`d_o,c_o,e_o,f_o`, and the two points fixed on the
wheels which are instantaneously in contact with the ground, :math:`d_n,f_n`
[#]_.

The mass center of the rear wheel, :math:`d_o`, is assumed to be at the center
of the wheel and is located by:

.. math::
   :label: rearWheelMassCenter

   \bar{r}^{d_o/n_o} = q_1\hat{n}_1 + q_2\hat{n}_2 - r_F\hat{b}_3

The rear frame mass center, :math:`c_o`, is located by two additional
parameters:

.. math::
   :label: frameMassCenter

   \bar{r}^{c_o/d_o} = l_1\hat{c}_1 + l_2\hat{c}_3

For convenience, I define an additional point on the steer axis, :math:`c_e`,
such that:

.. math::
   :label: DoToCe

   \bar{r}^{c_e/d_o} = d_1\hat{c}_1

The mass center of the front wheel, :math:`f_o`, is then located by:

.. math::
   :label: frontWheelMassCenter

   \bar{r}^{f_o/c_e} =  d_2\hat{c}_3 + d_3\hat{e}_1

The front frame mass center, :math:`e_o`, is located by two more additional
parameters:

.. math::
   :label: forkMassCenter

   \bar{r}^{e_o/f_o} = l_3\hat{e}_1 + l_4\hat{e}_3

The location of the point on the rear wheel instantaneously in contact with the
ground in the Newtonian frame is then defined by:

.. math::
   :label: rearWheelContact

   \bar{r}^{d_n/d_o} = r_F\hat{b}_3

The location of the front wheel contact point is less trivial. The vector from
the front wheel center to the contact point is defined as:

.. math::
   :label: frontWheelContact

   \bar{r}^{f_n/f_o} = r_F\left(\frac{(\hat{e}_2\times\hat{a}_3)\times\hat{e}_2}
   {||(\hat{e}_2\times\hat{a}_3)\times\hat{e}_2||}\right)

.. todo:: I can define m to reduce the length of several of the longer
   equations. :math:`m = \sqrt{c_4^2c_5^2+(s_4s_7-s_5c_4c_7)^2}`

.. math::

   \bar{r}^{f_n/f_o} =
   r_F(s_4s_7-s_5c_4c_7)/(c_4^2c_5^2+(s_4s_7-s_5c_4c_7)^2)^{1/2}\hat{e}_1 +
   r_Fc_4c_5/(c_4^2c_5^2+(s_4s_7-s_5c_4c_7)^2)^{1/2}\hat{e}_3

Where the triple cross product divided by its magnitude represents the unit
vector pointing from the front wheel center to the point on the front wheel
instantaneously in contact with the ground. [Basu-Mandal2007]_ give an
explanation and diagram. I originally thought of this vector in terms of dot
products, i.e. subtract the :math:`\hat{n}_3` component of :math:`\hat{e}_2` from
:math:`\hat{n}_3` to get a vector that points from the front wheel center to
the contact point.

.. math::
   :label: frontWheelContactDot

   \bar{r}^{f_n/f_o} =
   r_F\left(\frac{\hat{a}_3 - (\hat{e}_2 \cdot\hat{a}_3)\hat{e}_2}
   {||\hat{a}_3 - (\hat{e}_2 \cdot\hat{a}_3)\hat{e}_2||}\right)

This is easily shown to be equivalent to :eq:`frontWheelContact` by writing the
triple cross product as sum of dot products.

Holonomic Constraints
---------------------

Two holonomic configuration constraints, arising from the fact that both wheels
must touch the ground, complicate the model derivation. The first holonomic
equation is obviated by definition of the rear wheel center
:eq:`rearWheelMassCenter`. This enforces that the contact point
cannot have an displacement in the :math:`\hat{n}_3` direction. [#]_ The second
holonomic constraint is enforced by requiring the front wheel to touch the
ground plane. The constraint is characterized by a nonlinear relationship
between the roll angle :math:`q_4`, steer angle :math:`q_7` and pitch angle
:math:`q_5`.

.. math::
   :label: holonomicConstraint

   \bar{r}^{f_n/d_n}\cdot\hat{a}_3 =
   &d_2c_4c_5 - d_1s_5c_4 + r_Rc_4 +
   r_Fc_4^2c_5^2/(c_4^2c_5^2+(s_4s_7-s_5c_4c_7)^2)^{0.5} -\\
   &(s_4s_7-s_5c_4c_7)(d_3+r_F(s_4s_7-s_5c_4c_7)/(c_4^2c_5^2+
   (s_4s_7-s_5c_4c_7)^2)^{0.5})

I define pitch, :math:`q_6`, as the dependent coordinate. The choice of pitch
has some to do with the fact that for "normal" bicycle configurations, pitch is
practically constant. This is not universal and it may be smart to choose the
dependent coordinate differently for other cases. The constraint equation can
actually be formulated into a quartic in the sine of the pitch [Psiaki1979]_,
[Peterson2007]_ which does have an, albeit lengthy, analytic solution. I do not
opt for the analytical solution, so care is needed when simulating and
linearizing to properly take care of this dependent coordinate.

Kinematical Differential Equations
----------------------------------

The choice of generalized speeds can significantly reduce the length of the
equations of motion [Mitiguy1996]_. This is beneficial for both working with
the analytical forms of the equations of motion and the efficiency in
computation. I did not spend much effort in selecting optimal generalized
speeds, as the analytical form of the equations of motion of this system would
be difficult to interpret regardless of the choice and because computational speed
was of little concern. For :math:`i=1,\dotsc,8` I simply choose the generalized
speeds to be equal to the time derivatives of the generalized coordinates:

.. math::
   :label: generlizedSpeeds

   u_i = \dot{q}_i

Velocity
--------

The angular and linear velocities of each rigid body are required for computing
the partial velocities used in Kane's method. Also, the velocities of the
points on the wheel at the ground contact points are needed for the
development of the nonholomic constraints. The angular velocity of the rear
frame, :math:`C`, in :math:`N` is:

.. math::
   :label: omegaCinN

   ^N\omega^C = (c_5u_4-s_5c_4u_3)\hat{c}_1 + (u_5+s_4u_3)\hat{c}_2 +
   (s_5u_4+c_4c_5u_3)\hat{c}_3

Both the front frame and the rear wheel are connected to the bicycle frame by
simple revolute joints, so the angular velocities are simply:

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

   ^N\omega^F = ^N\omega^C + ^C\omega^E + ^E\omega^F

   ^F\omega^N =
   &(s_7c_8u_5-s_8u_7-(s_5s_8-c_5c_7c_8)u_4-
   (s_8c_4c_5-c_8(s_4s_7-s_5c_4c_7))u_3)\hat{f}_1 + \\
   &(u_8+c_7u_5+(s_4c_7+s_5s_7c_4)u_3-s_7c_5u_4)\hat{f}_2 + \\
   &(c_8u_7+s_7s_8u_5+(s_5c_8+s_8c_5c_7)u_4+
   (c_4c_5c_8+s_8(s_4s_7-s_5c_4c_7))u_3)\hat{f}_3

Using the angular velocities and the position vectors the velocities of the
mass centers can be computed. Starting with mass center of the rear wheel:

.. math::
   :label: DoInN

   ^N\bar{v}^{d_o} = \frac{d}{dt}\left(\bar{r}^{d_o/n_o}\right)

   ^N\bar{v}^{d_o} = u_1\hat{n}_1 + u_2\hat{n}_2 -
   r_Rs_4u_3\hat{b}_1 + r_Ru_4\hat{b}_2

The remaining velocities can be computed by taking advantage of the fact that
various pairs of points are fixed on the same rigid body. The mass centers of
the rear wheel, :math:`d_o` and the rear frame, :math:`c_o`, and the steer axis
point, :math:`c_e`, all lie on the rear frame.

.. math::
   :label: CoInN

   ^N\bar{v}^{c_o} = ^N\bar{v}^{d_o} + ^N\bar\omega^C\times\bar{r}^{c_o/d_o}

   ^N\bar\omega^C\times\bar{r}^{c_o/d_o} =
   l_2(u_5+s_4u_3)\hat{c}_1 +
   (l_1(s_5u_4+c_4c_5u_3)-l_2(c_5u_4-s_5c_4u_3))\hat{c}_2 -
   l_1(u_5+s_4u_3)\hat{c}_3

.. math::
   :label: CeInN

   ^N\bar{v}^{c_e} = ^N\bar{v}^{d_o} + ^N\bar\omega^C\times\bar{r}^{c_e/d_o}

   ^N\bar\omega^C\times\bar{r}^{c_e/d_o} = d_1(s_5u_4+c_4c_5u_3)\hat{c}_2 -
   d_1(u_5+s_4u_3)\hat{c}_3

The velocity of the front wheel mass center is computed with respect to the
steer axis point as they both lie on the front frame:

.. math::
   :label: FoInN

   ^N\bar{v}^{f_o} = ^N\bar{v}^{c_e} + ^N\bar\omega^E\times\bar{r}^{f_o/c_e}

   ^N\bar\omega^E\times\bar{r}^{f_o/c_e} =
   &-d_2(s_7c_5u_4-c_7u_5-(s_4c_7+s_5s_7c_4)u_3)\hat{e}_1 + \\
   &(d_3(u_7+s_5u_4+c_4c_5u_3)-d_2(s_7u_5+c_5c_7u_4+
   (s_4s_7-s_5c_4c_7)u_3))\hat{e}_2 + \\
   &d_3(s_7c_5u_4-c_7u_5-(s_4c_7+s_5s_7c_4)u_3)\hat{e}_3

Then the velocity of the front frame mass center is similarly:

.. math::
   :label: EoInN

   ^N\bar{v}^{e_o} = ^N\bar{v}^{f_o} + ^N\omega^E\times\bar{r}^{e_o/f_o}

   ^N\omega^E\times\bar{r}^{e_o/f_o} =
   &-l_4(s_7c_5u_4-c_7u_5-(s_4c_7+s_5s_7c_4)u_3)\hat{e}_1 +\\
   &(l_3(u_7+s_5u_4+c_4c_5u_3)-l_4(s_7u_5+c_5c_7u_4+(s_4s_7-s_5c_4c_7)u_3))\hat{e}_2 +\\
   &l_3(s_7c_5u_4-c_7u_5-(s_4c_7+s_5s_7c_4)u_3)\hat{e}_3

The velocity of the contact points on the wheel are needed to enforce the
no-slip condition and can be computed with respect to the rear and front wheel
centers. The rear contact point is:

.. math::
   :label: DnInN

   ^N\bar{v}^{d_n} = ^N\bar{v}^{d_o} + ^N\omega^D\times\bar{r}^{d_n/d_o}

   ^N\omega^D\times\bar{r}^{d_n/d_o} = r_R(u_5+u_6+s_4u_3)\hat{b}_1 - r_Ru_4\hat{b}_2

which simplifies to:

.. math::
   :label: SimpleDnInN

   ^N\bar{v}^{d_n} = r_R(u_5+u_6)\hat{b}_1 + u_1\hat{n}_1 + u_2\hat{n}_2

The front wheel contact velocity is:

.. math::
   :label: FnInN

   ^N\bar{v}^{f_n} = ^N\bar{v}^{f_o} + ^N\omega^F\times\bar{r}^{f_n/f_o}

   ^N\omega^F\times\bar{r}^{f_n/f_o} =
   &-r_Fc_4c_5(s_7c_5u_4-u_8-c_7u_5-(s_4c_7+s_5s_7c_4)u_3)/(c_4^2c_5^2+
   (s_4s_7-s_5c_4c_7)^2)^{0.5}\hat{e}_1 - \\
   &r_F(c_4c_7u_4+s_7c_4c_5u_5-s_4s_5s_7u_4-(s_4s_7-s_5c_4c_7)u_7)/(c_4^2c_5^2+
   (s_4s_7-s_5c_4c_7)^2)^{0.5}\hat{e}_2 + \\
   &r_F(s_4s_7-s_5c_4c_7)(s_7c_5u_4-u_8-c_7u_5-(s_4c_7+
   s_5s_7c_4)u_3)/(c_4^2c_5^2+(s_4s_7-s_5c_4c_7)^2)^{0.5}\hat{e}_3

Acceleration
------------

The angular acceleration of each body along with the linear acceleration of
each mass center are required to form :math:`F_r^*` in Kane's equations. The
angular acceleration of the bicycle reference frame in :math:`N` is:

.. math::
   :label: alphaCinN

   ^N\bar{\alpha}^C =
   &(s_4s_5u_3u_4+c_5\dot{u}_4-s_5u_4u_5-c_4c_5u_3u_5-s_5c_4\dot{u}_3)\hat{c}_1 + \\
   &(c_4u_3u_4+\dot{u}_5+s_4\dot{u}_3)\hat{c}_2 +\\
   &(c_5u_4u_5+s_5\dot{u}_4+c_4c_5\dot{u}_3-s_4c_5u_3u_4-s_5c_4u_3u_5)\hat{c}_3

The remaing bodies' angular accelerations follow from simple rotations:

.. math::
   :label: alphaDinC

   ^C\bar{\alpha}^D = \dot{u}_6\hat{c}_2

.. math::
   :label: alphaEinC

   ^C\bar{\alpha}^E = \dot{u}_7\hat{c}_3

.. math::
   :label: alphaFinE

   ^E\bar{\alpha}^F = \dot{u}_8\hat{e}_2

The linear acceleration of each mass center can then be computed. The
acceleration of the rear wheel center of mass is:

.. math::
   :label: aDoInN

   ^N\bar{a}^{d_o} = \frac{d}{dt}\left(^N\bar{v}^{d_o}\right)

   ^N\bar{a}^{d_o} = \dot{u}_1\hat{n}_1 + \dot{u}_2\hat{n}_2 -
   r_Rs_4u_3^2\hat{a}_2 - r_R(2c_4u_3u_4+s_4\dot{u}_3)\hat{b}_1 +
   r_R\dot{u}_4\hat{b}_2 + r_Ru_4^2\hat{b}_3

The remaining accelerations are computed using the anagolous two point relationship
utilized for the velocities. The acceleration of the rear frame center of mass
is:

.. math::
   :label: aCoinN

   ^N\bar{a}^{c_o} = ^N\bar{a}^{d_o} +
   ^N\omega^C\times(^N\omega^C\times\bar{r}^{c_o/d_o}) +
   ^N\bar{\alpha}^C\times\bar{r}^{c_o/d_o}

   ^N\omega^C\times(^N\omega^C\times\bar{r}^{c_o/d_o}) =
   &(-l_1(u_5+s_4u_3)^2-(s_5u_4+c_4c_5u_3)(l_1(s_5u_4+c_4c_5u_3)-l_2(c_5u_4-s_5c_4u_3)))\hat{c}_1 +\\
   &(u_5+s_4u_3)(l_2(s_5u_4+c_4c_5u_3)+l_1(c_5u_4-s_5c_4u_3))\hat{c}_2 + \\
   &((c_5u_4-s_5c_4u_3)(l_1(s_5u_4+c_4c_5u_3)-l_2(c_5u_4-s_5c_4u_3))-l_2(u_5+s_4u_3)^2)\hat{c}_3

   ^N\bar{\alpha}^C\times\bar{r}^{c_o/d_o} =
   &l_2(c_4u_3u_4+\dot{u}_5+s_4\dot{u}_3)\hat{c}_1 + \\
   &(-l_1(s_4c_5u_3u_4+s_5c_4u_3u_5-c_5u_4u_5-s_5\dot{u}_4-c_4c_5\dot{u}_3)-\\
   &l_2(s_4s_5u_3u_4+c_5\dot{u}_4-s_5u_4u_5-c_4c_5u_3u_5-s_5c_4\dot{u}_3))\hat{c}_2 - \\
   &l_1(c_4u_3u_4+\dot{u}_5+s_4\dot{u}_3)\hat{c}_3

The acceleration of the steer axis point is:

.. math::
   :label: aCeInN

   ^N\bar{a}^{c_e} = ^N\bar{a}^{d_o} +
   ^N\omega^C\times(^N\omega^C\times\bar{r}^{c_e/d_o}) +
   ^N\bar{\alpha}^C\times\bar{r}^{c_e/d_o}

   ^N\omega^C\times(^N\omega^C\times\bar{r}^{c_e/d_o}) =
   &-d_1((u_5+s_4u_3)^2+(s_5u_4+c_4c_5u_3)^2)\hat{c}_1 + \\
   &d_1(u_5+s_4u_3)(c_5u_4-s_5c_4u_3)\hat{c}_2 +\\
   &d_1(s_5u_4+c_4c_5u_3)(c_5u_4-s_5c_4u_3)\hat{c}_3

   ^N\bar{\alpha}^C\times\bar{r}^{c_e/d_o} =
   &-d_1(s_4c_5u_3u_4+s_5c_4u_3u_5-c_5u_4u_5-
   s_5\dot{u}_4-c_4c_5\dot{u}_3)\hat{c}_2 - \\
   &d_1(c_4u_3u_4+\dot{u}_5+s_4\dot{u}_3)\hat{c}_3

The acceleration of the front wheel center of mass is:

.. math::
   :label: aFoInN

   ^N\bar{a}^{f_o} = ^N\bar{a}^{c_e} +
   ^N\omega^E\times(^N\omega^E\times\bar{r}^{f_o/c_e}) +
   ^N\bar{\alpha}^E\times\bar{r}^{f_o/c_e}

   ^N\omega^E\times(^N\omega^E\times\bar{r}^{f_o/c_e}) =
   &(-d_3(s_7c_5u_4-c_7u_5-(s_4c_7+s_5s_7c_4)u_3)^2-
   (u_7+s_5u_4+c_4c_5u_3)(d_3(u_7+s_5u_4+c_4c_5u_3)-\\
   &d_2(s_7u_5+c_5c_7u_4+(s_4s_7-s_5c_4c_7)u_3)))\hat{e}_1 - \\
   &(s_7c_5u_4-c_7u_5-(s_4c_7+s_5s_7c_4)u_3)(d_2(u_7+s_5u_4+c_4c_5u_3)+
   d_3(s_7u_5+c_5c_7u_4+(s_4s_7-s_5c_4c_7)u_3))\hat{e}_2 + \\
   &((s_7u_5+c_5c_7u_4+(s_4s_7-s_5c_4c_7)u_3)(d_3(u_7+s_5u_4+c_4c_5u_3)-
   d_2(s_7u_5+c_5c_7u_4+(s_4s_7-s_5c_4c_7)u_3))-\\
   &d_2(s_7c_5u_4-c_7u_5-(s_4c_7+s_5s_7c_4)u_3)^2)\hat{e}_3

   ^N\bar{\alpha}^E\times\bar{r}^{f_o/c_e} =
   & -d_2(s_7u_5u_7+c_5c_7u_4u_7+u_3(s_4s_7u_7+s_4s_5s_7u_4-c_4c_7u_4-
   s_5c_4c_7u_7-s_7c_4c_5u_5)+s_7c_5\dot{u}_4-s_5s_7u_4u_5-\\
   & c_7\dot{u}_5-(s_4c_7+s_5s_7c_4)\dot{u}_3)\hat{e}_1 + \\
   & (d_2(s_5c_7u_4u_5+s_7c_5u_4u_7-c_7u_5u_7-
   u_3(s_4c_7u_7+s_7c_4u_4+s_4s_5c_7u_4+s_5s_7c_4u_7-c_4c_5c_7u_5)-
   s_7\dot{u}_5-\\
   & c_5c_7\dot{u}_4-(s_4s_7-s_5c_4c_7)\dot{u}_3)-
   d_3(s_4c_5u_3u_4+s_5c_4u_3u_5-c_5u_4u_5-\dot{u}_7-
   s_5\dot{u}_4-c_4c_5\dot{u}_3))\hat{e}_2 + \\
   & d_3(s_7u_5u_7+c_5c_7u_4u_7+u_3(s_4s_7u_7+s_4s_5s_7u_4-c_4c_7u_4-
   s_5c_4c_7u_7-s_7c_4c_5u_5)+s_7c_5\dot{u}_4-s_5s_7u_4u_5-\\
   &c_7\dot{u}_5-(s_4c_7+s_5s_7c_4)\dot{u}_3)\hat{e}_3

The acceleration of the front frame center of mass is:

.. math::
   :label: aEoInN

   ^N\bar{a}^{e_o} = ^N\bar{a}^{f_o} +
   ^N\omega^E\times(^N\omega^E\times\bar{r}^{e_o/f_o}) +
   ^N\bar{\alpha}^E\times\bar{r}^{e_o/f_o}

   ^N\omega^E\times(^N\omega^E\times\bar{r}^{e_o/f_o}) =
   &(-(d_3+l_3)(s_7c_5u_4-c_7u_5-(s_4c_7+s_5s_7c_4)u_3)^2-(u_7+s_5u_4+
   c_4c_5u_3)((d_3+l_3)(u_7+s_5u_4+c_4c_5u_3)-\\
   &d_2(s_7u_5+c_5c_7u_4+(s_4s_7-s_5c_4c_7)u_3)-l_4(s_7u_5+c_5c_7u_4+
   (s_4s_7-s_5c_4c_7)u_3)))\hat{e}_1 - \\
   &(s_7c_5u_4-c_7u_5-(s_4c_7+s_5s_7c_4)u_3)((d_2+l_4)(u_7+s_5u_4+
   c_4c_5u_3)+\\
   &(d_3+l_3)(s_7u_5+c_5c_7u_4+(s_4s_7-s_5c_4c_7)u_3))\hat{e}_2+ \\
   &((s_7u_5+c_5c_7u_4+(s_4s_7-s_5c_4c_7)u_3)((d_3+l_3)(u_7+s_5u_4+
   c_4c_5u_3)-d_2(s_7u_5+c_5c_7u_4+(s_4s_7-s_5c_4c_7)u_3)-\\
   &l_4(s_7u_5+c_5c_7u_4+(s_4s_7-s_5c_4c_7)u_3))-(d_2+l_4)(s_7c_5u_4-
   c_7u_5-(s_4c_7+s_5s_7c_4)u_3)^2)\hat{e}_3

   ^N\bar{\alpha}^E\times\bar{r}^{e_o/f_o} =
   & -(d_2+l_4)(s_7u_5u_7+c_5c_7u_4u_7+u_3(s_4s_7u_7+s_4s_5s_7u_4-c_4c_7u_4-
   s_5c_4c_7u_7-s_7c_4c_5u_5)+s_7c_5\dot{u}_4-\\
   & s_5s_7u_4u_5-c_7\dot{u}_5-
   (s_4c_7+s_5s_7c_4)\dot{u}_3)\hat{e}_1+ \\
   & (d_2(s_5c_7u_4u_5+s_7c_5u_4u_7-c_7u_5u_7-u_3(s_4c_7u_7+s_7c_4u_4+
   s_4s_5c_7u_4+s_5s_7c_4u_7-c_4c_5c_7u_5)-s_7\dot{u}_5-\\
   & c_5c_7\dot{u}_4-
   (s_4s_7-s_5c_4c_7)\dot{u}_3)+l_4(s_5c_7u_4u_5+s_7c_5u_4u_7-c_7u_5u_7-\\
   & u_3(s_4c_7u_7+s_7c_4u_4+s_4s_5c_7u_4+s_5s_7c_4u_7-c_4c_5c_7u_5)-
   s_7\dot{u}_5-\\
   & c_5c_7\dot{u}_4-(s_4s_7-s_5c_4c_7)\dot{u}_3)-
   (d_3+l_3)(s_4c_5u_3u_4+s_5c_4u_3u_5-c_5u_4u_5-\dot{u}_7-s_5\dot{u}_4-
   c_4c_5\dot{u}_3))\hat{e}_2 + \\
   & (d_3+l_3)(s_7u_5u_7+c_5c_7u_4u_7+u_3(s_4s_7u_7+s_4s_5s_7u_4-c_4c_7u_4-
   s_5c_4c_7u_7-s_7c_4c_5u_5)+s_7c_5\dot{u}_4-\\
   & s_5s_7u_4u_5-c_7\dot{u}_5-
   (s_4c_7+s_5s_7c_4)\dot{u}_3)\hat{e}_3

.. _nonholonomic:

Motion Constraints
------------------

I make use of motion constraints to reduce the locally achievable configuration
space from eight degrees of freedom to three. The first four constraints are
introduced to enforce the pure rolling, no side-slip, contact of the knife-edge
wheels with the ground plane and are non-holonomic. This sets the components of
velocity of the contact points on the wheels in the :math:`\hat{a}_1` and
:math:`\hat{a}_2` directions equal to zero, producing the following
relationships:

.. math::
   :label: eqNonholonomic1

   ^N\bar{v}^{d_n}\cdot\hat{a}_1 = s_3u_2 + c_3u_1 + r_R(u_5+u_6) = 0

.. math::
   :label: eqNonholonomic2

   ^N\bar{v}^{d_n}\cdot\hat{a}_2 = c_3u_2 - s_3u_1 = 0

.. math::
   :label: eqNonholonomic3

   ^N\bar{v}^{f_n}\cdot\hat{a}_1 =
   &s_3u_2 + c_3u_1 + d_2c_5u_5 + d_2s_4c_5u_3 + r_Fc_4c_7(u_8+c_7u_5+
   (s_4c_7+s_5s_7c_4)u_3)/(c_4^2c_5^2+(s_4s_7-s_5c_4c_7)^2)^{0.5} -\\
   &r_Rs_4u_3 - d_3s_7c_4u_3 - d_1s_5(u_5+s_4u_3) - s_7c_5(d_3u_7-
   r_F(s_7c_4c_5u_5-(s_4s_7-s_5c_4c_7)u_7)/(c_4^2c_5^2+(s_4s_7-s_5c_4c_7)^2)^{0.5}) - \\
   &s_5(d_3c_7(u_5+s_4u_3)+r_Fs_4s_7(u_8+c_7u_5+(s_4c_7+
   s_5s_7c_4)u_3)/(c_4^2c_5^2+(s_4s_7-s_5c_4c_7)^2)^{0.5}) = 0

.. math::
   :label: eqNonholonomic4

   ^N\bar{v}^{f_n}\cdot\hat{a}_2 =
   &c_3u_2 + d_1c_5u_3 + r_Rc_4u_4 + d_1s_4c_5u_5 + d_1s_5c_4u_4 +
   (c_4c_7-s_4s_5s_7)(d_3(u_7+s_5u_4+c_4c_5u_3)-\\
   &d_2(s_7u_5+c_5c_7u_4+(s_4s_7-s_5c_4c_7)u_3)-r_F(c_4c_7u_4+
   s_7c_4c_5u_5-s_4s_5s_7u_4-(s_4s_7-s_5c_4c_7)u_7)/(c_4^2c_5^2+(s_4s_7-s_5c_4c_7)^2)^{0.5}) - \\
   &s_3u_1 - (s_7c_4+s_4s_5c_7)(d_2(s_7c_5u_4-c_7u_5-(s_4c_7+s_5s_7c_4)u_3)+\\
   &r_Fc_4c_5(s_7c_5u_4-u_8-c_7u_5-(s_4c_7+s_5s_7c_4)u_3)/(c_4^2c_5^2+(s_4s_7-s_5c_4c_7)^2)^{0.5}) - \\
   &s_4c_5(d_3(s_7c_5u_4-c_7u_5-(s_4c_7+s_5s_7c_4)u_3)+r_F(s_4s_7-
   s_5c_4c_7)(s_7c_5u_4-u_8-c_7u_5-(s_4c_7+s_5s_7c_4)u_3)/(c_4^2c_5^2+(s_4s_7-s_5c_4c_7)^2)^{0.5}) = 0

The fifth motion constraint is used to manage the constraint on the velocities
imposed by the holonomic constraint, Equation :eq:`holonomicConstraint`. By
differentiating the holonomic constraint equation you arrive at an equation
that is linear in the generalized speeds and can be treated as any other motion
constraint:

.. math::

   \frac{d}{dt}(\bar{r}^{G_n/d_n}\cdot\hat{a}_3) =
   &r_Rs_4u_4 + d_1s_4s_5u_4 + (d_3+r_F(s_4s_7-s_5c_4c_7)/(c_4^2c_5^2+
   (s_4s_7-s_5c_4c_7)^2)^{0.5})\\
   &(s_4c_7u_7+s_7c_4u_4+s_4s_5c_7u_4+s_5s_7c_4u_7-c_4c_5c_7u_5) -
   d_1c_4c_5u_5 - \\
   &d_2s_4c_5u_4 -d_2s_5c_4u_5 -
   r_Fc_4c_5(s_4c_4^2c_5^3u_4+s_5c_4^3c_5^2u_5+\\
   &(s_4s_7-s_5c_4c_7)^2(s_4c_5u_4+s_5c_4u_5))/(c_4^2c_5^2+(s_4s_7-s_5c_4c_7)^2)^{1.5} = 0

These five equations are linear in the eight generalized speeds. Following
convention, I chose the roll rate, :math:`u_4`, the rear wheel rate,
:math:`u_6`, and steer rate, :math:`u_7`, as my independent generalized speeds.

I now find the solution for the dependent speeds as a function of the
independent speeds by solving the linear system of equations and differentiate
the resulting equations to find the dependent :math:`\dot{u}`'s. The dependent
speeds take this form:

.. math::
   :label: eqDependentSpeeds

   u_1 = f(u_4, u_6, u_7, q_3, \ldots, q_8)

   u_2 = f(u_4, u_6, u_7, q_3, \ldots, q_8)

   u_3 = f(u_4, u_6, u_7, q_4, \ldots, q_8)

   u_5 = f(u_4, u_7, q_4, \ldots, q_8)

   u_8 = f(u_4, u_6, u_7, q_4, \ldots, q_8)

At this point, the equations becomes analytically long and it is not
necessarily trivial to reduce the length of the equations from this point on.
A smarter choice of generalized speeds could certainly help, but I did not
spend any effort to search for a good set. From this point on in the
derivation, I will not show the analytical results of the equations of motion,
but will only walk through the remainder of the theory, as all of the building
blocks are in place to derive the equations with Kane's method (or any other
method). I highly recommend the use of computer aided algebra to continue on,
but the die-hard could certainly write them by hand. You will have to either run
my computer code to get the equations or write your own.

Generalized Active Forces
-------------------------

The three equations for the non-holomonic generalized active forces,
:math:`\tilde{F}_r` can now be formed. For our four body system with three
degrees of freedom, :math:`r=4,6,7`, they take the form:

.. math::

   \tilde{F}_r = (\tilde{F}_r)_C + (\tilde{F}_r)_D + (\tilde{F}_r)_E +
   (\tilde{F}_r)_F

   (\bar{F}_r)_X= ^N\bar{V}^{x_o}_r\cdot\bar{R}^{x_o} +
   ^N\bar{\omega}^X_r\cdot\bar{T}^X

where :math:`^N\bar{V}_r^{x_o}` is the partial velocity of the mass center with
respect to the generalized speed :math:`u_r`, :math:`\bar{R}^{x_o}` is the
resultant forces on the mass center (excluding non-contributing forces),
:math:`^N\bar{\omega}_r^X` is the partial angular velocity of the body with
respect to :math:`u_r`, and :math:`\bar{T}^X` is the resultant torques on the
body where :math:`X` is one of the four bodies. The partial velocities are
simply partial derivate of the velocities in question with respect to the
generalized speeds and can be found systematically as usual [Kane1985]_.We
assume that the only force acting on the system is the gravitational force,
:math:`g`. The forces and torques are as follows, thus:

.. math::

  \bar{R}^{c_o} = m_Cg\hat{n}_3

  \bar{R}^{d_o} = m_Dg\hat{n}_3

  \bar{R}^{e_o} = m_Eg\hat{n}_3

  \bar{R}^{f_o} = m_Fg\hat{n}_3

We also assume that there are three generalized active torques acting on the
system which correspond to the three independent generalized speeds found
in :ref:`nonholonomic`.

The roll torque, :math:`T_4`, acts between the rear frame and the Newtonian
frame about :math:`\hat{a}_1`. The rear wheel torque, :math:`T_6`, acts between
the rear frame and the rear wheel about :math:`\hat{c}_2` and the steer torque,
:math:`T_7`, acts between the rear frame and the front frame about
:math:`\hat{c}_3`.

.. math::

   \bar{T}^C = T_4\hat{a}_1-T_6\hat{c}_2-T_7\hat{c}_3

   \bar{T}^D = T_6\hat{c}_2

   \bar{T}^E = T_7\hat{c}_3

   \bar{T}^F = 0

Generalized Inertia Forces
--------------------------

The non-holonomic generalized inertia forces, :math:`\tilde{F}^*_r`, are formed
using the accelerations and the inertial properties of the bodies.

.. math::

   \tilde{F}^*_r = (\tilde{F}^*_r)_C + (\tilde{F}^*_r)_D + (\tilde{F}^*_r)_E +
   (\tilde{F}^*_r)_F

   (\bar{F}^*_r)_X= ^N\bar{V}^{X_o}_r\cdot\bar{R}^*_{X_o} +
   ^N\bar{\omega}^X_r\cdot\bar{T}^*_X

where :math:`^N\bar{V}_r^{x_o}` is once again the partial velocity of the mass
center with respect to the generalized speed :math:`u_r`,
:math:`\bar{R}^*_{x_o}` is the inertia force for :math:`X` in :math:`N` and is
defined as:

.. math::

   \bar{R}^*_{x_o} = -m_X^N\bar{a}^{x_o}

The mass of each rigid body is defined as a constant: :math:`m_C`, :math:`m_D`,
:math:`m_E` and :math:`m_F`.

:math:`^N\bar{\omega}_r^X` is the partial angular velocity of the body with
respect to :math:`u_r`, and :math:`\bar{T}^*_X` is the inertia torque on the
body which is defined as:

.. math::

   \bar{T}^*_X =
   -(^N\bar{\alpha}^X\cdot I_X+^N\bar{\omega}^X\times I_X\cdot\bar{\omega}^X

:math:`I_X` is the central inertia dyadic for the body in question which
corresponds to the following tensor definitions for the inertia of each rigid
body. The inertia tensor for each body is defined with respect to the mass
center and the body's local reference frame. The bicycle wheels are assumed to
be symmetric about both their 1-3 and 1-2 planes.

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

The rear frame and front frame are assumed to be symmetric about their 1-3 planes.

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

Dynamical Equations of Motion
-----------------------------

Kane's equations are now formed as:

.. math::

   \tilde{F}_r + \tilde{F}^*_r = 0

and are a vector function of three coupled equations which are linear in the
roll, steer and rear wheel accelerations. The linear system can be solved to
give the first order equations for :math:`\dot{u}_r`, where :math:`r=4,6,7`.
These can then be  paired with the essential kinematical differential equations
to form the complete set of dynamics equations of motion in the form.

.. math::

   \dot{u}_i=f(u_4, u_6, u_7, q_4, q_5, q_7)

   \dot{q}_j=u_j

where :math:`i=4,6,7` and :math:`j=4,5,6,7`. Keep in mind that the pitch angle,
:math:`q_5`, is in fact a dependent coordinate, :math:`f(q_4,q_7)`, that I
selected when dealing with the holonomic contraint, :eq:`holonomic`. Special
attention during simulation and linearization will have to be made to
accommodate the coordinate and will be described in the following sections.

Model discussion
----------------

[Astrom2006]_, [Meijaard2007]_, [BasuMandal2007]_, [Sharp2008]_, and many
others do excellent job describing the essential nature of both the nonlinear
Whipple model and various linearized models. Notable concepts include the fact
that many of the coordinates are ignorable, that is they do not show up in the
essential dynamical equations of motion. These are the location of the ground
contact point, :math:`q_1` and :math:`q_2`, the yaw angle, :math:`q_3`, and the
wheel angles, :math:`q_6` and :math:`q_8`. The model is also energy conserving,
because the contact points do no work. When linearized about the nominal
configuration at various constant forward speeds the open loop model (i.e.
inputs equal zero) can exhibit stability within various speed regimes. The
system can have left half plane zeros, which give a non-minimal phase behavior.
This corroborates what bicycle riders already experience with counter-steering.

.. todo:: Should I add more interesting facts about the model?

Simulation
----------

The nonlinear model can be simulated with various initial conditions. In the
presented formulation all of the initial conditions can be set independently
except for the roll, steer and pitch angles. Once two of the three are chosen,
the third must be solved for. I typically chose a steer and roll angle and then
solve the holonomic constraint equation numerically for pitch angle,
:math:`q_5`, to provide the correct initial condition. Figure :ref:`figFigFour`
is an example open loop simulation of the nonlinear model.

.. _figFigFour:

.. figure:: figures/eom/meijaard2007-figure-four.png
   :width: 3in
   :align: center

   figFigFour

   This is a reproduction of Figure 4 in [Meijaard2007]_. The model
   demonstrates stability. It also shows the energy conserving nature of the
   non-linear model (i.e. the forward speed settles on a higher value that the
   initial speed as the energy used to dissipate the roll and steer is
   transferred to the forward speed.

Nonlinear Validation
--------------------

Complex dynamical models are often very difficult to validate against one
another due to complexity of large analytical expressions which were
potentially formed by different methods. The now common method of validation is
to evaluate equations numerically for non-trivial inputs and compare the
results to high precision. These type of benchmark numerical sets are
invaluable so that researchers can work from the same baseline and  because
they allow for scientific reproducibility and error checking.

[BasuMandall2007]_ present the non-linear Whipple model derived with both the
Newton-Euler and Lagrange methods, along with a numerical benchmark. Table 1 in
their paper gives the derivatives of all the coordinates and speeds to high
precision for both of their derivations at a single state. They state that if
one can compute the values to machine precision to ~10 significant figures the
models can be concluded to be the same. The very first model I developed
in 2006 would not have held up to this test. I owe the validity of my model to
my labmate, Luke, as his persistence and interest in minute detail helped me
bring my model up to par.

The Basu-Mandal et al derivations are based on different coordinates than I
use, but regardless of the coordinates they provide numerical values which can
be benchmarked if the correct coordinate transformations are applied [#]_. In
Table :ref:`tabNonLinValidation` I present the values computed from my model in
comparison to the values presented by [BasuMandall2007]_. I've presented the
same number of significant digits as provided by Basu-Mandall for each
variable [#]_. My model produces the same result to at least eleven significant
figures, thus I feel confident that the derivation is correct.

.. _tabNonLinValidation:

.. include:: tables/eom/nonlin.rst

Linearized Equations of Motion
==============================

The nonlinear equations of motion can be linearized about various equilibrium
points.  The bicycle has many equilibrium points, the typical one studied is
about the nominal configuration [Meijaard2007]_ but their are many others such
as steady turns [BasuMandal2007]_. The equations can be linearized by computing
the Taylor series expansion of the nonlinear equations of motion about the
equilibrium point and disregarding the terms higher than first order. For the
nominal configuration this amounts to calculating the Jacobian of the system of
equations with respect to the coordinates, speeds and inputs to obtain state
matrix, :math:`\mathbf{A}`, and the input matrix, :math:`\mathbf{B}`. The
output, :math:`\mathbf{C}`, and feed-forward, :math:`\mathbf{D}`,  matrices are
computed in the same fashion except with regards to the nonlinear equations of
the outputs. The partial derivatives of each equation were evaluated at the
following fixed point: :math:`q_i=0` where :math:`i=4,5,7`, :math:`u_i=0` where
:math:`i=4,7`, and :math:`u_5=-v/r_R` where :math:`v` is the constant forward
speed of the bicycle. Care has to be taken when linearizing as :math:`q_5` is a
dependent coordinate which still appears on the right hand side of the
equations. In general the chain rule applies, but for the nominal
configuration, the extra derivatives also equal zero. The linearization
transforms the system to four linear first order differential equations in the
form:

.. math::
   :label: eqStateSpace

   \begin{bmatrix}
     \dot{q_4}\\
     \dot{q_7}\\
     \dot{u_4}\\
     \dot{u_7}
   \end{bmatrix}
   = \mathbf{A}
   \begin{bmatrix}
     q_4\\
     q_7\\
     u_4\\
     u_7
   \end{bmatrix}
   + \mathbf{B}
   \begin{bmatrix}
     T_4\\
     T_7
   \end{bmatrix}

I calculate the equations symbolically to reach the same results as presented
in [Meijaard2007]_, but my equations are much lengthier as the simplification
routines available for the derivatives of the full nonlinear equations didn't
provide much reprise. [Meijaard2007]_ assumes linearity in their derivation
from the start and avoids much of the simplification issue. The accuracy of the
linearized model was checked by comparing numerical results the benchmark
bicycle in two ways. First the linearized equations of motion, Equation
:eq:`eqStateSpace`, were formulated into two second order differential
equations in the canonical form (Equation :eq:`eqCanonical`) presented in
[Meijaard2007]_. They present the values for the coefficient matrices
(:math:`\mathbf{M}`, :math:`\mathbf{C}_1`, :math:`\mathbf{K}_0` and
:math:`\mathbf{K}_2`) for the benchmark parameter set to at least 13
significant figures and the linearization presented here matched all of the
significant figures. [Meijaard2007]_ also provide the eigenvalues of the state
matrix at various speeds. Table :ref:`tabLinCompare` shows the eigenvalues
computed at 5 m/s in comparison to the values in Table 2 of [Meijaard2007]_
where my model matches to at least 13 significant figures.

.. math::
   :label: eqCanonical

   \mathbf{M\dot{u}}+v\mathbf{C}_1\mathbf{u}+\left[g\mathbf{K}_0+
   v^2\mathbf{K}_2\right]\mathbf{q}=0

.. _tabLinCompare:

.. include:: tables/eom/linear-compare.rst

It is useful to plot the root loci with respect to the change in the
equilibrium forward speed to visualize the time constants, damping, frequency
and stability of each of the modes of motion.

.. _figRootLoci:

.. figure:: figures/eom/root-loci-complex.png
   :width: 5in
   :align: center

   figRootLoci

   The root loci with respect to forward speed. The color signifies speed as
   shown in the right side colorbar.

Another way to visualize this is by plotting the eigenvalue components
separately which gives the now ubiquitous eigenvalue plot versus
forward speed. This view clearly shows the stable speed range.

.. figure:: figures/eom/root-loci.png
   :width: 5in
   :align: center

   figEigenvalues

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

For speeds above the bifurcation point, this linear model exhibits three
distinct modes of motion, which have been named weave, capsize and caster. At a
forward speed of 0.5 m/s, all of the eigenvalues are real, with two unstable
and two stable. The eigenvector components help reveal the motion. Notice that
the unstable eigenvalue values predict two modes where the roll and steer
states decay rapidly (i.e. the bicycle falls over).

+---------------------------------------+---------------------------------------+
| .. image:: figures/eom/eVecHalf-1.png | .. image:: figures/eom/eVecHalf-2.png |
+---------------------------------------+---------------------------------------+
| .. image:: figures/eom/eVecHalf-3.png | .. image:: figures/eom/eVecHalf-4.png |
+---------------------------------------+---------------------------------------+

Once the bicycle is brought up to a speed of 3 m/s the two unstable eigenvalues
coalesce into a complex pair. The eigenvector components show that the steer
amplitude is almost twice the roll amplitude and roll angle leads the steer
angle by about 50 degrees. The caster mode, is a rapidly decay in steering and
the capsize mode is a decay in roll and steering, with the roll at about twice
the amplitude as steer.

+----------------------------------------+----------------------------------------+----------------------------------------+
| .. image:: figures/eom/eVecThree-1.png | .. image:: figures/eom/eVecThree-2.png | .. image:: figures/eom/eVecThree-3.png |
+----------------------------------------+----------------------------------------+----------------------------------------+

At 5 m/s the bicycle is stable, and now the weave mode shows that the roll and
steering act more in unison at a somewhat similar amplitude. The caster and
capsize are similar to 3 m/s.

+---------------------------------------+---------------------------------------+---------------------------------------+
| .. image:: figures/eom/eVecFive-1.png | .. image:: figures/eom/eVecFive-2.png | .. image:: figures/eom/eVecFive-3.png |
+---------------------------------------+---------------------------------------+---------------------------------------+

Finally, at 7 m/s the capsize mode goes unstable, with a slow decay in
primarily roll.

+----------------------------------------+----------------------------------------+----------------------------------------+
| .. image:: figures/eom/eVecSeven-1.png | .. image:: figures/eom/eVecSeven-2.png | .. image:: figures/eom/eVecSeven-3.png |
+----------------------------------------+----------------------------------------+----------------------------------------+

The complete motion of the bicycle is a superposition of each mode.

Notation
========

:math:`\lambda`
   The steer axis tilt as defined in [Meijaard2007]_.
:math:`c`
   The trail as defined in [Meijaard2007]_.
:math:`w`
   The wheelbase as defined in [Meijaard2007]_.
:math:`r_F,r_R`
   The front and rear wheel radii as defined in [Meijaard2007]_.
:math:`x_B,z_B,x_H,z_H`
   The global mass center locations of the rear frame and front frame as  defined in [Meijaard2007]_.
:math:`B,R,H,F`
   The rigid bodies as defined in [Meijaard2007]_.
:math:`m_B,m_R,m_H,m_F`
   The mass of each rigid body as defined in [Meijaard2007]_.
:math:`\mathbf{I}_B,\mathbf{I}_R,\mathbf{I}_H,\mathbf{I}_F`
   The global inertia tensor of each rigid body as defined in [Meijaard2007]_.
:math:`A,B,C,D,E,F`
   The reference frames and/or rigid bodies.
:math:`d_1,d_2,d_3`
   The rear and front frame essential geometry.
:math:`l_1,l_2,l_3,l_4`
   The in plane distances to the rear and front frame centers of mass.
:math:`m_C,m_D,m_E,m_F`
   The mass of each rigid body.
:math:`\mathbf{I}_C,\mathbf{I}_D,\mathbf{I}_E,\mathbf{I}_F`
   The local inertia tensor of each rigid body.
:math:`^Y\mathbf{R}^X`
   A rotation matrix of body or reference frame :math:`X` with respect to body
   or reference frame :math:`Y`.
:math:`q_i`
   The generalized coordinates.
:math:`u_i`
   The generalized speeds.
:math:`\hat{x}_1,\hat{x}_2,\hat{x}_3`
   Three orthogonal unit vectors in reference frame :math:`X`.
:math:`x_o`
   The mass center of body :math:`X`.
:math:`c_e`
   A point on the steer axis in both bodies :math:`C` and :math:`E`.
:math:`d_n,f_n`
   The points fixed in the rear and front wheels which are instantaneously in
   contact with the ground.
:math:`\bar{r}^{y_o/x_o}`
   The vector from point :math:`x_o` to point :math:`y_o`.
:math:`^X\omega^Y`
   The angular velocity of frame :math:`Y` in frame :math:`X`.
:math:`^Y\bar{v}^{x_o}`
   The velocity of point :math:`x_o` in reference frame :math:`Y`.
:math:`^X\bar{\alpha}^Y`
   The angular acceleration of frame :math:`Y` in frame :math:`X`.
:math:`^Y\bar{a}^{x_o}`
   The acceleration of point :math:`x_o` in reference frame :math:`Y`.
:math:`s_1,c_1`
   Shorthand notation for :math:`\operatorname{sin}(q_1)` and
   :math:`\operatorname{cos}(q_1)`.
:math:`s_\lambda,c_\lambda`
   Shorthand notation for :math:`\operatorname{sin}(\lambda)` and
   :math:`\operatorname{cos}(\lambda)`.
:math:`\tilde{F}_r`
   The non-holonomic generalized active forces. The subscript :math:`r` denotes
   one of the independent generalized speeds.
:math:`^N\bar{V}_r^{x_o}`
   The partial velocity in reference frame :math:`N` of point :math:`x_o` with
   respect to the :math:`r^{th}` independent generalized speed.
:math:`\bar{R}^{x_o}`
   The resultant forces on the point :math:`x_o`.
:math:`^N\bar{\omega}_r^C`
   The partial angular velocity of reference frame :math:`C` in reference frame
   :math:`N` with respect to the :math:`r^{th}` independent generalized speed.
:math:`\bar{T}^C`
   The resultant torques acting on body :math:`C`.
:math:`\tilde{F}^*_r`
   The non-holonomic generalized inertia forces. The subscript :math:`r` denotes
   one of the independent generalized speeds.
:math:`\bar{R}^*_{x_o}`
   The generalized inertia force of point :math:`x_o`.
:math:`\bar{T}^*_X`
   The generalized inertia torque of body :math:`X`.
:math:`I_X`
   The central inertia dyadic of body :math:`X`.
:math:`\mathbf{A},\mathbf{B},\mathbf{C},\mathbf{D}`
   The state, input, output and feed-forward matrices.
:math:`v`
   The forward speed of the linear bicycle model.
:math:`\mathbf{M},\mathbf{C}_1,\mathbf{K}_0,\mathbf{K}_2`
   The velocity and gravity independent mass, damping and stiffness matrices of
   the linearized Whipple model.

.. rubric:: Footnotes

.. [#] My colleague, Dale L. Peterson, has made significant progress
       formulating the equations of motion in a readable and compact form,
       which will most likely be published soon.

.. [#] The point of contact for the bicycle wheels are technically abstract
       points in dynamics. There are fundamentally four distinct points of
       concern. The first being the point in the ground plane that
       instantaneously contacts the wheel at any given time, the point in the
       ground plane that tracks the contact point in the plane, the point on
       the wheel that instantaneously contacts the ground at any given time,
       and the point on the wheel ...

.. todo::
   Contact points need better explanations.

.. [#] I don't necessarily agree that this is a great standard to follow,
       because it creates much unessary confusion when defining and mapping
       between parameterizations. The three axis pointing upward would be less
       error prone.

.. [#] Luke and I have dreamed of developing an open source version of Autolev
       for years and that has finally culminated through primarily Luke and Gilbert
       Gede's efforts in the creation of sympy.physics.mechanics.

.. [#] This constraint can readily be modified to support a non-flat ground.

.. [#] Basu-Mandall presents significant digits from 10 to 14.

.. [#] The conversion equations from the [BasuMandal2007]_ coordinates to mine and vice
       versa can be found in the source code.
