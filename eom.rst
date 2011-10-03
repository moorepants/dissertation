===========================
Bicycle Equations Of Motion
===========================

As was mentioned in the introduction, the bicycle has been studied by many
scientists over the years. The bicycle is a rich dynamic system that is
difficult to model accurately.  [Meijaard2007]_ did an excellent job of sorting
through 140 years of bicycle dynamics papers and providing a benchmarked
bicycle that finally verified the correct equations of the linearized Whipple
Model [Whipple1899]_. Bicycle-only models can be divided into two main
categories: models that do not exhibit open loop stability and models that do.
All of these models can be extended by adding additional dynamics such as
tire-road interactions, frame flexibility, and human biomechanics. These
extensions can have effects on the stability and control of the bicycle.

Simple Models
-------------

Typically a one degree of freedom model that produces a roll equation of motion
is used to model a bicycle in its most basic form. This model has been derived
and analyzed by many including, but not limited to, [Timoshenko1948]_,
[Karnopp2004]_ and [Astrom2005]_. These models do not have enough fidelity to
predict a real bicycle's uncontrolled motion and do not predict the speed
dependent stability that higher order models can. These models have been used
for control studies [Getz1994,CloydHubbardAlaways1996,Karnopp2004]_ as they
exhibit the non-minimum phase behavior that predicts the necessity of steering
into the roll for stabilization. Controllers based on these models have also
been used on actual experimental control models [Suryanarayanan2002]_. This
type of model will not be used in my studies.

Whipple Model
-------------

The lowest order model that has had some experimental validation
[Kooijman2008]_, is able to predict speed dependent stability and includes a
complete physical description of the four rigid bodies is typically referred to
as the "Whipple Model". This is in honor of Francis J.  W. Whipple, the first
author to publish a correct derivation of the linear equations of motion of
this particular bicycle model [Whipple1899]_.  This model will be used as a
basis for all further studies proposed herein. Many researchers over the past
century have attempted to derive and analyze this model but very few have been
successful. [Meijaard2007]_ give a complete historical review of uncontrolled
bicycle research which made use of the historical comparisons in the thesis by
[Hand1988]_. [Meijaard2007]_ also benchmarked the Whipple Model by deriving the
linearized equations of motion by four independent methods (two independent pen
and paper calculations and two different dynamic software packages).
Furthermore, [Basu-Mandal2007]_ benchmarked various torque free circular
motions in the non-linear case with two additional independent derivations of
the equations of motion. [Kooijman2006]_ has verified by experiment that the
linearized Whipple Model does in fact predict the uncontrolled motion of a
normal bicycle in a speed range of about 3 to 6 m/s.  These papers and my own
derivation of the Whipple Model are the basis for using this model in my
research.

Motorcycle Models
-----------------

The motorcycle is modeled in much the same fashion as the bicycle except that
tire-road interactions and suspension are included.  Also, the human's
biomechanical motions play a smaller role because the motorcycle typically
weighs more than the rider. The most cited models are those developed by Robin
S. Sharp. His first model [Sharp1971]_ includes tire compliance and side slip.
The model has been refined over the years to improve accuracy by adding frame
flexibility, rider models and improving the tire models
[SharpLimebeerGani1999,SharpLimebeer2001,SharpEvangelouLimebeer2004]_.  He was
also the first to give names to the eigenmodes of the Whipple Model
[Sharp1975]_. He and David Limebeer give a review of bicycle and motorcycle
modeling in [LimebeerSharp2006]_ covering much of their work. Other notable
studies include ones developed by [Koenen1983]_ and [CossalterLot2002]_.

Whipple Model
=============

Derivation
----------

The Whipple Model will be the foundation for any extensions we develop. This
section details a brief description of the model derivation using Kane's
method [KaneLevinson1985]_. The Whipple model (Fig. fig:bikeDim) is made up of
four rigid bodies (frame/rider, fork/handlebar and two wheels) connected to
each other by frictionless revolute joints. The wheels contact the ground under
pure rolling and no sideslip conditions. The bicycle is assumed to be laterally
symmetric.

.. todo::
   Figure of the bicycle geometry with caption: The bicycle in the upright no
   steer configuration. The rigid bodies are the rear wheel, C, frame/rider, D,
   fork/handlebar, F and front wheel, G. The geometric parameters are also
   shown.

