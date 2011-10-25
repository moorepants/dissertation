===================
Physical Parameters
===================

Preface
=======

This work started when we need to measure the first instrumented bicycle we
built a TU Delft. I agreed to measure the bike's physical parameters using the
equipment and procedures developed in :ref:`Kooijman2006`. These first
measurments are documented in :ref:`Moore2009`. Dr. Hubbard encouraged me to
think about the accuracy of the measurements in more detail and I also decided
to measure an assortment of bicycles we had available around the lab in Delft
because their was very little complete data available on the physical
parameters of real bicycles. Much of what follows is in :ref:`Moore2009` and
:ref:`Moore2010`.

ABSTRACT
========

Accurate measurements of a bicycle's physical parameters are required for
realistic dynamic simulation and analysis. The most basic models require the
geometry, mass, mass location and mass distributions for the rigid bodies. More
complex models require estimates of tire characteristics, human
characteristics, friction, stiffness, damping, etc. In this chapter I present
the measurement of the minimal bicycle parameters required for the benchmark
Whipple bicycle model presented in :ref:`Meijaard2007` including the effects of
a rigid rider. This model is composed of four rigid bodies, has ideal rolling
and frictionless joints, and is laterally symmetric. A set of 25 parameters
describes the geometry, mass, mass location and mass distribution of each of
the rigid bodies. The experimental methods used to estimate the parameters
described herein are based primarily on the work done in :ref:`Kooijman2006`
but have been refined for improved accuracy and methodology. Koojiman's work
was preceded by :ref:`Roland1971` who measured a bicycle in a similar fashion
and both :ref:`Dohring1953` and :ref:`Singh1971` who used similar techniques
with scooters.

We measured the physical characteristics of eight different bicycles, two of
which were set up in two different configurations. The six bicycles, chosen for
both variety and convenience, are as follows: *Batavus Browser*, a Dutch style
city bicycle measured with and without instrumentation as described
in :ref:`Kooijman2009a`; *Batavus Stratos Deluxe*, a Dutch style sporty city
bicycle; *Batavus Crescendo Deluxe* a Dutch style city bicycle with a suspended
fork; *Gary Fisher Mountain Bike*, a hardtail mountain bicycle; *Bianchi
Pista*, a modern steel frame track racing bicycle; and *Yellow Bicycle*, a
stripped down aluminum frame road bicycle measured in two configurations, the
second with the fork rotated in the headtube 180 degrees for larger trail.

These eight different parameter sets can be used with, but are not limited to,
the benchmark bicycle model. The accuracy of all the measurements are presented
up through the eigenvalue prediction of the linear model. The accuracies are
based on error propagation theory with correlations taken into account.

INTRODUCTION
============

This work is intended to document the indirect measurement of eight real
bicycles' physical parameters. The physical parameters measured are those
needed for the benchmark Whipple bicycle model presented in
:ref:`Meijaard2007`. The work is based on techniques used to measure the
instrumented bicycles in :ref:`Kooijman2006`, :ref:`Kooijman2008` and
:ref:`Moore2009a`. We improve upon these methods by both increasing and
reporting the accuracies of the measurements and by measuring the complete
moments of inertia of the laterally symmetric frame and fork needed for
analysis of the nonlinear model. Furthermore, very little data exists on the
physical parameters of different types of bicycles and this work aims to
provide a small sample of bicycles.

Döhring :ref:`Dohring1953` and Singh and Goel :ref:`Singh1971` measured the
physical parameters of scooters. Roland and Massing :ref:`Roland1971` measured
the physical parameters of a bicycle in much the same way as is presented,
including calculations of uncertainty from the indirect measurement techniques.
Patterson :ref:`Patterson2004` used a swing to measure the inertia of a bicycle
and rider. The present work is based on the work done by Kooijman
:ref:`Kooijman2006` using much of the same apparatus and refining the
measurement technique. :ref:`Jose` measured a bicycle for his class in Spain.
:ref:`Undergraduate thesis` where he used solid works. Brendan's solidwork
model.

.. todo::
   Find these more recent references on bike parameters.

BENCHMARK BICYCLE MODEL
=======================

The Whipple bicycle model is derived and described in :ref:`eom`. The unforced two
degree-of-freedom, :math:`\mathbf{q}` = [steer and roll], model takes the form:

.. math::
   :label: canonical
   \mathbf{M\ddot{q}}
   +v\mathbf{C}_1\mathbf{\dot{q}}
   +\left[g\mathbf{K}_0
   +v^2\mathbf{K}_2\right]\mathbf{q}
   =0

where the entries of the :math:`\mathbf{M}`, :math:`\mathbf{C}_1`,
:math:`\mathbf{K}_0` and :math:`\mathbf{K}_2` matrices are combinations of 25
bicycle physical parameters that include the geometry, mass, mass location and
mass distribution of the four rigid bodies. The 25 parameters presented in
:ref:`Meijaard2007` are not necessarily a minimum set for the Whipple model, as
shown in :ref:`Sharp2008`, but are useful none-the-less as they represent more
intuitively measurable quantities. Furthermore, many more parameters are not
needed due to the assumptions of the Whipple model such as no-slip tires,
lateral symmetry, knife edge wheels, etc.

