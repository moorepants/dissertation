===================
Physical Parameters
===================

Preface
=======

I was first concerned with the physical parameters of the bicycle and rider in
my multibody dynamics class project where I developed a method of estimating
the parameters from geometry and mass :ref:`Moore2006` which was subsenquently
presented at ISEA 2008 :ref:`Moore2008`. This method served me well until we
needed to have more accurate estimates for the first instrumented bicycle built
at TU Delft. I agreed to measure the bike's physical parameters using the
equipment and procedures developed in :ref:`Kooijman2006` and use the more
accurate bicycle measurements with my basic human model, :ref:`Moore2008`.
These first measurements and the details of the human model are documented in
:ref:`Moore2009a`.  After this, Dr. Hubbard encouraged me to think about the
accuracy of the measurements in more detail, as some of the practices we were
using were lacking. With that in mind and the fact that there was very little
complete data available on the physical parameters of real bicycles, I decided
to measure an assortment of bicycles we had available around the lab in Delft
:ref:`Moore2010`. Once I was back in Davis, we setup almost identical equipment
to measure the two new bicycles we were constructing. Danique Fintelman helped
us come up with a more accurate geometry measurement. Steven Yen measured a
children's bicycle with a gyro wheel. We also improved the human estimates when
Chris Dembia implemented Yeadon's human inertia model and we combined it with
the accurate bicycle measurements. These final methods are implemented in two
open source software packages.

Bicycle Parameters
==================

Accurate measurements of a bicycle's physical parameters are required for
realistic dynamic simulation and analysis. The most basic models require the
geometry, mass, mass location and mass distributions for the rigid bodies. More
complex models require estimates of tire characteristics, human
characteristics, friction, stiffness, damping, etc. In this chapter I present
the measurement of the minimal bicycle/rider parameters required for the
benchmark Whipple bicycle model presented in :ref:`Meijaard2007`. This model is
composed of four rigid bodies, has ideal rolling and frictionless joints, and
is laterally symmetric. A set of 25 parameters describes the geometry, mass,
mass location and mass distribution of each of the rigid bodies. The
experimental methods used to estimate the parameters described herein are based
primarily on the work done in :ref:`Kooijman2006`, :ref:`Kooijman2008` and
:ref:`Moore2009a` but have been refined for improved accuracy and methodology.

Koojiman's work was preceded by several others. Döhring :ref:`Dohring1953` and
Singh and Goel :ref:`Singh1971` measured the physical parameters of scooters.
Roland and Massing :ref:`Roland1971` measured the physical parameters of a
bicycle in much the same way as is presented, including calculations of
uncertainty from the indirect measurement techniques. Patterson
:ref:`Patterson2004` used a swing to measure the inertia of recumbent bicycles
with a rider. :ref:`Connors2009` and :ref:`Stevens2009` used a 3D CAD package
to estimate the parameters. ref:`Escalona2010` measured a bicycle class in
Spain.

Here I document the indirect measurement of ten real bicycles' physical
parameters. We improve upon these methods by both increasing and reporting the
accuracies of the measurements and by measuring the complete moments of inertia
of the laterally symmetric frame and fork needed for analysis of the nonlinear
model. Furthermore, very little data exists on the physical parameters of
different types of bicycles and this work aims to provide a small sample of
bicycles.

We measured the physical characteristics of eleven different bicycles, three of
which were set up in two different configurations. The first six bicycles,
chosen for both variety and convenience, are as follows: *Batavus Browser*, a
Dutch style city bicycle measured with and without instrumentation as described
in :ref:`Kooijman2009a`; *Batavus Stratos Deluxe*, a Dutch style sporty city
bicycle; *Batavus Crescendo Deluxe* a Dutch style city bicycle with a suspended
fork; *Gary Fisher Mountain Bike*, a hardtail mountain bicycle; *Bianchi
Pista*, a modern steel frame track racing bicycle; and *Yellow Bicycle*, a
stripped down aluminum frame road bicycle measured in two configurations, the
second with the fork rotated in the headtube 180 degrees for larger trail. The
last two bicycles were measured in Davis: the instrumented bicycle presented in
chapter :ref:`instrumentedbicycle` and a children's bicycle with a stabilzing
flywheel called the GyroBike.

These eleven different parameter sets can be used with, but are not limited to,
the benchmark bicycle model. The accuracy of all the measurements are
presented. The accuracies are based on error propagation theory with
correlations taken into account.

Parameters
----------

I was primarily concerned with measuring and estimating the 25 parameters
associated with the benchmark Whipple bicycle model which is derived and
described in :ref:`Meijaard2007`. The unforced two degree-of-freedom,
:math:`\mathbf{q} = [\delta \quad \phi]^T` model takes the form:

.. math::
   :label: eqCanonical

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
shown in :ref:`Sharp2008`, but are useful none-the-less as they represent
intuitively measurable quantities and have become become standard due to the
nature of the benchmark. They are also not parameters used in my derivation in
Chapter :ref:`eom` but can easily be converted, as will be shown. I don't
concern myself with measuring many more parameters that are not needed due to
the assumptions of the Whipple model such as no-slip tires, lateral symmetry,
knife edge wheels, etc.

