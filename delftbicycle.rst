.. _delftbicycle:

==========================
Delft Instrumented Bicycle
==========================

.. warning::

   This document is a draft which is updated regularly (Last updated |today|).
   Once I submit if for my doctoral degree at UC Davis, it will be done. So for
   now use at your own risk. The information may or may not be correct.
   Reviews, comments and suggestions are welcome.

Preface
=======

I had contacted the authors of [Meijaard2007]_ in the early winter of 2006 to
try to get some tips on where to go with my master's thesis, which I wanted to
do on the handling qualities of bicycles. I had come across Arend, Jaap and
Jim's conference paper [Schwab2004]_ on their benchmark Whipple model used it
to help me build and validate my first model earlier that year. Andy, Jim and
Arend all replied, Jim at great length as usual, and the seeds were sown for
some future collaboration. Jim began flooding my inbox with years of thoughts
on the handling of bicycles and it turned out that Arend had just applied for a
big grant to fund two PhD students for bicycle handling research that was
uncannily similar to what I was dreaming up myself. I hadn't decided to do my
PhD at UC Davis quite yet and Arend's potential PhD slot was enticing (Jodi was
slated for one). But I ended up finishing my masters the following spring and
signing on for the PhD at Davis. That summer I started thinking about applying
for a Fulbright grant to study somewhere. I contacted Arend again to see if he
was interested in having me and he was excited. I told him I was going to do it
and then put it off. A few weeks shy of the deadline, I told Arend I didn't
have time to do it. He encouraged me to apply anyways and I agreed. I spent the
next few weeks putting together the proposal and after several drafts I sent it
off.  I didn't think about it much after that, but luck was on my side and I
received the acceptance letter from the Fulbright commission the following
spring. I was headed to the Netherlands for my first time living abroad. In the
meantime Arend found a way to fund a PhD for Jodi so there was going to be some
momentum when I arrived.

When I arrived in Delft August 2008 Jodi was working on several projects: a
bicycle handling qualities review paper [Kooijman2011a]_, the two mass skate
bicycle [Kooijman2011]_ and an instrumented bicycle. I helped to some degree
with all the projects, but primarily with setting up the instrumented bicycle
and planning a set of experiments. This chapter details the work we did with
the first instrumented bicycle. I've taken the text directly from our
conference paper [Kooijman2009a]_ and gone through it with some updates,
clarifications and additions. Jodi and Arend were the primary writers of the
paper. My contributions were more of the experimental design, performing the
experiments, analyzing the data, discussing results and working on a
visualization graphical interface that we never really used due to the
in-ability to synchronize the video data we took with the sensor data.

Abstract
========

The purpose of this study is to identify human control actions in normal
bicycling. The task under study is the stabilization of the mostly unstable
lateral motion of the bicycle-rider system. We studied this by visual
observation of the rider and measuring the vehicle motions. The observations
show that very little upper-body lean occurs in normal riding and that
stabilization is done primarily maintained by steering control actions.
However, at very low forward speed a second control action was observed: knee
movement. Moreover, the frequency of the control actions are all dominated by
the pedaling frequency, while the amplitude of the steering motion increases
rapidly with decreasing forward speed.

Introduction
============

Riding a bicycle is an acquired skill. At very low speeds the bicycle is very
unstable and requires great attention by the rider. However, at moderate speed
the bicycle is easy to stabilize, often with little conscious thought by the
rider. These observations are corroborated by a stability analysis on a simple
dynamical model of an uncontrolled bicycle [Meijaard2007]_ and some experiments
[Kooijman2008]_ and [Kooijman2009]_. Although there is little established
knowledge on how a person stabilizes a bicycle, two basic features are known:
some uncontrolled riderless bicycles can balance themselves given some initial
speed, and one can balance a forward moving bicycle by turning the front wheel
in the direction of the undesired lean. But we all know that a rider on a
bicycle, not only moves the handlebars but also may make use of their upper
body and other extremities.  These rider body motions are even more profound
when riding a motorcycle [Cossalter2002]_.