BICYCLE DESCRIPTIONS
====================

We choose to measure the physical parameters of six bicycles Fig. fig:bicycles.
The three Batavus bicycles were donated by the manufacturer. We asked for a
bicycle that they considered stable and one that they did not. They claimed the
Browser was a "stable" bicycle and that the Stratos was "nervous". The Fisher
and the Pista were chosen to provide some variety, a mountain and road bike.
The yellow bike is used to demonstrate bicycle stability.

.. todo::
   Add the figurse of the bicycles.

    [Batavus Browser]{
        \\label{fig:browser}
        \\includegraphics[width=1.75in]{../../../images/browserIns\_sub.jpg}
        }[Batavus Crescendo Deluxe]{
        \\label{fig:crescendo}
        \\includegraphics[width=1.75in]{../../../images/crescendo\_sub.jpg}
        }[Gary Fisher]{
        \\label{fig:fisher}
        \\includegraphics[width=1.75in]{../../../images/fisher\_sub.jpg}
        }
    [Bianchi Pista]{
        \\label{fig:pista}
        \\includegraphics[width=1.75in]{../../../images/pista\_sub.jpg}
        }[Batavus Stratos Deluxe]{
        \\label{fig:stratos}
        \\includegraphics[width=1.75in]{../../../images/stratos\_sub.jpg}
        }[Yellow Bicycle]{
        \\label{fig:yellow}
        \\includegraphics[width=1.75in]{../../../images/yellow\_sub.jpg}
        }{The six bicycles measured in the experiments. The Batavus
    Browser~\\subref{fig:browser} is shown with the instrumentation and the
    Yellow Bicycle~\\subref{fig:yellow} is shown with its fork reversed.}(fig:bicycles)


PARAMETERS
==========

The 25 parameters can be estimated using many techniques. I attempted to
measured the benchmark parameter as directly as possible to improve the
accuracy.

ACCURACY
--------

We took great care to improve and report the accuracy of the measurements of
the parameters. Following the footsteps of :ref:`Roland1971` we used error
propagation theory to calculate accuracy of the 25 benchmark parameters. We
start by estimating the standard deviation of the actual measurements taken. If
:math:`x` is a parameter and is a function of the measurements,
:math:`u,v,\ldots`, then :math:`x` is a random variable defined as
:math:`x=f(u,v,\ldots)`. The sample variance of :math:`x` is defined as

.. math::
   :label: sampleVariance

   s_x^2 =
   \frac{1}{N-1}\sum^N_{i=1}
   \left[(u_i - \bar{u})^2\left(\frac{\partial x}{\partial u}\right)^2 +
   (v_i - \bar{v})^2\left(\frac{\partial x}{\partial v}\right)^2 +
   2(u_i - \bar{u})(v_i - \bar{v})\left(\frac{\partial x}{\partial u}\right)\left(\frac{\partial x}{\partial v}\right)
   + \ldots\right]

Using the definitions for variance and covariance, Equation
:eq:`sampleVariance` can be simplified to

.. math::
   :label: variance

   s_x^2 = s_u^2\left(\frac{\partial x}{\partial u}\right)^2 +
           s_v^2\left(\frac{\partial x}{\partial v}\right)^2 +
           2s_{uv}\left(\frac{\partial x}{\partial u}\right)\left(\frac{\partial x}{\partial v}\right)
           + \ldots

If :math:`u` and :math:`v` are uncorrelated then :math:`s_{uv}=0`. Most of the
calculations hereafter have uncorrelated variables but a few do not and the
covariance has to be taken into account. Equation eqn:variance can be used to
calculated the variance of all types of functions. Simple addition of two
random variables may be the most basic example:

.. math::
   :label: addition

   x =  au + bv\\
   s_x = a^2s_u^2 + b^2s_v^2

GEOMETRY
========

Geometry and wheel radii changes with rider weight, frame flex ,etc.

WHEEL RADII
-----------

The radii of the front :math:`r_\mathrm{F}` and rear :math:`r_\mathrm{R}`
wheels were estimated by measuring the linear distance traversed along the
ground through either 13 or 14 rotations of the wheel. Each wheel was measured
separately and the measurements were taken with a 72kg rider seated on the
bicycle. A 30 meter tape measure (resolution: 2mm) was pulled tight and taped
on a flat level smooth floor. The tire was marked with chalk and aligned with
the tape measure Fig. fig:tireChalk. The accuracy of the distance measurement
is approximately :math:`\pm0.01` m. The tires were pumped to the recommended
inflation pressure before the measurements. The wheel radius is calculated by