The 25 parameters can be measured using many techniques. In general, I
attempted to measure the benchmark parameter as directly as possible to improve
the accuracy.

Conversion
~~~~~~~~~~

This section details the conversion from the benchmark parameter set to my
parameter set as defined in Chapter :ref:`eom`. When the bicycle is in the
nominal configuration the parameters can be converted with the following
realtionships. The wheel radii are defined the same, but the remaining geometry
is calculated with:

.. math::

   d_1 = \operatorname{cos}(\lambda) (c + w - r_R * \operatorname{tan}(\lambda))

   d_3 = -\operatorname{cos}(\lambda) (c - r_F \operatorname{tan}(\lambda))

   d_2 = \frac{(r_R + d_1 \operatorname{sin}(\lambda) - r_F + d_3
   \operatorname{sin}(\lambda))}{\operatorname{cos}(\lambda)}

The mass center locations are as follows:

.. math::

   l_1 = (x_B  \operatorname{cos}(\lambda) - z_B  \operatorname{sin}(\lambda) -
   r_R  \operatorname{sin}(\lambda))

   l_2 = (x_B  \operatorname{sin}(\lambda) + z_B  \operatorname{cos}(\lambda) +
   r_R  \operatorname{cos}(\lambda))

   l_4 = ((z_H + r_F)  \operatorname{cos}(\lambda) + (x_H - w)
   \operatorname{sin}(\lambda))

   l_3 = ((x_H - w - l_4  \operatorname{sin}(\lambda)) /
   \operatorname{cos}(\lambda))

The masses are equivalent:

.. math::

   m_c = m_B

   m_d = m_R

   m_e = m_H

   m_f = m_F

The moments of inertia of the wheels are also equivalent:

.. math::

     I_D =
     \begin{bmatrix}
       I_{D11} & 0 & 0\\
       0 & I_{D22} & 0\\
       0 & 0 & I_{D33}
     \end{bmatrix}
     = I_R =
     \begin{bmatrix}
       I_{Rxx} & 0 & 0\\
       0 & I_{Ryy} & 0\\
       0 & 0 & I_{Rzz}
     \end{bmatrix}

     I_F =
     \begin{bmatrix}
       I_{F11} & 0 & 0\\
       0 & I_{F22} & 0\\
       0 & 0 & I_{F33}
     \end{bmatrix}
     = I_F =
     \begin{bmatrix}
       I_{Fxx} & 0 & 0\\
       0 & I_{Fyy} & 0\\
       0 & 0 & I_{Fzz}
     \end{bmatrix}

The moments and products of inertia for the frame and fork require the
direction cosine matrix with respect to rotation through :math:`\lambda`.

.. math::

   R =
   \begin{bmatrix}
     ca & 0. & -sa\\
     0. & 1. & 0.\\
     sa & 0. & ca
   \end{bmatrix}

.. math::
    I_B =
    \begin{bmatrix}
      I_{Bxx} & 0 & I_{Bxz}\\
      0 & I_{Byy} & 0\\
      I_{Bxz} & 0 & I_{Bzz}
    \end{bmatrix}

    I_C =  R I_B R^T

.. math::
    I_H =
    \begin{bmatrix}
      I_{Hxx} & 0 & I_{Hxz}\\
      0 & I_{Hyy} & 0\\
      I_{Hxz} & 0 & I_{Hzz}
    \end{bmatrix}

    I_E =  R I_H R^T


Bicycle Descriptions
--------------------

We measured a total of eight bicycles in eleven configurations.  The three
Batavus bicycles were donated by the manufacturer. We asked for a bicycle that
they considered stable and one that they did not. They offered the Browser as a
"stable" bicycle and the Stratos as "nervous". The Crescendo was considered
average handling. We measured an instrumented version of the Browser that was
used in the experiments described in Chapter :ref:`delftbicycle`. The Fisher
and the Pista were chosen to provide some variety, a mountain and road bike.
The yellow bike is used to demonstrate bicycle stability and the forked is
reversed to provide better stability when perturbed with no rider. The Davis
instrumented bicycle is an instrumented bicycle described in Chapter
:ref:`davisbicycle` and we measured the frame in configurations for different
rider seating positions. The child's bicycle has the GyroWheel product
installed in the front wheel.

.. list-table:: Bicycles

   * - Batavus Browser
     - Instrumented Batavus Browser
   * - .. image:: figures/physicalparameters/browser_sub.jpg
     - .. image:: figures/physicalparameters/browserIns_sub.jpg
   * - Batavus Crescendo Deluxe
     - Batavus Stratos Deluxe
   * - .. image:: figures/physicalparameters/crescendo_sub.jpg
     - .. image:: figures/physicalparameters/stratos_sub.jpg
   * - Gary Fisher
     - Bianchi Pista
   * - .. image:: figures/physicalparameters/fisher_sub.jpg
     - .. image:: figures/physicalparameters/pista_sub.jpg
   * - Yellow Bicycle
     - Yellow Bicycle with reversed fork
   * - .. image:: figures/physicalparameters/yellow_sub.jpg
     - .. image:: figures/physicalparameters/yellowRev_sub.jpg
   * - Davis Instrumented Bicycle
     - Gyro Bicycle
   * - .. image:: figures/physicalparameters/davisBicycle_sub.jpg
     - .. image:: figures/physicalparameters/gyroBicycle_sub.jpg

