.. _physicalparameters:

===================
Physical Parameters
===================

.. warning::

   This document is a draft which is updated regularly (Last updated |today|).
   Once I submit if for my doctoral degree at UC Davis, it will be done. So for
   now use at your own risk. The information may or may not be correct.
   Reviews, comments and suggestions are welcome.

.. todo:: Check the figure numbering in this Chapter.

Preface
=======

I was first concerned with the physical parameters of the bicycle and rider in
my multi-body dynamics class project [Moore2006]_. There I developed a method
of estimating the parameters from simply the geometry and mass of the bicycle
and rider. I cleaned that work up and presented it in Biarritz, France
[Moore2008]_. This method served me well until we needed to have more accurate
estimates of the parameters for the first instrumented bicycle I helped build
at TU Delft, see Chapter :ref:`delftbicycle`. I signed on to the task of
measuring the bike's physical parameters using the equipment and procedures
developed in [Kooijman2006]_ and to combine the reuslt with my basic human
model from [Moore2008]_ for the estimation of the complete system parameters of
the Whipple model.  These first measurements and the details of the human model
were eventually presented in San Diego [Moore2009a]_. During this work, Dr.
Hubbard encouraged me to think about the accuracy of the measurements in more
detail, as some of the practices we were using were not as accurate as they
could be. With that in mind and the fact that there was very little complete
data available on the physical parameters of real bicycles, I decided to
measure an assortment of bicycles we had available around the lab in Delft
[Moore2010]_. This was certainly a tedious task, but I believe a rich data set
was created and the measurement methodology tightened up considerably. Once I
was back in Davis, we setup almost identical equipment to measure the two new
bicycles we were constructing, see Chatper :ref:`davisbicycle`. Danique
Fintelman helped us come up with a more accurate geometry measurement. Steven
Yen also used the equipment to measure a children's bicycle with a gyro wheel.
Additionally, we improved the human parameter estimates when Chris Dembia
implemented Yeadon's human inertia model and we combined it with the accurate
bicycle measurements. These final methods for both bicycle and rider are
implemented in two open source software packages.


.. _secBicycleParameters:

Bicycle Parameters
==================

Accurate measurements of a bicycle's physical parameters are required for
realistic dynamic simulation and analysis. The most basic models require the
geometry, mass, mass location and mass distributions for the rigid bodies. More
complex models require estimates of tire characteristics, human
characteristics, friction, stiffness, damping, etc. In this chapter I present
the measurement of the minimal bicycle/rider parameters required for the
benchmark Whipple bicycle model presented in [Meijaard2007]_. This model is
composed of four rigid bodies, has ideal rolling and frictionless joints, and
is laterally symmetric. A set of 25 parameters describes the geometry, mass,
mass location and mass distribution of each of the rigid bodies. The
experimental methods used to estimate the parameters described herein are based
primarily on the work done in [Kooijman2006]_, [Kooijman2008]_ and
[Moore2009a]_ but have been refined for improved accuracy and methodology.

Koojiman's work was preceded by several others, I'll mention the most notable
measurements related to bicycles. Roland and Massing [Roland1971]_ measured the
physical parameters of a bicycle in much the same way as is presented,
including calculations of uncertainty from the indirect measurement techniques.
Patterson [Patterson2004]_ used a swing to measure the roll inertia of
recumbent bicycles with a rider. [Connors2009]_ and [Stevens2009]_ used a
computer aided design package to estimate the parameters.  [Escalona2010]_
measured a bicycle for his bicycle dynamics class in Spain. Some notable
motorcycle and scooter measurements include [Dohring1953]_, [Dohring1955]_,
[Singh1971]_, [Eaton1973]_, [Roland1973]_, [Zytveld1975]_, and [Sharp1997b]_.

Here I document the indirect measurement of ten real bicycles' physical
parameters. We improve upon previous methods by both increasing and reporting
the accuracies of the measurements and by measuring the complete moments of
inertia of the laterally symmetric frame and fork needed for analysis of the
nonlinear model. Furthermore, very little data exists on the physical
parameters of different types of bicycles and this work aims to provide a small
sample of bicycles.

We measured the physical characteristics of eleven different bicycles, three of
which were set up in two different configurations. The first six bicycles,
chosen for both variety and convenience, are as follows: *Batavus Browser*, a
Dutch style city bicycle measured with and without instrumentation as described
in [Kooijman2009a]_; *Batavus Stratos Deluxe*, a Dutch style sporty city
bicycle; *Batavus Crescendo Deluxe* a Dutch style city bicycle with a suspended
fork; *Gary Fisher Mountain Bike*, a hard-tail mountain bicycle; *Bianchi
Pista*, a modern steel frame track racing bicycle; and *Yellow Bicycle*, a
stripped down aluminum frame road bicycle measured in two configurations, the
second with the fork rotated in the head tube 180 degrees for larger trail. The
last two bicycles were measured in Davis: the instrumented bicycle presented in
chapter :ref:`davisbicycle` and a children's bicycle with a stabilizing
flywheel called the GyroBike.

These eleven different parameter sets can be used with, but are not limited to,
the benchmark bicycle model. The accuracy of all the measurements are
presented. The accuracies are based measurement inaccuracies and the proper use
of error propagation theory with correlations taken into account.

.. _secParameters:

Parameters
----------

I was primarily concerned with measuring and estimating the 25 parameters
associated with the benchmark Whipple bicycle model which is derived and
described in [Meijaard2007]_. The unforced two degree-of-freedom,
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
[Meijaard2007]_ are not necessarily a minimum set for the Whipple model, as
shown in [Sharp2008a]_, but are useful none-the-less as they represent
intuitively measurable quantities and have become become standard due to the
nature of the benchmark. They are also not parameters used in my derivation in
Chapter :ref:`eom` but can easily be converted, as was shown. I did not
concern myself with measuring many more parameters than are required due to
the assumptions of the Whipple model such as no-slip tires, lateral symmetry,
knife edge wheels, etc.

The 25 parameters can be measured using many techniques. In general, I
attempted to measure the benchmark parameter as directly as possible to improve
the accuracy.

Bicycle Descriptions
--------------------

We measured a total of eight bicycles in eleven configurations, :ref:`Figure 1
<figBicycles>`. The three Batavus bicycles were donated by the manufacturer.
We asked for a bicycle that they considered stable and one that they did not.
They offered the Browser as a "stable" bicycle and the Stratos as "nervous".
The Crescendo was considered average handling. We measured an instrumented
version of the Browser that was used in the experiments described in Chapter
:ref:`delftbicycle`. The Fisher and the Pista were chosen to provide some
variety, a mountain and road bike. The yellow bike is used to demonstrate
bicycle stability and the forked is reversed to provide better stability when
perturbed with no rider. The Davis instrumented bicycle is an instrumented
bicycle described in Chapter :ref:`davisbicycle` and we measured the frame in
configurations for different rider seating positions. The child's bicycle has
the GyroWheel product installed in the front wheel. The first six of these
bicycles were measured in Delft and will hereafter be referred to as the *Delft
Bicycles*. The remaining two bicycles were measure in Davis and will be
referred to as the *Davis Bicycles*.

.. _figBicycles:

.. figure:: figures/physicalparameters/bicycles.*
   :width: 3.75in
   :align: center
   :target: _images/bicycles.jpg

   The ten measured bicycles: (a) Batavus Browser, (b) Instrumented Batavus
   Browser, (c) Batavus Crescendo Deluxe, (d) Batavus Stratos Deluxe, (e) Gary
   Fisher, (f) Bianchi Pista, (g) Yellow Bicycle, (h) Yellow Bicycle with
   reversed fork, (i) Davis Instrumented Bicycle, (j) Gyro Bicycle. The Davis
   Instrumented Bicycle was measured twice each with the body cast and seat
   height in different positions. The first "Rigid" was set up for Jason and
   the second "Rigidcl" was set up for Luke and Charlie.

.. _secAccuracy:

Accuracy
--------

I have attempted to report the accuracy of the measurements of the parameters.
Following the footsteps of [Roland1971]_ I used error propagation theory to
calculate accuracy of the 25 benchmark parameters. I began by estimating the
standard deviation of the actual measurements taken, see Section
:ref:`secBicycleMeasuredParameters`. If :math:`x` is a parameter and is a function of
the measurements, :math:`u,v,\ldots`, which are Gaussian random variables then
:math:`x` is also a Gaussian random variable defined as
:math:`x=f(u,v,\ldots)`. The sample variance of :math:`x` is defined as

.. math::
   :label: sampleVariance

   s_x^2 =
   \frac{1}{N-1}\sum^N_{i=1}
   \left[(u_i - \bar{u})^2\left(\frac{\partial x}{\partial u}\right)^2 +
   (v_i - \bar{v})^2\left(\frac{\partial x}{\partial v}\right)^2 +
   2(u_i - \bar{u})(v_i - \bar{v})\left(\frac{\partial x}{\partial u}\right)
   \left(\frac{\partial x}{\partial v}\right)
   + \ldots\right]

Using the definitions for variance and covariance, Equation
:eq:`sampleVariance` can be simplified to

.. math::
   :label: variance

   s_x^2 = s_u^2\left(\frac{\partial x}{\partial u}\right)^2 +
           s_v^2\left(\frac{\partial x}{\partial v}\right)^2 +
           2s_{uv}\left(\frac{\partial x}{\partial u}\right)
           \left(\frac{\partial x}{\partial v}\right)
           + \ldots