Four rigid bodies (the rear wheel, C, frame/rider, D, fork/handlebar, F and
front wheel, G), three intermediate reference frames (yaw, A, lean, B and steer
axis, E) and eight generalized coordinates (:math:`q_i`, :math:`i =
1,\ldots,8`) were used to characterize the bicycle configuration
(Fig. fig:genCoord) within the Newtonian reference frame, N. The generalized
coordinates are defined as follows: :math:`q_1` and :math:`q_2` locate the
rear wheel contact point in the ground plane, :math:`q_3` the yaw angle,
:math:`q_4` the lean angle, :math:`q_5` the rotation angle of the rear
wheel relative to the lean frame B, :math:`q_6` the frame pitch angle,
:math:`q_7` the steer angle and :math:`q_8` the rotation of the front wheel.
The wheel contact points for the front and rear wheel are :math:`C_n` and
:math:`G_n`, respectively. The Whipple model is further characterized by a
non-minimum set of physical parameters which include geometry, mass, and
moments of inertia. The geometrical parameters are depicted in Fig. fig:bikeDim
where each body (C, D, F and G) has mass and moment of inertia.

.. todo::
   Diagram of the bicycle showing each generalized coordinate.

A holonomic configuration constraint, arising from the fact that
both wheels must touch the ground, complicates the model
derivation. The constraint (Eq. eq:wheelsTouch) is characterized by
a nonlinear relationship between the lean angle :math:`q_4`,
steer angle :math:`q_7` and pitch angle :math:`q_6`. Pitch,
:math:`q_6`, is taken as the dependent coordinate and the
constraint equation can be formulated into a quartic in the sine of
the pitch [Psiaki1979]_, [Peterson2007]_. To avoid having to
solve the quartic algebraically, the derivative of the constraint
equation is taken.

This produces a velocity constraint equation that is linear in the
derivatives of the pitch angle, steer angle and lean angle
(Eq. eq:pitchVelCon) where :math:`a`, :math:`b` and :math:`c`
are functions of the coordinates and geometric parameters. This
allows an explicit solution for the pitch angular velocity
:math:`u_6`, making it a dependent generalized speed.

.. math::
   \bar{\mathbf[r]_}^{G_n/C_n}\cdot\hat{\mathbf[n]_}_3=f\left(q_4,q_6,q_7\right)=0
   :label: eq:wheelsTouch

.. math::
   \frac[d]_[dt]_\left(\bar{\mathbf[r]_}^{G_n/C_n}\cdot\hat{\mathbf[n]_}_3\right)=a\cdot u_4+b\cdot u_5+c\cdot u_7=0
   :label: {eq:pitchVelCon}

Four nonholomic constraints (Eq.eq:noSlip) further reduce the
locally achievable configuration space to three degrees of freedom.
The pure rolling, no side-slip, contact of the knife-edge wheels
with the ground plane requires that there are no components of
velocity of the wheel contact points in the
:math:`{\mathbf[n]_}_1` and :math:`{\mathbf[n]_}_2` directions.

.. math::
   ^N\bar{\mathbf[v]_}^[C_n]_\cdot\hat{\mathbf[n]_}_1=
   ^N\bar{\mathbf[v]_}^[C_n]_\cdot\hat{\mathbf[n]_}_2=
   ^N\bar{\mathbf[v]_}^[G_n]_\cdot\hat{\mathbf[n]_}_1=
   ^N\bar{\mathbf[v]_}^[G_n]_\cdot\hat{\mathbf[n]_}_2=0
   :label: {eq:noSlip}

Eight generalized coordinates, one of which is dependent, and three
independent generalized speeds (:math:`u_i=\dot[q]__i` where
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
   \dot[u]__i=f\left(u_4,u_5,u_7,q_4,q_6,q_7\right)\textrm{ where }i=4,5,7
   :label: {eq:accels}

.. math::
   \dot[q]__i=u_i\textrm{ where }i=4,5,6,7
   :label: {eq:speeds}

The equations of motion can then be linearized by calculating the
Jacobian of the system of equations. The partial derivatives were
evaluated at the following fixed point: :math:`q_i=0` where
:math:`i=4,6,7`, :math:`u_i=0` where :math:`i=4,7`, and
:math:`u_5=-v/R_r` where :math:`v` is the constant forward
speed of the bicycle. This reduces the system to four linear first
order differential equations in the form:

.. math::
   \frac[d]_[dt]_
    \left[
    \begin[array]_[c]_
        q_4\\q_5\\q_6\\q_7\\u_4\\u_5\\u_7
    \end[array]_
    \right]
    =
    \mathbf[A]_
    \left[
    \begin[array]_[c]_
        q_4\\q_5\\q_6\\q_7\\u_4\\u_5\\u_7
    \end[array]_
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
(:math:`\mathbf[M]`, :math:`\mathbf[C]_1`,
:math:`\mathbf[K]_0` and :math:`\mathbf[K]_2`) for the
benchmark parameter set at least 15 significant figures and my
model matched all of the significant figures.

.. math::
   \mathbf{M\dot[u]_}+v\mathbf[C]__1\mathbf[u]_+\left[g\mathbf[K]__0+v^2\mathbf[K]__2\right]\mathbf[q]_=0
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