.. math::
    :label: wheelRadius

    r\pm\sigma_r=
    \frac{d}{2\pi n}
    \pm\left(\frac{\sigma_d}{2\pi n}\right)

.. figure:: /images/physicalparameters/tireChalk.jpg
   :caption: Wheel and tire with chalk mark aligned to the tape measure.
   :align: center

.. _secHeadtube:

Head tube angle
---------------

For the first six bicycles the head tube angle was measured directly using an
electronic level with a :math:`\pm0.2^{\circ}` accuracy. The bicycle frame was
fixed perpendicular to the ground, the steering angle was set to the nominal,
tire pressures were at recommended levels and the bicycle was unloaded. The
steer axis tilt :math:`\lambda` is the complement to the head tube angle.

.. math::
   :label: eqHeadTubeAngle

   \lambda\pm\sigma_\lambda
   =\frac{\pi}{180^{\circ}}(90^{\circ}-\lambda_{ht})
   \pm\left(\frac{\pi}{180^\circ}\right)\sigma_{\lambda_{ht}}

Trail
-----

Trail is difficult to measure directly due to the fact that the tire has a
contact patch and there is no distinct point to measure to. I instead chose to
measure the fork offset. The fork offset was measured by clamping the steer
tube of the front fork into a v-block on a flat table. A ruler was used to
measure the height of the center of the head tube and the height of the center
of the axle axis. The fork blades were aligned such that the axle axis was
parallel to the table surface.

.. math::
   :label: eqTrail

   c=\frac{r_\mathrm{F}\sin{\lambda}-f_o}{\cos{\lambda}}

.. math::
   :label: eqTrailVar

   \sigma_{c}^{2}=\sigma_{r_{\mathrm{F}}}^{2}\tan^2{\lambda} -
   \sigma_{f_o}^{2}\sec^2{\lambda} +
   \sigma_{\lambda}^{2}\left(r_\mathrm{F}\sec^2{\lambda} -
   f_o\sec{\lambda}\tan{\lambda}\right)^2

Wheelbase
---------

We measured the wheelbase with the bicycle in nominal configuration described
in Section :ref:`secHeadtube`. We used a tape measure to measure the distance
from one wheel axle center to the other with a 0.002 m accuracy.

Alternative Geometry Method
===========================

Our forumulation of the geometry in the Whipple bicycle model is different that
the :ref:`Meijaard2007` definition. These can almost be measured directly
giving a more accurate estimate.

.. todo:: Added new geometrey method

MASS
====

.. figure:: ../../../images/massScale.jpg
   :caption: The scale used to measure the mass of each bicycle component.
   :align: center
   :label: figMassScale

The total mass of each bicycle was measured using a spring scale with a
resolution of 100 grams. The total mass was only used for comparison purposes.
Each of the four bicycle parts were measured using a Molen 20 kilogram scale
with a resolution of 20 grams. The accuracy was conservatively assumed to also
be :math:`\pm20` grams.

CENTER OF MASS
==============

WHEELS
------

The centers of mass of the wheels are assumed to be at their geometrical
centers to comply with the Whipple model.

REAR FRAME
----------