If :math:`u` and :math:`v` are uncorrelated then :math:`s_{uv}=0`. Most of the
calculations hereafter have uncorrelated variables but a few do not and the
covariance has to be taken into account. Equation :eq:`variance` can be used to
calculate the variance of all types of functions. I made use of the Python
package `uncertainties <http://pypi.python.org/pypi/uncertainties/>`_
[Lebigot2001]_ to simplify the book keeping of the correlations and variance
calculations , thus some of the equations for the error are not shown in the
following sections.

.. _secGeometry:

Geometry
--------

The geometry measurements of the Delft bicycles focused on measuring the
benchmark parameters: trail, wheelbase, and steer axis tilt as directly as
possible. I also present an alternative method for the geometry used with the
Davis bicycles that attempts to measure the distances in my model derivation,
Chapter :ref:`eom`, which improves the accuracy of the parameters. Keep in mind,
that I assumed that the frame did not flex and that the wheel radii do not
change with rider weight when taking geometric measurements.

.. _secWheelRadii:

Wheel Radii
~~~~~~~~~~~

The radii of the front :math:`r_\mathrm{F}` and rear :math:`r_\mathrm{R}`
wheels were estimated by measuring the linear distance traversed along the
ground through at least ten rotations of the wheel. Each wheel traversal was
measured separately and the measurements were taken with rider seated on the
bicycle, except for the gyro bicycle which had no rider. A 72 kg rider sat on
the Delft bicycles and an 84 kg rider on the Davis instrumented bicycle
[#weight]_. A 30 meter tape measure (resolution: 2mm) was pulled tight and
taped on a flat level smooth floor for the Delft bicycles and we marked a 68
foot length on the floor and used a 1/16 inch resolution ruler to measure the 6
to 15 inch additional distance for the Davis bicycles. The tire was marked and
aligned with the tape measure :ref:`Figure 2 <figTireChalk>`. The accuracy of the
distance measurement is approximately :math:`\pm0.01` meter. The tires were
pumped to the recommended inflation pressure before the measurements. The wheel
radius is calculated by

.. math::
    :label: wheelRadius

    r\pm\sigma_r=
    \frac{d}{2\pi n}
    \pm\left(\frac{\sigma_d}{2\pi n}\right)

where :math:`r` is the wheel radius, :math:`d`, is the traversal distance,
:math:`n`, is the number of rotations and :math:`\sigma` is the respective
standard deviation of the subscripted variable. I use subscripts :math:`F` and
:math:`R` from front and rear wheels, respectively, in the measurement tables in
Section :ref:`secBicycleMeasuredParameters`.

.. _figTireChalk:

.. figure:: figures/physicalparameters/tire-chalk.*
   :align: center
   :width: 4in
   :target: _images/tire-chalk.jpg

   Wheel and tire with chalk mark aligned to the tape measure.

.. _secHeadtube:

Head Tube Angle
~~~~~~~~~~~~~~~

For the Delft Bicycles, the head tube angle was measured directly using an
electronic level, :ref:`Figure 3 <figHeadTube>`. The bicycle frame was fixed
perpendicular to the ground, the steering angle was set to the nominal
position, tire pressures were at recommended levels, and the bicycle was
unloaded. The steer axis tilt :math:`\lambda` is the complement to the head
tube angle, :math:`\gamma`.

.. math::
   :label: eqHeadTubeAngle

   \lambda\pm\sigma_\lambda
   =\frac{\pi}{180^{\circ}}(90^{\circ}-\gamma)
   \pm\left(\frac{\pi}{180^\circ}\right)\sigma_{\gamma}

.. _figHeadtube:

.. figure:: figures/physicalparameters/headtube.*
   :align: center
   :width: 2.5in
   :target: _images/headtube.jpg

   The digital level set against the Yellow Bicycle's head tube.

.. _secTrail:

Trail
~~~~~

The idealized trail is difficult to measure directly due to the fact that the
tire has a contact patch and there is no distinct contact point. I instead
chose to measure the fork offset, :math:`f_o`, and compute the ideal trail. The
fork offset was measured by clamping the steer tube of the front fork into a
v-block on a flat table, :ref:`Figure 4 <figForkOffset>`. For the Delft
bicycles, a ruler was used to measure the height of the center of the head tube
and the height of the center of the axle axis, and for the Davis bicycles we
made use of more accurate height gages. The fork blades were aligned such that
the axle axis was parallel to the table surface.

.. math::
   :label: eqTrail

   c=\frac{r_\mathrm{F}\sin{\lambda}-f_o}{\cos{\lambda}}

.. math::
   :label: eqTrailVar

   \sigma_{c}^{2}=\sigma_{r_{\mathrm{F}}}^{2}\tan^2{\lambda} -
   \sigma_{f_o}^{2}\sec^2{\lambda} +
   \sigma_{\lambda}^{2}\left(r_\mathrm{F}\sec^2{\lambda} -
   f_o\sec{\lambda}\tan{\lambda}\right)^2

.. _figForkOffset:

.. figure:: figures/physicalparameters/fork-offset.*
   :align: center
   :width: 2.5in
   :target: fork-offset.jpg

   The fork of the Davis Bicycle setup for measuring the fork offset.

.. _secWheelbase:

Wheelbase
~~~~~~~~~

I measured the wheelbase directly with the bicycle in nominal configuration
described in Section :ref:`secHeadtube`. We used a tape measure to measure the
distance from one wheel axle center to the other.

Alternative Geometry Measurement Method
---------------------------------------

The geometry for the bicycle model presented in Chapter:`eom` can almost be
measured directly. I used this method for the Davis Bicycles. The bicycle frame
is set on a granite measurement table such that the head tube is in a v-block
and parallel to the table surface and the bicycle frame is situated such that
the frame is perpendicular to the table surface, :ref:`Figure 5
<figAlternativeGeometry>`. The is fork rotated in the head tube such that the
fork blades curve upwards. Two dummy axles are fit into the front and rear
dropouts and the axles are ensured to be parallel to the table surface. The
height from the table surface to the top of each axle are recorded with a
height gage and the diameters of the axles are measured with a micrometer or
caliper.

.. _figAlternativeGeometry:

.. figure:: figures/physicalparameters/alternative-geometry.*
   :align: center
   :width: 2.7in
   :target: _images/alternative-geometry.png

   The actual measurements taken to compute the basic bicycle geometry.

These measurements can then be converted to the three essential bicycle
dimensions, :math:`d_1`, :math:`d_2`, :math:`d_3` described in Chapter
:ref:`eom`.

.. math::
   :label: d1

   d_1 = h_1 + h_2 - h_3 + \frac{\hat{d}_1 - \hat{d}_2}{2}

.. math::
   :label: d3

   d_3 = h_4 - h_5 + \frac{\hat{d}_4 - \hat{d}_3}{2}

.. math::
   :label: d2

   d_2 = \sqrt{\left(d + \frac{\hat{d}_2 + \hat{d}_3}{2}\right)^2 - (d_1 - d_2)^2}

The traditional [Meijaard2007]_ parameters can then be calculated. If the
:math:`r_F` does not equal :math:`r_R` then the steer axis tilt cannot be
computed analytically as Equation :eq:`eqLambda`  holds.

.. math::
   :label: eqLambda

   \operatorname{sin}(\lambda) = \frac{r_F - r_R + d_2 \operatorname{cos}(\lambda)}{d_1 + d_3}

It is trivial to find the solution to Equation :eq:`eqLambda` numerically. If
:math:`r_F=r_R`, the solution for :math:`\lambda` is analytic.

.. math::
   :label: lambdaEqualRadii

   \lambda = \operatorname{arctan}\left(\frac{d_2}{d_1 + d_3}\right)

The wheelbase is

.. math::
   :label: eqWheelbase

    w = (d_1 + d_3) \operatorname{cos}(\lambda) + d_2 \operatorname{sin}(\lambda)

and trail is then computed with Equation :eq:`eqTrail`, realizing :math:`f_o = d_3`:

.. math::
   :label: eqTrailD3

    c = \frac{r_F \operatorname{sin}(\lambda) - d_3}{\operatorname{cos}(\lambda)}

.. _secMass:

Mass
----

For the Delft bicycles, each of the four bicycle parts were measured using a
Molen 20 kilogram scale with a resolution of 20 grams. The accuracy was
conservatively assumed to also be :math:`\pm20` grams. Also, the total mass was
measured using a spring scale with a resolution of 100 grams. The total mass
was only used for comparison purposes, as it was not very accurate. The mass of
the parts of the Davis bicycles were measured with a digital scale with a
resolution of 50 grams (A & D FV-150k Industrial Scale).

.. _figMassScale:

.. figure:: figures/physicalparameters/mass-scale.*
   :align: center
   :width: 3in
   :target: _images/mass-scale.jpg

   figMassScale

   The scale used to measure the mass of each Delft bicycles' components.

.. _secCenterOfMass:

Center of Mass
--------------

.. _secWheelCoM:

Wheels
~~~~~~

The centers of mass of the wheels were assumed to be at their geometrical
centers to comply with the Whipple model. This was also assumed for the
flywheel in the gyro bike.

.. _secRearFrameCoM:

Rear Frame
~~~~~~~~~~

The rear frame bicycle configuration was hung in at least three orientations
through the assumed lateral plane of symmetry. I assumed that the frame was
laterally symmetric, complying with the Whipple model, thus reducing the need
to use a more complex three dimensional measurement setup. The frame could
rotate about a joint such that gravity aligned the center of mass with the
support rod axis. The orientation angle of the steer axis,
:math:`\alpha_\mathrm{B}`, see :ref:`Figure 7 <figAngles>`, relative to the
earth was measured using a digital level (:math:`\pm0.2^{\circ}` accuracy),
:ref:`Figure 8 <figPendulumAngle>`. A thin string was aligned with the pendulum
axis which passed by the frame. The horizontal distance :math:`a_\mathrm{B}`
between the rear axle and the string was measured by aligning a 1 mm resolution
ruler perpendicular to the string :ref:`Figure 9 <figPendulumDistance>`. The
distance :math:`a_\mathrm{B}` was negative if the string fell to the right of
the rear axle and positive if it fell to the left of the rear axle, when
viewing the bicycle from the right side. These measurements allow for the
calculation of the center of mass location in the global reference frame.

.. _figAngles:

.. figure:: figures/physicalparameters/angles.*
   :align: center
   :width: 3in
   :target: _images/angles.png

   Pictorial description of the angles and dimensions that related the nominal
   bicycle reference frame :math:`XYZ_B` with the pendulum reference frame
   :math:`XYZ_P`.

.. _figPendulumAngle:

.. figure:: figures/physicalparameters/pendulum-angle.*
   :align: center
   :width: 2.75in
   :target: _images/pendulum-angle.jpg

   The digital level was mounted to a straight edge aligned with the head tube
   of the bicycle frame. This was done without allowing the straight edge to
   touch the frame. The frame was not absolutely stationary so this was
   difficult. The light frame oscillations could be damped out by submerging a
   low hanging area of the frame into a bucket of water to decrease the
   oscillation.

.. _figPendulumDistance:

.. figure:: figures/physicalparameters/pendulum-distance.*
   :align: center
   :width: 2.75in
   :target: _images/pendulum-distance.jpg

   Measuring the distance from the pendulum axis to the rear wheel axle using
   a level ruler.

The frame rotation angle :math:`\beta_\mathrm{B}` is defined as rotation of the
frame in the nominal benchmark configuration to the hanging orientation,
rotated about the :math:`Y` axis.

.. math::
   :label: eqFrameRotAng

   \beta_\mathrm{B} = \lambda - \alpha_\mathrm{B}

   \sigma_{\beta}^{2} = \sigma_{\lambda}^{2} + \sigma_{\alpha}^{2}

The center of mass can be found by realizing that the pendulum axis :math:`X_P`
is simply a line in the nominal bicycle reference frame with a slope :math:`m`
and a z-intercept :math:`b` where the :math:`i` subscript corresponds the
different frame orientations, see :ref:`Figure 10 <figTriangle>`. The slope can
be shown to be

.. math::
   :label: eqSlope

   m_{\mathrm{B}i} = -\tan{\beta_{\mathrm{B}i}}

   \sigma_{m}^{2} = \sigma_{\beta}^{2}\sec^{4}{\beta}

.. _figTriangle:

.. figure:: figures/physicalparameters/com-triangle.*
   :align: center
   :width: 2.75in
   :target: _images/com-triangle.png

   Exaggerated intersection of the three pendulum axes and the location of the
   center of mass.

The z-intercept can be shown to be

.. math::
   :label: eqZInt

   b_{\mathrm{B}i} = -\left(\frac{a_{\mathrm{B}i}}{\cos{\beta_{\mathrm{B}i}}} +
   r_\mathrm{R}\right)

   \sigma_{b}^{2} = \sigma_{a}^{2}\sec^{2}{\beta} +
   \sigma_{r_\mathrm{R}}^{2} +
   \sigma_{\beta}^{2}a^{2}\sec^{2}{\beta}\tan^{2}{\beta}

Theoretically, the center of mass lies on each line but due to experimental
error, if there are more than two lines, the lines do not cross all at the same
point. Only two lines are required to calculate the center of mass of the
laterally symmetric frame, but more orientations increase the center of mass
measurement accuracy. The three lines are defined as

.. math::
   :label: eqLine

   z_{\mathrm{B}i}(x) = m_{\mathrm{B}i} x + b_{\mathrm{B}i}

The mass center location can be calculated by finding the intersection of these
three lines. Two approaches were used used to calculate the center of mass.
Intuition leads one to think that the center of mass may be located at the
centroid of the triangle made by the three intersecting lines. The centroid can
be found by calculating the intersection point of each pair of lines and then
averaging the three intersection points [#leastsquares]_.

.. math::
   :label: eqLinearSystem

    \begin{bmatrix}
        x_a\\
        z_a
    \end{bmatrix}
    =
    \begin{bmatrix}
        -m_1 & 1\\
        -m_2 & 1
    \end{bmatrix}^{-1}
    \begin{bmatrix}
        b_1\\
        b_2
    \end{bmatrix}

    \begin{bmatrix}
        x_b\\
        z_b
    \end{bmatrix}
    =
    \begin{bmatrix}
        -m_1 & 1\\
        -m_3 & 1
    \end{bmatrix}^{-1}
    \begin{bmatrix}
        b_1\\
        b_3
    \end{bmatrix}

    \begin{bmatrix}
        x_c\\
        z_c
    \end{bmatrix}
    =
    \begin{bmatrix}
        -m_2 & 1\\
        -m_3 & 1
    \end{bmatrix}^{-1}
    \begin{bmatrix}
        b_2\\
        b_3
    \end{bmatrix}

.. math::
   :label: eqXCenter

   x_\mathrm{B} = \frac{x_a + x_b + x_c}{3}

.. math::
   :label: eqZCenter

   z_\mathrm{B} = \frac{z_a + z_b + z_c}{3}

.. _secForkCoM:

Fork and Handlebar
~~~~~~~~~~~~~~~~~~

The fork and handlebars are generally a bit trickier to hang in three different
orientations, :ref:`Figure 11 <figStratosFork>`. Typically two angles can be
obtained by clamping to the steer tube at the top and the bottom. The third
angle can be obtained by clamping to the stem. The center of mass of the fork
is calculated in the same fashion as the frame. The slope of the line in the
benchmark reference frame is the same as for the rear frame but the z-intercept
is different

.. math::
   :label: eqZIntFork

   b_{\mathrm{H}i} = w \tan{\beta_{\mathrm{H}i}} - r_\mathrm{F} -
   \frac{a}{\cos{\beta_{\mathrm{H}i}}}

   \sigma_{b}^{2} = \sigma_{w}^{2}\tan^{2}\beta +
   \sigma_{\beta}^{2}\left(w\sec^{2}\beta -
   a\sec\beta\tan\beta\right)^{2} + \sigma_{r_\mathrm{F}}^{2} +
   \sigma_{a}^{2}\sec^{2}\beta

.. _figStratosFork:

.. figure:: figures/physicalparameters/stratos-fork-pendulum.*
   :align: center
   :width: 2.75in
   :target: _images/stratos-fork-pendulum.jpg

   The Stratos fork and handlebar assembly hung as a torsional pendulum.

The fork of the Davis instrumented bicycle was connected to the handlebars by a
steer torque sensor with universal joint. Due to the fact that the sensor and
joint were not designed to support the weight of the adjacent components and
the fact that we needed the inertia of the portion above the torque sensor for
proper estimation of the steer torque applied by the rider [#steertorque]_, we
opted to measure the center of mass and inertia of the fork and handlebar
separately. The fork was measured as previously described, with the universal
joint locked in its nominal position. The handlebar was measured in a similar
fashion making use of small clamps to hang it in different orientations,
:ref:`Figure 11 <figHandlebar>`.

.. _figHandlebar:

.. figure:: figures/physicalparameters/handlebar.*
   :align: center
   :width: 2.5in

   The handlebar mounted as a torsional pendulum.

I choose the center of the stem clamp bolt to be the reference point (as was
the front and rear wheel centers for the front and rear frames). The location
of this point relative to the front wheel center was measured as shown in
:ref:`Figure 12 <figHandlebarGeometry>`.

.. _figHandlebarGeometry:

.. figure:: figures/physicalparameters/handlebar-geometry.*
   :align: center
   :width: 2.56in
   :target: _images/handlebar-geometry.png

   A diagram of how the handlebar reference point was located with respect to
   the front wheel center. These were the raw measurements taken.

The distances along and perpendicular to the steer axis from the front wheel
center to the handlebar reference point are as follows

.. math::
   :label: l1l2

   l_1 = h_7 - h_6 + \frac{\hat{d}_5 - \hat{d}_6}{2}

   l_2 = \left(l - \frac{]hat{d}_5 + \hat{d}_6}{2}\right)
   \operatorname{cos}\left[\operatorname{arcsin}\left(\frac{l_1}{l -
   \frac{\hat{d}_5+\hat{d}_6}{2}}\right)\right]

The distance from the front wheel center to the handlebar reference point in
the global bicycle reference frame are

.. math::
   :label: u1u2

   u_1 = l_2 \operatorname{sin}(\lambda) - l_1 \operatorname{cos}(\lambda)

   u_2 = \frac{u_1}{\operatorname{tan}(\lambda)} + \frac{l_1}{\operatorname{sin}(\lambda)}

The center of mass in computed with respect to the handlebar reference point
and :math:`u_1` and `u_2` locate the reference point of the handlebar to the
front wheel center and thus the global origin.

.. _secMoI:

Inertia
-------

The moments of inertia of the wheels, rear frame, and fork (and handlebar) were
measured both by taking advantage of the assumed symmetry of the parts and by
hanging the parts as both compound and torsional pendulums while measuring
their periods of oscillation when perturbed at small angles. The rate of
oscillation was measured using a `Silicon Sensing CRS03 100 deg/s rate gyro
<http://www.siliconsensing.com/CRS03>`_ for the Delft bicycles and a `Silicon
Sensing CRS04 200 deg/s rate gyro <http://www.siliconsensing.com/CRS04>`_ for
the Davis bicycles. The rate gyros were sampled at 1000 hz with a `National
Instruments USB-6008 12 bit data acquisition unit
<http://sine.ni.com/nips/cds/view/p/lang/en/nid/14604>`_ and at 500 hz with a
`National Instruments USB-6218 16 bit data acquisition unit
<http://sine.ni.com/nips/cds/view/p/lang/en/nid/203092>`_, respectively, and
the Matlab data acquisition toolbox. The measurement durations were between 15
and 30 secs and each moment of inertia measurement was performed at least three
times. No extra care was taken to calibrate the rate gyro, maintain a constant
power source (i.e. the battery drains slowly), or account for drift because I
was only concerned with the period. The raw voltage signal was used to
determine the period of oscillation which is needed for the moment of inertia
calculations, :ref:`Figure 13 <figVoltage>`.

.. _figVoltage:

.. figure:: figures/physicalparameters/BrowserFrameCompoundFirst2.*
   :align: center
   :width: 4in
   :target: _images/BrowserFrameCompoundFirst2.jpg

   Example portion of the raw voltage data taken during a 30 second measurement
   of the oscillation of the Browser rear frame as a compound pendulum.

The function Equation :eq:`eqDecayOs` was fit to the data using the least
squares method for each experiment to determine the quantities :math:`A`,
:math:`B`, :math:`C`, :math:`\zeta`, and :math:`\omega`.

.. math::
   :label: eqDecayOs

   f(t) = A + e^{-\zeta\omega t}\left[B\sin{\sqrt{1-\zeta^2}\omega t} +
   C\cos{\sqrt{1-\zeta^2}\omega t}\right]

Most of the data fit the damped oscillation function well with very light (and
potentially ignorable) damping. There were several instances in the Delft
experiments of beating-like phenomena for some of the parts at particular
orientations. Roland and Massing, [Roland1971]_, also encountered this problem
and used a bearing to prevent the torsional pendulum from swinging.
:ref:`Figure 14 <figBeating>` shows an example of the beating like phenomena. I
used Roland and Massing's solution to prevent this in the Davis measurements.

.. _figBeating:

.. figure:: figures/physicalparameters/CrescendoForkTorsionalFirst2.*
   :align: center
   :width: 4in
   :target: _images/CrescendoForkTorsionalFirst2.jpg

   An example of the beating-like phenomena observed during less than 5% of
   the Delft trials.

The physical phenomenon observed corresponding to data sets such as these
occurred when the bicycle frame or fork was perturbed torsionally. After set
into motion the torsional motion dampened and a longitudinal swinging motion
increased. The motions alternated back and forth with neither ever reaching
zero. The frequencies of these motions were very close to one another and it
was not apparent how dissect the two. We explored fitting to a function such as

.. math::
   :label: eqnSumSines

   y(t) = A\sin{(\omega_1 t)} + B\sin{(\omega_2 t + \phi)} + C

But the fit predicts that :math:`\omega_1` and :math:`\omega_2` are very
similar frequencies. There was no easy way to choose which of the two
:math:`\omega`'s was the one associated with the torsional oscillation. Some
work was done to model the torsional pendulum as a laterally flexible beam to
determine this, but we ended up assuming that the accuracy of the period
calculation would not improve enough for the effort required. The later
experiments simply prevented the swinging motion of the pendulum without
damping the torsional motion.

The period for a damped oscillation is

.. math::
   :label: eqnPeriodDamped

   T = \frac{2\pi}{\sqrt{1-\zeta^2}\omega_n}

The uncertainty in the period, :math:`T`, can be determined from
the fit. First, the variance of the fit is calculated

.. math::
   :label: eqnFitVariance

   \sigma_y^2 =
   \frac{1}{N-5}\sum_{i=1}^N(y_{mi}-\bar{y}_m)^2-(y_{pi}-\bar{y}_m)^2

The covariance matrix of the fit function can be formed

.. math::
   :label: eqnCovariance

   \mathbf{U} = \sigma_y^2\mathbf{H}^{-1}

where :math:`\mathbf{H}` is the Hessian [Hubbard1989b] of the fit function,
:eq:`eqDecayOs`.  :math:`\mathbf{U}` is a :math:`5\times5` matrix with the
variances of each of the five fit parameters along the diagonal.  The variance
of :math:`T` can be computed using the variance of :math:`\zeta` and
:math:`\omega`. It is important to note that the uncertainties in the period
are very low (:math:`<1e-4`) due to the high sample rate, even for the fits
with low :math:`r^2` values.

.. _secTorsionalPendulum:

Torsional Pendulum
~~~~~~~~~~~~~~~~~~

A torsional pendulum was used to measure all moments of inertia about axes in
the laterally symmetric plane of each of the wheels, fork and frame. The
pendulum is made up of a rigid mount, an upper clamp, a torsion rod, and
various lower clamps, :ref:`Figure 15 <figFixture>` .

.. _figFixture:

.. figure:: figures/physicalparameters/fixture.*
   :align: center
   :width: 2in
   :target: _images/fixture.jpg

   The rigid pendulum fixture from the Delft experiments mounted to a concrete
   column.

A mild steel rod was used as the torsion spring. Lightweight, low relative
moment of inertia clamps were constructed that could clamp the torsional rod to
the various bicycle parts. The moments of inertia of the clamps were neglected
[#clamps]_.

The torsional pendulum was calibrated using a rod with an easily computed, i.e.
"known", moment of inertia :ref:`Figure 16 <figRod>` [#rod]_. A torsional
pendulum almost identical to the one used in [Kooijman2006]_ was used to
measure the average period :math:`\overline{T}_i` of oscillation of the rear
frame at three different orientation angles :math:`\beta_i`, where :math:`i=1`,
:math:`2`, :math:`3`, as shown in :ref:`Figure 10 <figTriangle>`. The parts were
perturbed lightly, around 1 degree, and allowed to oscillate about the pendulum
axis through several periods. This was repeated at least three times for each
frame and the recorded periods were averaged.

.. _figRod:

.. figure:: figures/physicalparameters/rod.*
   :align: center
   :width: 2in
   :target: _images/rod.jpg

   The steel calibration rod. The moment of inertia of the rod, :math:`I_P =
   \frac{m_P}{12}(3 r_P^2 + l_P^2)`, can be used to estimate the stiffness of the
   pendulum, :math:`k = \frac{4 I_P \pi^2}{\overline{T_P}^2}`.

Wheels
~~~~~~

Estimating the full inertia tensors of the wheels is less complex because the
wheels are assumed symmetric about three orthogonal planes making all products
of inertia to be zero. The :math:`I_{xx}=I_{zz}` moments of inertia were
calculated by measuring the averaged period of oscillation about an axis in the
:math:`XZ_B`-plane using the torsional pendulum setup and Equation
:eq:`eqTorPend`. The wheels are assumed to be laterally symmetric about any
radial axis. Thus only two moments of inertia are required for the set of
benchmark parameters [Meijaard2007]_. The moment of inertia about the axle was
measured by hanging the wheel as a compound pendulum, :ref:`Figure 17
<figWheelIyy>`. The wheel was hung on a horizontal rod and perturbed to
oscillate about the axis of the rod. The rate gyro was attached to the spokes
near the hub and oriented mostly along the axle axis. The wheels for the Delft
bicycles would rotate at the rod contact point about the vertical axis which
added a very low frequency component of rate along the vertical radial axis,
but this should have little affect on the period estimation about the compound
pendulum axis. A fixture was designed for the Davis bicycles that prevented
non-desired rotation. The pendulum length is the distance from the rod/rim
contact point to the mass center of the wheel.  The inner diameter of the rim
was measured and divided by two to get :math:`l_\mathrm{F,R}`. The moment of
inertia about the axle is calculated from

.. math::
   :label: eqCompoundInertia

   I_{\mathrm{F,R}yy} = \left(\frac{\bar{T}_\mathrm{F,R}}{2\pi}\right)^2
   m_\mathrm{F,R} g l_\mathrm{F,R} - m_\mathrm{F,R} l_\mathrm{F,R}^2

.. _figWheelIyy:

.. figure:: figures/physicalparameters/wheelIyy.*
   :align: center
   :width: 2.75in
   :target: _images/wheelIyy.jpg

   A wheel hung as a compound pendulum.

The radial moment of inertia was measured by hanging the wheel as a torsional
pendulum, :ref:`Figure 18 <figFwheelTor>`. The wheel was first hung freely such
that the center of mass aligned with the torsional pendulum axis and then the
clamp secured. The wheel was then perturbed and oscillated about the vertical
pendulum axis. The radial moment of inertia can be calculated with

.. math::
   :label: eqWheelTorInertia

   I_{\mathrm{F,R}xx} = \frac{k\bar{T_\mathrm{F,R}}^2}{4\pi^2}

.. _figFwheelTor:

.. figure:: figures/physicalparameters/CrescendoFwheelTorsionalFirst.*
   :align: center
   :width: 2.75in
   :target: _images/CrescendoFwheelTorsionalFirst.jpg

   The front wheel of the Crescendo hung as a torsional pendulum.

Frame
~~~~~

At least three measurements were made to estimate the globally referenced
moments and products of inertia (:math:`I_{\mathrm{B}xx}`,
:math:`I_{\mathrm{B}xz}` and :math:`I_{\mathrm{B}zz}`) of the rear frame. The
rear frame was typically hung from either the three main tubes (seat tube, down
tube and top tube), the seat post, or a small fixture mounted to the brake
mounts :ref:`Figure 8 <figPendulumAngle>`. The rear fender prevented easy connection
to the seat tube on some of the bikes and the clamp was attached to the fender.
The fender was less rigid than the frame tube. For best accuracy with only
three orientation angles, the frame should be hung at three angles that are
:math:`120^\circ` apart. Attaching by the three tubes on the frame generally
provide that the orientation angles were spread evenly at about
:math:`120^\circ`. Furthermore, taking data at more orientation angles improved
the accuracy and was generally possible with standard diamond frame bicycles.

Three moments of inertia :math:`J_{\mathrm{B}i}` about the pendulum axes were
calculated using

.. math::
   :label: eqTorPend

   J_{\mathrm{B}i} = \frac{k \overline{T}_{\mathrm{B}i}^2}{4\pi^2}

The moments and products of inertia of the rear frame and handlebar/fork
assembly with reference to the benchmark coordinate system were calculated by
formulating the relationship between inertial frames

.. math::
   :label: eqRotIn

   \mathbf{J}_{\mathrm{B}i} = \mathbf{R}_i \mathbf{I}_\mathrm{B} \mathbf{R}_i^T

where :math:`\mathbf{J}_{\mathrm{B}i}` is the inertia tensor about the pendulum axes,
:math:`\mathbf{I}_\mathrm{B}`, is the inertia tensor in the global reference frame and
:math:`\mathbf{R}_{\mathrm{B}i}` is the rotation matrix relating the two frames,
:ref:`Figure 7 <figAngles>`. The global planar inertia tensor is defined as

.. math::
   :label: eqMoI

   \mathbf{I}_\mathrm{B}=
   \begin{bmatrix}
     I_{\mathrm{B}xx}  & I_{\mathrm{B}xz}\\
     I_{\mathrm{B}xz} & I_{\mathrm{B}zz}
   \end{bmatrix}

The inertia tensor can be reduced to a :math:`2 \times 2` matrix because the
frame is assumed to be laterally symmetric and the :math:`Y` axis of the
pendulum reference is the same as the :math:`Y` axis of the benchmark reference
frame. The simple rotation matrix about the :math:`Y`-axis can similarly be
reduced to a :math:`2 \times 2` matrix where :math:`s_{\beta i}` and
:math:`c_{\beta i}` are defined as :math:`\sin{\beta_i}` and
:math:`\cos{\beta_i}`, respectively.

.. math::
   :label: eqRotMat

   \mathbf{R}=
   \begin{bmatrix}
     c_{\beta i} & -s_{\beta i}\\
     s_{\beta i} & c_{\beta i}
   \end{bmatrix}

The first entry of :math:`\mathbf{J}_{\mathrm{B}i}` in Equation :eq:`eqRotIn`
is the moment of inertia about the pendulum axis and is written explicitly as

.. math::
   :label: eqInRelComp

   J_{\mathrm{B}i} = c^{2}_{\beta i}I_{\mathrm{B}xx} -
   2s_{\beta i}c_{\beta i}I_{\mathrm{B}xz} +
   s^{2}_{\beta i}I_{\mathrm{B}zz}

Similarly, calculating all three, or more, :math:`J_{\mathrm{B}i}` allows one to form

.. math::
   :label: eqInRel

    \begin{bmatrix}
        J_{\mathrm{B}1}\\
        J_{\mathrm{B}2}\\
        J_{\mathrm{B}3}\\
        \vdots
    \end{bmatrix}
    =
    \begin{bmatrix}
        c_{\beta 1}^2 & -2s_{\beta 1}c_{\beta 1} & s_{\beta 1}^2\\
        c_{\beta 2}^2 & -2s_{\beta 2}c_{\beta 2} & s_{\beta 2}^2\\
        c_{\beta 3}^2 & -2s_{\beta 3}c_{\beta 3} & s_{\beta 3}^2\\
        \vdots & \vdots & \vdots
    \end{bmatrix}
    \begin{bmatrix}
        I_{\mathrm{B}xx}\\
        I_{\mathrm{B}xz}\\
        I_{\mathrm{B}zz}
    \end{bmatrix}

and the moments of inertia can be solved as a linear system or with least
squares if it is over determined. The inertia of the frame about an axis normal
to the plane of symmetry was estimated by hanging the frame as a compound
pendulum at the wheel axis, :ref:`Figure 19 <figFrameCompound>`. Equation
:eq:`eqCompoundInertia` is used but with the mass of the frame and the frame
pendulum length.

.. math::
   :label: eqFramePendLength

   l_B = \sqrt{x_B^2+(z_B + r_R)^2}

.. _figFrameCompound:

.. figure:: figures/physicalparameters/YellowFrameCompoundFirst.*
   :align: center
   :width: 2in
   :target: _images/YellowFrameCompoundFirst.jpg

   The yellow bicycle rear frame hung as a compound pendulum.

Fork and handlebar
~~~~~~~~~~~~~~~~~~

The inertia of the fork and handlebar is calculated in the same way as the
frame. The fork is hung as both a torsional pendulum, :ref:`Figure 11
<figStratosFork>`, and as a compound pendulum, :ref:`Figure 20
<figForkCompound>`. The fork provides fewer mounting options to obtain at least
three equally spaced orientation angles, especially if there is no fender. We
designed a connection to the brake mounts for the Davis bicycles to remedy
that. The torsional calculations follow equations :eq:`eqTorPend` through
:eq:`eqInRel` and the compound pendulum calculations is calculated with
Equation :eq:`eqCompoundInertia`. The fork pendulum length is calculated using

.. math::
   :label: eqForkPendulumLength

   l_H=\sqrt{(x_H - w)^2 + (z_H + r_F)^2}

.. _figForkCompound:

.. figure:: figures/physicalparameters/BrowserInsForkCompoundFirst.*
   :align: center
   :width: 2in
   :target: _images/BrowserInsForkCompoundFirst.jpg

   Browser fork hung as a compound pendulum.

Notation
--------

The notation used in the bicycle parameter estimation.

:math:`v`
   Forward speed of the linear bicycle model.
:math:`g`
   Acceleration due to gravity.
:math:`\mathbf{M},\mathbf{C}_1,\mathbf{K}_0,\mathbf{K}_2`
   Velocity and gravity independent mass, damping, and stiffness matrices of
   the linearized Whipple model from [Meijaard2007]_.
:math:`\mathbf{q}`
   Essential coordinates from [Meijaard2007]_.
:math:`\phi`
   Roll angle.
:math:`\delta`
   Steer angle.
:math:`\sigma`
   Standard deviation. The subscript corresponds to the associated nominal
   variable.
:math:`r_{(F,R)} \pm \sigma_{r(F,R)}`
   Front :math:`F` and rear wheel :math:`R` radii and their respective standard
   deviations.
:math:`d_{(F,R)} \pm \sigma_{d(F,R)}`
   The traversed distance of each wheel.
:math:`n_{(F,R)}`
   The number of wheel rotations.
:math:`\gamma \pm \sigma_\gamma`
   The head tube angle and standard deviation.
:math:`\lambda \pm \sigma_\lambda`
   The steer axis tilt and standard deviation.
:math:`f_o`
   Fork offset.
:math:`c \pm \sigma_c`
   Trail and its standard deviation.
:math:`d_1,d_2,d_3`
   Fundamental bicycle geometry from Chapter :ref:`eom`.
:math:`d_1,d_2,d_3`
   Fundamental bicycle geometry from Chapter :ref:`eom`.
:math:`d`
   Inner dimension between the axles from the alternative geometry method.
:math:`\hat{d}_1,\hat{d}_2,\hat{d}_3,\hat{d}_4`
   Measured diameters from the alternative geometry method.
:math:`h_1,h_2,h_3,h_4,h_5`
   Measured heights from the table surface in the alternative geometry method.
:math:`i`
   Indices for each orientation of the front and rear frames in the pendulum.
:math:`\alpha_{\mathrm{H,B}i}`
   Angle of the steer axis relative to horizontal when the front frame and rear
   frame are hung as a pendulum.
:math:`a_{\mathrm{H,B}i}`
   Horizontal distance from the front or rear axle to the pendulum axis when
   the front and rear frames are hung as a pendulum.
:math:`XYZ_P`
   Pendulum reference frame.
:math:`XYZ_{B}`
   Global bicycle reference frame from [Meijaard2007]_.
:math:`\beta_{\mathrm{H,B}i}`
   Angle of the pendulum axis relative to the bicycle's reference frame.
:math:`m_{\mathrm{H,B}i}`
   Slope of the pendulum axis in the bicycle reference frame.
:math:`b_{\mathrm{H,B}i}`
   Z intercept of the pendulum axis in the bicycle reference frame.
:math:`z_{\mathrm{B}i}(x)`
   Function describing the pendulum axis line in the :math:`XZ_B` plane.
:math:`\hat{d}_5,\hat{d}_6`
   Handlebar and front wheel axle diameters.
:math:`l`
   The outer distance from the front wheel axle to the handlebar reference
   point.
:math:`l_1,l_2`
   The distances along and perpendicular to the steer axis from the front wheel
   center to the handlebar reference point.
:math:`u_1,u_2`
   The distances from the front wheel center to the handlebar reference point
   in the global bicycle reference frame.
:math:`A,B,C`
   The offset, sin amplitude, and cosine amplitude in the oscillations.
:math:`\omega,\zeta`
   The frequency and damping ratio in the oscillations.
:math:`T`
   Period of oscillation.
:math:`\sigma_y`
   The standard deviation of the measured voltage about the best fit curve.
:math:`y_{mi}`
   The measured voltage at each time.
:math:`\bar{y}_m`
   The mean of the measured voltage across all time.
:math:`y_{pi}`
   The predicted voltage value at each time.
:math:`\mathbf{U}`
   Covariance matrix of the fit function parameters.
:math:`\mathbf{H}`
   Hessian of the fit function parameters.
:math:`\overline{T}_i`
   Average period at orientation :math:`i`.
:math:`I_P`
   Inertia of the calibration rod about the pendulum axis.
:math:`k`
   Stiffness of the torsional pendulum.
:math:`m_P`
   Mass of the calibration rod.
:math:`r_P`
   Radius of the calibration rod.
:math:`l_P`
   Length of the calibration rod.
:math:`T_P`
   Oscillation period of the calibration rod.
:math:`l_\mathrm{F,R}`
   Front and rear wheel compound pendulum length.
:math:`I_{Fyy},I_{Ryy}`
   Moment of inertia of the front and rear wheels about the axle.
:math:`I_{\mathrm{F,R}xx}`
   Moment of inertia of the front and rear wheels about the radii.
:math:`I_{\mathrm{B}xx},I_{\mathrm{B}xz},I_{\mathrm{B}zz}`
   Moments and products of inertia of the rear fame with reference to the
   bicycle reference frame and the center of mass.
:math:`\mathbf{I}_\mathrm{H,B}`
   The inertia tensor of the front and rear frame with reference to the bicycle
   reference frame and the center of mass.
:math:`\mathbf{J}_{\mathrm{H,B}i}`
   The inertia tensor of the front and rear frame with reference to the
   pendulum reference frame and the center of mass for each orientation.
:math:`\mathbf{R}_i`
   The rotation matrix relating the pendulum and bicycle reference frames.
:math:`s_{\beta i},c_{\beta i}`
   Shorthand for :math:`\sin{\beta_i}` and :math:`\cos{\beta_i}`.
:math:`x_B,z_B`
   The :math:`X` and :math:`Z` coordinates of the rear frame center of mass.
:math:`l_B`
   The rear frame pendulum length.
:math:`x_H,z_H`
   The :math:`X` and :math:`Z` coordinates of the front frame center of mass.
:math:`l_H`
   The front frame pendulum length.

Human Parameters
================

To properly model the bicycle rider system it is necessary to estimate the
physical parameters of the bicycle rider. The measurement of the physical
properties of a human is more difficult than for a bicycle because the human
body parts are not as easily described as rigid bodes with defined joints and
due to flexible geometry, daily varying mass, wobbly mass, etc.

Human mass, center of mass, and inertial properties have been measured and
estimated in a multitude of ways. Each method has its advantages and
disadvantages. Many methods exist including cadaver measurements
([Dempster1955]_, [Clauser1969]_, [Chandler1975]_), photogrammetry, ray
scanning techniques ([Zatsiorsky1983]_, [Zatsiorsky1990]_), water displacement
([Park1999]_), rotating platforms ([Griffith2005]_), and mathematical
geometrical estimation of the body segments ([Yeadon1990a]_). [Dohring1953]_,
[Eaton1973]_, and [Patterson2006]_ measured the moments of inertia and centers
of mass of a combined rider and vehicle, but this is not always practical
especially if the properties of multiple riders is desired.

I approached the human parameter estimation in a more analytical fashion with
minimal geometrically centric measurements as compared to some of the popular
measurement techniques. Both methods that were used were based on estimating
the inertial parameters from mass and geometry measurement along with a human
body density estimate. With the first method, I estimated the physical
properties of the rider in a seated position using a simple mathematical
geometrical estimation similar in idea to [Yeadon1990a]_ in combination with
mass data from [Dempster1955]_. The second method substitutes Yeadon's more
robust model with my previous one.

Simple Geometry Method
----------------------

This method calculates the center of mass and inertia of a simplified model of
the ten major human body parts: head, torso, upper and lower arms, and upper
and lower legs, in a general configuration for sitting on typical bicycles. The
mass of the rider was measured along with fourteen anthropomorphic measurements
of the body. These measurements in combination with the geometrical bicycle
measurements taken in the previous section (:ref:`secBicycleParameters`) and
several additional bicycle geometrical measurements are used to define a model
of the rider made up of simple geometrical shapes (:ref:`Figure 21
<figMooreModel>`). The legs and arms are represented by cylinders, the torso
by a cuboid and the head by a sphere. The feet are positioned at the center of
the bottom bracket axis to maintain symmetry about the :math:`XZ`-plane.

.. _figMooreModel:

.. figure:: figures/physicalparameters/moore-model.*
   :align: center
   :width: 2.5in
   :target: _images/moore-model.png

   Locations of grid points and simple geometric shapes of the simple geometric
   inertia model.

All but one of the anthropomorphic measurements are taken when the rider was
standing casually on flat ground. The lower leg length :math:`l_{ll}` is the
distance from the floor to the knee joint. The upper leg length :math:`l_{ul}`
is the distance from the knee joint to the hip joint. The length from hip to
hip :math:`l_{hh}` and shoulder to shoulder :math:`l_{ss}` are the distances
between the two hip joints and two shoulder joints, respectively. The torso
length :math:`l_{to}` is the distance between hip joints and shoulder joints.
The upper arm length :math:`l_{ua}` is the distance between the shoulder and
elbow joints. The lower arm length :math:`l_{al}` is the distance from the
elbow joint to the center of the hand when the arm is outstretched. The
circumferences are taken at the cross section of maximum circumference (e.g.
around the bicep, around the brow, over the nipples for the chest). The final
dimension is taken while the rider is seated on the bicycle in a normal riding
position. The forward lean angle :math:`\lambda_{fl}` is the approximate angle
made between the floor (:math:`XY`-plane) and the line connecting the center of
the rider's head and the top of the seat. This was estimated by taking a side
profile photograph of the rider on the bicycle and scribing a line from the
center of the head to the top of the seat. The measurements were made as
accurately as possible with basic tools but no special attention is given
further to the accuracy of the calculations due to the fact that modeling the
human as basic geometric shapes already introduces an unknown error.

I measured twelve additional geometric values (only five of which are needed
for this setup [#f1]_) to assist in configuring the rider to the be seated on
the bicycle, :ref:`Figure 22 <figBatavusBrowserDim>`.

:math:`h_{bb}`, Bottom Bracket Height
   The distance from the ground to the bottom bracket when the bicycle is in
   the nominal configuration.
:math:`l_{cs}`, Chain stay length
   Not the true chain stay length, but the distance from the center of the
   bottom bracket to the center of the rear wheel.
:math:`l_{sp}`, Seat post length
   The distance from the intersection of a horizontal top tube and the seat
   tube to the top of the seat. Measured along the center line of the seat
   post.
:math:`l_{st}`, Seat tube length
   The distance from the bottom bracket to the point at which a horizontal top
   tube would intersect the seat tube.
:math:`\lambda_{st}`, Seat tube angle
   The acute angle between the ground and the seat tube.
:math:`l_{f}`, fork length [#f1]_
   The distance from the center of the front wheel to the intersection of the
   head tube and the down tube.
:math:`w_{fh}`, front hub width [#f1]_
   The distance between the front dropouts.
:math:`w_{hb}`, handlebar width [#f1]_
   The distance between the handlebar grips.
:math:`l_{hb}`, handlebar length [#f1]_
   The horizontal distance from the steer axis to the handlebar grips.
:math:`\lambda_{ht}`, head tube angle [#f1]_
   The angle between the ground and the head tube.
:math:`w_{rh}`, rear hub width [#f1]_
   The distance between the rear dropouts.
:math:`l_{s}`, stem length [#f1]_
   The distance from the intersection of the top tube and the head tube to the
   level of the handlebar grips.

.. _figBatavusBrowserDim:

.. figure:: figures/physicalparameters/batavusBrowserDim.*
   :align: center
   :width: 3.189in
   :target: _images/batavusBrowserDim.png

   The dimensions need to construct the grid point system in the simple inertia
   method.

The masses of each segment (:ref:`Table 1 <tabSegmentMass>`) were defined as a
proportion of the total mass of the rider :math:`m_{\mathrm{B}r}` using data
from cadaver studies by [Dempster1955]_.

.. _tabSegmentMass:

.. tabularcolumns:: lll

.. list-table:: Body mass and segment masses.

   * - Segment
     - Symbol
     - Equation
   * - body
     - :math:`m_{B_r}`
     - :math:`m_{B_r}`
   * - head
     - :math:`m_h`
     - :math:`0.068 \cdot m_{B_r}`
   * - lower arm
     - :math:`m_{la}`
     - :math:`0.022 \cdot m_{B_r}`
   * - lower leg
     - :math:`m_{ll}`
     - :math:`0.061 \cdot m_{B_r}`
   * - torso
     - :math:`m_{to}`
     - :math:`0.510 \cdot m_{B_r}`
   * - upper arm
     - :math:`m_{ua}`
     - :math:`0.028 \cdot m_{B_r}`
   * - upper leg
     - :math:`m_{ul}`
     - :math:`0.100 \cdot m_{B_r}`

The geometrical and anthropomorphic measurements are converted into a set of
thirty one grid points in three dimensional space that map the skeleton of the
rider and bicycle (:ref:`Figure 22 <figMooreModel>`). The position vectors to
these grid points are listed in :ref:`Table 2 <tabGridPoints>`. Several
intermediate variables used in the grid point equations are listed in
:ref:`Table 3 <tabIntVar>` where :math:`f_o` is the fork offset and the rest
arise due to multiple solutions to the location of the elbow and knee joints
and have to be solved numerically. The correct solutions are the ones that
force the arms and legs to bend in a natural fashion. The grid points mark the
center of the sphere and the end points of the cylinders and cuboid. The
segments are aligned along lines connecting the appropriate grid points.

.. _tabGridPoints:

.. tabularcolumns:: ll

.. list-table:: Skeleton grid points with respect to the global frame.

   * - Description
     - Equation
   * - rear contact point
     - :math:`\mathbf{r}_1=\left[0 \quad 0 \quad 0\right]`
   * - rear wheel center
     - :math:`\mathbf{r}_2=\left[0 \quad 0 \quad -r_\mathrm{R}\right]`
   * - right rear hub center
     - :math:`\mathbf{r}_3=\mathbf{r}_2+\left[0 \quad \frac{w_{rh}}{2} \quad 0\right]`
   * - left rear hub center
     - :math:`\mathbf{r}_4=\mathbf{r}_2+\left[0 \quad -\frac{w_{rh}}{2} \quad 0\right]`
   * - bottom bracket center
     - :math:`\mathbf{r}_5=\left[\sqrt{l_{cs}^2-(r_\mathrm{R}-h_{bb})^2} \quad 0 \quad -h_{bb}\right]`
   * - front wheel contact point
     - :math:`\mathbf{r}_6=\left[w \quad 0 \quad 0\right]`
   * - front wheel center
     - :math:`\mathbf{r}_7=\mathbf{r}_6+\left[0 \quad 0 \quad -r_\mathrm{F}\right]`
   * - right front hub center
     - :math:`\mathbf{r}_8=\mathbf{r}_7+\left[0 \quad \frac{w_{fh}}{2} \quad 0\right]`
   * - left front hub center
     - :math:`\mathbf{r}_9=\mathbf{r}_7+\left[0 \quad -\frac{w_{fh}}{2} \quad 0\right]`
   * - top of seat tube
     - :math:`\mathbf{r}_{10}=\mathbf{r}_5+\left[-l_{st}\cos{\lambda_{st}} \quad 0 \quad -l_{st}\sin{\lambda_{st}}\right]`
   * - fork crown
     - :math:`\mathbf{r}_{11}=\mathbf{r}_7+\left[-f_o\sin{\lambda_{ht}}-\cos{\lambda_{ht}}\sqrt{l_{f}^2-f_o^2} \quad 0 \quad f_o\cos{\lambda_{ht}}-\sin{\lambda_{ht}}\sqrt{l_{f}^2-f_o^2}\right]`
   * - top of head tube
     - :math:`\mathbf{r}_{12}=\left[r_{X11}-\frac{r_{Z11}-r_{Z10}}{\tan{\lambda_{ht}}} \quad 0 \quad r_{Z10}\right]`
   * - top of seat
     - :math:`\mathbf{r}_{13}=\mathbf{r}_{10}+\left[-l_{sp}\cos{\lambda_{st}} \quad 0 \quad -l_{sp}\sin{\lambda_{st}}\right]`
   * - center of knees
     - :math:`\mathbf{r}_{14}=\mathbf{r}_5+\left[s \quad 0 \quad -t\right]`
   * - shoulder midpoint
     - :math:`\mathbf{r}_{15}=\mathbf{r}_{13}+\left[l_{to}\cos{\lambda_{fl}} \quad 0 \quad -l_{to}\sin{\lambda_{fl}}\right]`
   * - top of stem
     - :math:`\mathbf{r}_{16}=\mathbf{r}_{12}+\left[-l_{s}\cos{\lambda_{ht}} \quad 0 \quad -l_{s}\sin{\lambda_{ht}}\right]`
   * - right handlebar
     - :math:`\mathbf{r}_{17}=\mathbf{r}_{16}+\left[0 \quad \frac{l_{ss}}{2} \quad 0\right]`
   * - left handlebar
     - :math:`\mathbf{r}_{18}=\mathbf{r}_{16}+\left[0 \quad -\frac{l_{ss}}{2} \quad 0\right]`
   * - right hand
     - :math:`\mathbf{r}_{19}=\mathbf{r}_{17}+\left[-l_{hb} \quad 0 \quad 0\right]`
   * - left hand
     - :math:`\mathbf{r}_{20}=\mathbf{r}_{18}+\left[-l_{hb} \quad 0 \quad 0\right]`
   * - right shoulder
     - :math:`\mathbf{r}_{21}=\mathbf{r}_{15}+\left[0 \quad \frac{l_{ss}}{2} \quad 0\right]`
   * - left shoulder
     - :math:`\mathbf{r}_{22}=\mathbf{r}_{15}+\left[0 \quad -\frac{l_{ss}}{2} \quad 0\right]`
   * - right elbow
     - :math:`\mathbf{r}_{23}=\mathbf{r}_{19}+\left[-u \quad \frac{l_{ss}}{2} \quad -v\right]`
   * - left elbow
     - :math:`\mathbf{r}_{24}=\mathbf{r}_{23}+\left[0 \quad -l_{ss} \quad 0\right]`
   * - center of head
     - :math:`\mathbf{r}_{25}=\mathbf{r}_{15}+\left[\frac{c_{h}}{2\pi}\cos{\lambda_{fl}} \quad 0 \quad -\frac{c_{h}}{2\pi}\sin{\lambda_{fl}}\right]`
   * - right foot
     - :math:`\mathbf{r}_{26}=\mathbf{r}_{5}+\left[0 \quad \frac{l_{hh}}{2} \quad 0\right]`
   * - left foot
     - :math:`\mathbf{r}_{27}=\mathbf{r}_{5}+\left[0 \quad -\frac{l_{hh}}{2} \quad 0\right]`
   * - right knee
     - :math:`\mathbf{r}_{28}=\mathbf{r}_{14}+\left[0 \quad \frac{l_{hh}}{2} \quad 0\right]`
   * - left knee
     - :math:`\mathbf{r}_{29}=\mathbf{r}_{14}+\left[0 \quad -\frac{l_{hh}}{2} \quad 0\right]`
   * - right hip
     - :math:`\mathbf{r}_{30}=\mathbf{r}_{13}+\left[0 \quad \frac{l_{hh}}{2} \quad 0\right]`
   * - left hip
     - :math:`\mathbf{r}_{31}=\mathbf{r}_{13}+\left[0 \quad -\frac{l_{hh}}{2} \quad 0\right]`

.. _tabIntVar:

.. tabularcolumns:: ll

.. list-table:: Grid point intermediate variables.

   * - Symbol
     - Equation
   * - :math:`f_o`
     - :math:`r_\mathrm{F}\cos{\lambda_{ht}}-c\sin{\lambda_{ht}}`
   * - :math:`s`
     - :math:`0=l_{ul}^2-l_{ll}^2-(r_{Z13}-r_{Z5})^2-(r_{X5}-r_{X13})^2-2(r_{Z13}-r_{Z5})\sqrt{(l_{ll}^2-s^2)}-2s(r_{X5}-r_{X13})`
   * - :math:`t`
     - :math:`\sqrt{l_{ll}^2-s^2}`
   * - :math:`u`
     - :math:`0=l_{la}^2-l_{ua}^2+(r_{Z21}-r_{Z19})^2+(r_{X19}-r_{X21})^2+2(r_{Z21}-r_{Z19})\sqrt{(l_{la}^2-u^2)}-2u(r_{X19}-r_{X21})`
   * - :math:`v`
     - :math:`\sqrt{l_{la}^2-u^2}`

The segments are assumed to have uniform density so the centers of mass are
taken to be at the geometrical centers. The midpoint formula can then be used
to calculate the local centers of mass for each segment in the global reference
frame. The total body center of mass can be found from the standard formula

.. math::
   :label: eqCoM

   \mathbf{r}_{\mathrm{B}r}=
   \frac{\sum{m_i\mathbf{r}_i}}{m_{\mathrm{B}r}}

where :math:`\mathbf{r}_i` is the position vector to the centroid of each
segment and :math:`m_i` is the mass of each segment. The local moments of
inertia of each segment are determined using the ideal definitions of inertia
for each segment type (:ref:`Table 4 <tabLocInertia>`).

.. _tabLocInertia:

.. tabularcolumns:: ll

.. list-table:: Segment inertia tensors defined in their local reference frames.

   * - Segment
     - Inertia
   * - cuboid
     - :math:`\frac{1}{12}m\begin{bmatrix}l_y^2+l_z^2 & 0 & 0\\0 & l_x^2+l_z^2 & 0\\0 & 0 & l_x^2+l_y^2\end{bmatrix}`
   * - cylinder
     - :math:`I_x`, :math:`I_y=\frac{1}{12}m\left(\frac{3c^2}{4\pi^2}+l^2\right)`, :math:`I_z=\frac{mc^2}{8\pi^2}`
   * - sphere
     - :math:`I_x`, :math:`I_y`, :math:`I_z=\frac{mc^2}{10\pi^2}`

The width of the cuboid representing the torso :math:`l_y` is defined by the
shoulder width and upper arm circumference.

.. math::
   :label: eqCuboidWidth

   l_y=l_{ss}-\frac{c_{ua}}{\pi}

The cuboid thickness was estimated using the chest circumference measurement
assuming that the cross section of the chest is similar to a stadium shape.

.. math::
   :label: eqCuboidThick

   l_x=\frac{c_{ch}-2l_y}{\pi-2}

The local :math:`\hat{\mathbf{z}}_i` unit vector for the segments was defined
along the line connecting the associated grid points from the lower numbered
grid point to the higher numbered grid point. The local unit vector in the
:math:`y` direction was set equal to the global :math:`\hat{\mathbf{Y}}` unit
vector with the :math:`\hat{\mathbf{x}}_i` unit vector following from the right
hand rule. The rotation matrix needed to rotate each of the moments of inertia
to the global reference frame can be calculated by dotting the global unit
vectors :math:`\hat{\mathbf{X}}`, :math:`\hat{\mathbf{Y}}`,
:math:`\hat{\mathbf{Z}}` with the local unit vectors
:math:`\hat{\mathbf{x}}_i`, :math:`\hat{\mathbf{y}}_i`,
:math:`\hat{\mathbf{z}}_i` for each segment.

.. math::
   :label: eqRotMat2

   \mathbf{R}_i=
   \begin{bmatrix}
     \hat{\mathbf{X}}\cdot\hat{\mathbf{x}}_i &
     \hat{\mathbf{X}}\cdot\hat{\mathbf{y}}_i &
     \hat{\mathbf{X}}\cdot\hat{\mathbf{z}}_i\\
     \hat{\mathbf{Y}}\cdot\hat{\mathbf{x}}_i &
     \hat{\mathbf{Y}}\cdot\hat{\mathbf{y}}_i &
     \hat{\mathbf{Y}}\cdot\hat{\mathbf{z}}_i\\
     \hat{\mathbf{Z}}\cdot\hat{\mathbf{x}}_i &
     \hat{\mathbf{Z}}\cdot\hat{\mathbf{y}}_i &
     \hat{\mathbf{Z}}\cdot\hat{\mathbf{z}}_i\\
   \end{bmatrix}

The local inertia matrices are then rotated to the global reference frame with

.. math::
   :label: eqRotInertia

   \mathbf{I}_i=\mathbf{R}_i\mathbf{J}_i\mathbf{R}^T_i

The local moments of inertia can then be translated to the center of mass of
the entire body using the parallel axis theorem

.. math::
   :label: eqPAT

   \mathbf{I}^*_i=\mathbf{I}_i+m_i
   \begin{bmatrix}
     d_y^2+d_z^2 & -d_xd_y & -d_xd_z\\
     -d_xd_y & d_z^2+d_x^2 & -d_yd_z\\
     -d_xd_z & -d_yd_z & d_x^2+d_y^2
   \end{bmatrix}

where :math:`d_x`, :math:`d_y` and :math:`d_z` are the distances along the
:math:`X`, :math:`Y` and :math:`Z` axes, respectively, from the local center of
mass to the global center of mass. Finally, the local translated and rotated
moments of inertia are summed to give the total moment of inertia of the rider.

.. math::
   :label: eqSumInertia

   \mathbf{I}_{\mathrm{B}r}=
   \sum{\mathbf{I}^*_i}

The results of measuring the riders are presented in Chapter
:ref:`delftbicycle`, :ref:`motioncapture`, and [Moore2009a]_.

Yeadon method
-------------

The [Yeadon1990a]_ human inertial model was developed for estimating the
inertial parameters needed to describe a human model for complex gymnastic
maneuvers. It is essentially a more complete and accurate method than the one
previously presented. There are 95 geometrical measurements of the human and a
single mass measurement for scaling the body part densities. Yeadon makes use
of stadium solids and a single semi-ellipse to more accurately model the human
geometry. Two apparent deficiencies are the fact that too much detail is taken
for body parts that have less inertia (i.e. the hands/feet) and at large
configuration angles for some joints, the inertia is poorly modeled (e.g. the
butt disappears when the human in a seated position). The model also does not
have full freedom at each joint. Refer to [Yeadon1990a]_ for a complete
description of the model.

Once the inertia of each segment in the Yeadon model is computed, the joint
angles must be set. We set the somersault angle to match the forward lean angle
as described in the previous section. We then measure three additional bicycle
dimensions to assist in the configuration of the rider. They are as follows:

:math:`w_{hb}`, Handlebar width
   The lateral distance between the points the hands hold the handlebars.
:math:`l_{hbR}`, Rear hub to handlebar.
   The distance from the center of the rear hub to the point on the handlebar
   where the hand grips.
:math:`l_{hbF}`, Front hub to handlebar.
   The distance from the center of the front hub to the point on the handlebar
   where the hand grips.

We locate the hip center (Ls0) at the top of the bicycle seat and the
somersault joint angle is set such that the torso (P, T, C) aligned by the
forward lean angle :math:`\lambda_{fl}`.

The basic process for setting the elbow elevation angle is to find the distance
between the shoulder (La0, Lb0) and the handlebar grip. The handle bar grip
location is at the point at which the lateral line with length
:math:`\frac{w_{hb}}{2}` intersects the circle formed by the intersection of
the two spheres which are centered at the front and rear wheel centers with
radii :math:`l_{hbF}` and :math:`l_{hbR}`, respectively. The elevation angle of
the elbow then is defined as the angle at which the distance from the shoulder
(La0, Lb0) to the knuckle (La6, Lb6) is equal to the distance from the shoulder
(La0, Lb0) to the handlebar grip. We then assume that the shoulder rotation
angle is zero and find the shoulder elevation and abduction angles which force
the vector from the shoulder to the knuckle to equal the vector from the
shoulder to the handlebar grip.

The thigh and knee elevation angles are set such that the center of the heel
level (Lj6, Lk6) is aligned with the bottom bracket axis and that both the
thigh abduction and rotation angles are zero. We assume that the foot peg is
located at the bottom bracket center and is the same lateral distance from the
sagittal plane as the hip centers. The knee and thigh elevation angles are then
found in the same fashion as the elbow and shoulder angles, which the lesser
restriction that the thigh abduction angle is zero.

:ref:`Figure 23 <figHuman>` shows a visualization of the Yeadon modle when
configured to sit on a bicycle. The details of the calculations and all of the
data is included with the Yeadon [Dembia2011]_ and BicycleParameters
[Moore2011a]_ software packages.

.. _figHuman:

.. figure:: figures/physicalparameters/human.png
   :align: center
   :width: 3in

   A visualization of the Yeadon inertia model configured to sit on a bicycle.
   Output is from the BicycleParameters software package.

Bicycle-Rider Parameters
========================

Once both the bicycle and rider parameters are known, the parameter for various
systems can be extracted. The simplest being that the rider is rigidly attached
to the frame. The parallel axis theorem allows one to calculate the combined
inertia of the bicycle frame and the rigid rider. Both of the rider
formulations also allow one to segment the body for more complex rider models
with multiple degrees of freedom. For example, the inertia for a leaning rider's
upper body can be determined separately and the legs can be fixed the bicycle
frame. We make use of this for the different rider biomechanical models
presented in Chapter :ref:`extensions`.

Software Implementation
=======================

The bicycle parameter calculation and the Yeadon method have been implemented in
two open source software package written in the python language, called `yeadon
<http://pypi.python.org/pypi/yeadon>`_ and `BicycleParameters
<http://pypi.python.org/pypi/BicycleParameters>`_. The Yeadon package takes
geometric measurements and joint configuration angles and outputs the total
inertia inertial properties of the human in an arbitrary reference frame or
inertial properties of individual segments or combinations of segments. It is
suitable for a wide variety of human dynamic models. The BicycleParameters
package accepts either the raw measurements described in Section
:ref:`secBicycleParameters` or the benchmark parameterization [Meijaard2007]_
and computes the benchmark bicycle parameters. It makes use of the Yeadon
package to allow one to configure riders to sit on the bicycle models and
outputs the inertial properties of the bicycle/rider system.  It allows one to
measure all of the raw measurements as described in both the Bicycle and Yeadon
parameter sections, provide the values, with uncertainties, and it computes the
parameters for the Whipple Bicycle model. Details of use of the software can be
found in the documentation for each of the packages:
`<http://packages.python.org/yeadon>`_,
`<http://packages.python.org/BicycleParameters>`_.

.. _secPartables:

Parameter Tables
================

The tabulated values for the both the raw measurements and the physical
parameters of the ten bicycles are given in the following tables.

.. _secBicycleMeasuredParameters:

Bicycle Measured Parameters
---------------------------

.. tabularcolumns:: lllllll
.. include:: tables/physicalparameters/batavusMeasured.rst

.. tabularcolumns:: lllllll
.. include:: tables/physicalparameters/delftMeasured.rst

.. tabularcolumns:: lllll
.. include:: tables/physicalparameters/yellowMeasured.rst

.. tabularcolumns:: lllllll
.. include:: tables/physicalparameters/davisMeasured.rst

.. _secBicycleBenchmarkParameters:

Bicycle Benchmark Parameters
----------------------------

.. include:: tables/physicalparameters/batavusBenchmark.rst

.. include:: tables/physicalparameters/delftBenchmark.rst

.. include:: tables/physicalparameters/yellowBenchmark.rst

.. include:: tables/physicalparameters/davisBenchmark.rst

.. rubric:: Footnotes

.. [#weight] This is actually the same rider: I gained some weight after
   drinking all that good beer in the Netherlands!

.. [#leastsquares] Alternatively, the three lines can be treated as an over
   determined linear system and the least squares method is used to find a
   unique solution. This solution is not the same as the triangle centroid
   method. The solution with the higher accuracy would likely be the preferred
   one.

.. [#steertorque] See Chapter :ref:`davisbicycle`.

.. [#clamps] The Davis clamp was a bit larger relative to forks with no
   handlebars. This may have decreased the accuracy of the related measurments.

.. [#rod] A different rod was used for the Delft and Davis Bicycles.

.. [#f1] These dimensions are not necessary for the provided methods, but are
   necessary to build the grid point system. Early on they were used to
   analytically estimate the inertia of the bicycle frame. See [Moore2008]_
