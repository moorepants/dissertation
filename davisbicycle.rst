.. _davisbicycle:

==========================
Davis Instrumented Bicycle
==========================

.. warning::

   This document is a draft which is updated regularly (Last updated |today|).
   Once I submit if for my doctoral degree at UC Davis, it will be done. So for
   now use at your own risk. The information may or may not be correct.
   Reviews, comments and suggestions are welcome.

Preface
=======

At the beginning of 2009 I was in Delft working with Jodi and Arend on much of
the work explained in the previous chapters. I was still also in contact with
Mont and Luke back in Davis. Before I had come to Delft, Luke had mentioned the
possibilities of applying for an NSF grant to fund the remainder of our bicycle
dynamics projects. This was enticing, as there were few sources of grant
funding over the years for in the Davis lab. We really needed some dedicated
research time, as we spent the first few years taking teaching assistant
positions which ate up most of our available research time outside of our
classes. I fortunately got a Fulbright grant for the 2008 school year which
gave me a year's stipend so that I could focus on research and on top of that
Jodi's PhD budget helped fund the practical research costs in Delft and some of
my conference trips. At the beginning of December 2008 Luke sent me an email
with a renewed interest in applying for the NSF grant and Mont seemed to be on
board. Mont also talked with Ron and got him interested. We spent the next two
months writing our grant proposal using video conferencing and collaborative
word processing to get it done. The basic idea was to pair Ron's manual control
expertise with our bicycle dynamics expertise to study the dynamics, control
and handling qualities of bicycles with the theoretical constructs supported by
extensive experimentation. Our work paid off and we received the grant, albeit
at a smaller amount than asked for so we had to cut back some of the scope
(which Arend had correctly forecast of being too large!). This set us up for a
two year study where we'd develop a manual control model, verify it and the
basic bicycle dynamics with both an instrumented bicycle and a robotic bicycle,
and wrap it up with some work on handling qualities predictions.