.. todo:: add the gyro bike, davis bike and pictures of the other two bicycles

ACCURACY
--------

I took more care to improve and report the accuracy of the measurements of
the parameters. Following the footsteps of :ref:`Roland1971` I used error
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
covariance has to be taken into account. Equation :eq:`variance` can be used to
calculate the variance of all types of functions. Simple addition of two random
variables may be the most basic example:

.. math::
   :label: addition

   x =  au + bv\\
   s_x = a^2s_u^2 + b^2s_v^2

Geometry
--------

First attempts at measuring the geometry focused on the benchmark parameters:
trail, wheelbase, and steer axis tilt, but I also present an alternative method
for the geometry that attempts to measure the distances in my model derivation
which improves the accuracy of the parameters. I assumed that the frame did not
flex and that the wheel radii do not change with rider weight.

Wheel Radii
~~~~~~~~~~~

The radii of the front :math:`r_\mathrm{F}` and rear :math:`r_\mathrm{R}`
wheels were estimated by measuring the linear distance traversed along the
ground through either 13 or 14 rotations of the wheel. Each traversal was
measured separately and the measurements were taken with rider seated on the
bicycle, except for the gyro bicycle which had no rider (72kg rider for the
Delft bikes and 82kg for the Davis bike...I gained some weight drinking all
that beer in the Netherlands). A 30 meter tape measure (resolution: 2mm) was
pulled tight and taped on a flat level smooth floor. The tire was marked with
chalk and aligned with the tape measure Fig. :ref:`figTireChalk`. The accuracy
of the distance measurement is approximately :math:`\pm0.01` meter. The tires
were pumped to the recommended inflation pressure before the measurements. The
wheel radius is calculated by

.. math::
    :label: wheelRadius

    r\pm\sigma_r=
    \frac{d}{2\pi n}
    \pm\left(\frac{\sigma_d}{2\pi n}\right)

.. _figTireChalk:

.. figure:: figures/physicalparameters/tireChalk.jpg
   :align: center

   Wheel and tire with chalk mark aligned to the tape measure.

   One

.. _secHeadtube:

Head tube angle
~~~~~~~~~~~~~~~

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

.. _figHeadtube:

.. figure:: figures/physicalparameters/headtube.jpg
   :align: center

Trail
~~~~~

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
~~~~~~~~~

We measured the wheelbase with the bicycle in nominal configuration described
in Section :ref:`secHeadtube`. We used a tape measure to measure the distance
from one wheel axle center to the other with a 0.002 m accuracy.

Alternative Geometry Method
---------------------------

Our forumulation of the geometry in the Whipple bicycle model is different that
the :ref:`Meijaard2007` definition. These can almost be measured directly
giving a more accurate estimate. The bicycle frame is set on a granite
measurment table such that the head tube is in in a v-block and parallel to the
table surface and the bicycle frame's rear axle is above the headtube. The is
fork rotated in the headtube such that the fork blades curve upwards. Two dummy
axles are fit into the front and rear dropouts and the axles are ensured to be
parrallel to the table surface. The height from the table surface to the top
of each axle are recorded with a height gage and the diameters of the axles are
measured with a micrometer or caliper. These give direct measurments of the
front and rear offsets, :math:`d_3` and :math:`d_1`. The outer distance between the
two axles are then measured giving :math:`d_4`. :math:`d_2` can be computed
with:

.. math::
   :label: d2

   d_2 = \sqrt{d_4^2 - (d_1 - d_3)^2}


If the :math:`r_F` does not equal :math:`r_R` then the steer axis tilt cannot
be computed analytically as the relation holds:

.. math::
   :label: eqLambda

   \operatorname{sin}(\lambda) = \frac{r_F - r_R + d_2 \operatorname{cos}(\lambda)}{d_1 + d_3}

It is trivial to find the solution numerically. If :math:`r_F=r_R`,
:math:`\lambda` has an analytic solution:

.. math::
   :label: lambdaEqualRadii

   \lambda = \operatorname{arctan}\right(\frac{d_2}{d_1 + d_3}\left)

Wheelbase is:

.. math::
   :label: eqWheelbase

    w = (d_1 + d_3) \operatorname{cos}(\lambda) + d_2 \operatorname{sin}(\lambda)

Trail is then computed with Equation :eq:`eqTrail`, realizing :math:`f_o = d_3`:

.. math::
   :label: eqTrailD3

    c = \frac{r_F \operatorname{sin}(\lambda) - d_3}{\operatorname{cos}(\lambda)}

Mass
----