The rear frame was hung in at least three orientations as a torsional pendulum
(both for the center of mass measurements and the moment of inertia
measurements described in Section :ref:`sec`. We assumed that the frame was
laterally symmetric, complying with the Whipple model. The frame could rotate
about a joint such that gravity aligned the center of mass with the pendulum
axis. The orientation angle of the headtube, :math:`\alpha_\mathrm{B}`, Fig.
fig:angles relative to the earth was measured using a digital level
(:math:`\pm0.2^{\circ}` accuracy), Figure fig:level. A thin string was aligned
with the pendulum axis and allowed to pass by the frame. The horizontal
distance :math:`a_\mathrm{B}` between the rear axle and the string was measured
by aligning a ruler perpendicular to the string. The distance
:math:`a_\mathrm{B}` was negative if the string fell to the right of the rear
axle and positive if it fell to the left of the rear axle. These measurements
allow for the calculation of the center of mass location in the global
reference frame.

.. todo::
    []{\\label{fig:angles}\\includegraphics[width=3in]{../../../figures/angles.pdf}}[]{\\label{fig:triangle}\\includegraphics[width=2.75in]{../../../figures/triangle.pdf}}{\\subref{fig:angles} Pictorial description of the angles and dimensions that related
    the nominal bicycle reference frame $XYZ\_B$ with the pendulum reference frame
    $XYZ\_P$. \\subref{fig:triangle} Exaggerated intersection of the three pendulum axes and the
    location of the center of mass.}


    []{\\label{fig:level}\\includegraphics[width=2.75in]{../../../images/YellowFrameTorsionalThird.jpg}}[]{\\label{fig:PendDist}\\includegraphics[width=2.75in]{../../../images/pendDist.jpg}}{\\subref{fig:level} The digital level was mounted to a straight edge aligned
    with the headtube of the bicycle frame. This was done without allowing the
    straight edge to touch the frame. The frame wasn't completely stationary so
    this was difficult. The light frame oscillations could be damped out by
    submerging a low hanging area of the frame into a bucket of water to
    decrease the oscillation. \\subref{fig:PendDist} Measuring the distance from
    the pendulum axis to the rear wheel axle using level ruler.}


The frame rotation angle :math:`\beta_\mathrm{B}` is defined as rotation of the
frame in the nominal configuration to the hanging orientation, rotated about
the :math:`Y` axis.

.. math::
   :label: eqFrameRotAng
   \beta=\lambda-\alpha

.. math::
   :label: eqFrameRotAngVar
   \sigma_{\beta}^{2} = \sigma_{\lambda}^{2} + \sigma_{\alpha}^{2}

The center of mass can be found by realizing that the pendulum axis :math:`X_P`
is simply a line in the nominal bicycle reference frame with a slope :math:`m`
and a z-intercept :math:`b` where the :math:`i` subscript corresponds the
different frame orientations Fig. :ref:`figTriangle`. The slope can be shown to be

.. math::
   :label: eqSlope

   m_i=-\tan{\beta_i}

.. math::
   :label: eqSlopeVar

   \sigma_{m}^{2} = \sigma_{\beta}^{2}\sec^{4}{\beta}

The z-intercept can be shown to be

.. math::
   :label: eqZInt

   b_i=-\left(\frac{a_\mathrm{B}}{\cos{\beta_i}}+r_\mathrm{R}\right)

.. math::
   :label: eqZIntvar

   \sigma_{b}^{2} = \sigma_{a}^{2}\sec^{2}{\beta} +
   \sigma_{r_\mathrm{R}}^{2} +
   \sigma_{\beta}^{2}a^{2}\sec^{2}{\beta}\tan^{2}{\beta}

Theoretically, the center of mass lies on each line but due to experimental
error, if there are more than two lines, the lines do not cross all at the same
point. Only two lines are required to calculate the center of mass of the
laterally symmetric frame, but more orientations increase the center of mass
measurement accuracy.  The three lines are defined as:

.. math::
   :label: eqLine
   z = m_ix+b_i

The mass center location can be calculated by finding the intersection of these
three lines. Two approaches were used used to calculate the center of mass.
Intuition leads one to think that the center of mass is located at the centroid
of the triangle made by the three intersecting lines. The centroid can be found
by calculating the intersection point of each pair of lines and then averaging
the three intersection points.

.. math::
   :label: eqLinearSystem}
   \left[
    \begin{array}{cc}
        -m_1 & 1\\
        -m_2 & 1
    \end{array}
    \right]
    \left[
    \begin{array}{c}
        x_a\\
        z_a
    \end{array}
    \right]
    =
    \left[
    \begin{array}{c}
        b_1\\
        b_2
    \end{array}
    \right]

.. math::
   x_\mathrm{B} = \frac{x_a + x_b + x_c}{3}

.. math::
   z_\mathrm{B} = \frac{z_a + z_b + z_c}{3}

Alternatively, the three lines can be treated as an over determined linear
system and the least squares method is used to find a unique solution. This
solution is not the same as the triangle centroid method.

.. math::
   :label: eqLeastSquares

   \left[
    \begin{array}{cc}
        -m_1 & 1\\
        -m_2 & 1\\
        -m_3 & 1
    \end{array}
    \right]
    \left[
    \begin{array}{c}
        x_\mathrm{B}\\
        z_\mathrm{B}
    \end{array}
    \right]
    =
    \left[
    \begin{array}{c}
        b_1\\
        b_2\\
        b_3
    \end{array}
    \right]

The solution with the higher accuracy is the preferred one.

Fork and Handlebar
------------------

The fork and handlebars are a bit trickier to hang in three
different orientations. Typically two angles can be obtained by
clamping to the steer tube at the top and the bottom. The third
angle can be obtained by clamping to the stem. The center of mass
of the fork is calculated in the same fashion. The slope of the
line in the benchmark reference frame is the same as for the frame
but the z-intercept is different:

.. math::
   :label: eqZIntFork

   b = w\tan{\beta} - r_\mathrm{F} - \frac{a}{\cos{\beta}}

.. math::
   :label: eqZIntForkVar

   \sigma_{b}^{2} = \sigma_{w}^{2}\tan^{2}\beta +
   \sigma_{\beta}^{2}\left(w\sec^{2}\beta -
   a\sec\beta\tan\beta\right)^{2} + \sigma_{r_\mathrm{F}}^{2} +
   \sigma_{a}^{2}\sec^{2}\beta

.. _secMoI:

MOMENT OF INERTIA
=================