When I got back to Davis in September 2009 we started gearing up for the grant
work that would start October 1st. I had to get my qualifying exam done in
October and I also signed up for a Spanish class (which wasn't necessarily a
good idea for the grant's sake). Luke also took some programming classes and
this gave us a really slow start, as neither Luke or I realized that the scope
of what we had to do didn't really allow any more time for classes. We got
moving though and started to plan out the bicycle(s) we were going to build.

Our proposal called for two bicycles, but somehow Luke and I hatched a plan to
build a single multi-purpose bicycle to "save money and time". Arend sent
Danique over in January 2010 to do her internship with us. She was an excellent
intern and made great progress on the custom data acquisition system we had
envisioned.  We decided to use a low level microprocessor, the Arduino, paired
with with a set of digital sensors for data acquisition and control. During
this time, Luke and I had our roughest moments working together which was
mostly rooted in my frustrations with the progress of this bicycle design. I'd
already built a bicycle with Jodi that did almost everything I needed and I
felt like I was reinventing the wheel and wasting time with all this low level
data acquisition work. Things eventually broke down after the stress boiled to
the top and we sat down with Mont to figure out how to solve things. The
conclusion was to split the bicycle back into two and each of us move forward
more independently. I think this was the absolutely right move for me in terms
of getting the project done as I planned and the stress immediately went away.
But the part I'm still bothered about was my inability to work in a direct team
with Luke when the pressure to get things done was high. I know that if we work
together, the final product would be many times greater than our independent
work because of our complimentary skill sets, but conflicting visions of the
final product and the path to get there really put a wall between us. I'm
continually learning how to do teamwork and probably always will be. I doubt it
is one of my strong points, as I always tend to want control. I hope that I can
develop strong team environments for my students in the future.

Nevertheless, the instrumented bicycle moved forward. I was awarded an extra
grant to cover my stipend for the summer of 2010 so we hired Gilbert, a new
student in our lab, to help us out for the summer. Between me, Gilbert, and our
undergraduate interns Mohammed, Stephen, Eric, and Chet we plowed through the
bicycle construction through the summer pretty much putting the instrumented
bicycle back on schedule for experimentation in the fall. But even with the
summer push, it ended up taking me all fall quarter and some into the new year
to get the bicycle in a working state and ready for the experimentation. This
chapter discusses the design and operation of the Davis instrumented bicycle.

Introduction
============

This chapter details the design and implementation of an instrumented bicycle
capable of accurately measuring the essential kinematics and kinetics
associated with human control of the bicycle.

I had originally considered using motion capture for the kinematics as we had
very successful results measuring the complete kinematic configuration of the
bicycle and rider with motion capture techniques as explained in Chapter
:ref:`motioncapture`, but I no longer had access to a system as good as the one
at the Vrije Universiteit. The systems available in Davis could capture the
motion on the treadmill but were not especially not suited to capture the
motion of the bicycle on the ground. With this in mind, we decided to expand
upon the on board measurement techniques used in the Delft Instrumented bicycle
as the basic design principle. This would allow the bicycle to collect data in
a variety of environments. The most notable downside was inaccurate location
tracking of the system. But we concluded that this wouldn't be detrimental to
system identification and moved forward with the instrumentation.

The bicycle's primary design criteria were as follows:

- Sized for our intended riders: average adult males.
- Restrict the rider's biomechanical movement to more closely meet the Whipple
  model rigid rider assumption. This in turn also required the bicycle to be
  self propelled so that the rider does not have to move their legs to pedal.
- Accurately measure the rider's applied steering torque.
- Accurately measure the fundamental kinematics of the bicycle: three
  dimensional rates and orientations of the bicycle rear frame, front frame,
  and wheels.
- Accurately apply and measure a lateral disturbance force to the bicycle
  frame.

From early on, I intended to attempt some experiments with some constrained
rider biomechanical motion, such as leaning, because the interplay of the
various control inputs available to the rider, such as leaning, are a common
theoretical research topic with little experimental backing. This led to
secondary design criteria that as the project progressed were never fully
implemented, but I'll discuss them for completeness. They are as follows:

- Restrict the rider's body motion to a limited set and measure the additional
  kinematics: hip roll, torso relative to hip lean, torso relative to hip
  twist, and lateral knee motions.
- Measure the additional reaction forces between the rider and bicycle: forces
  and moments in the seatpost and forces at the foot pegs.

These criteria framed the subsequent design choices described herein.

Bicycle
=======

We needed a bicycle that would allow for easy modification and various mounting
points for sensors and data acquisition equipment. Our original requirements
for a bicycle were as follows:

- Steel frame for easy modification and welding.
- Disc brake brackets for mounting the wheel speed encoders.
- 100mm front dropout spacing and 135mm rear dropout spacing.
- 1-1/8" threadless headset to allow for easy modification.
- Cylindrical tubes for head, down, top, and seat tube (i.e. nothing non standard)
- Horizontal top tube for equipment mounting purposes.
- Threaded rack mount for instrumentation mounting.
- Accept 700c rims with high pressure tires.
- Frame size: 54-58cm for our intended riders.
- An electric hub motor for forward propulsion.

We ended up choosing a large size Surly 1x1 model, :ref:`Figure
11.1<figSurly>`. It is designed as a single-speed off-road bicycle for 26"
wheels with fat tires, but can be setup with 700c higher pressure tires. The
frame is constructed from butted 4130 CroMoly steel tubing. It has both front
and rear cantilever brake mounts in addition to disc brake mounts. Otherwise it
met all of our requirements. We purchased some standard components including
700c aluminum wheels with 23c Continental Gatorskin high pressure tires and
basic handlebars and brakes.

.. _figSurly:

.. figure:: figures/davisbicycle/surly.*
   :width: 4in
   :align: center
   :target: _images/surly.jpg

   The Surly 1x1 with 700c wheels and basic handlebars for upright seating. An
   Amped Bikes geared hub motor is shown installed along with the lead acid
   battery kit on the rear rack.

To allow the bicycle to be propelled without requiring the rider to pedal, we
opted for a bicycle electric hub motor kit. `Amped Bikes
<http://www.ampedbikes.com>`_ graciously donated both direct drive and geared
kits which included the motors, controllers, throttle, and 36 volt lead acid
batteries. I used the direct drive version on the instrumented bicycle. The
lead acid batteries were very heavy so we purchased a light, ~2.8 kg, 36 volt
lithium ion battery as a substitute to help decrease the bicycle weight.  The
kit comes with a motor controller with a rudimentary "cruise control". We
needed some form of cruise control to allow the rider to set the speed during
the experiment allowing them to focus their attention on lateral control as
opposed to throttle control. The Amped Bike cruise control worked well for the
experiments performed on the floor, but was more difficult to match the cruise
control to the speed of the treadmill. Some sort of feedback control would
alleviate the difficulties, but we made due. The exposed wires from the hub
motor are also easily susceptible to damage. The bicycle fell over once,
damaging the wires and shorting the Hall effect sensors in the hub. I spent a
couple of weeks repairing it\ [#hubdamage]_. Overall, the motor met our needs
for constant speed propulsion and the single battery would last through an
entire day of experimentation, but was susceptible to being easily damaged.

Rider Harnesses
===============

The bicycle was designed to accommodate a range of allowable rider motions. I
designed it with three modes in mind. First, the rider can simply have
complete free rider biomechanical motion as they would when normally riding a
bicycle. The second design was intended to restrict almost all of the rider's
ability to move with respect to the bicycle frame to better mimic the rigid
rider assumptions in many bicycle models. And third, a harness was designed
to restrict the rider's movement to a particular subset of hypothesized
dominant motions.

Rigid Rider
-----------

Rigid rider models are often employed in single track vehicle research but the
rider has been rigidified very few times in experimental work. This is
potentially problematic as the rigid rider assumption is a large one.
:cite:`Stassen1973` made use of a rider brace in their bicycle simulator to
prevent rider lean.  :cite:`Eaton1973` rigidified his motorcyclists' torso and
performed several perturbation tests with the rider's hands off the handlebars!
He found it difficult to identifying the linear modes of motion.
:cite:`Doyle1987` comments on the utility of rigidifying the rider which was an
example of his techniques to simplify the system, but he left the rider free to
move in his experiments.  Jim Papadopolous has been a proponent of using
recumbent bicycles in studies due to the natural rigidification of the rider.
His thoughts and the difficulties we had in the studies from Chapters
:ref:`delftbicycle` and :ref:`motioncapture` influenced my decision to restrict
the rider's motion.

I constructed a harness such that the rider was rigidified as much as possible
with respect to the rear frame, :ref:`Figure 11.2<figRigidHarness>`. A medical
back brace was used to rigidify the spine and hip motion. I then attached the
brace to the bicycle frame via a stout adjustable arm.

.. _figRigidHarness:

.. figure:: figures/davisbicycle/rigid-harness.*
   :width: 3in
   :align: center
   :target: _images/rigid-harness.jpg

   Jason strapped into the rigid rider harness. The arm allows for multiple
   degrees of adjustability to allow different riders and seating positions.

I fashioned some knee straps with strong magnets taken from computer hard
drives which would engage with a ferrous attachment plate on the frame so that
the rider's legs would be rigid with respect to the rear frame, :ref:`Figure
11.3<figKneeRestraints>`. Chapters :ref:`delftbicycle` and :ref:`motioncapture`
showed the rider tends to use lateral knee motions and we wanted to eliminate
that as a confounding factor. The magnets were weak enough that the rider could
remove his legs in an emergency.

.. _figKneeRestraints:

.. figure:: figures/davisbicycle/knee-restraints.*
   :width: 6in
   :align: center
   :target: _images/knee-restraints.jpg

   The left image shows the knee straps with hard drive magnets and the right
   image shows the knee attachment plates mounted to the top tube of the
   bicycle.

These restrictions left the rider's arms and head free to move. The arm motion
was required for controlling the bicycle, although one could imagine fixing the
rider's arms and only allowing control with motion of their hands. The head
probably should have been rigidified with respect to the body cast, but we
didn't due to comfort reasons\ [#halo]_.

Restricted Motion
-----------------

A second harness was partially developed to restrict the rider's motion to that
described in :ref:`secFlexibleRider`. A back brace which left the hips free to
move was used to keep the spine straight and a custom-molded hip brace was
developed to hold securely to the pelvis, :ref:`Figure
11.4<figRestrictedHarness>`. The plan was to attach the hip brace to the
bicycle seat via a revolute joint in the roll direction which would allow the
hips to *only* roll about the seat. The back brace would then be attached to
the hip brace via a joint which would allow torso lean with respect to the
hips. The feet would be attached to the foot pegs via clip-in pedals.  Forces
applied from the feet to the foot pegs would effectively allow the rider's hips
to roll with respect to the bicycle frame (in reality because the rider is more
massive and more inert, the bicycle frame would roll with respect to the
inertial reference frame).

.. _figRestrictedHarness:

.. figure:: figures/davisbicycle/restricted-harness.*
   :width: 3.957in
   :align: center
   :target: _images/restricted-harness.jpg

   The hip and upper torso harnesses.

My hypothesis was that this harness would allow for the essential motion and
torque application needed to effectively control the bicycle with no hands and
would provide the next effective means of control to complement steer torque
when riding with hands. This design was only partially finished, so the merits
of it were never tested.

Orientations, Rates and Accelerations
=====================================

The two most important states that describe the lateral dynamics of the bicycle
are roll and steer (as defined in Chapter :ref:`eom`). Ideally one would like
to measure the angular orientation, angular rate, and angular accelerations of
both the rear frame and the front frame. Sensors that allow direct, independent
and accurate measurements of each are ideal, to avoid having to estimate
measurements through differentiation, integration, or state estimators. The
kinematics of each body need not be measured if they are connected to the rear
fame via revolute joints, only measurement of the extra degree of freedom for
each connected body relative to the rear frame is required. :ref:`Table
11.1<tabKinematicSensors>` gives general ranges of bicycle kinematic motions
from my previously collected data.

.. _tabKinematicSensors:

.. tabularcolumns:: LLLL

.. list-table:: Table of maximal measured values found in all experimental data
   taken in Chapter :ref:`motioncapture`. The ranges were determined from 75
   percentiles, the accuracy as a percentage of the range and the bandwidth as
   75th percentile of the power in the signal.
   :header-rows: 1

   * - Measurement
     - Range
     - Accuracy
     - Bandwidth
   * - Roll Angle
     - :math:`\pm 8` deg
     - 0.2 deg
     - 45 hz
   * - Roll Rate
     - :math:`\pm 30` deg/s
     - 0.6 deg/s
     - 40 hz
   * - Roll Acceleration
     - :math:`\pm 100 \frac{\textrm{deg}}{\textrm{s}}`
     - :math:`2 \frac{\textrm{deg}}{\textrm{s}}`
     - 25 hz
   * - Steer Angle
     - :math:`\pm 65` deg
     - 1 deg
     - 45 hz
   * - Steer Rate
     - :math:`\pm 150` deg
     - 1.5 deg/s
     - 35 hz
   * - Steer Acceleration
     - :math:`\pm 600 \frac{\textrm{deg}}{\textrm{s}}`
     - :math:`12 \frac{\textrm{deg}}{\textrm{s}}`
     - 30 hz

The yaw, roll, pitch and steer rates, are typically measured directly with rate
gyros, which have been available for the later half of the 20th century. The
direct measurement of angular accelerations has yet to mature :cite:`Ovaska1998`, so
numerical differentiation and filtering of the angular rates is often used. The
angular accelerations can also be computed if the acceleration and location of
multiple points are measured with accelerometers. Most all experimental work
with bicycles and motorcycles provides good examples of employing these type of
kinematic sensors.

Roll
----

The roll angle is typically the most difficult kinematic measurement due to the
fact that both the bicycle translates with respect to the ground plane making
mechanical measurement difficult and that the ground plane may not be normal to
earth's gravitational field. Herein, we did not concern ourselves with the
later because all of our experiments were on level ground. Integration of the
easier roll rate measurement is an option, but definite initial conditions and
some way to account for the drift due to integration are required, and not
necessarily trivial. Past researchers have measured the roll angle with a
variety of methods from trailers and third wheels to lasers and rate gyros with
complementary state estimators.

:cite:`Dohring1953` used a trailer to measure roll angle. :cite:`Kageyama1959`
and :cite:`Fu1965` introduced one of the earliest direct roll angle measurements.
They made use of a third wheel attached to one side of the motorcycle and
measured the angle between the wheel mounting arm and the motorcycle frame.
:cite:`Singh1964` also used a third wheel after having little luck with
accelerometers and rate gyros. He obtained decent measurements but abandoned
the wheel because it was too large, dangerous and susceptible to vibration.
:cite:`Roland1971` measured roll angle with a potentiometric free gyro with
seemingly good results. Their data was captured with direct write recorders in
a pace car. :cite:`Eaton1973` used a third wheel and a potentiometer to measure
roll angle on a motorcycle, but also had reliability issues. :cite:`Zytveld1975`
used a small trailer with two roller skate wheels and potentiometer to measure
the roll angle on this robotic motorbike.

More modern techniques often focus around roll angle estimation.
:cite:`Boniolo2008`, :cite:`Boniolo2009` developed a simple algorithm to remove
the low frequency drift and only require yaw rate, roll rate and speed
measurements to get peak roll estimation errors of 5 degrees, which were larger
than we could accept. But their methods did allow for roll angle estimation on
banked curves.  Distance lasers have been used to directly measure the roll
angle with respect to the ground but are particularly expensive
:cite:`Evertse2010`. The roll angle can also be estimated with a state
estimator such as a Kalman filter (:cite:`Gustafsson2002`,
:cite:`Teerhuis2010`). The plant in the Kalman filter can be general 3D motion
of a rigid body or a model of the bicycle. Constraining the estimation with the
use of a bicycle model as the plant could have drawbacks when using the
resulting angle for model validation but can give potentially great results
otherwise. These types of algorithms are implemented in many modern sensor
packages and we decided to pursue one of these.

There is a class of sensors called Inertial Measurement Units (IMU) and/or
Attitude Heading Reference Systems (AHRS) that have recently become very
affordable and small enough to be appropriate for orientation and rate
estimation due to the advent of MEMs rate gyros, accelerometers, magnetometers,
and GPS technologies. An IMU can theoretically be rigidly affixed to each body
of the system to give complete kinematic details of the motion of that body.

Inertial Measurement Units
   An inertial measurement unit typically measures three body fixed components
   of angular rate of a rigid body and the three dimensional acceleration of a
   single point.
Attitude Heading Reference System
   An attitude heading reference system measures what an IMU does but also
   often includes earth magnetic field measurements and/or GPS combined with a
   microprocessor and estimation algorithm to additionally provide orientation
   and/or location estimations.

Many of these systems were within our budget range so we scouted various
companies (MemSense, Navionex, MotionNode, MicroPilot, Crossbow, VectorNav, Ch
Robotics, etc.) to see what was offered\ [#imus]_. We ended up choosing the VN-100
development board from a relatively new company called `VectorNav
<http://www.vectornav.com>`_ due to price, on board orientation calculations, and
the potential ease of collecting data via a typical RS-232 serial interface. My
preferred software tools, Matlab and Python, both had good serial interface
packages. We placed a single VN-100 on the rear frame to measure the angular
orientations and rates along with the acceleration of a point on the rear
frame. The VN-100 relies on additional magnetometer readings and an on-board
proprietary algorithm based on a Kalman filter for computing the real time
orientation about the three axes.

The VN-100 turned out to be a poor choice for our application in multiple ways,
the second of which I'll talk about in a later section. The first is that the
orientation estimations were very poor. I wanted *at least* accurate estimate
of the roll angle of the bicycle. The VN-100 repeatedly was not able to provide
this. VectorNav worked with me and tried offer various methods of tuning the
VN-100 with state covariance weightings for the Kalman filter and also to tune
out any static magnetic fields from the bicycle frame, but with no success. The
issues were associated with both the wheel and front frame relative rotations
to the rear frame, with could cause varying disturbances in the magnetic field.
The hub motor also negatively affected the sensor readings and these may have
been too great to tune out. I also realized that going with a proprietary
generic estimator is a bad idea, especially when one has a good model of the
dynamics of the rigid body that the sensor is attached to. In our case if the
Kalman filter was programmable, we could tailor it with the bicycle model to
improve the orientation estimation significantly. Also if the VN-100 could
accept input signals, the filter could be tuned well too. After countless hours
trying to tune their proprietary filter I gave up and went with a classic roll
angle measurement design that I should have done in the beginning.

I designed a simple trailer, :ref:`Figure 11.5<figRollTrailer>`, that was pulled
behind the bicycle to measure roll angle with a potentiometer, much in the way
the steer angle was measured. The trailer needed to be light such that it
didn't adversely affect the lateral dynamics and be able to give a good
estimate of the roll angle. All of our experiments were to be on smooth
surfaces, so the vibration issues that on-road tests have seen were of little
concern. I designed the trailer around two caster style polyurethane wheels
(roller blade wheels). They were attached to a frame which attached via a
revolute joint aligned with the roll axis to a yoke that attached at the axle
of the rear wheel.

.. _figRollTrailer:

.. figure:: figures/davisbicycle/roll-trailer-annotated.*
   :width: 5in
   :align: center
   :target: _images/roll-trailer-annotated.png

   On the left is photo of the roll angle trailer with it's components
   annotated. The right photo shows it attached to the instrumented bicycle.

The potentiometer effectively measures the angle between the yoke and the main
trailer frame\ [#rolltrailer]_. For a direct measurement of the true roll angle
of the bicycle, the trailer roll axis must lie in the ground plane, but this is
physically impossible so it is preferable for the axis to be as close to the
ground as possible. :ref:`Figure 11.6<figTrailerAngle>` shows how the yoke pitch
angle and the trailer roll angle change as functions of the bicycle roll angle
for various heights above the ground. Notice that the trailer roll angle is
virtually identical to the bicycle roll angle for given heights.

.. _figTrailerAngle:

.. figure:: figures/davisbicycle/trailer-angle.*
   :width: 4in
   :align: center
   :target: _images/trailer-angle.png

   The yoke pitch angle :math:`\alpha` and the potentiometer angle :math:`\beta`
   as a function of the bicycle roll angle :math:`\theta` for different for
   various joint heights :math:`h`. The potentiometer angle is highly linear
   with respect to the roll angle. Generated by
   ``src/davisbicycle/roll_angle_trailer.py``

Steer
-----

The steer angle is easy to measure with either some form of write recorder,
potentiometer, or encoder and has been accurately measured on many bicycle and
motorcycle systems since the early 50's. Of the early methods,
:cite:`Wilson-Jones1951` has a particularly interesting mechanical protractor design
and :cite:`Dohring1953` makes use of a mechanical write recorder. Because the front
frame is attached to the rear frame via a revolute joint only an additional
single orientation and rate measurement is needed to measure the front frame
motion. I used a similar design and setup as the Delft instrumented bicycle,
:ref:`Figure 11.7<figSteerSensors>`: a potentiometer for relative steering angle
measurement and a single axis rate gyro for the body fixed angular rate of the
front frame about the steer axis\ [#rategyro]_. I modified the design with some
minor improvements such as better tension adjustability and switching to a
screw mount potentiometer.

.. _figSteerSensors:

.. figure:: figures/davisbicycle/steer-sensors.*
   :width: 3in
   :align: center
   :target: _images/steer-sensors.png

   The steer angle and steer rate sensors.

Wheel Rate
----------

As has been shown in previous chapters, bicycle dynamics are highly dependent
on speed. This requires good estimation of the average speed for each constant
speed run. I measured the rear wheel rate in the same fashion as on the Delft
instrumented bicycle. We mounted a small DC permanent magnet motor (Globe
Motors E-2120 without the encoder) to the rear frame in much the same way as a
simple friction generator for a bicycle light :ref:`Figure
11.8<figSpeedometer>`. A small knurled aluminum disc on the motor shaft engaged
the sidewall of the tire which is radius :math:`r_c` from the wheel hub.
:math:`r_c` was slightly different for runs 0 to 226 than for run numbers
greater than 226 because it was remounted for better tangential disc to tire
contact.

.. math::
   :label: eqDiscContactRadius

   r_c =
   \begin{cases}
      0.333 m & \textrm{if the run number is $\leq 226$}\\
      0.320 m & \textrm{if the run number is $> 226$}
   \end{cases}

The voltage of DC motors is linearly proportional to the angular speed of the
disc. The disc diameter, :math:`r_d=0.029` m, was chosen such that 0 to 10
volts would correspond to approximately 0 to 30 mph.

.. _figSpeedometer:

.. figure:: figures/davisbicycle/speedometer.*
   :width: 4in
   :align: center
   :target: _images/speedometer.jpg

   The wheel rate sensor mounted just below the bottom bracket. The original
   configuration is pictured where the velocity of the contact point was not
   quite in the plane of the disc. We later remounted it so that the motor disc
   contacted the tire casing tangential to the linear velocity at the contact
   point.

Sensors
-------

:ref:`Table 11.2<tabFinalSensors>` gives the characteristics of the final choice
in sensors.

.. _tabFinalSensors:

.. tabularcolumns:: LLLL

.. list-table:: Final Kinematic Sensors, \*Accuracies reported with respect
   to the calibrated and filtered output.

   * - Measurements
     - Range
     - Accuracy
     - Sensor
   * - Roll Angle
     - :math:`\pm 42.5^\circ` (pot :math:`340^\circ \pm 5^\circ` with 1:4 gear reduction)
     -
     - Single turn potentiometer (ETI Systems SP22F)
   * - Steer Angle
     - pot :math:`340^\circ \pm 5^\circ`
     -
     - Single turn potentiometer (ETI Systems SP22F)
   * - Yaw Rate, Roll Rate, Pitch Rate
     - :math:`\pm 500` deg/s, :math:`\pm 500` deg/s, :math:`\pm 500` deg/s
     - :math:`<\pm 0.06` deg/s (bias stability)*
     - VN-100 (Invensense IDG500 and ISZ500)
   * - Front frame fixed angular rate about the steer axis
     - :math:`\pm200` deg/s
     - See manufacturer's spec sheet
     - Single axis rate gyro (Silicon Sensing CRS03-04S)
   * - Rear wheel rate
     - 0 - 40 rad/s
     -
     - Globe Motors E-2120 DC Motor without the encoder
   * - Rear frame 3D point acceleration
     - :math:`\pm2` g
     - x/y :math`<2` mg, z :math:`<3` mg (bias stability)
     - VN-100 (Analog Devices ADXL325)

The VN-100 was mounted to the rear frame with its factory X axis aligned with
:math:`\hat{c}_1`, Y axis aligned with the :math:`-\hat{c}_3`, and Z axis
aligned with :math:`\hat{c}_2` as described in Chapter :ref:`eom`. I made use
of the VN-100's ability to output it's measurements with respect to a different
reference frame than the factory frame and aligned the X, Y and Z axes with the
:math:`\hat{c}_1`, :math:`\hat{c}_2` and :math:`\hat{c}_3` axes, respectively.
This pre-output rotation matrix was recorded in the meta data for each run. The
steer rate gyro was attached such that its axis was aligned with
:math:`\hat{e}_3`.

The yaw, roll and pitch rates as defined in Chapter :ref:`eom` are computed
from the measured body fixed rear frame rates :math:`\omega_{x,y,z}`, the
measured roll angle :math:`q_4` and the steer axis tilt :math:`\lambda`

.. math::
   :label: eqRearFrameRates

   u_3 = \frac{\omega_x \sin(\lambda) - \omega_z \cos(\lambda)}
   {\cos(q_4)}

   u_4 = \omega_x \cos(\lambda) + \omega_z \sin(\lambda)

   u_5 = \omega_y + \omega_x \sin(\lambda) \tan(q_4) - \omega_z
   \cos(\lambda) \tan(q_4)

The steer rate is found by subtracting the body fixed rear frame rate,
:math:`\omega_z` from the body fixed front frame rate, :math:`\omega_{ff_z}`

.. math::
   :label: eqSteerRate

   u_7 = \omega_{ff_z} - \omega_z

The yaw angle, :math:`q_3`, can be estimated by integrating the yaw rate,
:math:`u_3`. The result is affected by drift but for runs that are centered
around zero, this drift can be removed by subtracting the resulting line from a
linear regression on the drifted data. The resulting yaw angle can be used to
compute estimates for the rear wheel contact velocities: :math:`u_1` and
:math:`u_2` by making use of the measured rear wheel rate, :math:`u_6`.

.. math::
   :label: eqRearContactRates

   u_1 = -u_6 r_R \cos(q_3)

   u_2 = -u_6 r_R \sin(q_3)

The rear wheel contact rates can also be integrated and the linear drift
subtracted out to find the position from an arbitrary initial condition. I also
make use of the lengthy non-linear relationships for the front wheel contact
points as a function of the rear wheel contact points, steer, roll, and pitch
to compute the front wheel track. See the ``BicycleDataProcessor`` source code
for these details.

Kinetics
========

A human is able to use contact forces and body movements to control the
bicycle. The forces applied by the rider's hands to the handlebars are the most
obvious and most effective method of controlling the bicycle [#rollcontrol]_.
But the rider also can impart forces through the seat and the foot pegs. If the
rider is controlling the bicycle without touching the handlebar, these would be
the only locations of rider to bicycle contact. For a complete dynamic picture
of the rider's control inputs, all of the essential forces and moments at the
rider/bicycle interface's need be measured. In the case of the rigidified
rider, the steering torque is sufficient for characterizing the control inputs.

For the sake of perturbing the closed loop bicycle/rider system, we also needed
to measure and externally apply force or torque. We opted for a simple lateral
force perturbation.

Lateral Perturbation Force
--------------------------

I was introduced to the idea of external lateral force perturbations from some
of my first email exchanges with Arend and when I was in Delft we did several
experiments with lateral perturbations :cite:`Kooijman2009a`. We applied the
impulsive type of perturbations without measuring the applied force assuming
they could be modeled as impulses. There are also many other past attempts at
exciting the system. :cite:`Roland1971` on the other hand attached a calibrated
rocket to the handelbars of a riderless bicycle to give a known step input to
steer torque. :cite:`Eaton1973` had the motorcycle rider tap the handlebars to
apply an impulse and also drop weights from the side of the motorcycle to
apply a roll torque. :cite:`Doria2012` similarly had the motorcycle rider apply
impulsive forces to the handlebars to excite the weave mode. :cite:`Lange2011`
discusses several methods of applying a roll torque to the bicycle
including a mass swing, a mass slider, a rope, and laterally accelerating the
ground. His designs are intended to apply an oscillatory roll torque to
facilitate system identification in the frequency domain\ [#idealinput]_.

We weren't able to come up with a clever way of perturbing the system with a
harmonic input and frankly I did not think a great deal about the perturbation
methods, so I simply attached a 100 lb force load cell (Interface SSM-100) in
line with a rope attached to the underside of the bicycle seat. We intended to
apply impulsive lateral forces to the bicycle rear frame. This worked for the
first round of experiments, but only provided a negative lateral force as it
could only be pulled. After the first experiment attempts, we solved this by
attaching the load cell in line with a push/pull stick which was attached to
the seat via a ball joint, :ref:`Figure 11.9<figLateralForceStick>`. The ball
joint prevented any external moments from being applied to the bicycle and the
force to be in a mostly lateral direction.

.. _figLateralForceStick:

.. figure:: figures/davisbicycle/lateral-force-stick.*
   :width: 4in
   :align: center
   :target: _images/lateral-force-stick.jpg

   The lateral force stick attached to the underside of the seat. A rod end was
   used at the connection to prevent moments from being applied to the rear
   frame.

We were also concerned with the rider predicting the lateral perturbations.
Ideally the rider shouldn't be able to predict the instant or the direction of
the upcoming perturbation. The rider wore a helmet with a blinder on the side
of the lateral force stick so that they could not see the movements of the
stick or the person operating the stick. And secondly, we wrote a simple
program which randomly instructed the perturber when and in which direction to
apply the force for the treadmill experiments. During the runs in the
gymnasium, we retained the blinder and provided the perturber with a series of
random push/pull sequences before each run. The operator applied as many
perturbations as possible over the length of the track, which didn't give much
unpredictability in the time of perturbation. :ref:`Figure
11.10<figPerturbation>` gives an example perturbation measurement during a
treadmill run.

.. _figPerturbation:

.. figure:: figures/davisbicycle/perturbation.*
   :width: 5in
   :align: center
   :target: _images/pertubation.png

   The left figure shows an example of a lateral perturbation sequence during a
   treadmill run. The right figure shows the profile of a perturbation over one
   second.

Seat Post
---------

As already mentioned, I had intended to measure the forces at all of the
rider/bicycle interfaces. Cal Stone :cite:`Stone1990` developed a seat post which
was capable of measuring five components of force in the seat post with an
array of strain gauges. I was going to add a strain gage bridge for the
remaining unmeasured component, torque about the seat axis, to complete the
force measurements and use the seat post in combination with the flexible rider
harness. The seat post was originally instrumented by simply gluing strain gage
bridges onto a stock seat post and carefully calibrating the sensor for a
variety of loading combinations. The accuracy of the seat post force
measurements was not all that high due to the small strains seen along the
outer wall of the seat post. In a way, the use of the seatpost was more because
of the convenience of having access to it than obtaining the actual kinetics
involved when using the flexible rider harness. Gilbert and I spent a
lot of time figuring out how to use and calibrate the seatpost and associated
equipment. Fortunately, a copy of Cal's research notes were found that helped
decipher most of the work. We even got in touch with Cal and he provided
additional information. But as time constraints weighed in, we had to abandon
the effort.

Foot Pegs
---------

Gilbert designed a set of foot pegs such that clipless bicycle pedals could be
screwed into the ends providing secure attachment of the feet but allowing
easier detachment, :ref:`Figure 11.11<figFootPeg>`. Each foot peg was fit with
two strain gage bridges to measure the downward force applied by the rider's
feet. These were also abandoned due to time constraints.

.. _figFootPeg:

.. figure:: figures/davisbicycle/foot-peg.*
   :width: 4in
   :align: center
   :target: _images/foot-peg.jpg

   One of the foot pegs after the strain gages were applied. The 7075 aluminum
   peg was press fit into the bottom bracket insert made from 1018 steel.

Steer Torque
------------

A rider applies forces to the handlebars that cause the front frame to rotate
relative to the bicycle frame. These forces can be lumped into an effective
steer torque. Steer torque is the most effective natural input to control a
bicycle and the input that the human most often utilizes. :cite:`Roland1972`
explicitly differentiates steer torque based control from steer angle as
opposed to :cite:`Lunteren1969` which hypothesized that steer angle was the
controlled input. :cite:`Weir1972` demonstrates that steer angle control input
has poor gain and phase margins as compared to steer torque control input.
:cite:`Weir1979a` shows that a no hand lane change is much less "precise and
efficient" as to one done with steer torque control. :cite:`Sharp2008a` shows
that steer torque is always the optimal control input when the cost function is
based on control power. Accurately measuring the applied steer torque can
provide rich data with which to understand the bicycle dynamics and the
validity of the underlying models. But steer torque is one of the more
difficult variables to properly measure. The required steering torque for
controlling a bicycle in normal maneuvers is of relatively low magnitude,
typically less than 5 Nm. This small torque can be swamped by the other
potentially large forces a rider may apply to the bicycle's handlebars. These
small torque magnitudes require a well designed load cell to give accurate
measurements.

There are very few published studies that measure or attempt to measure steer
torque on a bicycle or lightweight single track vehicles and these measurements
typically do not match the results of the analytical models. There have been
more attempts at measuring the steer torque on motorcycles.

Bicycle Experiments
~~~~~~~~~~~~~~~~~~~

:cite:`Lorenzo1997`
   David de Lorenzo instrumented a bicycle which could measure pedal,
   handlebar, and hub forces to characterize the in-plane structural loads
   during downhill mountain biking. The handlebar forces were measured with a
   handlebar sensitive to :math:`x` (pointing forward and parallel to the
   ground) and :math:`z` (pointing upwards, perpendicular to the ground) axis
   forces on both the left and right sides of the handlebar. Net torque about
   any vector in the fork plane of symmetry can be calculated from the applied
   forces. Figure 3d in the paper shows a single plot of steering torque with
   maximums around 7 Nm. The stem extension torque (representing the torque
   from pushing down and up on the handlebars) reaches 15 Nm, which is about
   twice the maximum steer torque shown. The calibration details lead me to
   believe that the crosstalk from the all of the forces and moments on the
   handlebars gives a very low accuracy for the reported torques, probably in
   the :math:`\pm 1` to 3 Nm range.
:cite:`Jackson1998`
   They don't measure steer torque explicitly but attempt to predict the
   contributions to the torques acting on the front frame based on orientation,
   rate and acceleration data taken while riding a bicycle with no-hands. They
   show a single graph with torques under :math:`\pm2.5` Nm acting on the front
   frame about the steer axis.
:cite:`Cheng2003`
   This is a report about a design project at UCSB to develop and implement a
   steer torque measurement device on a bicycle. The experiments and
   measurements seem to be one of a kind for bicycles up to that point in time.
   They begin with doing some basic experiments by attaching a torque wrench to
   a bicycle and made left at right turns at speeds from 0 to 13 m/s (0 to
   30mph). The torques were found to be under 5 Nm except for the 13 m/s trial
   which read about 20 Nm. They designed a pretty nice compact torque
   measurement setup by mounting the handlebars on bearings and using a linear
   force transducer to connect the handlebars to the steer tube, :ref:`Figure
   11.11<figCheng>`, which reduced the effects of other moments and forces
   acting on the steer tube. It seems that downward forces applied to the
   handlebars could possibly still be transmitted to the load cell. The design
   does allow one to choose the lever arm for the load cell, thus giving some
   choice to amplify the force signal. They set it up to measure from 0 to 84
   Nm with a Model SM Series S-type load cell from Interface with a 670 Newton
   range. This range is quite large with respect to the torque values found in
   the first experiments. They self calibrated the sensor with with a set of
   pulleys and cables to apply a pure torque to the handlebars. They measured
   the torque during two different maneuver types: a sharp turn at various
   angles and steady turns on various diameter circles, both at 10 mph (4.5
   m/s). The rider maintained constant speed through visual feedback of a
   speedometer. The signals were very noisy and Cheng filters the data with a
   moving average. He was not able to identify any countersteering. Cheng
   claimed the rider turns the handle bars right to initiate a right turn,
   which is counter to what models and other experiments predict. For the sharp
   turns the highest reported torque is about 10 Nm, for the steady turning
   they report the highest average torque as 1 Nm.
:cite:`Astrom2005`
   Åström et al. talks briefly about the steer torque measurement system
   constructed for the UCSB instrumented bicycle but with little extra
   information. He does include a nice photo of the apparatus, :ref:`Figure
   11.12<figCheng>`.

   .. _figCheng:

   .. figure:: figures/davisbicycle/cheng-steer-torque-design.*
      :width: 3in
      :align: center
      :target: _images/cheng-steer-torque-design.jpg

      Cheng's design, from :cite:`Astrom2005`.
:cite:`Iuchi2006`
   They construct a bicycle with a steer motor and controller which treats the
   rider's additional input as an additive input instead of a disturbance. The
   rider's steer torque contribution is estimated from the motor torque and the
   handlebar and motor moments of inertia. Little detail is given to properly
   assess the design, but measuring steer torque by motor current may be
   effective. They are one of the few studies that takes into account some of
   the inertial effects of the handlebar.
:cite:`Cain2010`
   He designed a custom torque sensor that fit inside a bicycle steer tube. He
   mostly removed the crosstalk effects due to an axial load on the sensor, but
   the design still seems very likely susceptible to bending moments on the
   steer tube. He also didn't account for the dynamic inertial affects of the
   handlebar and fork/wheel which are above and below the sensor, but this is
   most likely inconsequential for steady turns. His measured steer torques for
   steady turns never exceeded 2.4 Nm. He wasn't able to predict steer torque
   well with his bicycle model and only points to the fact that the sensor was
   90% oversized for an explanation of the poor results.
:cite:`Ouden2011`
   Designs a steer torque sensor for a bicycle which has a range of about
   :math:`\pm7.5` Nm. He was acutely aware of crosstalk issues with respect to
   the other forces applied to the handlebars and tried to design accordingly,
   but found that his design was still very susceptible to handlebar loads. He
   modifies the device to eventually get more reliable readings. He also didn't
   account for the inertial effects of the front frame. He had test subjects
   ride the bicycle around town so the data is difficult to interpret.

Motorcycle Experiments
~~~~~~~~~~~~~~~~~~~~~~

:cite:`Wilson-Jones1951`
   Wilson-Jones beautiful treatise on single track vehicle dynamics may
   document the first steer torque measurements ever done. He constructed an
   mechanical analog torsion bar that provided the instantaneous steer torque
   readings to the motorcycle driver via a head tube mounted protractor. He
   used this to gage torques in turns.
:cite:`Kondo1955`
   Kondo's work is the first electrical measurement of steer torque that I've
   come across. He does not give great detail of the sensor and shows only one
   plot of steer torque and steer angle from experimental measurements. The
   units for the steering force are in kilograms and I'm not completely sure
   what was being measured. My poor understanding is limited by the light
   translations with which I got help.
:cite:`Fu1965`
   Measures steering torque in steady turns but the resulting data is not
   published in this paper. He refers to it as future work in the review
   section. He claims agreement with :cite:`Kageyama1959` of which he was a
   co-author, but I wasn't able find this paper.
:cite:`Eaton1973`
   Eaton attached a torque bar with strain gages to the top of the motorcycle
   handlebar, :ref:`Figure 11.13<figEatonSteerTorque>` and had the rider control
   the motorcycle with one hand to get a measure of steering torque. The steer
   torque sensor design was very simplistic, but he found good agree with his
   motorcycle model when identifying the motorcycle from the steer torque input
   and roll angle output.  The motorcycle steer torque measurements are
   probably more forgiving as the steer torques are of a much higher average
   magnitude. For his roll stabilization tasks (i.e. straight riding) he
   measured maximum values of steer torques of 3.4 Nm for speeds of 15 to 30
   mph.

   .. _figEatonSteerTorque:

   .. figure:: figures/davisbicycle/eaton-steer-torque.*
      :width: 3in
      :align: center
      :target: _images/eaton-steer-torque.jpg

      Eaton's simple bar torque sensor.

:cite:`Weir1979a`
   Weir et al. designed a modular torque sensor which could be affixed to
   multiple motorcycles, :ref:`Figure 11.14<figWeirSteerTorque>`. The range was
   +/- 70 Nm with 1% accuracy and >10 Hz dynamic range. The crosstalk due to
   the other moments on the steer was removed by utilizing two thrust
   bearings. It included stops to prevent sensor overload protection and
   weighed 14 Newtons. They comment that the handlebars are significantly rigid
   for their purposes. They comment that the range is too large for small
   amplitude inputs used in steady turning and straight running and that more
   sensitivity would be needed to measure these accurately. Weir used this to
   measure steer torques for several motorcycles at various speeds (>10 m/s)
   for steady turning and lane change maneuvers. Steady turning produced
   torques in the range of -10 to 30 Nm and the lane change produced -20 to 55
   Nm.

   .. _figWeirSteerTorque:

   .. figure:: figures/davisbicycle/weir-torque-load-cell.*
      :width: 4in
      :align: center
      :target: _images/weir-torque-load-cell.jpg

      The steer torque measurement design from :cite:`Weir1979a`. The adaptor plate
      allowed one to attached the main housing to a variety of motorcycle forks.
      The handlebar mounting block "floated" on a set of thrust bearings that
      resisted all forces applied to the handlebars except the moment about
      the steer axis. The Lebow torque sensor resisted the moment about the
      steering axis to give a pure torque measurement.

:cite:`Sugizaki1988`
   They measure steer torque on four motorcycles during high speed lane
   changes. No detail of the steering torque measurement system is given but
   they show the time traces of steer torque for some of the maneuvers which
   vary between -20 and 20 Nm. The time traces have little visible human remnant
   or noise, which is questionable.
:cite:`Taro2000`
   The abstract for this paper indicates steer torque measurements on a
   motorcycle, but I haven't located the paper. I include the citation for
   completeness.
:cite:`Bortoluzzi2000`
   Same description of the transducer as :cite:`Biral2003`.
:cite:`Biral2003`
   Biral et al. designed a custom steer torque measurement system for a
   motorcycle using a cantilever beam, :ref:`Figure 11.15<figBiralSteerTorque>`.
   The handlebars were mounted on a bearing similar in idea to :cite:`Weir1979a` but
   the steering torque load is transmitted through a thin cantilever beam which
   engages the fork. The design is such that other handlebar forces will not
   influence the torque measurement. It includes stops in case the beam breaks.
   They report experimental values for torque that match their model
   predictions very well. The measure torques from -20 to 20 Nm for a slalom
   maneuver at 40 m/s.

   .. _figBiralSteerTorque:

   .. figure:: figures/davisbicycle/biral-steer-torque-design.*
      :width: 4in
      :align: center
      :target: _images/biral-steer-torque-design.jpg

      The cantilever beam design taken from :cite:`Biral2003`.
:cite:`James2002`, :cite:`James2005`
   James measures steer torque on an off-road motorcycle by attaching a
   lightweight secondary handlebar connected to the primary handlebar via a
   load cell. In the second paper he has a single wheel trailer attached to the
   vehicle.
:cite:`Capitani2006`
   They measure steer torque on a scooter during a lane change and turning to
   compare with their model. No detail is given on how steer torque is
   measured, so I can't comment on the quality of the measurement but they
   report values of -15 to 40 Nm on a couple of graphs. The paper is extremely
   poor and makes false conclusions.
:cite:`Evertse2010`
   He mounts two axis load cells at the handlebar grips to measure the forces
   on the grip. This puts the sensor right at the human/machine interface thus
   negating the need to worry about the inertial effects of the front frame.
   For his obstacle maneuver tests the maximum steer torques were no greater
   than 40 Nm.
:cite:`Teerhuis2010`
   Measured motorcycle steer torque in steady turns and slalom maneuvers. The
   torques in the two time history graphs are less than 20 Nm.

Bicycle Models
~~~~~~~~~~~~~~

:cite:`Limebeer2006`
   Limebeer and Sharp show a graph of a steer torque prefilter (i.e. torque
   generated for roll control) output to command a ~40 degree roll angle for
   the benchmark bicycle model. The torques are in the realm of -0.5 to 2.5 Nm.
:cite:`Sharp2007a`
   Sharp uses the benchmark bicycle model and an LQR controller with
   preview to follow a randomly generated path that has about 2 meter lateral
   deviations. The bicycle is traveling at 10 m/s and the steer torque ranges
   from about -15 to 15 Nm. Medium control reduces the torques to under
   :math:`\pm 10` Nm. Straight line to circle path maneuvers show torques
   ranging from -0.5 to 0.5 Nm for loose control and -2.5 to 2.5 for medium
   control.
:cite:`Connors2008`
   They model a recumbent bicycle with the Whipple model and additional
   rotating legs. The bicycle is stabilized in roll from 5 to 30 m/s requiring
   up to :math:`\pm 8` Nm of steering torque, which is a function of the leg
   oscillation frequency.
:cite:`Sharp2008a`
   Sharp used the benchmark bicycle model and an LQR controller with preview to
   make a bicycle track a 4 meter lane change at 6 m/s. During this maneuver,
   the steer toque ranged from about -1 to 1 Nm. He also showed a very fine
   steer torque variation in the range of 0 to 0.0025 Nm about 10 meters before
   the start of the lane change.
:cite:`Peterson2009`
   Peterson and Hubbard show the steady turning required steering torques for
   the benchmark bicycle on page 7. The torques for lean angles from 0 to 10
   degrees and steer from 0 to 45 degrees are under 3 Nm.

Motorcycle Models
~~~~~~~~~~~~~~~~~

:cite:`Sharp1971`
   Reports steady state motorcycle steering torques for 10 degree banking turns
   in the range of -25 Nm to 2.35 Nm for speeds 10 ft/s to 160 ft/s.
:cite:`Cossalter1999`
   Studies steady turning of a motorcycle model with toroidal tires and tires
   as force generators. For slower speed steady turns, the model predicts
   steering torques up to 10 Nm.
:cite:`Tanelli2006`
   They stabilize a motorcycle model at roll angle up to 30 degrees with -5 to
   7.5 Nm of steer torque.
:cite:`Sharp2007`
   Sharp uses a multi-degree of freedom motorcycle model and an LQR controller
   with preview to control a motorcycle moving at 30 m/s through a 4 meter lane
   change and a 250 meter S-turn. For the lane change he gets torques ranging
   from about -20 Nm to 55 Nm for a more aggressive control and -4 to 6 Nm for
   less aggressive control. The S-turn gives torques from -40 Nm to 70 Nm with
   a sharp peak in torque in the middle of the S-turn.
:cite:`Cossalter2007`
   They study steady turning of motorcycles and show a plot that predicts steer
   torques in the range of -3 to 10 Nm for lateral accelerations from 0 to
   11 m/s^2 and speeds from 5 to 50 m/s.
:cite:`Marumo2007`
   Their steer controller for Sharps four degree of freedom motorcycle model
   shows a -50 nm maximum steer torque for a commanded roll angle of 20 degrees.

Steering torque has been measured in relatively few instances of bicycle
experiments and not many more for motorcycles. Of these, very few of
the designs may actually measure a pure rider applied steer torque. This is
more consequential for bicycles than motorcycles because the small torques used
in typical bicycle control are certainly less than 10 Nm with the majority less
than 5 Nm. :cite:`Ouden2011`, in particular, showed how sensitive the torque
measurements are to other handlebar loads. Also, most of these designs measure
the torque somewhere between the rider hands and the ground contact point.
This is a physically ideal way to measure the steer torque, but no one has
accounted for the dynamic inertial effects of the front frame above or below
the sensor. :cite:`Evertse2010` may be the only design which mitigates this issue.
I'll show later in this chapter that for maneuvers that require large steer
angular accelerations, that this is a significant additive effect.

With these previous works in mind, I wanted to develop a very accurate steer
torque measurement system for our bicycle. If one is interested in extracting
the "pure torque" applied by the rider to control the bicycle for model
validation purposes, it is critical to take care of several important details.

Another thing to note is the differences in magnitudes of steer torques in the
bicycle models as compared to the bicycle experiments. The steer torque used to
control the various models presented are much lower than the measured values.
This implies that there may be some missing components of torque in the models,
especially with respect to tire interactions with the ground.

I started by taking some crude steer torque measurements myself, similar to the
first method presented by :cite:`Cheng2003`, as I hadn't found Cheng's paper or any
of the post 2008 references yet. Secondly, I address the issue of the potential
loads acting on the steer tube other than steer torque. And finally, I show the
calculations to account for the inertial effects of the front frame.

Torque Wrench Experiments
~~~~~~~~~~~~~~~~~~~~~~~~~

Following in Cheng's footsteps, we decided to do some experiments with an
accurate torque wrench to get an idea of the maximum torques we would see in
our experiments. We designed a simple attachment to the steer tube that allowed
easy connection of various torque wrenches, :ref:`Figure
11.16<figTorqueWrenchMount>`.  A helmet camera was mounted to the bicycle such
that it could view the torque wrench, handlebars and speedometer relative to
the bicycle frame, :ref:`Figure 11.17<figTorqueWrenchCamera>`. The torque
wrench (CDI Torque Products 751LDIN) had a range from 1.7 to 8.5 Nm and a
:math:`\pm 2\%` accuracy of full scale (:math:`\pm 0.17` Nm) for static
measurements, :ref:`Figure 11.18<figTorqueWrenchFace>`. The bicycle speed was
maintained by an electric hub motor (i.e.  no pedaling) with a crude power
based cruise control, but speeds remaining fairly constant.

.. _figTorqueWrenchMount:

.. figure:: figures/davisbicycle/torque-wrench-mount.*
   :width: 3in
   :align: center
   :target: _images/torque-wrench-mount.jpg

   The mounting bracket for the torque wrenches. The lower portion clamps to a
   1 1/8" steer tube and the upper portion clamps of a 1/4" socket end.

.. _figTorqueWrenchFace:

.. figure:: figures/davisbicycle/torque-wrench-face.*
   :width: 4in
   :align: center
   :target: _images/torque-wrench-face.jpg

   The dial indicator face of the torque wrench which reads out in inch pounds
   and newton meters.

.. _figTorqueWrenchCamera:

.. figure:: figures/davisbicycle/torque-wrench-camera.*
   :width: 4in
   :align: center
   :target: _images/torque-wrench-camera.jpg

   The complete setup with the frame mounted helmet camera.

We recorded video data for two riders performing seven different maneuvers:
straight run into tracking a half circle of radius 6 and 10 meters, tracking a
straight line, 2 meter lane change, slalom with 3 meter spacing, and steady
circle tracking of radius 5 and 10 meters. I viewed the videos and noted the
maximum and minimum torques for each run. I ignored obviously high torque
readings from accelerations due to riding over bumps.

The single comma separated data file includes the run number that corresponds
to the video number, the rider's estimate of the speed after the run in miles
per hour, the maximum reading from the torque needle after the run in inch-lbs,
the rider's name, the maneuver, the minimum speed seen on the video footage in
miles per hour, the maximum speed seen on the video footage in miles per hour,
the maximum torque seen on the video footage in inch-lbs, the minimum torque
seen on the video footage in Nm, and the rotation sense for each run
(+ for clockwise [right turn] and - for counter clockwise [left turn]). The
videos, data file and R source code are archived at
`<http://www.archive.org/details/BicycleSteerTorqueExperiment01>`_ .

The primary goal was to determine the maximum torques we will see for the types
of maneuvers we are interested in. The histogram, :ref:`Figure
11.19<figTwrenchTorqueHistogram>`, shows that we never recorded any torques
higher than 5 Nm and table :ref:`Table 11.3<tabTorqueManeuver>` gives the
maximum and minimum torques for each maneuver. :ref:`Figure
11.20<figTwrenchTorqueSpeed>` shows all of the recorded torques as a function
of speed. There may be an underlying dependency on speed, i.e. that the maximum
torques decrease as speed decreases.

.. _figTwrenchTorqueHistogram:

.. figure:: figures/davisbicycle/twrench-torque-histogram.*
   :width: 4in
   :align: center
   :target: _images/twrench-torque-histogram.png

   A histogram of the maximum recorded torques for all runs. The median is
   around 2 Nm with torques measured up to 5 Nm. Generated by
   ``src/davisbicycle/torque-wrench.R``.

.. _tabTorqueManeuver:

.. tabularcolumns:: LLL

.. list-table:: Maximum and minimum torques values for the different maneuvers.
   :header-rows: 1

   * - Maneuver
     - Maximum Torque
     - Minimum Torque
   * - Steady Circle (r = 10m)
     - 3.4
     - -2.4
   * - Steady Circle (r = 5m)
     - 2.4
     - -2.2
   * - Half Circle (r = 10m)
     - 3.8
     - -3.2
   * - Half Circle (r = 6m)
     - 3.4
     - -5.0
   * - Lane Change (2m)
     - 2.9
     - -2.6
   * - Line Tracking
     - 2.6
     - -3.4
   * - Slalom
     - 4.5
     - -4.8

.. _figTwrenchTorqueSpeed:

.. figure:: figures/davisbicycle/twrench-torque-speed.*
   :width: 4in
   :align: center
   :target: _images/twrench-torque-speed.png

   The maximum torques as for each run as a function of speed. Generated by
   ``src/davisbicycle/torque-wrench.R``.

This set of experiments enforces the previously cited experimental findings
that steer torques in bicycle control are typically very small. Ideally our
sensor's range should be somewhere around :math:`\pm 8` to 10 Nm.

Forces on the steer tube
~~~~~~~~~~~~~~~~~~~~~~~~

Measuring the steer torque is not trivial. This is because various models
predict torques ranging in the 0-2 Nm (0-1.5 ft lbs) range with signal
variations and reversals requiring :math:`\pm 0.01` Nm (0.01 ft lbs) in
measurement accuracy. The range and accuracy are easily measured with modern
torque sensors, but the fact that large moments can be applied to the fork and
handlebars by the ground and/or rider introduces the problem of crosstalk. The
forces and moments applied to the fork will corrupt the relatively small torque
measurements as they can be hundreds of times larger in magnitude. With this in
mind, we seek a way to isolate the torque measurement to eliminate or minimize
the crosstalk and get good, noiseless, accurate readings.

One of the simplest ways to measure steer torque may be to apply a strain gauge
bridge primarily sensitive in torque to the steer tube of the fork. This method
and others would require that the cross sensitivity of the bridge to other loads
in the steer tube to be negligible. For example, :cite:`Lorenzo1997` effectively did
this with his handlebar design but used several other bridges to measure
additional moments and forces in handlebar assembly and calibrated the set of
bridges together to help eliminate the crosstalk. The measured steer torques
are less than 10 n-m and the loads due to the applied forces at the wheel
contact, headset bearings and handlebars can potentially be orders of magnitude
greater. :cite:`Ouden2011` clearly experienced the difficultly in removing the cross
talk from a steer torque sensor and few studies have explicitly addressed this.

Assuming we may want to measure steer torque somewhere between the handlebars
and fork crown, a simple static analysis can be performed to gage the relative
magnitudes of loads in the steer tube. The bicycle steer tube has various other
forces acting on it. For the most basic case, the ground contact force at the
front wheel puts the fork into bending and compression. Likewise the person can
apply forces to the handlebars which also put the steer tube into bending and
compression. :ref:`Figure 11.21<figBicycleForces>` shows the free body diagram
for a bicycle statically loaded.

.. _figBicycleForces:

.. figure:: figures/davisbicycle/bicycle-forces.*
   :width: 2.5in
   :align: center
   :target: _images/bicycle-forces.png

   The free body diagram allows for an external steering torque, independent
   downward forces on each handlebar, the ground reaction forces and a force
   acting on the mass of the bicycle and rider due to vertical acceleration.
   The vertical acceleration is simply due to gravity when static, but can be
   thought of as a multiple of the acceleration due to gravity for dynamic
   purposes.

The forces and moments acting on the fork can be isolated algebraically and the
fork modeled as a basic beam supported by the headset bearings (points C and D)
and the forces/moments due to the ground reaction force and force applied to
the handlebars were calculated and applied to points A and B, :ref:`Figure
11.22<figForkBeam>`.

.. _figForkBeam:

.. figure:: figures/davisbicycle/beam.*
   :width: 2.98in
   :align: center
   :target: _images/beam.png

   The free body diagram of the fork under the loads shown in :ref:`Figure
   11.21<figBicycleForces>`. The headset bearings at C and D are assumed to not
   resist moments.

The following graph, :ref:`Figure 11.23<figForkLoad>`, shows what the shear and
bending moment diagrams for a 2g vertical acceleration and ~200 N force on one
handlebar grip look like both from the side and the front of the bike.

.. _figForkLoad:

.. figure:: figures/davisbicycle/fork-load-diagram.*
   :width: 5in
   :align: center
   :target: fork-load-diagram.png

   The shear and bending diagrams of the fork under a 2g acceleration and a
   right side handlebar load. The vertical black lines represent the headset
   bearing locations. Generated by ``src/davisbicycle/fork_load.py``.

This graph shows that the bending moments and shear stresses can be of much
larger magnitude than the steer torques. Misalignment of strain gages and the
resulting sensor crosstalk are magnified by the differences in loads and need to be
carefully accounted for. If the cross talk strains due to the bending moments
are even 1% of the of the total strain due to the moments, that can still
corrupt the steer torque measurement.

This analysis also predicts that if no loads are placed on the handlebars the
entire portion of the steer tube/stem above the headset has no bending moments
and no shear stress. This could be the ideal place for a torque sensor, if one
can eliminate the transfer of forces applied by the handlebars to the steer
tube.

This lead me through several design ideas but ultimately to a design that
isolates the steer torque sensor from the handlebar and fork loads with a zero
backlash telescoping double universal joint. The idea solidified after thinking
about an upside down tall bike I had created several years before. This
bicycle's tall handlebar, to reach the high rider, was attached to the bicycle
stem at the headset by a horizontal revolute joint which prevented the rider
from applying a fore/aft moment to the handlebar extension, but the rider could
still apply steer torques. My design exploited this odd feature by using a
universal joint which could only transmit a torque about it's primary axis. The
telescoping degree of freedom was added after Gilbert explained its necessity,
:ref:`Figure 11.24<figSteerTorqueDesign>`.

.. _figSteerTorqueDesign:

.. figure:: figures/davisbicycle/steer-torque-design.*
   :width: 4.75in
   :align: center
   :target: _images/steer-torque-design.png

   The final steer torque design. The steer torque sensor is mounted atop the
   universal joint such that the only load component which can be transferred
   through the sensor is an axial torque.

I attached the universal joint to a Futek 150 in-lb (:math:`\pm 17` Nm) TFF350
torque sensor for accurate torque measurements. The torque sensor overloads at
150% of the rated output (i.e. 22.5 Nm), so some care was needed to protect the
sensor from overload and to prevent the rider from losing steer control if the
sensor were to break. I found a "slip" clutch distributed by `Stock Drive
Products <http://www.sdp-si.com>`_ (SDP). It turned out that the device was the
Torq-Tender manufactured by `Zero-Max Inc.  <http://www.zero-max.com>`_, but as
usual practice SDP doesn't readily provide that information. This particularly
expensive torque overload protection turned into a major headache. SDP lists
the rated torques but with no indication of the operating speed the torques are
measured at. It turns out they are with respect to an 1800 rpm operating speed.
My rates were rather low, I purchased a much larger torque sensor than I
needed. It was rather painful trying to get them to change the springs around
the Christmas holidays and check the torque rating at zero rotational speed.
The second issue had to do with it not actually being a slip clutch. I wanted
the torque protection to slip at a given torque (just under overload of the
sensor). The friction based slipping would still allow the rider to control the
bicycle, but SDP mistakenly called them "slip clutches" when in fact they are
more like binary torque limiters and transfer little to no torque after the
limit is reached, so the rider would most likely crash if the torque limiter
broke loose. Thirdly, there was play in the torque limiter. I used shim
material to take up much of the play, but there remained some backlash. I
ultimately locked the slip clutch and relied on careful attendance of the
bicycle and the fact that the rider was unlikely to ever apply greater than
22.5 Nm of torque. The runs 0-226 may have a tiny bit of play in the torque
limiter and for runs greater than 226 the limiter was locked.

Steer Dynamics
~~~~~~~~~~~~~~

The final design was setup to exclusively measure the torque in the steer tube
along the steer axis, but this measured torque, :math:`T_M`, is not the same as
the input torque used for our bicycle models, (i.e. :math:`T_\delta`). The
steer torque in the model is defined as the torque between the front frame and
the rear frame about the steer axis. If the torque sensor measures the steering
torque anywhere but at the interface of the human's hands and the front frame,
one must account for the inertial effects of the front frame. As far as I can
tell, no one who has measured steer torque on a single track vehicle has
accounted for these effects. There is a relationship from :math:`T_M` to
:math:`T_\delta` that requires one to know, at a minimum, the friction in
the steer axis bearings above the torque sensor (this is potentially both
viscous and Coulomb) and the inertial characteristics of the front frame above
the torque sensor\ [#elastic]_.

In our case, we measured the torque in the steering column, :math:`T_M`, from a
sensor that is mounted between the handlebars and the fork. The sensor was also
mounted between two sets of bearings: the headset and the slip clutch bearings.
We are interested in knowing the torque applied about the steer axis by the
rider's contact forces to the handlebars, :math:`T_\delta`.

A free body diagram can be drawn of the upper portion of the handlebar/fork
assembly, where the lower portion is cut at the steer torque sensor,
:ref:`Figure 11.25<figHandlebarFreeBody>`. The torques acting on the handlebar
about the steer axis are the measured torque, :math:`T_M`, the rider applied
steer torque, :math:`T_\delta`, and the friction from the upper bearing set,
:math:`T_U`, which can be described by Coulomb, :math:`T_{U_F}`, and viscous
friction, :math:`T_{U_V}`.

.. _figHandlebarFreeBody:

.. figure:: figures/davisbicycle/handlebar-free-body.*
   :width: 3in
   :align: center
   :target: _images/handlebar-free-body.png

   A free body diagram of the handlebar with all of the torques acting on it
   about the steer axis. The rear frame, :math:`B`, is at an arbitrary
   orientation with respect to the Newtonian reference frame.

We measure the angular rate of the bicycle frame, :math:`B`, with three rate
gyros

.. math::
   :label: frameRate

   ^N\bar{\omega}^B = w_{b1}\hat{b}_1 + w_{b2}\hat{b}_2 + w_{b3}\hat{b}_3

The handlebar, :math:`G`, is connected to the bicycle frame, :math:`B`, by a
revolute joint that rotates through the steering angle, :math:`\delta`, and we
measure the body fixed angular rate of the handlebar, :math:`w_{h3}` about the
steer axis directly with a rate gyro. The angular velocity of the handlebar can
be written as follows

.. math::
   :label: handlebarRate

   ^N\bar{\omega}^G = (w_{b1}c_\delta + w_{b2}s_\delta)\hat{g}_1 +
   (-w_{b1}s_\delta + w_{b2}c_\delta)\hat{g}_2 +
   w_{h3}\hat{g}_3

The steer rate, :math:`\dot{\delta}`, can be computed by subtracting the
angular rate of the bicycle frame about the steer axis from the angular rate of
the handlebar about the steer axis.

.. math::
   :label: steerRate

   \dot{\delta} = w_{h3} - w_{b3}

Now define a point, :math:`s`, on the steer axis closest to the center of mass
of the handlebar, :math:`g_o`.

.. math::
   :label: locationOfGo

   \bar{r}^{g_o/s} = d\hat{g}_1

We also measure the acceleration of a point, :math:`v`, on the bicycle frame.

.. math::
   :label: accelerationOfV

   ^N\bar{a}^v = a_{v1}\hat{b}_1 + a_{v2}\hat{b}_2 + a_{v3}\hat{b}_3

The location of point :math:`v` is known with respect to :math:`s`

.. math::
   :label: locationOfV

   \bar{r}^{s/v} = d_{s1}\hat{b}_1 + d_{s3}\hat{b}_3

:math:`^N\bar{a}^{g_o}` can now be calculated using the two point theorem for
acceleration :cite:`Kane1985` twice starting at the point :math:`v`

.. math::
   :label: AofSinN

   ^N\bar{a}^s = {}^N\bar{a}^v + {}^N\dot{\bar{\omega}}^B\times\bar{r}^{s/v} +
   {}^N\bar{\omega}^B\times({}^N\bar{\omega}^B\times\bar{r}^{s/v})

.. math::
   :label: AofGoinN

   ^N\bar{a}^{g_o} = {}^N\bar{a}^s + {}^N\dot{\bar{\omega}}^G\times\bar{r}^{g_o/s} +
   {}^N\bar{\omega}^G\times({}^N\bar{\omega}^G\times\bar{r}^{g_o/s})

The angular momentum of the handlebar about its center of mass is

.. math::
   :label: angMoGGo

   ^N\bar{H}^{G/g_o} = I^{G/g_o} \cdot {}^N\bar{\omega}^G

where :math:`I^{G/g_o}` is the inertia dyadic with reference to the center of mass
which exhibits symmetry about the 1-3 plane.

Now, the dynamic equations of motion of the handlebar can be written: the sum
of the torques on the handlebar about point :math:`s` is equal to the
derivative of the angular momentum of :math:`G` in :math:`N` about :math:`g_o`
plus the cross product of the vector from :math:`s` to :math:`g_o` with the
mass times the acceleration of :math:`g_o` in :math:`N` :cite:`Meriam1975`

.. math::
   :label: eqEuler

   \sum \bar{T}^{G/s} = {}^N\dot{\bar{H}}^{G/g_o} +
   \bar{r}^{g_o/s} \times m_G\,{}^N\bar{a}^{g_o}

We are only interested in the components of the previous equation in which the
steer torque appears, so only the torques about the steer axis are examined.

.. math::
   :label: eqSteerAxisTorques

   \sum T^{G/s}_3 = T_\delta - T_U - T_M = \left({}^N\dot{\bar{H}}^{G/g_o} +
   \bar{r}^{g_o/s} \times m_G\,{}^N\bar{a}^{g_o}\right) \cdot \hat{g}_3

And :math:`T_\delta` can be written as

.. math::
   :label: eqSteerTorque

   T_{\delta} =
   & I_{G_{22}} \left[ \left( -w_{b1} s_\delta + w_{b2} c_\delta \right)
   c_\delta + w_{b2} s_\delta \right] + I_{G_{33}} \dot{w}_{g3} + \\
   & I_{G_{31}} \left[ (-w_{g3} + w_{b3} ) w_{b1} s_\delta +
   (-w_{b3} + w_{g3}) w_{b2} c_\delta +
   s_\delta \dot{w}_{b2} + c_\delta \dot{w}_{b1} \right] + \\
   & \left[ I_{G_{11}} (w_{b1} c_\delta + w_{b2}s_\delta) +
   I_{G_{31}} w_{g3} \right] \left[-w_{b1} s_\delta +
   w_{b2} c_\delta \right] + \\
   & d m_G \left[ d (-w_{b1} s_\delta + w_{b2} c_\delta)
   (w_{b1} c_\delta + w_{b2} s_\delta) + d \dot{w}_{g3} \right] - \\
   & d m_G \left[-d_{s1} w_{b2}^{2} + d_{s3} \dot{w}_{b2} -
   (d_{s1} w_{b3} - d_{s3} w_{b1}) w_{b3} + a_{v1} \right] s_\delta + \\
   & d m_G \left[d_{s1} w_{b1} w_{b2} + d_{s1} \dot{w}_{b3} +
   d_{s3} w_{b2} w_{b3} - d_{s3} \dot{w}_{b1} + a_{v2} \right]
   c_\delta + \\
   & T_U + T_M

The expression for steer torque can be linearized by assuming that the steer
and pitch angles are small, to see the dominant terms around the point of
linearization.

.. math::
   :label: eqSteerTorqueLinear

   T_{\delta} = T_M + T_U + (I_{G_{33}} + d^2 m_G) \dot{w}_{g3} +
   (I_{G_{31}} - d d_{s3} m_G) \dot{w}_{b1} + d d_{s1} m_G \dot{w}_{b3} +
   d m_G a_{v2}

All of the terms in :math:`T_\delta` are measured by the on-board sensors or
are previously estimated physical parameters except for the upper bearing
frictional torque, :math:`T_U`. We estimated this torque contribution through
experiments described in the following sections.

Bearing Friction
~~~~~~~~~~~~~~~~

The torque sensor is mounted between two sets of bearings. The upper set are
tapered roller bearings and the lower are typical bicycle headset bearings.
Each are preloaded a nominal amount during installation. We assume that the
rotary friction due to each bearing set can be described as the sum of viscous
and Coulomb friction. The Coulomb friction can be described as a piecewise
function of the steering rate, :eq:`eqCoulomb`, and viscous friction as a
function linear in the steer rate, :eq:`eqViscous`.

.. math::
   :label: eqCoulomb

   T_{Bc} = t_B \operatorname{sgn}(\dot\delta) =
   \begin{cases}
     t_B  & \textrm{if $\dot{\delta}>0$}\\
     0    & \textrm{if $\dot{\delta}=0$}\\
     -t_B & \textrm{if $\dot{\delta}<0$}
   \end{cases}

.. math::
   :label: eqViscous

   T_{Bv} = c_B \dot{\delta}

The total friction due to all of the bearings is

.. math::
   :label: eqTotalBearingFriction

   T_B = T_{Bc} + T_{Bv}

To estimate :math:`t_B` and :math:`c_B`, we set up the bicycle such that the
steer axis was vertical, the front wheel was off the ground, and the rear frame
was rigidly fixed in inertial space. We then attached two springs of stiffness
:math:`k` each to the handlebars such that the force from the springs acted on
a lever arm, :math:`l`, relative to the steer axis, :ref:`Figure
11.26<figSteerExperiment>`.

.. _figSteerExperiment:

.. figure:: figures/davisbicycle/steer-experiment.*
   :width: 4in
   :align: center
   :target: _images/steer-experiment.jpg

   An overhead view of the steer friction experimental setup. The steer axis of
   the bicycle is vertical and the bicycle frame is secured such
   that it is rigid with respect to the earth. The wheel was isolated from
   rotation relative to the fork. Two springs in series were attached to the
   handlebars.

This configuration allowed us to apply small perturbations to the handlebars
and measure the dampened vibrations in the steer angle, steer rate, and steer
torque. For the first set of trials the sensors were mounted as they normally
are, with the steer angle and rate measurements taken just above the headset
and the steer torque measured between the upper and lower bearing sets. We also
took data for a second set of trials with the steer rate sensor mounted to the
top of the steer column in case the steer column to account for any torsional
flexibility.

The equations of motion governing the system are

.. math::
   :label: eqSteerExpEoM

   I_{HF} \ddot{\delta} + c_B \dot{\delta} + t_B
   \operatorname{sgn}(\dot{\delta}) + 2 k l^2 \delta = 0

The length of the lever arm was 0.231 meters. The spring stiffness was
estimated by suspending an 11.4 kg mass from one of the spring and letting it
oscillate while measuring its vertical acceleration via an accelerometer. A
grey box identification routine was used to estimate the spring stiffness for
three trials. We found the average spring stiffness to be :math:`904.7 \pm 0.6`
N/m. The inertia of the handlebar, fork, and front wheel about the steer axis,
:math:`I_{HF}`, was computed based on the measurements described in Chapter
:ref:`physicalparameters` and found to be :math:`0.1297+/-0.0005` :math:`kg
\cdot m^2`\ [#inertia]_.

The friction coefficients are found with a non-linear grey box identification
based on the measured steer angle over 15 trials (runs 209-223) where the
steering assembly was perturbed from equilibrium. The resulting viscous
coefficient is :math:`c_B = 0.34 \pm 0.04` :math:`N \cdot m \cdot s^2` and the
Coulomb coefficient is :math:`t_B = 0.15 \pm 0.05` :math:`N \cdot m`.

To calculate the applied steer torque, :math:`T_\delta`, we need an estimate of
the upper bearing friction, :math:`T_U`. A simple assumption is that the
friction in the upper bearings equals the friction in the lower bearings,
:math:`T_U = T_B / 2`, but for some of the trials we measured the torque
between the bearings, the steer angle just above the lower bearings and the
steer rate above the upper bearings. This information allows the estimation of
the upper and lower bearing friction independently. The equations of motion of
the assembly above the torque sensor are

.. math::
   :label: eqUpperBearingEOM

   I_G \ddot{\delta}_U + c_U \dot{\delta} + t_U
   \operatorname{sgn}(\dot{\delta}) + 2 k l^2 \delta = -T_m

The friction coefficients of the upper bearings can be estimated by treating
the measured torque as an input and the measured steer rate as the output in a
non-linear grey box formulation. The moment of inertia, :math:`I_G`, of the
handlebars about the steer axis, i.e. the portion above the torque sensor, is
computed from the physical parameter measurement described in Chapter
:ref:`physicalparameters` and is :math:`0.0656 \pm 0.0003` :math:`kg \cdot
m^2`.

Assuming :math:`I_G`, :math:`k`, and :math:`l` as fixed parameters gave poor
fits (around 50% of the data variability was accounted for by the model), and
thus most likely poor estimates of the friction coefficients. The viscous
coefficient was found to be :math:`c_U = 0.6 \pm 0.1` and the Coulomb friction
as :math:`t_U = 4.0E-8 \pm 7E-8`. These results are questionable. From the
previous excellent estimates of :math:`I_{HF}`, I would have not expected our
:math:`I_G` number to be a poor estimate, but this leaves either our
precomputed value of :math:`I_G` or the measure torque :math:`T_m` as the most
likely candidates to being incorrect. If :math:`I_G` is a free parameter the
identification produces outputs that fit the data well, but :math:`I_G` is
different than what was found with other techniques, :math:`I_G = 0.0955 \pm
0.0005`. The fits for the 7 trials rose to over 87% of the variability
explained by the model and the viscous friction was :math:`c_U = 0.38 \pm 0.06`
and the Coulomb :math:`t_U = 0.08 \pm 0.06`. The same can be done to compute
the lower bearing friction, but the fits were very poor. The results of finding
the upper bearing and lower bearing friction are inconclusive. So the
assumption that the upper friction is half of the total friction is used to
compute the actual steer torque.

It is also worth noting that the bearings are under load when a rider is seated
on the bicycle and that we didn't measure the friction under that loading of
the bicycle and rider's weight.

Rider Applied Torque
~~~~~~~~~~~~~~~~~~~~

With decent estimates of the torque due to upper bearing friction the actual
rider applied steering torque, :math:`T_\delta`, can be computed using Equation
:eq:`eqSteerTorque`. :ref:`Figure 11.27<figSteerTorqueComponents>` gives a
breakdown of the torque components found in Equation :eq:`eqSteerTorque` in a
typical run. The frictional torques are broken into the viscous and Coulomb
parts and the dynamic torques are broken into the terms due to the change in
angular momentum and the terms due to the acceleration terms. Notice that up to
2 Nm of additional torque is required for the rider to overcome the friction
and inertia of the front assembly and that the majority of that torque is due
to the inertial effects. This extra torque may be negligible in motorcycle
dynamics, but must be accounted for when studying the much lighter bicycle.

.. _figSteerTorqueComponents:

.. figure:: figures/davisbicycle/steer-torque-components.*
   :width: 5.5in
   :align: center
   :target: _images/steer-torque-components.png

   This is a plot of the steer torque components for run #700. The top plot
   shows the additive viscous and Coulomb friction. The total bearing friction
   during the run is less 0.3 Nm. The second plot shows the torque the
   rider must apply to overcome the handlebar inertia. The dominant term is the
   :math:`I_{G_{33}} w_{b3}` and during the peak accelerations the additive
   torque is up to 1.5 Nm for this run. The third plot shows the total additive
   torque which is up to 2 Nm. And finally the last plot shows the difference
   in the measured torque and the rider applied torque. There are large
   differences, especially at the peaks. Generated by
   ``src/davisbicycle/steer_torque_components.py``.

Strain Gauge Amplification
--------------------------

All of the load cells (lateral force, steer torque, seat post and foot pegs)
required analog amplification of the millivolt bridge signals to bring them up
to a level measurable by the NI USB-6218 which had a maximum input range of
:math:`\pm 10` volts at 16 bit. I purchased the Futek CSG-110 strain gage
amplifier for the torque sensor and had the sensor factory-calibrated in tandem
with the amplifier for a :math:`\pm10` volt output. Cal Stone :cite:`Stone1990`
had developed a custom amplifier for his seat post and handlebars which could
amplify up to fourteen bridge signals. Because I was intending to make use of
the seat post, the amplifier box was used for all the other strain gages. I did
not make use of the seat post and foot pegs, so the amplifier was only used for
the lateral force load cell. I used the amplifier box as it was except for
changing the first stage analog amplifier resistor to 16.5k ohm for a
:math:`\pm100` lbs range of the lateral force load cell. Cal Stone's thesis,
his research notes, and the `system electrical diagram
<http://biosport.ucdavis.edu/research-projects/bicycle/instrumented-bicycle/electrical-diagram/>`_
give the details of the circuit designs.

Calibration
===========

All of the analog sensors I used require some sort of calibration that can be
used to develop a relationship between the measured voltage from the sensor and
the physical phenomenon that is being measured. I self-calibrated some sensors,
had one calibrated at the factory, and used the reported manufacturer
specifications for others. The calibration data that is not presented below is
stored in the main trial database.

Potentiometers
--------------

I calibrated the steer angle sensor by inserting a custom protractor into the
steer tube of the fork, :ref:`Figure 11.28<figSteerAngleCalibration>` and
measuring the voltage of the potentiometer output at a series of distinct
angles. This calibration was done anytime the timing belt or pulleys were
disengaged and before each experimentation session.

.. _figSteerAngleCalibration:

.. figure:: figures/davisbicycle/steer-angle-calibration.*
   :width: 6in
   :align: center
   :target: _images/steer-angle-calibration.jpg

   The left image shows the protractor mounted in the fork. It is pinned in
   place with a roll pin for precise alignment with the front brake mounting
   hole. The right image shows the underside of the protractor with the
   engraved angles at every five degrees and the scribe line on the center of
   the downtube.

The roll angle potentiometer was calibrated by measuring the bicycle frame's
absolute roll angle with a digital level and recording the voltage output for a
sweep of angles, :ref:`Figure 11.29<figRollAngleCalibration>`. I also took static
measurements each day of experiments so that the roll angle could be computed
from the accelerometer's output in case the bias in the roll angle calibration
was poor.

.. _figRollAngleCalibration:

.. figure:: figures/davisbicycle/roll-calibration.*
   :width: 2.5in
   :align: center
   :target: _images/roll-calibration.jpg

   The bicycle during a roll angle calibration. The digital level is taped to
   the side of the steer column and the bicycle is set at various roll angles
   while the roll angle potentiometer is sampled.

For both cases the potentiometer's output voltage is ratiometric (i.e. scale
with respect to the supply voltage :math:`V_s`) with respect to the supply
voltage :math:`V_s` and the potentiometer angle :math:`\delta` can be computed
given the average calibration supply voltage :math:`V_c`, the slope :math:`m`,
and intercept of the calibration curve :math:`b` relating voltage to the angle.
Depending on the calibration, the angle could be the rotation angle of the
potentiometer as in the case of the roll angle measurement or the actual steer
angle in the case of the steer angle due to the gearing from the steer tube\
[#pots]_. For example

.. math::
   :label: eqPotentiometerCalibration

   \delta = \frac{V_c}{V_s} m V + b

Rate Gyros and Accelerometers
-----------------------------

The analog accelerometers and rate gyros typically have specifications for the
sensitivity and the zero bias :math:`z`, where both are ratiometric. The
sensitivity gives the linear relationship of the output voltage for a given
acceleration or rate. The zero bias is the output voltage of the sensor for
zero acceleration or rate for a given supply voltage. For example

.. math::

   \dot{\delta}_m = m \left(V - \frac{V_s}{V_c} z\right)

Wheel Rate
----------

We measured rear wheel angular speed with the same technique used with the
Delft instrumented bicycle. We mounted a small DC motor such that a knurled
roller wheel attached to its shaft rolled against the rear tire. The voltage of
of a DC motor has a linear relationship with the rotational speed of the motor.
To generate a calibration curve, we used an AMETEK 1726 Digital Tachometer to
measure the rotational speed in rpm and digital multimeter to measure the
voltage for a sweep of motor rotational speeds. :ref:`Table 11.4<tabTachData>`
gives the calibration data and :ref:`Figure 11.X<figSpeedRegression>` shows the
results of a linear regression through the data.

.. _tabTachData:

.. tabularcolumns:: LL

.. list-table:: DC Tachometer Calibration Data
   :header-rows: 1

   * - RPM
     - Voltage
   * - 42.5
     - 0.094
   * - 62.0
     - 0.1385
   * - 89.0
     - 0.199
   * - 132.0
     - 0.291
   * - 185.0
     - 0.406
   * - 271.5
     - 0.595
   * - 391.0
     - 0.857
   * - 569.0
     - 1.252
   * - 855.0
     - 1.879
   * - 1243.0
     - 2.738
   * - 1785.0
     - 3.91
   * - 2588.0
     - 5.67

.. _figSpeedRegression:

.. figure:: figures/davisbicycle/speed-calibration.*
   :width: 3in
   :align: center
   :target: _images/speed-calibration.png

   The best fit line through the wheel speed motor calibration data presented
   in :ref:`Table 11.4<tabTachData>`. Generated by
   ``src/davisbicycle/calibration_fits.py``.

The relationship from motor rotational speed to voltage is :math:`mV+b` with
the slope and intercept of the rpm to voltage curve determined by regression;
:math:`m=456.3862\frac{\textrm{rpm}}{\textrm{volt}}` and
:math:`b=-1.2846\textrm{ rpm}`, respectively. We then attached a small disc to
the motor shaft such that the disc rubs against the rotating tire. The disc
diameter was chosen such that the motor would output 0 to 10 volts for a
bicycle forward speed range of about 0 to 13.4 m/s (0 to 30 mph). The
rotational speed of the rear wheel as a function of voltage can be written as a
linear relationship

.. math::
   :label: eqTachSlope

   \dot{\theta}_R = s_f (m V + b) \frac{r_d}{r_c}

where :math:`r_d` is the radius of the generator disc and :math:`r_c` is
distance from the rear wheel center to the disc/tire contact point and
:math:`s_f=\frac{2\pi}{60}` is a scaling factor from rpm to radians per second.
:math:`r_d=0.028985` m and :math:`r_c=0.333375` m when the generator was first
attached (runs 0 to 226) and :math:`r_c=0.3199511` m after the generator was
remounted (runs 227 to end). The relationship between the rear wheel rate as a
function of voltage can more generally be rewritten as

.. math::

   \dot{\theta}_R = m_R V + b_R

where :math:`m_R=\frac{s_fmr_d}{r_c}` and :math:`b_R=\frac{s_fbr_d}{r_c}`. The
nominal forward speed of the bicycle can also be computed

.. math::

   v = \dot{\theta}_R r_R

Lateral Force
-------------

The lateral force was calibrated by applying a series of compressive and
tensile loads to the load cell and measuring the amplified voltage output,
:ref:`Figure 11.30<figLoadCellCalibration>`.
Before calibrations, the amplifier offset voltage potentiometer was set to
about 2.5 v and the nulling potentiometer adjusted so that the voltage was zero
for the no load case.

.. math::

   F = \frac{V_c}{V_s} (m V + b)

.. _figLoadCellCalibration:

.. figure:: figures/davisbicycle/load-cell-calibration.*
   :width: 3in
   :align: center
   :target: _images/load-cell-calibration.jpg

   The load cell under a compressive static loading during the calibration
   procedure, with Jan looking on.

Steer Torque
------------

The steer torque sensor was calibrated at the factory in tandem with the
amplifier and Futek supplies a certified calibration document with the
calibration data. The CSG-110 amplifier supplies constant 10 vdc to excite the
strain gauge bridge. I did not measure this voltage because the maximum voltage
for the NI USB-6218 is 10 V, so no ratiometric scaling was used. As long as the
battery supplied 12+ V to the CSG-110, this would not be an issue. Tables
:ref:`11.5<tabClockwise>` and :ref:`11.6<tabCounterClockwise>` give the factory
reported data and :ref:`Figure 11.<figTorqueRegression>` shows the regression
results.

.. math::

   T_{\delta} = m V + b

.. _tabClockwise:

.. tabularcolumns:: LL

.. list-table:: Factory Calibration Data Clock Wise Torque
   :header-rows: 1

   * - Load (in-lb)
     - Output (Vdc)
   * - 0
     - 0.000
   * - 30
     - 1.998
   * - 60
     - 3.993
   * - 90
     - 5.997
   * - 120
     - 7.994
   * - 150
     - 9.997
   * - 0
     - 0.002

.. _tabCounterClockwise:

.. tabularcolumns:: LL

.. list-table:: Factory Calibration Data Counter Clockwise Torque
   :header-rows: 1

   * - Load (in-lb)
     - Output (Vdc)
   * - 0
     - 0.000
   * - 30
     - -1.995
   * - 60
     - -3.994
   * - 90
     - -5.989
   * - 120
     - -7.986
   * - 150
     - -9.986
   * - 0
     - 0.002

.. _figTorqueRegression:

.. figure:: figures/davisbicycle/torque-calibration.*
   :width: 3in
   :align: center
   :target: _images/torque-calibration.png

   The best fit line through the steer torque sensor calibration data presented
   in Tables :ref:`11.5<tabClockwise>` and :ref:`11.6<tabCounterClockwise>`.
   Generated by ``src/davisbicycle/calibration_fits.py``.

Calbration Software
-------------------

I wrote a simple program that collects the data for the self calibrations and
generates a generic calibration file with a standard format for the various
sensors. The files for the data from the manufacturer-supplied calibration data
were manually constructed. All of the files are then parsed and collected into
a single calibration table in the main database. When converting raw voltage
signals to engineering units, the calibration coefficients are applied with
respect to the calibration date (i.e. the calibration coefficients are selected
with respect to the date up to and nearest the date of the run). The programs
can be found in the tools directory in ``BicycleDAQ`` and in
``BicycleDataProcessor``.

Software
========

Data Acquisition
----------------

Both the VectorNav VN-100 and the NI USB-6218 were connected to a small ASUS
EEEPC netbook which was mounted on the rear rack of the bicycle, :ref:`Figure
11.31<figLaptop>`. The devices were controlled and the data logged using Matlab.
I interacted with the VN-100 with Matlab's Serial I/O toolbox and the NI
USB-6218 with the Data Acquisition Toolbox. A custom program written within
Matlab's Graphical User Interface framework was designed to allow the user to
set meta data before each run, arm the system, and view the raw data signals
after the run, :ref:`Figure 11.32<figDAQGUI>`. The general features are as
follows:

- Automatically increments run numbers
- Sets meta data: rider, environment, speed, maneuver, notes
- Initializes the system
- Views raw data time history traces
- Loads previous runs, view the time traces, edit the meta data and resave
- Saves output as a Matlab mat file
- Converts the run and calibration mat files to HDF5 format
- Collects calibration data

.. _figLaptop:

.. figure:: figures/davisbicycle/laptop.*
   :width: 4in
   :align: center
   :target: _images/laptop.jpg

   The laptop mounted to the rear rack.

.. _figDAQGui:

.. figure:: figures/davisbicycle/bicycle-daq-gui.*
   :width: 6 in
   :align: center
   :target: _images/bicycle-daq-gui.png

   A screenshot of the software running under Matlab 7.8.0 (2009a) on Windows XP .

Due to the time synchronization issue talked about below we were limited to a
single trigger setup, versus a multiple trigger for repeated runs. (i.e. we had
to stop after every run to re-initialize the devices, versus allowing the
rider to trigger a series of runs in a row without having to stop).

The source code for the software is available in a Github repository
`<https://github.com/moorepants/BicycleDAQ>`_, including some tools for initial
post-processing of the collected data.

Time Synchronization
--------------------

When we originally chose to use the VectorNav VN-100 and the NI USB-6218 with a
netbook PC, we had convinced ourselves that they would all work together
seamlessly. The manufacturers of each device seemed to think so and their
disconnected knowledge helped convince us too. This turned out to be very
wrong.  The main issue, which seems to rear its head often in data acquisition,
is time synchronization of all the hardware involved. A PC running a typical
operating system is not capable of detailed and strict time management of
processes. This is certainly true of collecting serial data from two
independent devices. My intention was to collect data from both the VN-100 and
the USB-6218 simultaneously with the Matlab Serial I/O and Data acquisition
toolboxes, hopefully triggering the initial collection of data from the two
devices simultaneously or by reading the VN-100 serial data through the
USB-6218.

The simultaneous triggering was hampered primarily by the VN-100's asynchronous
data transfer and no apparent ways to either start it with a trigger or by
recording some signal from it through the USB-6218. It may be possible to read
serial data through the USB-6218, but I did not figure it out. It very well may
have been missing the features to do so, or that Matlab didn't have a robust
enough interaction with the USB-6218 to do so. I struggled quite a bit with
this unforeseen issue and we started devising solutions to measure an
identical event with both the VN-100 and the USB-6218 and to synchronize the signals
afterwards. :cite:`Ouden2011` had to use a similar technique. We would need to
select a sensor which was also on the VN-100 and then excite the two sensors
with the same event. Ideally this event would be a step input to both sensors.
We tried rate gyros and accelerometers but couldn't come up with an adequate
event, until we mentioned the problem to Ron and he immediately suggested just
riding over a bump! This was the ticket. We ended up attaching an additional
three axis accelerometer to the VN-100 development board which would read the
same vertical component of acceleration and constructing a bump for the bicycle
to travel over at the beginning of each run. This provided us with two signals
which could be synchronized in time.

Bump
~~~~

The accelerometers had a :math:`\pm 3` g range, so we needed a bump which would
provide vertical accelerations within that range for speeds from 1 to 7 m/s.
For a sinusoidal shaped bump, the vertical acceleration for a given speed can
easily be computed. The height of a bump as a function of time is

.. math::
   :label: eqBumpHeight

   y(t) = \frac{h}{2}\left[1 - \operatorname{cos}\left(\frac{2 \pi v}{L}t\right)\right]

where the maximum bump height is :math:`h`, :math:`v` is the forward speed and
:math:`L` is the length of the bump. The acceleration

.. math::

   \frac{d^2 y(t)}{dt^2} = 2 h \left(\frac{\pi v}{L}\right)^2
   \operatorname{cos}\left( \frac{2 \pi v}{L} t \right)

Because the cosine varies from -1 to 1, the maximum acceleration due to the
bump and acceleration due to gravity is

.. math::

   a = 2 h \left(\frac{\pi v}{L}\right)^2 + g

The maximum height of a 1 meter long bump and forward speed of 7 m/s to give
a 3 g acceleration is

.. math::

   h = \frac{a - g}{2}\left(\frac{L}{\pi v}\right)^2 =
   \frac{3 * 9.81 \textrm{m/s} - 9.81 \textrm{m/s}}{2}
   \left(\frac{1 \textrm{m}}{\pi 7 \textrm{m/s}}\right)^2 = 0.020 m

I fashioned a very low sinusoidal bump from wood that we laid on the track on
the floor at the beginning of the track, :ref:`Figure 11.33<figBump>`  and also
launched under the bicycle on the treadmill. The bump launching is somewhat
amusing and we had to construct a "bump catcher" so that the bump didn't fly
off the back of the treadmill and hurt anyone or anything, :ref:`Figure
11.34<figBumpCatcher>`.

.. _figBump:

.. figure:: figures/davisbicycle/bump.*
   :width: 6in
   :align: center
   :target: _images/bump.jpg

   The sinusoidal profile of the finished bump.

.. _figBumpCatcher:

.. figure:: figures/davisbicycle/bump-catcher.*
   :width: 3in
   :align: center
   :target: _images/bump-catcher.jpg

   The high precision bump catcher.

Signal Synchronization
----------------------

The bump provides the event and the acceleration output of the tandem
accelerometers logs the event. The time shift between the two signals can be
computed by minimizing the least squares error of one signal minus the other
signal which has been interpolated at the sample times of the first signal.
:ref:`Figure 11.35<figUnsync>` shows the two independent recorded events.

.. _figUnsync:

.. figure:: figures/davisbicycle/unsync.*
   :width: 4in
   :align: center
   :target: _images/unsync.png

   This plot shows the accelerometer signals collected by both the NI USB-6218
   and the VN-100 for a typical run. The spikes in acceleration are due to the
   bicycle traversing the bump. The NI signal starts about a third of a second
   before the VN signal. Generated by ``src/davisbicycle/time_sync.py``.

The basic algorithm for computing the error between the two signals is:

1. Shift the NI signal some time :math:`\tau`.
2. Truncate both signals around the common data.
3. Interpolate the NI signal at the VN time samples.
4. Compute the sum of squares of the VN signal minus the interpolated NI
   signal.

Using this formulation, then minimize the error with respect to
:math:`\tau`. The minimization requires a good guess, as the minimizing
function has local minima. I use both the location of the max values in the
signals and finding the minimal value of the error as a function of a fixed
number of :math:`\tau` values to get good guesses. See the
``BicycleDataProcessor`` source code for the details. The computed time
shift is used to shift and truncate all of the signals as in :ref:`Figure
11.36<figSync>`.

.. _figSync:

.. figure:: figures/davisbicycle/sync.*
   :width: 4in
   :align: center
   :target: _images/sync.png

   This plot shows the same accelerometer signals shown in the previous figure
   after finding the optimal time shift. Generated by
   ``src/davisbicycle/time_sync.py``.

Data Processing
---------------

To handle processing the large amount of data, I developed an object oriented
program, `BicycleDataProcessor
<https://github.com/moorepants/BicycleDataProcessor>`_, in Python that
interacts with an HDF5 database containing the data. The program makes use of
`PyTables <http://www.pytables.org>`_ for database interaction and the
`SciPy/NumPy <http://www.scipy.org>`_ `matplotlib
<http://matplotlib.sourceforge.net>`_ stack for computation and plotting. The
program is structured around three classes:

Signal
   This is a subclass of the NumPy ndarray. It tracks a 1 dimensional time
   series along with its units. There are basic methods for typical signal
   processing such as differentiation, filtering, and frequency spectrum.
RawSignal
   This a subclass of Signal for the raw signals. The attributes are populated
   from the database. In addition to the Signal methods, it has the ability to
   scale the signal based on calibration data.
Sensor
   This class contains calibration data for particular sensors and has methods
   to extract the correct calibration constants based on calibration date.
Run
   This is the primary class which stores the meta data and signal data for a
   specific run. It has methods to process the raw data into  more
   meaningful time series that are useful for analyzing the bicycle dynamics.
   There are also methods for plotting and exporting the data.

The data collection and initial processing follows this pattern:

1. Collect data during a run via the BicycleDAQ software. This stores the
   metadata and raw signal data for each run in a Matlab mat file.
2. Build the complete HDF5 database with BicycleDataProcessor by importing all
   of the run and calibration data files.
3. Load runs from the database and manipulate them for further processing such
   as plotting.

This approach works well and allows for easy querying of the 700+ runs for
further data analysis. The processed data can be exported to generic file
formats or as ones compatible with Matlab. This example gives the basics of
loading a run and plotting the processed data in :ref:`Figure
11.37<figProcessedData>`::

   import bicycledataprocessor as bdp
   dataset = bdp.DataSet()
   trial = bdp.Run('00699', dataset, filterFreq=40.)
   fig = trial.plot('PullForce', '2289*RollAngle', '1448*SteerAngle', '32*SteerTorque')
   fig.show()

.. _figProcessedData:

.. figure:: figures/davisbicycle/processed-data.*
   :width: 6in
   :align: center
   :target: _images/processed-data.png

   The resulting output of a basic plot command for a run.

Conclusion
==========

In this chapter I gave a detailed description of the Davis instrumented bicycle
with the hope that enough information is present for someone to make use of the
bicycle and/or recreate one (of course with improvements). The bicycle served
us well in terms of the kinematic and kinetic data we were interested in
collecting.

Some recommendations for improvements are as follows:

- Power the entire system from the hub motor battery to reduce the number of
  batteries.
- The steering universal joint needs keyways instead of set screws for a more
  solid connection.
- Get rid of the VN-100 and replace with two analog rate gyros for yaw and roll. This
  would take away the time synchronization issue. The newer versions of the
  VN-100 offer more capabilities including synchronization signals, so that could
  be looked into, but overall it is still a poor (and expensive) choice for
  this application.
- Add some gearing to the roll angle measurement for better resolution, and
  develop a more accurate calibration scheme, perhaps by making use of the
  on-board accelerometers.
- Do away with the torque limiter. Another solution for safeguarding the sensor
  and rider in case of failure is needed.

.. rubric:: Footnotes

.. [#hubdamage] See `<http://biosport.ucdavis.edu/blog/hub-motor-woes>`_ for
   repair details.

.. [#halo] Nonetheless, Jan had great plans for a halo-like ring with nails
   sticking through to the rider's scalp so that they couldn't move their head
   without excruciating pain; we just never got around to making it.

.. [#imus] See our selection spreadsheet at `<https://docs.google.com/spreadsheet/pub?key=0Asn6BMg-bB_EdFJKVXFfeEgyMnpwR0JXNVlOYjg0Q0E&output=html>`_

.. [#rolltrailer] As designed, the potentiometer measures exactly the angle
   between the yoke and the trailer frame. This is somewhat limiting as the
   full range of the potentiometer isn't utilized as was in the steering angle
   design.  This effectively reduces the measured voltage range from the
   potentiometer, especially since the measured angles are often no more than
   10 degrees. The NI USB-6218 has 16 bit resolution so it still adequatedly
   measures the data, but a step down gearing would improve the resolution of
   the roll measurement.

.. [#rategyro] The Silicon Sensing rate gyros had to be purchased in bulk but they
   offered samples. A single sample gyro cost upwards of $300 with half of the
   price required to ship a 1' x 1' x 1' giant box from Japan to California for
   a 1" x 1" x 1" sensor. I initially thought that this was worth it for the
   quality of the sensor, but I never saw any appreciable difference in the
   sensor quality as compare to the rate gyros on the VN-100 which can be
   purchased individually for less than $50.

.. [#rollcontrol] :cite:`Weir1972` shows that large rider lean angles are required
   to give similar capabilities as steer control. :cite:`Sharp2008a` shows that the
   use of steer torque control is always the more optimal choice than rider
   lean torque control for optimal control based on path deviation error and
   control power. :cite:`Moore2011` experimentally shows that the steering angle
   magnitudes are much larger than other rider body movements.

.. [#idealinput] A sum of sines would be ideal, see :cite:`Lange2011` for some ideas
   on other types of inputs. It has been shown that a sum of sines can provide
   a non-predictable signal to the human :cite:`McRuer1974`.

.. [#elastic] The elasticity of the steer column may also be a factor.

.. [#inertia] If :math:`I_{HF}` is left as a free parameter, along with
   :math:`c_B` and :math:`t_B`, the mean of :math:`I_HF` over 15 trials is
   identified to be :math:`0.1269 \pm 0.0008`. This good agreement lends
   confidence to the methods in Chapter :ref:`physicalparameters`.

.. [#pots] It slipped my mind to add a step-up gear for the roll angle measurement,
   leaving the output voltage range small with respect to the roll angle range.
   Ideally, the potentiometer should rotate its full rotation for a desired
   roll angle range.