For the first six bicycles, each of the four bicycle parts were measured using
a Molen 20 kilogram scale with a resolution of 20 grams. The accuracy was
conservatively assumed to also be :math:`\pm20` grams. Also, the total mass was
measured using a spring scale with a resolution of 100 grams. The total mass
was only used for comparison purposes, as it was not very accurate. The mass of
the parts of the Davis Instrumented Bicycle and the Gyro Bicycle were measured
with a digital scale with a resolution of 0.01 kg.

.. todo:: list the details of the scale in Hull's lab

.. _figMassScale:

.. figure:: figures/physicalparameters/massScale.jpg
   :align: center

   The scale used to measure the mass of each bicycle component.

CENTER OF MASS
--------------

WHEELS
~~~~~~

The centers of mass of the wheels were assumed to be at their geometrical
centers to comply with the Whipple model.

REAR FRAME
----------

The rear frame bicycle configuration was hung in at least three orientations
through the lateral mid-plane. I assumed that the frame was laterally
symmetric, complying with the Whipple model, thus reducing the need to use a
more complex three dimensional measurement setup. The frame could rotate about
a joint such that gravity aligned the center of mass with the support rod axis.
The orientation angle of the steer axis, :math:`\alpha_\mathrm{B}`, see Figure
:ref:`figAngles`, relative to the earth was measured using a digital level
(:math:`\pm0.2^{\circ}` accuracy), Figure :ref:`figLevel`. A thin string was
aligned with the pendulum axis and whiched passed by the frame. The horizontal
distance :math:`a_\mathrm{B}` between the rear axle and the string was measured
by aligning a 1 mm resolution ruler perpendicular to the string. The distance
:math:`a_\mathrm{B}` was negative if the string fell to the right of the rear
axle and positive if it fell to the left of the rear axle. These measurements
allow for the calculation of the center of mass location in the global
reference frame.

.. _figAngles:

.. figure:: figures/physicalparameters/angles.pdf

   Pictorial description of the angles and dimensions that related the nominal
   bicycle reference frame :math:`XYZ\_B` with the pendulum reference frame
   :math:`XYZ\_P`.

.. _figTriangle:

.. figure:: figures/physicalparameters/triangle.pdf

   Exaggerated intersection of the three pendulum axes and the location of the
   center of mass.

.. _figLevel:

.. figure:: figures/physicalparameters/YellowFrameTorsionalThird.jpg

   The digital level was mounted to a straight edge aligned with the headtube of
   the bicycle frame. This was done without allowing the straight edge to touch
   the frame. The frame wasn't completely stationary so this was difficult. The
   light frame oscillations could be damped out by submerging a low hanging area
   of the frame into a bucket of water to decrease the oscillation.

.. _figPendDist:

.. figure:: figures/physicalparameters/pendDist.jpg

   Measuring the distance from the pendulum axis to the rear wheel axle using
   level ruler.

The frame rotation angle :math:`\beta_\mathrm{B}` is defined as rotation of the
frame in the nominal benchmark configuration to the hanging orientation,
rotated about the :math:`Y` axis.

.. math::
   :label: eqFrameRotAng

   \beta=\lambda-\alpha

.. math::
   :label: eqFrameRotAngVar

   \sigma_{\beta}^{2} = \sigma_{\lambda}^{2} + \sigma_{\alpha}^{2}

The center of mass can be found by realizing that the pendulum axis :math:`X_P`
is simply a line in the nominal bicycle reference frame with a slope :math:`m`
and a z-intercept :math:`b` where the :math:`i` subscript corresponds the
different frame orientations, see Figure :ref:`figTriangle`. The slope can be
shown to be:

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
   :label: eqLinearSystem

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

.. todo:: add details about measuring the handlebar separate in the davis bike

.. _secMoI:

Inertia
-------

The moments of inertia of the wheels, frame and fork (and handlebar) were
measured both by taking advantage of the assumed symmetry of the parts and by
hanging the parts as both compound and torsional pendulums and measuring their
periods of oscillation when perturbed at small angles. The rate of oscillation
was measured using a `Silicon Sensing CRS03 100 deg/s rate gyro
<http://www.siliconsensing.com/CRS03>`_ for the Delft bicycles and a `Silicon
Sensing CRS04 200 deg/s rate gyro <http://www.siliconsensing.com/CRS04>`_ for
the Davis bicycles. The rate gyro was sampled at 1000hz with a `National
Instruments USB-6008 12 bit data acquisition unit
<http://sine.ni.com/nips/cds/view/p/lang/en/nid/14604>`_ and at 500 hz with a
`National Instruments USB-6218 16 bit data acquisition unit
<http://sine.ni.com/nips/cds/view/p/lang/en/nid/203092>`_ and the Matlab data
aquisition toolbox. The measurement durations were between 15 and 30 secs and
each moment of inertia measurement was performed at least three times. No extra
care was taken to calibrate the rate gyro, maintain a constant power source
(i.e. the battery drains slowly), or account for drift because I was only
concerned with the period. The raw voltage signal was used to determine the
period of oscillation which is needed for the moment of inertia calculations.