The moments of inertia of the wheels, frame and fork were measured by taking
advantage of the assumed symmetry of the parts and by hanging the parts as both
compound and torsional pendulums and measuring their periods of oscillation
when perturbed at small angles. The rate of oscillation was measured using a
`Silicon Sensing CRS03 100 deg/s rate gyro
<http://www.siliconsensing.com/CRS03>`_.  The rate gyro was sampled at 1000hz
with a `National Instruments USB-6008 12 bit data acquisition unit
<http://sine.ni.com/nips/cds/view/p/lang/en/nid/14604>`_ and {Matlab}. The
measurement durations were either 15 or 30 secs and each moment of inertia
measurement was performed three times. No extra care was taken to calibrate
the rate gyro, maintain a constant power source (i.e. the battery drains
slowly), or account for drift. The raw voltage signal was used to determine
only the period of oscillation which is needed for the moment of inertia
calculations.

.. figure:: ../../../plots/PendFit/BrowserFrameCompoundFirst1.png
   :label: figVoltage
   :caption:Example of the raw voltage data taken during a 30 second
   measurement of the oscillation of one of the components.
   :align: center

The function Eqn eqn:decayOs was fit to the data using a nonlinear
least squares fit routine for each experiment to determine the
quantities :math:`A`, :math:`B`, :math:`C`, :math:`\zeta`,
and :math:`\omega`.

.. math::
   :label: eqnDecayOs

   f(t) = A + e^{-\zeta\omega t}\left[B\sin{\sqrt{1-\zeta^2}\omega t} +
   C\cos{\sqrt{1-\zeta^2}\omega t}\right]

Most of the data fit the damped oscillation function well with very light (and
ignorable) damping. There were several instances of beating-like phenomena for
some of the parts at particular orientations. Roland and Massing
:ref:`Roland1971` also encountered this problem and used a bearing to prevent
the torsional pendulum from swinging. Figure :ref:`figBeating` shows an example
of the beating like phenomena.

.. figure:: ../../../plots/PendFit/CrescendoForkTorsionalFirst2.png
   :caption:An example of the beating-like phenomena observed on 5\\% of the
    experiments.
   :align: center
   :label: figBeating

The physical phenomenon observed corresponding to data sets such as these was
that the bicycle frame or fork was perturbed torsionally.  After set into
motion the torsional motion died out and a longitudinal swinging motion
increased. The motions alternated back and forth with neither ever reaching
zero. The frequencies of these motions were very close to one another and it is
not apparent how dissect the two. We explored fitting to a function such as

.. math::
   :label: eqnSumSines

   f(t) = A\sin{(\omega_1 t)} + B\sin{(\omega_2 t + \phi)} + C

But the fit predicts that :math:`\omega_1` and :math:`\omega_2`
are very similar frequencies. There was no easy way to choose which
of the two :math:`\omega`'s was the one associated with the
torsional oscillation. Some work was done to model the torsional
pendulum as a laterally flexible beam to determine this, but we
thought accuracy of the period calculation would not improve enough
for the effort required. Future experiments should simply prevent
the swinging motion of the pendulum without damping the torsional
motion.

The period for a damped oscillation is

.. math::
   :label: eqnPeriodDamped

   T = \frac{2\pi}{\sqrt{1-\zeta^2}\omega_n}

The uncertainty in the period, :math:`T`, can be determined from
the fit. Firstly, the variance of the fit is

.. math::
   :label: eqnFitVariance

   \sigma_y^2 =
   \frac{1}{N-5}\sum_{i=1}^N(y_{mi}-\bar{y}_m)^2-(y_{pi}-\bar{y}_m)^2

The covariance matrix of the fit function can be formed

.. math::
   :label: eqnCovariance

   \mathbf{U} = \sigma_y^2\mathbf{H}^{-1}

where :math:`\mathbf{H}` is the Hessian :ref:`Hubbard1989b`.
:math:`\mathbf{U}` is a :math:`5\times5` matrix with the variances of each of
the five fit parameters along the diagonal.  The variance of :math:`T` can be
computed using the variance of :math:`\zeta` and :math:`\omega`. It is
important to note that the uncertainties in the period are very low
(:math:`<1e-4`), even for the fits with low :math:`r^2` values.

Torsional Pendulum
------------------

A torsional pendulum was used to measure all moments of inertia about axes in
the laterally symmetric plane of each of the wheels, fork and frame. The
pendulum is made up of a rigid mount, an upper clamp, a torsion rod, and
various lower clamps.

.. figure:: ../../../images/fixture.jpg
   :caption: The rigid pendulum fixture mounted to a concrete column.
   :align: center
   :label:figFixture

A 5 mm diameter, 1 m long mild steel rod was used as the torsion spring. A
lightweight, low relative moment of inertia clamp was constructed that could
clamp the rim and the tire. The moments of inertia of the clamps were
neglected. The wheel was hung freely such that the center of mass aligned with
the torsional pendulum axis and then secured. The wheel was then perturbed and
oscillated about the pendulum axis. The rate gyro was mounted on the clamp
oriented along the pendulum axis.