The purpose of this study is to identify the major human control actions in
normal bicycling focusing on the stabilization task. [#]_ We use the term
"normal" to describe casual bicycling that requires minimal conscious control.
The identification is done by visual observation of the rider and measurement
of the motions of the instrumented bicycle, see Figure
:ref:`figInstrumentedBicycle`. In order to observe the human control actions a
number of experiments were carried out.  First, a typical town ride was
performed to investigate what sort of actions take place during casual riding
through an urban environment. After this, experiments were carried out in more
controlled environment, a large treadmill (3 × 5 m), at various speeds. The
same bicycle was used during all the experiments. The bicycle was ridden by two
averagely skilled riders. Three riding cases were considered: normal bicycling,
bicycle without pedaling (towing) and normal bicycling with lateral
perturbations. These experiments were carried out to identify the upper body
motions and the effect of the pedaling motion on the control. The rider was
told to simply stabilize the bicycle and to generally ride in the longitudinal
direction of the treadmill; no tracking task was set. Recorded data included
the rigid body motions of the bicycle rear frame and the front assembly. The
rider motion relative to the rear frame was recorded via video.

Instrumented Bicycle
====================

A standard Dutch bicycle, 2008 Batavus Browser, was chosen for the experiments
and is shown in Figure :ref:`figInstrumentedBicycle`. This is a bicycle of
conventional design, fitted with a 3-speed SRAM rear hub and coaster brakes.
Some of the peripheral components were removed in order to be able to install
measurement equipment and sensors (see Table :ref:`tabEquipment`).
The bicycle was equipped with a 1/3” CCD color bullet-camera with 2.9mm (wide
angle) lens. The camera was located at the front and directed towards the rider
and rotated 90 degrees clockwise to get portrait aspect ratio. The video
signal was recorded, via the AV-in port, on DV tape of a Sony Handycam located
on the rear rack of the bicycle. The bullet camera was placed horizontally,
approximately 65 cm in front of the handlebars and 1.2 m above the ground and
held in place by a carbon-fiber boom connected to the down-tube of the rear
frame, see Figure :ref:`figInstrumentedBicycle`. This allowed us to view the
rider's motion with respect to the bicycle frame.

.. todo:: Add instrumented bicycle figure.

.. todo:: Add equipment table.

We used a National Instruments CompactRIO (type CRIO-9014) computer for data
collection. The CompactRIO was installed on the rear rack of the bicycle. It
was fitted with a 32-channel, 16 bit analogue input module and a 4-channel, 16
bit analogue output module as well as a CRIO WLAN-MH1000 wireless modem by
S.E.A. Datentechnik GmbH for a wireless connection with a “ground station”
router, to which a laptop was connected. The measurement system is able to run
autonomously once a measurement sequence is initiated. The CompactRIO was
powered by a 11.1V, 1500mAh Lithium Polymer battery which was also placed on
the bicycle’s rear rack.

The recorded signals were the body fixed roll, yaw and steer rates, the steer
angle, the rear wheel speed and the pedaling cadence frequency. The angular
rates were measured using 3 Silicon Sensing CRS03, single axis angular rate
sensors with a rate range of ± 100 deg/s. The steer angle was measured using a
potentiometer placed on the rear-frame against the front of the head tube and
connected via a belt and pulley pair. The angular rate sensors and the angular
potentiometer were powered by a 4.8V, 2100mAh Nickel Cadmium battery. The
forward speed was measured by measuring the output voltage of a Maxon motor
that was driven by the rear wheel. The cadence frequency was measured by a
reed-relay placed on the rear frame, and a magnet placed on the left crank-arm.

Town Ride Experiment
====================

Our first basic experiment was a short, 15 minute, ride around town. This
experiment took place under normal riding conditions (dry weather, day-light,
etc.), on roads that the rider was familiar with. The course covered included a
round-a-bout, dedicated cycling paths, speed-bumps, pavement, normal tarmac
roads, tight bends in a residential area and the rider had to stop at a number
of traffic lights. There were no special precautions taken and the experiment
was carried out amongst other traffic. From the recorded video and
sensor data two main observations were made:

1. The video data showed that there was very little upper body lean relative to
   the rear frame during the entire ride. The small relative upper body lean
   that was noted appeared to simply be a result of pedaling. Only in the last
   few seconds prior to a sharp corner was an upper body lean angle observed,
   indicating that the lean was carried out because of a sudden heading change.

2. The recorded data, part of which is shown in Figure :ref:`figTownData`,
   clearly shows that only very small steering actions (± 3 deg) are carried
   out during most of the experiment. Only when the forward speed has dropped,
   prior to making a corner, are large steer angles (± 15 deg) seen.

Treadmill Experiments
=====================

Riding a bicycle on the open road amongst normal traffic subjects the
bicycle-rider system to many external disturbances such as side wind, traffic
and road unevenness. To eliminate these disturbances a more controlled
environment was selected to carry out further studies on human rider control
for stabilization tasks. The experiments were carried out on a large (3 × 5 m)
treadmill, shown in Figure :ref:`figTreadmill`. The dynamics of a riderless
bicycle on a treadmill have been shown to be the same as for on flat level
ground [Kooijman2009]_ for speeds between 4-6 m/s, so we make this assumption
for the case with a rider too, albeit with caution. The experiments were
carried out by two, male, average ability, riders of different age and build on
the same bicycle. The saddle height was adjusted for each rider to ensure
proper seating. The rider characteristics are given in Table :ref:`tabRiders`.
For both riders very similar results were found. The data and figures presented
in this chapter were collected with rider 1.

.. todo:: Add treadmill figure.

.. todo:: Add rider table.

The uncontrolled dynamics of the bicycle rider system can potentially be
described by the linearized model of the bicycle [Meijaard2007]_. This model
consists of four rigid bodies: the rear frame with rigid rider connected, the
front handlebar and fork assembly, and the two wheels. These are connected by
ideal hinges and the wheels have idealized pure-rolling contact with level
ground. [Moore2009]_ describes the method used to determine the model
parameters for the instrumented bicycle-rider system. [#]_ These parameters are
given in Table :ref:`tabParameters` and the root loci of the system with
respect to speed is depicted in Figure :ref:`figRootLoci`. At low speed, the
dominant mode is the unstable oscillatory weave mode. This weave motion becomes
stable around 18 km/h, the weave critical speed. At higher speeds, the
non-oscillatory capsize motion becomes unstable but since its time to double so
long it considered to be very easy to control. With those assumptions, we
assert that the instrumented bicycle rider system is in need of human
stabilizing control below 18 km/h and is stable otherwise.

For safety reasons the riders were fitted with a harness that was connected to
the ceiling via a long climbing rope. This ensured that should the rider fall
over no contact with the moving part of the treadmill would be made. Also a
retractable dog leash was connected between the front of the harness and the
treadmill kill switch. This ensured that the treadmill would immediately come
to a halt, should the bicycle go too far back, reducing the chance that the
bicycle could go off the end of the treadmill.

Herein, three types of riding experiments are examined: normal bicycling,
bicycle without pedaling (towing) and normal bicycling with lateral
perturbations. The normal bicycling experiment was carried out to investigate
what type of control actions a rider carries out to simply stabilize a bicycle.
The towing experiment was carried out to remove the effects of the dominant
pedaling motion, seen during the town-ride experiment, from the system. The
bicycling with lateral perturbations was performed to investigate how the human
rider recovers from a lateral impulsive force applied to the rear frame.

Each of the three experiments was carried out at 6 different speeds: 30, 25,
20, 15, 10 and 5 km/h. In total 36 experiments were performed. During the
normal bicycling and bicycling with lateral perturbations experiments the rider
pedalled normally and used first gear during the 5 and 10 km/h runs. Second
gear was used in the 15 and 20 km/h runs and third gear was used during the
25 and 30 km/h runs. The cadence varied between 24 rpm at 5 km/h and 80 rpm at
30 km/h. During the towing series of experiments, the bicycle and rider were
towed by a rope connected to the bicycle rear frame at the lower end of the
head tube. The rider kept the pedals in the horizontal position during these
experiments. The crank arm side that was placed forward was left to rider
preference. During the lateral perturbations experiment the bicycle was
perturbed by applying a lateral impulse to the rear frame. The impulse was
applied by manually yanking a rope tied to the seat tube. The rider could not
see the rope being actuated to ensure that the rider was unprepared, however,
they knew the direction of the perturbation which was always a pull from the
right.

The riders were instructed to stay on the treadmill and to generally ride in
the longitudinal direction of the treadmill but not to concentrate on their
exact position on the treadmill. We wanted the rider to focus on stabilization
and maintaining heading and not to track lateral deviation. Sensor data was
collected for 1 minute during each experiment at a 100Hz sample rate and the
video data at XX frames per second . Video footage can be found at <link>.

.. todo:: What was our video frame rate.

.. todo:: Upload all the video data and link to it here. Also add a single
   video for the web version of the dissertation.

Normal Bicycling
================

Visual inspection of the video footage showed very little rider lean action
during the experiment other than what resulted directly from the pedaling
motion.  During the low speed runs at 5 km/h, the rider’s upper body was almost
stationary, i.e. it could be considered to be rigidly attached to the rear
frame. However at this speed the rider’s knees showed significant lateral
motion. This lateral knee motion can be seen in the video image in Figure
:ref:`figKnee`. A third observation was that the rider actuated the handlebars
with higher amplitudes at lower speeds than at higher speeds.

.. todo:: Add the knee figure.

This third observation is confirmed by the measured steer angle data. Figures
:ref:`figSteer20` and :ref:`figSteer5` show the time history of the steer angle
for the experiments carried out at 20 and 5 km/h, respectively. The standard
deviation of the steer angle during the sixty seconds of measurement is also
shown in the figures. At speeds above 20 km/h the average steer angle remains
approximately constant. However the average magnitude of the steer angle grows
by more than 500% when the speed is decreased from 20 km/h to 5 km/h.  This
increase in steer angle magnitude for the decreasing speeds is illustrated in
Figure :ref:`figSteerSigma`. This jump in steering amplitude could be
indicative of a threshold at which the system becomes harder to control, but
there is no apparent connection to the open loop dynamics. For example the
change in both the weave mode time to double and natural frequency is
approximately the same between 5 and 10 km/h as between 10 and 15 km/h.

.. todo:: Add the steering plots.

The frequency content of the steering signal for the different forward speeds
is shown in Figure :ref:`figSteerFreq`. The grey vertical dashed line indicates
the rigid rider-bicycle weave frequency. We were not able to ascertain any
connection between the dominate measured frequencies and the natural frequency
of the weave mode. We had hypothesized that for speeds in the stable speed
range, the optimal control frequency of the rider would correspond to the weave
frequency, due to the fact that an uncontrolled bicycle-rider system recovers
from perturbations at its natural frequency. The black vertical dashed line in
each of the plots in Figure :ref:`figSteerFreq` indicates the measured pedaling
frequency. The figure shows that during normal pedaling most of steering action
takes place at, or around, the pedaling frequency, irrespective of the speed
that the bicycle is moving. The pedaling frequency is especially dominant in
the steering signal at the highest speeds where practically all of the steering
takes place at the pedaling frequency.

.. todo:: I don't really like this graph. I don't think it means much or adds
   anything significant to the discussion.

Figure :ref:`figMaxAmp` plots the maximum steering amplitude versus speed. This
maximum amplitude reduces with increasing speed and is similar in shape to the
standard deviation plot in Figure :ref:`figSteerSigma`.

Towing; no pedaling
===================

Visual inspection of the video footage revealed, similar to the normal
bicycling experiment, that little to no upper body leaning occurred at any of
the measured speeds and that larger steer angles occurred at the slower speeds.
However, unlike the normal bicycling experiment, no knee motion was noticed
from visual inspection of the video footage at any of the speeds, other than
small remnant motion as a result of slight steering deviations from straight
ahead. The recorded steer angle data also confirmed that larger steer angles
were made at decreasing speeds. Figure :ref:`figSteerSigma` shows how the
standard deviation of the steer angle reduces rapidly with increasing speed up
to 20 km/h and from then on remains approximately constant.  The figure also
shows that the average steering amplitude at all speeds is lower than that for
the pedaling case. The standard deviation is less than a degree for all speeds
above 10km/h indicating that little to no steer action is required at higher
speeds.

The steer angle frequency spectrum for each of the speeds is shown in Figure
:ref:`figTowFreq`. It was once again expected that the rigid rider/bicycle
weave frequency would be a dominant frequency in the frequency spectrum,
especially with no pedaling. However there appears to be no connection with the
open loop weave frequency even in the unstable speed range.  In fact the
frequency spectrum shows a wide range of frequencies of similar amplitude at
all the speeds and none of the speeds seem to show any noticeable dominant
frequencies.

Perturbing; pedaling
====================

The video footage showed that, as a result of the lateral perturbation, the
bicycle was pulled laterally away from under the rider causing the bicycle to
lean over and in turn cause a short transient lean motion of the rider’s upper
body. The upper body appears to only lag behind the lower body and bicycle
during this destabilizing part of the perturbation maneuver. During the
subsequent recovery of the bicycle to the upright, straight ahead position, no
body lean could be noted other than that as a result of the normal pedaling.

A second phenomenon observable in the video footage, as shown in Figure
:ref:`figPerturb`, is that at all speeds we observed a lateral knee motion
during the short transient recovery process of the bicycle to the upright
position.  The lateral knee motion was very large during the 5 km/h measurement
and much smaller at the higher speeds, but even at 30 km/h it is visible.

From the video footage we also concluded that the angle that the handlebars
are turned during and after a perturbation decreased with increasing speed as
can also be seen in the measured steer angle data as shown in Figure
:ref:`figSteerSigma`.

Figure :ref:`figPerturbFreq` shows the frequency spectrum of the measured steer
angle. Once again, for the higher speeds, the steer control action is carried
out at the pedaling frequency. At the lower speeds (5 - 10 km/h) a wider
frequency range is again present but the pedaling frequency is dominant. Figure
:ref:`figMaxAmp` shows the steering amplitude for the frequency with the
maximum amplitude.  Again the values for the highest speeds are similar to
those of the standard deviation of the steer angle.

Once again, the frequency spectrum shows no significant steering motion taking
place at the rigid rider-bicycle weave natural frequency for any of the speeds.

Conclusion
==========

The observations show that human stabilization control of the lateral motions
of a bicycle during normal bicycling show little use of upper body lean, and
that the primary control actions done through steering control. Only at very
low forward speed is a potential second control action observed: knee movement.
Moreover, this lateral knee motion seems to only occur while pedaling. The
steering actions are dominated by the pedaling frequency while the amplitude of
the steering motion increases rapidly with decreasing forward speed.

Appendix
========

The following sections details some extra information that was not conveyed in
the paper [Kooijman2009]_ and previous sections.

Other Experiments and data
--------------------------

As usual with the data deluge, we analyzed very little of the data. We recorded
at total of 109 one minute runs with two different riders. The previous
sections only detail some analysis on runs from a single rider and did not
include results from some other experiments. As a result, the statisical
signifiance of the presented anaylsis is somewhat weak. The following list
details all of the experiments we perfomed:

- Normal pedaling at five speeds in which we started at the low speed, sped up
  to the highest and then sped down to the lowest giving twelve runs for each
  rider. (runs 1-6, 8-19, 101-106, 108-113)
- Normal pedaling starting at 5 km/h and decreasing speed until the rider could
  no longer balance with both riders. (runs 20, 21, 107, 114)
- Without pedaling (towed) at five speeds in which we either started at the low
  speed, sped up to the highest and then sped down to the lowest or did the
  oposite with both riders. (runs 22-27, 29-34, 115-120, 122-123, 126-131)
- Without pedaling starting at 5 km/h and decreasing speed until the rider could
  no longer balance with both riders. (runs 28, 121, 124, 125)
- Riderless weave stability test in which we increased the speed
  from 12 km/h to 25 km/h to try to detect detect the weave critical speed of
  the bicycle. We didn't have much luck getting the bicycle to stablize at all.
- Lateral perturbation at six speeds for each rider. (runs 132-133)
- No hand balancing with pedaling for one rider. (runs 60-71)
- Lane changes for both riders at six speeds. (runs 160-165, 80-85)
- A single attempt at riding with eyes closed. at 30 km/h [#]_
- Line tracking at six speeds for one rider. (runs 90-96)

Sensor Details
--------------

We did not analyze any of the data from the rate sensors on the bicycle. We
attached a rate gyro to the fork and handlebar assembly which was aligned with
the steer axis.

.. math::

   u_3 = u_{3s}
   u_4 = -u_{4s}
   u_7 = u_{7s}_ + u_{4s} \operatorname{sin}(\lambda) - u_{3s} \operatorname{cos}(\lambda)

Steer sensor design
-------------------

Data visualization GUI
----------------------


.. rubric:: Footnotes

.. [#] We took data for line tracking tasks also.

.. [#] The instrumented bicyle was measured less accuratley at this time than
   what is presented in Chapter :ref:`physicalparameters`, so the parameters are
   slightly different.

.. [#] The closed eye attempt would have been successful if the treadmill was
   infinitely wide