.. _figVoltage:

.. figure:: figures/physicalparameters/BrowserFrameCompoundFirst1.png
   :align: center

   Example of the raw voltage data taken during a 30 second measurement of the
   oscillation of one of the components.

The function Eqn :eq:`eqDecayOs` was fit to the data using the least
squares method for each experiment to determine the quantities :math:`A`,
:math:`B`, :math:`C`, :math:`\zeta`, and :math:`\omega`.

.. math::
   :label: eqnDecayOs

   f(t) = A + e^{-\zeta\omega t}\left[B\sin{\sqrt{1-\zeta^2}\omega t} +
   C\cos{\sqrt{1-\zeta^2}\omega t}\right]

Most of the data fit the damped oscillation function well with very light (and
ignorable) damping. There were several instances in the earlier Delft
experiments of beating-like phenomena for some of the parts at particular
orientations. Roland and Massing :ref:`Roland1971` also encountered this
problem and used a bearing to prevent the torsional pendulum from swinging.
Figure :ref:`figBeating` shows an example of the beating like phenomena. This
was remedied in a similar fashion for the Davis measurements.

.. _figBeating:

.. figure:: figures/physicalparameters/CrescendoForkTorsionalFirst2.png
   :align: center

   An example of the beating-like phenomena observed on 5\\% of the
   experiments.

The physical phenomenon observed corresponding to data sets such as these
occured when the bicycle frame or fork was perturbed torsionally. After set into
motion the torsional motion dampened and a longitudinal swinging motion
increased. The motions alternated back and forth with neither ever reaching
zero. The frequencies of these motions were very close to one another and it is
not apparent how dissect the two. We explored fitting to a function such as

.. math::
   :label: eqnSumSines

   f(t) = A\sin{(\omega_1 t)} + B\sin{(\omega_2 t + \phi)} + C

But the fit predicts that :math:`\omega_1` and :math:`\omega_2` are very
similar frequencies. There was no easy way to choose which of the two
:math:`\omega`'s was the one associated with the torsional oscillation. Some
work was done to model the torsional pendulum as a laterally flexible beam to
determine this, but we ended up assuming that the accuracy of the period
calculation would not improve enough for the effort required. The later
experiments simply prevented the swinging motion of the pendulum without
damping the torsional motion.

The period for a damped oscillation is:

.. math::
   :label: eqnPeriodDamped

   T = \frac{2\pi}{\sqrt{1-\zeta^2}\omega_n}

The uncertainty in the period, :math:`T`, can be determined from
the fit. Firstly, the variance of the fit is calcualted:

.. math::
   :label: eqnFitVariance

   \sigma_y^2 =
   \frac{1}{N-5}\sum_{i=1}^N(y_{mi}-\bar{y}_m)^2-(y_{pi}-\bar{y}_m)^2

The covariance matrix of the fit function can be formed:

.. math::
   :label: eqnCovariance

   \mathbf{U} = \sigma_y^2\mathbf{H}^{-1}

where :math:`\mathbf{H}` is the Hessian _[Hubbard1989b].  :math:`\mathbf{U}` is
a :math:`5\times5` matrix with the variances of each of the five fit parameters
along the diagonal.  The variance of :math:`T` can be computed using the
variance of :math:`\zeta` and :math:`\omega`. It is important to note that the
uncertainties in the period are very low (:math:`<1e-4`), even for the fits
with low :math:`r^2` values.

Torsional Pendulum
------------------

A torsional pendulum was used to measure all moments of inertia about axes in
the laterally symmetric plane of each of the wheels, fork and frame. The
pendulum is made up of a rigid mount, an upper clamp, a torsion rod, and
various lower clamps.

.. _figFixture:

.. figure:: figures/physicalparameters/fixture.jpg
   :align: center

   The rigid pendulum fixture mounted to a concrete column.

A 5 mm diameter, ~1 m long mild steel rod was used as the torsion spring. A
lightweight, low relative moment of inertia clamp was constructed that could
clamp the rim and the tire. The moments of inertia of the clamps were
neglected. The wheel was hung freely such that the center of mass aligned with
the torsional pendulum axis and then secured. The wheel was then perturbed and
oscillated about the pendulum axis. The rate gyro was mounted on the clamp
oriented along the pendulum axis.

The torsional pendulum was calibrated using a rod with known moment of inertia
Figure :ref:`figRod`. A torsional pendulum almost identical to the one used in
:ref:`Kooijman2006` was used to measure the average period
:math:`\overline{T}_i` of oscillation of the rear frame at three different
orientation angles :math:`\beta_i`, where :math:`i=1`, :math:`2`, :math:`3`, as
shown in Figure :ref:`figTriangle`. The parts were perturbed lightly, around 1
degree, and allowed to oscillate about the pendulum axis through several
periods. This was repeated at least three times for each frame and the recorded
periods were averaged.

.. _figRod:

.. figure:: figures/physicalparameters/rod.jpg
   :align: center

   The steel calibration rod. The moment of inertia of the rod,
   :math:`I=\\frac{m}{12}(3r^2+l^2)`, can be used to estimate the stiffness of
   the pendulum, :math:`k=\\frac{4I\\pi^2}{\\overline{T}^2}`, with
   :math:`k=5.62\\pm0.02 \\frac{\\textrm{Nm}}{\\textrm{rad}}`.


WHEELS
------

Estimating the full inertia tensors of the wheels is less complex because the
wheels are assumed symmetric about three orthogonal planes forcing all products of
inertia to be zero. The :math:`I_{xx}=I_{zz}` moments of inertia were calculated
by measuring the averaged period of oscillation about an axis in the
:math:`XZ`-plane using the torsional pendulum setup and Equation :eq:`torPend`.
The wheels are assumed to be laterally symmetric about any radial axis.
Thus only two moments of inertia are required for the set of benchmark
parameters. The moment of inertia about the axle was measured by hanging the
wheel as a compound pendulum, Figure :ref:`figWheelIyy`. The wheel was hung on a
horizontal rod and perturbed to oscillate about the axis of the rod. The rate
gyro was attached to the spokes near the hub and oriented mostly along the axle
axis. The wheels for the Delft bicycles would rotate at the rod contact point
about the vertical axis which added a very low frequency component of rate
along the vertical radial axis, but this should have had little affect the
period estimation about the compound pendulum axis. A fixture was designed for
the Davis bicycles that prevented non-desired rotation.  The pendulum length is
the distance from the rod/rim contact point to the mass center of the wheel.
The inner diameter of the rim was measured and divided by two to get
:math:`l_\mathrm{F,R}`. The moment of inertia about the axle is calculated
from:

.. math::
   :label: eqCompoundInertia

   I_{\mathrm{R}yy} = \left(\frac{\bar{T}}{2\pi}\right)^2m_\mathrm{R}gl_\mathrm{R} -
    m_\mathrm{R}l^2

.. _figFwheelTor:

.. figure:: figures/physicalparameters/CrescendoFwheelTorsionalFirst.jpg

   The front wheel of the Crescendo hung as a torsional pendulum.

.. _figWheelIyy:

.. figure:: figures/physicalparameters/wheelIyy.jpg

   A wheel hung as a compound pendulum.

The radial moment of inertia was measured by hanging the wheel as a torsional
pendulum, Figure :ref:`figFwheelTor`. The wheel was hung freely such that the
center of mass aligned with the torsional pendulum axis and then secured. The
wheel was then perturbed and oscillated about the vertical pendulum axis. The
radial moment of inertia can can calculated as such:

.. math::
   :label: eqWheelTorInertia

   I_{xx} = \frac{k\bar{T}^2}{4\pi^2}


FRAME
-----

At least three measurements were made to estimate the globally referenced
moments and products of inertia (:math:`I_{xx}`, :math:`I_{xz}` and
:math:`I_{zz}`) of the rear frame. The frame was typically hung from either the
three main tubes: seat tube, down tube and top tube, the seat post or a fixture
mounted to the brake mounts Figure :ref:`figLevel`. The rear fender prevented
easy connection to the seat tube on some of the bikes and the clamp was
attached to the fender. The fender was generally less rigid than the frame
tube. For best accuracy with only three orientation angles, the frame should be
hung at three angles that are :math:`120^\circ` apart. The three tubes on the
frame generally provide that the orientation angles were spread evenly at about
:math:`120^\circ`. Furthermore, taking data at more orientation angles improved
the accuracy and was generally possible with standard diamond frame bicycles.

Three moments of inertia :math:`J_{i}` about the pendulum axes were calculated
using :eq:`eqTorPend`.

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
matrix relating the two frames, Figure :ref:`figAngles`. The global inertia
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

The first entry of :math:`\mathbf{J}_i` in Equation :eq:`eqRotIn` is the moment of
inertia about the pendulum axis and is written explicitly as

.. math::
   :label:eqInRelComp

   J_{i}=c^{2}_{\beta i}I_{xx}-2s_{\beta i}c_{\beta i}I_{xz}+s^{2}_{\beta i}I_{zz}\textrm{.}

Similarly, calculating all three, or more, :math:`J_{i}` allows one to form

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
compound pendulum at the wheel axis, Figure :ref:`figFrameCompound`. Equation
:eq:`eqCompoundInertia` is used but with the mass of the frame and the frame
pendulum length.

.. math::
   :label: eqFramePendLength

   l_B=\sqrt{x_B^2+(z_B+r_R)^2}

.. _figFrameCompound:

.. figure:: figures/physicalparameters/YellowFrameCompoundFirst.jpg

   Rear frame hung as a compound pendulum.

.. _figForkCompound:

.. figure:: figures/physicalparameters/BrowserInsForkCompoundFirst.jpg

   Browser fork hung as a compound pendulum.


FORK AND HANDLEBAR
------------------