The torsional pendulum was calibrated using a known moment of inertia
Fig. fig:rod. A torsional pendulum almost identical to the one used in
:ref:`Kooijman2006` was used to measure the average period
:math:`\overline{T}_i` of oscillation of the rear frame at three different
orientation angles :math:`\beta_i`, where :math:`i=1`, :math:`2`, :math:`3`, as
shown in Fig. fig:triangle. The parts were perturbed lightly, less than 1
degree, and allowed to oscillate about the pendulum axis through at least ten
periods. This was done at least three times for each frame and the recorded
periods were averaged.

.. figure:: ../../../images/rod.jpg
   :align: center
   :alt: image
   :caption:The steel calibration rod. The moment of inertia of the rod,
    I=\\frac{m}{12}(3r^2+l^2), can be used to estimate the stiffness of the
    pendulum, k=\\frac{4I\\pi^2}{\\overline{T}^2}, with k=5.62\\pm0.02 \\frac{\\textrm{Nm}}{\\textrm{rad}}
   :label:figRod


WHEELS
------

Finding the full inertia tensors of the wheels is less complex because the
wheels are assumed symmetric about three orthogonal planes so products of
inertia are zero. The :math:`I_{xx}=I_{zz}` moments of inertia were calculated
by measuring the averaged period of oscillation about an axis in the
:math:`XZ`-plane using the torsional pendulum setup and Eq. eq:torPend.The
wheels are assumed to be laterally symmetric and about any radial axis. Thus
only two moments of inertia are required for the set of benchmark parameters.
The moment of inertia about the axle was measured by hanging the wheel as a
compound pendulum, Fig. fig:wheelIyy. The wheel was hung on a horizontal rod
and perturbed to oscillate about the axis of the rod. This rate gyro was
attached to the spokes near the hub and oriented mostly along the axle axis.
The wheels tended to precess at the contact point about the vertical axis which
added a very low frequency component of rate along the vertical radial axis,
but this should not affect the period estimation about the compound pendulum
axis. A fixture that prevented precession would be preferable for future
measurements. The pendulum arm length is the distance from the rod/rim contact
point to the mass center of the wheel. The inner diameter of the rim was
measured and divided by two to get :math:`l_\mathrm{F,R}`. The moment of
inertia about the axle is calculated from:

.. math::
   :label: eqCompoundInertia

   I_{\mathrm{R}yy} = \left(\frac{\bar{T}}{2\pi}\right)^2m_\mathrm{R}gl_\mathrm{R} -
    m_\mathrm{R}l^2


        \\label{fig:FwheelTor}
        \\includegraphics[width=2.75in]{../../../images/CrescendoFwheelTorsionalFirst.jpg}
        \\label{fig:wheelIyy}
        \\includegraphics[width=2.75in]{../../../images/wheelIyy.jpg}
    }{\\subref{fig:FwheelTor} The front wheel of the Crescendo hung as a
    torsional pendulum. \\subref{fig:wheelIyy} A wheel hung as a compound pendulum.}(fig:wheelPend)


The radial moment of inertia was measured by hanging the wheel as a torsional
pendulum, Fig. fig:FwheelTor. The wheel was hung freely such that the center of
mass aligned with the torsional pendulum axis and then secured. The wheel was
then perturbed and oscillated about the vertical pendulum axis. The radial
moment of inertia can can calculated as such:

.. math::
   I_{xx} = \frac{k\bar{T}^2}{4\pi^2}


FRAME
-----

Three measurements were made to estimate the globally referenced moments and
products of inertia (:math:`I_{xx}`, :math:`I_{xz}` and :math:`I_{zz}`) of the
rear frame. The frame was typically hung from the three main tubes: seat tube,
down tube and top tube, Fig. fig:level. The rear fender prevented easy
connection to the seat tube on some of the bikes and the clamp was attached to
the fender. The fender was generally less rigid than the frame tube.  For best
accuracy with only three orientation angles, the frame should be hung at three
angles that are :math:`120^\circ` apart.  The three tubes on the frame
generally provide that the orientation angles were spread evenly at about
:math:`120^\circ`. Furthermore, taking data at more orientation angles could
improve the accuracy and is generally possible with standard diamond frame
bicycles.

Three moments of inertia :math:`J_{i}` about the pendulum axes were calculated
using :eq:eqTorPend.

.. math::
   :label:eqTorPend

   J_i=\frac{k\overline{T}_i^2}{4\pi^2}

The moments and products of inertia of the rear frame and handlebar/fork
assembly with reference to the benchmark coordinate system were calculated by
formulating the relationship between inertial frames

.. math::
   :label:eqRotIn

   \mathbf{J}_i=\mathbf{R}_i\mathbf{IR}_i^T

where :math:`\mathbf{J}_i` is the inertia tensor about the
pendulum axes, :math:`\mathbf{I}`, is the inertia tensor in the
global reference frame and :math:`\mathbf{R}` is the rotation
matrix relating the two frames, Fig. fig:angles. The global inertia
tensor is defined as

.. math::
   :label:eqMoI

   \mathbf{I}=
    \left[
    \begin{array}{rr}
        I_{xx}  & I_{xz}\\
        I_{xz} & I_{zz}
    \end{array}
    \right]\textrm{.}

The inertia tensor can be reduced to a :math:`2\times2` matrix because the
frame is assumed to be laterally symmetric and the :math:`y` axis of the
pendulum reference is the same as the :math:`y` axis of the benchmark reference
frame. The simple rotation matrix about the :math:`Y`-axis can similarly be
reduced to a :math:`2\times2` matrix where :math:`s_{\beta i}` and
:math:`c_{\beta i}` are defined as :math:`\sin{\beta_i}` and
:math:`\cos{\beta_i}`, respectively.

.. math::
   :label:eqRotMat

   \mathbf{R}=
   \left[
     \begin{array}{rr}
       c_{\beta i} & -s_{\beta i}\\
       s_{\beta i} & c_{\beta i}
     \end{array}
   \right]

The first entry of :math:`\mathbf{J}_i` in Eq. eq:rotIn is the moment of
inertia about the pendulum axis and is written explicitly as

.. math::
   :label:eqInRelComp

   J_{i}=c^{2}_{\beta i}I_{xx}-2s_{\beta i}c_{\beta i}I_{xz}+s^{2}_{\beta i}I_{zz}\textrm{.}

Similarly, calculating all three :math:`J_{i}` allows one to form

.. math::
   :label:eqInRel

   \left[
    \begin{array}{c}
        J_{1}\\
        J_{2}\\
        J_{3}
    \end{array}
    \right]
    =
    \left[
    \begin{array}{ccc}
        c_{\beta 1}^2 & -2s_{\beta 1}c_{\beta 1} & s_{\beta 1}^2\\
        c_{\beta 2}^2 & -2s_{\beta 2}c_{\beta 2} & s_{\beta 2}^2\\
        c_{\beta 3}^2 & -2s_{\beta 3}c_{\beta 3} & s_{\beta 3}^2
    \end{array}
    \right]
    \left[
    \begin{array}{c}
        I_{xx}\\
        I_{xz}\\
        I_{zz}
    \end{array}
    \right]

and the moments of inertia can be solved for. The inertia of the frame about an
axis normal to the plane of symmetry was estimated by hanging the frame as a
compound pendulum at the wheel axis, Fig.:ref:`figFrameCompound`. Equation
:eq:`eqCompoundInertia` is used but with the mass of the frame and the frame
pendulum length.

.. math::
   :label: eqFramePendLength

   l_B=\sqrt{x_B^2+(z_B+r_R)^2}


    []{
        \\label{fig:frameCompound}
        \\includegraphics[width=2in]{../../../images/YellowFrameCompoundFirst.jpg}
        }[]{
        \\label{fig:forkCompound}
        \\includegraphics[width=2in]{../../../images/BrowserInsForkCompoundFirst.jpg}
        }{\\subref{fig:frameCompound} Rear frame hung as a compound
        pendulum. \\subref{fig:forkCompound} Browser fork hung as a
        compound pendulum.}(fig:compound)


FORK AND HANDLEBAR
------------------

The inertia of the fork and handlebar is calculated in the same way
as the frame. The fork is hung as both a torsional pendulum,
Fig.fig:StratosFork, and as a compound pendulum,
Fig.fig:forkCompound. The fork provides fewer mounting options to
obtain at least three equally spaced orientation angles, especially
if there is no fender. The torsional calculations follow
equations :eq:`eqTorPend` through :eq:`eqInRel` and the compound pendulum
calculations is calculated with equationeq:CompoundInertia. The
fork pendulum length is calculated using

.. math::
   l_H=\sqrt{(x_H-w)^2+(z_H+r_F)^2}


    {The Stratos fork and handlebar assembly hung as a torsional
        pendulum.}(fig:StratosFork)


LINEAR ANALYSIS
===============

Once all bicycle parameters have been calculated the canonical
matrices can be formed and the linear dynamics of the bicycles can
be explored. The values of the canonical matrices can be found in
the second table in Appendix sec:partables. We also added the same
rigid rider to each bicycle for further comparison. The rigid rider
was assumed to be in the same position and posture for each bicycle
relative to the rear wheel contact point.

    {Mass, center of mass and moment of inertia for the rider relative
    to the benchmark coordinate system from~\\cite{Moore2009a}}

        Parameter & Value
        :math:`m_\mathrm{P}` [kg] & 72
        :math:`x_\mathrm{P}` [m] & 0.2909
        :math:`z_\mathrm{P}` [m] & -1.1091
        :math:`I_\mathrm{P}` [:math:`\mathrm{kg\ m}^2`] &
        :math:`\left[
            \begin{array}{ccc}
                 7.9985 & 0      & -1.9272\\
                 0      & 8.0689 & 0\\
                -1.9272 & 0      & 2.3624
            \end{array}
            \right]`


    (tab:riderParam)