The inertia of the fork and handlebar is calculated in the same way as the
frame. The fork is hung as both a torsional pendulum, Figure
:ref:`figStratosFork`, and as a compound pendulum, Figure
:ref:`figForkCompound`. The fork provides fewer mounting options to obtain at
least three equally spaced orientation angles, especially if there is no
fender. We designed a connection to the brake mounts for the Davis bicycles.
The torsional calculations follow equations :eq:`eqTorPend` through
:eq:`eqInRel` and the compound pendulum calculations is calculated with
Equation :eq:`eqCompoundInertia`. The fork pendulum length is calculated using

.. math::
   l_H=\sqrt{(x_H-w)^2+(z_H+r_F)^2}

.. _figStratosFork:

.. figure:: figures/physicalparameters/stratosFork.jpg

    The Stratos fork and handlebar assembly hung as a torsional pendulum.

Human Parameters
================

To properly model the bicycle rider system it is necessary to estimate the
physical parameters of the bicycle rider. The measurement of the physical
properties of a human is more difficult than for a bicycle because the human
body parts are not as easily described as rigid bodes with defined joints and
inflexible geometry.Human mass, center of mass and inertia properties have been
measured and estimated in a multitude of ways.  Each method has its advantages
and disadvantages. The inertia properties of a human are not as clearly defined
as the bicycle, due to the human's daily varying mass, wobbly mass, flexibility
etc. I approached the parameter estimation in an analytical fashion. Both
methods that were used were based on estimating the inertial parameters from
mass and geometry measurement along with a human body density estimate.

Many methods exist for estimating the geometry, centers of mass and moments of
inertia of a human including cadaver measurements _[Dempster1955],
_[Clauser1969], _[Chandler1975], photogrammetry, ray scanning techniques
_[Zatsiorsky1983], _[Zatsiorsky1990], water displacement _[Park1999], and
mathematical geometrical estimation of the body segments _[Yeadon1990a]. We
estimated the physical properties of the rider in a seated position using a
simple mathematical geometrical estimation similar in idea to _[Yeadon1990a] in
combination with mass data from _[Dempster1955].

 Döhring
_[Dohring1953] measured the moments of inertia and centers of mass of a combined
rider and motor-scooter with a large measurement table, but this is not always
practical.  The validity of the presented methods could be determined if such
data existed for a bicycle and rider.

Moore method
------------

This method is a simplified model of the ten major body parts of a human.
Several measurements of the human rider were needed to calculate the physical
properties. The mass of the rider was measured along with fourteen
anthropomorphic measurements of the body (Tab. tab:riderDimensions and
Tab. tab:segmentMass). These measurements in combination with the geometrical
bicycle measurements taken in the previous section (Tab. tab:bicycleDimensions)
are used to define a model of the rider made up of simple geometrical shapes
(Fig. fig:model). The legs and arms are represented by cylinders, the torso by
a cuboid and the head by a sphere. The feet are positioned at the center of the
pedaling axis to maintain symmetry about the :math:`$XZ$`-plane.

All but one of the anthropomorphic measurements were taken when the
rider was standing casually on flat ground. The lower leg length
:math:`$l_{ll}$` is the distance from the floor to the knee joint.
The upper leg length :math:`$l_{ul}$` is the distance from the knee
joint to the hip joint. The length from hip to hip :math:`$l_{hh}$`
and shoulder to shoulder :math:`$l_{ss}$` are the distances between
the two hip joints and two shoulder joints, respectively. The torso
length :math:`$l_{to}$` is the distance between hip joints and
shoulder joints. The upper arm length :math:`$l_{ua}$` is the
distance between the shoulder and elbow joints. The lower arm
length :math:`$l_{al}$` is the distance from the elbow joint to the
center of the hand when the arm is outstretched. The circumferences
are taken at the cross section of maximum circumference (e.g.
around the bicep, around the brow, over the nipples for the chest).
The forward lean angle :math:`$\lambda_{fl}$` is the approximate
angle made between the floor (:math:`$XY$`-plane) and the line
connecting the center of the rider's head and the top of the seat
while the rider is seated normally on the bicycle. This was
estimated by taking a side profile photograph of the rider on the
bicycle and scribing a line from the head to the top of the seat.
The measurements were made as accurately as possible with basic
tools but no special attention is given further to the accuracy of
the calculations due to the fact that modeling the human as basic
geometric shapes already introduces a large error. The values are
reported to the same decimal places as the previous section for
consistency.

The masses of each segment (Tab. tab:segmentMass) were defined as a
proportion of the total mass of the rider :math:`$m_{\mathrm{B}r}$`
using data from cadaver studies by {Dempster1955}.