EIGENVALUES
-----------

    |image1|
    {Eigenvalues versus speed for all eight bicycles without the rider.}(fig:bikeEigPlot)


The eigenvalues of the bicycles with (Fig. fig:bikeEigPlot) and
without (Fig. fig:bikeRiderEigPlot the rider can be plotted versus
forward speed. Figure fig:bikeEigPlot shows that the bikes have the
typical characteristics of the benchmark bicycle: four real roots
at very slow speeds, two of which are unstable; a complex pair that
is unstable at lower speeds and stable at intermediate speeds; and
a root that is mildly unstable at higher speeds. The one noticeable
difference is that the capsize and caster modes are contained in a
complex pair between about 0.5 and 3 m/s. The frequency of
oscillation is of comparable magnitude to that of the weave mode.
But, the root locus in the real and imaginary plane,
Fig. fig:rootloci, shows that the mode damps out quickly. Examining
the eigenvectors reveals that the mode is steer leading roll with a
90 degree phase, both of their magnitudes being similar,
Fig fig:evec.

        .. figure:: ../../../plots/Bike/CrescendoRootLoci.pdf
           :align: center
           :alt: image
           
           image
        

    {The root loci with speed as the parameter for the Crescendo.}(fig:rootloci)


        .. figure:: ../../../plots/cres.pdf
           :align: center
           :alt: image
           
           image
        

    {Eigenvector components for the second complex mode
    pair at low speed.}(fig:evec)


With the rider added, the second complex pair disappears and the
bikes have the typical characteristics of the benchmark bicycle
model. Reversing the fork on the yellow bike lowers the weave
critical speed and increases the stable speed range. Also, the
addition of weight to the rear rack of the Browser does little to
the eigenvalues.

    |image2|
    {Eigenvalues versus speed for all eight bicycles with the same
    rigid rider.}(fig:bikeRiderEigPlot)


FREQUENCY RESPONSE
------------------

The frequency response of the bicycles (Fig. fig:bikeBode) and
bicycle with rider (Fig. fig:bikeRiderBode) also reveal some
interesting things. In the steer-torque-to-roll Bode diagram the
magnitude difference among bicycles can vary up to 10 dB (or about
8.5 degrees per Newton-meter of torque) for the particular speed
shown. The difference in the frequency response for the bicycle
with the rigid rider shows less variation among the bicycles,
Fig. fig:bikeRiderBode, as the rider's mass and inertia play a
larger roll.

    |image3|
    {The frequency response for steer-torque-to-roll for all eight
    bicycles without the rider at 2 m/s.}(fig:bikeBode)


    |image4|
    {The frequency response for steer-torque-to-roll for all eight
    bicycles with the same rigid rider at 2 m/s.}(fig:bikeRiderBode)


CONCLUSION
==========

We have presented a detailed method to accurately estimate the
physical parameters of a bicycle needed for the benchmarked Whipple
bicycle model :ref:`Meijaard2007`. We measured eight different bicycles
providing both the parameter sets and linear model coefficient
matrices for the bicycles alone and the bicycles with the same
rigid rider. The uncertainties in the parameters and matrix
coefficients are included for the bicycle alone. Finally, we have
presented a brief comparison of the eight bicycles using
eigenanalysis and Bode frequency response.

ACKNOWLEDGEMENTS
================

This material is based upon work partially supported by the
National Science Foundation under Grant No. 0928339.

{acm}{bicycle}

PARAMETER TABLES
================

(sec:partables) The tabulated values for the both the physical
parameters and the canonical matrix coefficients are shown in the
following four tables. The uncertainties in the estimations of both
the parameters and coefficients are also shown for the bicycle
without a rider.

        {The parameters for the eight bicycles with uncertainties in the
estimations.}{../../../tables/Bike/Parameters/MasterParTable.tex}(tab:bicyclePar)


        {The canonical matrix coefficients for the eight bicycles with the
uncertainty in the estimations.}{../../../tables/Bike/Canonical/MasterCanTable.tex}(tab:bicycleCan)


        {The parameters for the eight bicycles with the same rigid rider.}{../../../tables/BikeRider/Parameters/MasterParTable.tex}(tab:bicycleRiderPar)


        {The canonical matrix coefficients for the eight bicycles with the
rigid rider.}{../../../tables/BikeRider/Canonical/MasterCanTable.tex}(tab:bicycleRiderCan)




.. |image| image:: ../../../images/StratosForkTorsionalThird.jpg
.. |image1| image:: ../../../plots/Bike/eig_plot.pdf
.. |image2| image:: ../../../plots/BikeRider/eig_plot.pdf
.. |image3| image:: ../../../plots/Bike/Bode/Tdel2phi.pdf
.. |image4| image:: ../../../plots/BikeRider/Bode/Tdel2phi.pdf