The geometrical and anthropomorphic measurements were converted
into a set of 31 grid points in three dimensional space that mapped
the skeleton of the rider and bicycle (Fig. fig:model). The
position vectors to these grid points are listed in
Tab. tab:gridPoints. Several intermediate variables used in the
grid point equations are listed in Tab. tab:intVar where
:math:`$f_o$` is the fork offset and the rest arise from the
multiple solutions to the location of the elbow and knee joints and
have to be solved for using numeric methods. The correct solutions
are the ones that force the arms and legs to bend in a natural
fashion. The grid points mark the center of the sphere and the end
points of the cylinders and cuboid. The segments are aligned along
lines connecting the appropriate grid points. The segments are
assumed to have uniform density so the centers of mass are taken to
be at the geometrical centers. The midpoint formula is used to
calculate the local centers of mass for each segment in the global
reference frame. The total body center of mass can be found from
the standard formula
:math:`$$\mathbf{r}_{\mathrm{B}r}=\frac{\sum{m_i\mathbf{r}_i}}{m_{\mathrm{B}r}}=\left[0.291\quad0\quad-1.109\right]\mathrm{m}
\label{eq:CoM}
$$`
where :math:`$\mathbf{r}_i$` is the position vector to the centroid
of each segment and :math:`$m_i$` is the mass of each segment. The
local moments of inertia of each segment are determined using the
ideal definitions of inertia for each segment type
(Tab. tab:locInertia). The width of the cuboid representing the
torso :math:`$l_y$` is defined by the shoulder width and upper arm
circumference.
:math:`$$l_y=l_{ss}-\frac{c_{ua}}{\pi}
\label{eq:cuboidWidth}
$$`
The cuboid thickness was estimated using the chest circumference
measurement and assuming that the cross section of the chest is
similar to a stadium shape.
:math:`$$l_x=\frac{c_{ch}-2l_y}{\pi-2}
\label{eq:cuboidThick}
$$`
The local :math:`$\hat{\mathbf{z}}_i$` unit vector for the segments
was defined along the line connecting the associated grid points
from the lower numbered grid point to the higher numbered grid
point. The local unit vector in the :math:`$y$` direction was set
equal to the global :math:`$\hat{\mathbf{Y}}$` unit vector with the
:math:`$\hat{\mathbf{x}}_i$` unit vector following from the right
hand rule. The rotation matrix needed to rotate each of the moments
of inertia to the global reference frame can be calculated by
dotting the global unit vectors :math:`$\hat{\mathbf{X}}$`,
:math:`$\hat{\mathbf{Y}}$`, :math:`$\hat{\mathbf{Z}}$` with the
local unit vectors :math:`$\hat{\mathbf{x}}_i$`,
:math:`$\hat{\mathbf{y}}_i$`, :math:`$\hat{\mathbf{z}}_i$` for each
segment.
:math:`$$\mathbf{R}_i=
    \left[
    \begin{array}{ccc}
        \hat{\mathbf{X}}\cdot\hat{\mathbf{x}}_i & \hat{\mathbf{X}}\cdot\hat{\mathbf{y}}_i & \hat{\mathbf{X}}\cdot\hat{\mathbf{z}}_i\\
        \hat{\mathbf{Y}}\cdot\hat{\mathbf{x}}_i & \hat{\mathbf{Y}}\cdot\hat{\mathbf{y}}_i & \hat{\mathbf{Y}}\cdot\hat{\mathbf{z}}_i\\
        \hat{\mathbf{Z}}\cdot\hat{\mathbf{x}}_i & \hat{\mathbf{Z}}\cdot\hat{\mathbf{y}}_i & \hat{\mathbf{Z}}\cdot\hat{\mathbf{z}}_i\\
    \end{array}
    \right]
\label{eq:rotMat2}
$$`
The local inertia matrices are then rotated to the global reference
frame with
:math:`$$\mathbf{I}_i=\mathbf{R}_i\mathbf{J}_i\mathbf{R}^T_i\textrm{.}
\label{eq:rotInertia}
$$`
The local moments of inertia can then be translated to the center
of mass of the entire body using the parallel axis theorem
:math:`$$\mathbf{I}^*_i=\mathbf{I}_i+m_i
    \left[
    \begin{array}{ccc}
        d_y^2+d_z^2 & -d_xd_y & -d_xd_z\\
        -d_xd_y & d_z^2+d_x^2 & -d_yd_z\\
        -d_xd_z & -d_yd_z & d_x^2+d_y^2
    \end{array}
    \right]
\label{eq:PAT}
$$`
where :math:`$d_x$`, :math:`$d_y$` and :math:`$d_z$` are the
distances along the the :math:`$X$`, :math:`$Y$` and :math:`$Z$`
axes, respectively, from the local center of mass to the global
center of mass. Finally, the local translated and rotated moments
of inertia are summed to give the total moment of inertia of the
rider by
:math:`$$\mathbf{I}_{\mathrm{B}r}=\sum{\mathbf{I}^*_i}=\left[\begin{array}{ccc}8.00&0&-1.93\\0&8.07&0\\-1.93&0&2.36\end{array}\right]\mathrm{kg\ m}^2\textrm{.}
\label{eq:sumInertia}
$$`

Yeadon method
-------------

The Yeadon human inertial model was developed for estimating the inertial
parameters needed to describe a human model for complex gymnasitic manuevers.
It is essentially a more advanced and accurate method than the one presented.
There are 95 geometrical measurements of the human and a single mass
measurement for scaling the body part densities. Once the 


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

