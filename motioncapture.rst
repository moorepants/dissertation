.. _motioncapture:

==============
Motion Capture
==============

.. warning::

   This document is a draft which is updated regularly (Last updated |today|).
   Once I submit if for my doctoral degree at UC Davis, it will be done. So for
   now use at your own risk. The information may or may not be correct.
   Reviews, comments and suggestions are welcome.

Preface
=======

Sometime during the winter of 2008, Arend proposed our next project while I was
at Delft. I had told him that I wanted to have a project to call my own while I
was there, that could be written up as a major portion of my dissertation and
he proposed doing a motion study using principal components techniques in much
the same fashion as :cite:`Troje2002` had done with walking subjects. I think he'd
formulated the idea in discussion with Andy Ruina, his longtime vacation buddy
and colleague. I'd never heard of principal components (my statistics were and
are still weak), so I started reading up on principal components and what Troje
had done with walkers. I got a grasp of the technique and formulated a plan
based on a bicyclist riding on the large treadmill we had access to and
capturing their kinematics with a motion capture system. We went up for a
preliminary test day to check out the motion capture system and meet Richard
Casius who was the lab technician that knew the equipment. I was expecting he'd
just show us the on/off button and make sure we didn't break anything, but he
actually was there to run the system, help us figure it all out, and even do
some post processing of the data. This was odd for me, as my experience in the
U.S. was always that I had to do *everything* myself. Jodi was the rider for
the preliminary tests. It went well and we felt confident that we'd get the
kind of data we wanted. So we came back and started planning for three days of
testing with three riders. Jodi and I were going to ride and my fixie friend,
Victor, agreed to ride for us one day too. We had three successful days of
testing. Jodi and I then began analyzing the data with him coding a
visualization GUI that we'd devised and me processing the data using the PCA
methods. Once we could *see* the data, we went through every run manually and
coded each run for specific observations.

I got frustrated at this point, because we'd finally got to the results part
and it seemed to me that Jodi and Arend were getting to do the majority of the
analysis. I felt as if I'd put all my 100% effort into the work up to that
point and because I had this notion of ownership of the final product it seemed
as if my colleagues were getting to do the grand finale, whereas I wanted to be
in control. We made it through it though, despite my discontent. Arend and Jodi
didn't really understand my frustrations and deemed it a cultural difference. I
didn't buy that then, but now reflecting I tend to agree. My upbringing and
school training left me with little experience with *true* teamwork and I've
had my eye on the PhD dissertation as some kind of embodiment of my personal
understanding of *everything* that has to do with the subject I've been
studying. I had never really seen it as a collection of many people's effort,
the result being my orchestration of the collective ideas. These kinds of
realizations reflect on what the heart the Fulbright grant is. I went into the
grant thinking more about accomplishing the research goals that I proposed to
do, but after the fact I realize that cultural understanding and personal
interactions allowed me to grow as a person and realize the world in a more
global sense than any of the research accomplishments did. That kind of
foresight from the founders of grants like the Fulbright are invaluable to
humanity as a whole. I wish every high school student or college student in the
U.S. were required to study abroad. I think the political climate we see in the
world would be positively affected in a great way.

Another tactic I that was new to me was sending in an abstract for a conference
that really only talked about what we hoped to do, with the idea that it gives
us a deadline to get something done. This worked in this case, but I can't say
that it has been successful for me since. We first presented the results of this
study at the ECCOMAS Multibody Dynamics conference in June of 2009 and I think
it went pretty well :cite:`Moore2009b`.

After the conference, the paper was selected to be published in the Multibody
System Dynamics journal. I turned it down because Arend was more interested in
publishing in the Journal of Biomechanics. In the meantime, I had been
learning a lot about the open science movement and knew that our University
currently had an agreement with Springer that the open access fee would be
waived for all articles published by UCD affiliates and Multibody System
Dynamics is a Springer journal. So I decided that would be the better choice,
as journal titles seem like they are more and more irrelevant for my
generation. We search for articles on the internet and read them regardless of
where they are published, and the filtering of content quality is becoming an entirely
different mechanism than it was for science in previous generations. I see the
journal as a soon-to-be-lost relic. And hopefully, the closed peer review
system may be consumed by collective quality control by the readers and
appointed reviewers.

The work in this Chapter comes from two sources, the first is the peer reviewed
Multibody System Dynamics article, :cite:`Moore2011`, which I've copied
verbatim albeit with some fixed errata. The second is an addendum to the
results which was presented at the ISEA 2010 conference in Austria
:cite:`Moore2010`. It is a lead in to looking at the data with some other
statistical tools which I've had a growing interest in, but less than adequate
understanding.

Experiment Design
=================

We performed a wide range of maneuvers with three different riders at several
speeds. The aim of this section is to provide a detailed description of the
experiments and the accompanying data.

The experiments were performed in a controlled environment while the motion of
the bicycle and rider were measured with an active motion capture system
:cite:`NorthernDigitalIncorporated2009`. The rider rode on a :math:`3 \times 5`
meter treadmill, (:ref:`Figure 10.1<figVrijeTreadmill>`) capable of belt speeds
up to 35 km/h. Three male riders [Victor, Jason, Jodi] of similar age [23, 26,
31 years] and build [height (1.84, 1.83, 1.76 m) and mass (74, 72, 72 kg)]
participated as subjects. Each rode two different Dutch bicycles. Each rider
performed all runs in one day in the same order (no randomization) and was
instructed to bicycle comfortably at a constant speed in the range of 2 to 30
km/h for the duration of the run. There were at least 2 repetitions of each
speed with each bicycle. A run was sampled at a frequency of 100 Hz for 60
seconds.

Equipment
---------

All of the experiments were performed on a 3x5 m treadmilll at the the Vrije
Universiteit over a three day period. The treadmill had a 1% incline to counter
the rolling resistance. We used two bicycle donated by Batavus: the Browser and
the Stratos Deluxe.

Manuevers
---------

Normal
   For the "normal" bicycling task we instructed the riders to focus their
   sight into the distance and simply stabilize the bicycle and keep the
   heading generally pointing in the direction of the treadmill band velocity.
   Thus they were required to keep the bicycle roll angle and heading angle
   at zero. The rider pedaled during the experiment and was told to ride as if
   you were traveling down a straight empty road.
Towed
   The towed experiments were the same as the normal except that a rope was
   attached to the head tube of the bicycle and attached to the front railing of
   the treadmill. This allowed the rider to not have to pedal. The rider kept
   the cranks horizontal and was left to choose which foot he wanted forward.
   The rope could potentially have applied lateral forces to the frame if the
   rider drifted too much laterally, but we also held the rope taught and moved
   left and right to lessen the effect.
Line tracking
   The line tracking maneuver was the same at the normal maneuver except that
   the rider was instructed to keep his front wheel on a line we drew on the
   treadmill. This caused the rider to focus on not only stabilization but
   lateral deviation control.
No-hand
   We did some experiments with no hands riding (i.e. no steering control). The
   riders placed their hands on their hips and attempted to stabilize roll and
   yaw. Most of the these runs were with pedaling, but a few were taken with
   towing.

Data
----

The primary data was the three dimensional locations of the 31 markers for each
run. We sampled at 100 hz, giving (31 markers)(3 coordinates)(100 hz)(60
seconds) = 558,000 data points per each one minute run. We collected data for
268 one minute runs and 3 shorter static measurements of the bicycles for a
total of 271. The data for the first rider ended up somewhat corrupted. There
are a lot of erratic value changes in the data. The basic motion is there
though and clever filtering could clean the data for use.

We also collected data on the preliminary day with one rider and slightly
different marker locations and we collected some data during a TV show filming
of our work. We did not follow as strict protocols to the filmed experiments.

Source Code
-----------

The original data was processed with a series of Matlab scripts and then the
resulting processed data files were viewed with a Matlab program.

The source code can be found at
`<http://github.com/moorepants/MotionCapture>`_.

Principal Component Analysis
============================

Abstract
--------

Recent observations of a bicyclist riding through town and on a treadmill show
that the rider uses the upper body very little when performing normal maneuvers
and that the bicyclist may, in fact, primarily use steering input for control.
The observations also revealed that other motions such as lateral movement of
the knees were used in low speed stabilization. In order to validate the
hypothesis that there is little upper body motion during casual cycling, an
in-depth motion capture analysis was performed on the bicycle and rider system.

We used motion capture technology to record the motion of three similar young
adult male riders riding two different city bicycles on a treadmill. Each rider
rode each bicycle while performing stability trials at speeds ranging from 2
km/h to 30 km/h: stabilizing while pedaling normally, stabilizing without
pedaling, line tracking while pedaling, and stabilizing with no-hands. These
tasks were chosen with the intent of examining differences in the kinematics at
various speeds, the effects of pedaling on the system, upper body control
motions and the differences in tracking and stabilization.

Principal component analysis was used to transform the data into a manageable
set organized by the variance associated with the principal components. In this
paper, these principal components were used to characterize distinct kinematic
motions that occur during stabilization with and without pedaling. These
motions were grouped on the basis of correlation and conclusions were drawn
about which motions are candidates for stabilization-related control actions.

Introduction
------------

Much progress has been made in understanding the rigid body dynamics of an
uncontrolled bicycle (:cite:`Meijaard2007`, :cite:`Kooijman2008`) and various
control schemes have been explored for tracking purposes
(:cite:`Peterson2008a`, :cite:`Schwab2008`, :cite:`Sharp2008a`), but little is
understood about how a bicyclist actually stabilizes a bicycle during normal
riding. The bicycle and rider system is unique among vehicles in that the rider
is from 80 to 90% of the total mass of the system, the system is laterally
unstable, and the rider is flexibly coupled to the bicycle in such a way that
many body motions can be used as control inputs. Previous research into
realistic bicycle control has focused on both steering and rider lean as
control inputs, but there has been no experimental verification of which
motions a rider actually uses for control.  Recent observations of a bicyclist
riding through town and on a treadmill :cite:`Kooijman2009a` show that the
rider moves the upper body very little when performing normal maneuvers and
that the bicyclist may, in fact, primarily use steering input for control. This
corresponds well with the fact that control by leaning requires high gains
compared to the gains required for steering when employing an optimal control
strategy on a model (:cite:`Peterson2008a`, :cite:`Schwab2008`,
:cite:`Sharp2008a`). The observations also revealed that the rider may use
other control inputs such as drastic knee movements at low speeds.  These
conclusions were drawn by visually reviewing video data, so a more rigorous
objective method of characterizing the dominant movements of the bicyclist
while stabilizing a bicycle was needed. In order to validate the hypothesis
that there is little upper body motion during normal cycling, motion capture
techniques were used on the bicycle and rider system with the intent to use
principal component analysis to identify the major motion patterns.

Principal component analysis has successfully been used with data collected
from motion capture techniques to identify the dominant modes of motion of a
person walking on a treadmill :cite:`Troje2002` and to characterize different
types of walking. We use similar methods for steady, normal bicycle riding on a
treadmill. Cyclic motions, such as pedaling, are easily identified and
separated from the other less cyclic control actions. Identifying the patterns
of movement gives insight into which body movements are primarily used and are
candidates for control inputs. This will be valuable for our overall research
goals that include the design of a realistic biomechanical-based control system
of a bicycle rider, among other things.

Experiments
-----------

To test our hypotheses, three riders performed a set of stability tasks in a
controlled environment while the motion of the bicycle and rider were collected
with a motion capture system. The tasks were performed on a :math:`3 \times 5`
meter treadmill :ref:`Figure 10.1<figVrijeTreadmill>` capable of belt speeds up
to 35 km/h.  The treadmill was chosen because the envelope of space was
suitable for the motion capture system and it eliminated any disturbances such
as wind, rough ground, and obstacles. We chose three male riders of similar age
[31, 23, 26 years], build [height (1.76, 1.84, 1.83 m) and mass (72, 74, 72
kg)]. We also used two different Dutch bicycles: a 2008 Batavus Browser with a
3 speed hub and a 2008 Batavus Stratos Deluxe with a 7 speed hub. The Browser
is described by the manufacturer as “stable” and the Stratos Deluxe as
“nervous.”

.. _figVrijeTreadmill:

.. figure:: figures/motioncapture/treadmill.*
   :width: 4.69in
   :align: center
   :target: treadmill.png

   The :math:`3 \times 5` m treadmill at the Vrije Universiteit Amsterdam.

We made use of the Optotrak Certus Motion Capture System
:cite:`NorthernDigitalIncorporated2009` to record the motion of the bicycle and
rider during the stability tasks. The system is based on active infrared
emitting markers that are placed on the moving bodies and connected to a
central control unit. Each marker emits a sequential infrared signal and the
infrared pulses are captured by camera modules each containing three cameras.
The accuracy of the three dimensional measurements is :math:`\pm0.15` mm
:cite:`NorthernDigitalIncorporated2009`. The system has no hardware based noise
reduction. Wiring harnesses were built for both the rider and the bicycles to
facilitate easy bicycle and rider exchange :ref:`Figure 10.2<figMarkers>`.

.. _figMarkers:

.. figure:: figures/motioncapture/markers.*
   :width: 5.133in
   :align: center
   :target: _images/markers.jpg

   Rider 1 and the Batavus Stratos Deluxe with marker positions. Body marker
   positions visible from the rear.

The marker coordinates were measured with respect to an inertial frame,
:math:`\mathbf{M}`, where the plane normal to :math:`\hat{\mathbf{m}}_3` is
coplanar with the treadmill surface and :math:`\hat{\mathbf{m}}_3` is directed
upward. We collected the three dimensional locations of 31 markers, 11 of which
were located on the bicycle and 20 that mapped the rider :ref:`Figure
10.3<figMarkerLocation>`.

.. _figMarkerLocation:

.. figure:: figures/motioncapture/marker-location.*
   :width: 3in
   :align: center
   :target: _images/marker-location.png

   Schematic of the marker positions. The rider and bicycle are colored light
   gray and dark gray, respectively.

The markers were placed on the bicycle so that we could easily extract the
rigid body motion (i.e. body orientations and locations) of the bicycle frame
and fork. Four markers were attached to the fork and seven markers were
attached to the rear frame. A marker was attached on the right and left sides
of the center of each wheel, the seat stays, the ends of the handlebars, and
the head tube. A single marker was also attached to the back of the seat post.

We recorded the locations of 20 points on the rider :ref:`Figure
10.3<figMarkerLocation>`: left and right sides of the helmet near the temple,
back of the helmet, shoulders (greater tuberosity of the humerus), elbows
(lateral epicondyle of the humerus), wrists (pisiform of the carpus), between
the shoulder blades on the spine (T6 of the thoracic vertebrae), the tail bone
(coccyx), midpoint on the spine between the coccyx and shoulder blades (L1 on
the lumbar vertebrae), hips (greater trochanter of the femur), knees (lateral
epicondyle of the femur), ankles (lateral malleolus of the fibula) and feet
(proximal metatarsal joint). The body markers were not necessarily placed such
that a complete rigid body model could easily be fit to the data. This was done
to save setup and processing time because we only wanted a stick figure
representation of the rider that allowed us to visually observe the dominant
motions of the rider.

The stability tasks were designed such that the rider would ride at a constant
speed within the range of 2 to 30 km/h. The bicyclists were told to maintain an
upright straight-ahead course on the treadmill and to look into the distance,
with exception of the line tracking task. The bicyclists were instructed to
bicycle comfortably at the designated speed and data recording was started at
random. In all cases the subject rode at the set speed until comfortable, then
data was taken for 60 seconds at a 100 hertz sampling rate. Each test was
performed on each bicycle with each rider. The following list describes the
various tests:

Normal pedaling
    The subject was instructed to simply stabilize the bicycle while pedaling
    and keep the heading in approximately the forward direction. The speed
    started at 5 km/h and increased in 5 km/h increments up to 30 km/h. The
    speeds were then decreased in the same fashion to 5 km/h. From then on the
    speed was decreased in 1 km/h increments until the subject was not able
    stabilize the bicycle any longer. Therefore, there were two sets of data
    for each speed and each bicycle except speeds below 5 km/h. Several
    additional runs were also performed with the rider pedaling using a
    different gear and thus a different cadence.
Without pedaling
    This was the same as the normal pedaling task except that a string was
    attached to the head tube of the bicycle such that the bicycle was fixed
    longitudinally relative to the treadmill and no pedaling was required. The
    rider kept the feet in the same position throughout the task.
No-hands
    The riders stabilized the bicycle without using steering for control. They
    were instructed to keep their hands on their hips while bicycling. The
    rider started at 30 km/h and decreased in 5 km/h increments through 20 km/h
    and thereafter the speeds were decreased in 1 or 2 km/h increments until
    the rider was not able to comfortably stabilize the bicycle.
Line tracking
    This was the same as normal pedaling except that the rider was instructed
    to track a line on the treadmill surface with the front wheel. A smaller
    subset of speeds was performed.

These tasks were designed with the intent to answer several questions:

#. What upper body motions are used while bicycling?
#. How does the system motion change with respect to changes in forward
   speed?
#. How does pedaling influence the control actions?
#. Can the open loop rigid body dynamics be detected in the controlled
   state?
#. What does the rider do differently to control the bicycle when riding
   no-hands?
#. Do different bicyclists perform similar motions while performing the
   same task?
#. Is there a difference in motion when stabilizing and trying to track
   a line?

Since there is no room to address all of these questions in this chapter, we
focus on a single rider on the Browser bicycle and two of the tasks: normal
pedaling and without pedaling. We were able to draw some conclusions on
questions 1 through 4 with this smaller data set.

Open loop rigid body dynamics
-----------------------------

One question we have is whether or not the eigenfrequencies of the weave motion
for the uncontrolled system can be detected in the results from the
stabilization tasks. In order to predict the uncontrolled (open loop)
eigenvalues of the rigid rider system, the basic geometry, mass, center of
gravity locations, and moments of inertia of the bicycle were measured. Also,
the riders were measured and weighed such that the body segment geometry, mass,
center of gravity locations, and moments of inertia could be estimated. The
physical parameter estimation methods are described in :cite:`Moore2009a`. This
data was used to calculate eigenvalues and eigenvectors of the uncontrolled
open loop system :ref:`Figure 10.4<figEigPlot>`.

.. _figEigPlot:

.. figure:: figures/motioncapture/eig-plot.*
   :width: 6in
   :align: center
   :target: _images/eig-plot.png

   Eigenvalues of the Browser bicycle with the third rider rigidly
   attached as a function of speed. Note that the initially unstable
   weave motion becomes stable above 16 km/h, the weave speed.

Data processing
---------------

Missing markers
~~~~~~~~~~~~~~~

The Optotrak Certus Motion Capture System
:cite:`NorthernDigitalIncorporated2009` is based on the cameras’ ability to
detect the infrared light from the sensors so there are occasional gaps in the
coordinate data due to the markers going out of view. We attempted to minimize
this by careful marker and camera placement but were not able to totally
eliminate the error. Any missing markers on the bicycle were reconstructed
using the assumption that the bicycle is a rigid body. We had more than three
markers on both the frame and fork, so if one marker location was not detected
we used the relative location of the remaining markers to reconstruct the
missing marker. The gaps in the data of the markers on the human were repaired
by fitting a cubic spline through the data. The spline estimated the marker
coordinates during the gaps. We only used the splined data if the gaps were
less than 10 time steps, or 0.1 sec; otherwise the trials were discarded.

Relative motion
~~~~~~~~~~~~~~~

We were interested in the analysis of three different marker combinations: the
bicycle alone, the rider alone, and the bicycle and rider together. The motion
of the bicycle and the bicycle-rider were calculated with reference to the
:math:`\mathbf{N}` inertial frame[1] {The :math:`\mathbf{N}` frame is used
instead of the :math:`\mathbf{M}` frame to be consistent with the vehicle
coordinate standards used in :cite:`Meijaard2007` . See Section
:ref:`secInFrames` for the derivation.} and the motion of the rider was
calculated with respect to the rear frame of the bicycle :math:`\mathbf{B}`
:ref:`Figure 10.5<figFrames>`. These three marker combinations allowed us to
differentiate more easily between rider specific and bicycle specific motions.
Furthermore, six of the variables that describe the configuration of the
bicycle in time were calculated to give insight into the rigid body dynamics.
The configuration variables :math:`q_1` and :math:`q_2` locate the contact
point of the rear wheel of the bicycle. The :math:`\mathbf{B}` frame captures
the yaw (:math:`q_3`) and roll (:math:`q_4`) motions of the bicycle frame, the
:math:`\mathbf{D}` frame is an intermediate frame that differs from
:math:`\mathbf{B}` only by the bike’s steer axis tilt (:math:`\lambda`), and
the :math:`\mathbf{E}` frame captures the steering angle (:math:`q_7`) of the
bicycle fork relative to the bicycle frame. The pitch of the bicycle frame
(:math:`q_6`) is assumed to be zero. Details of these calculations are shown in
Section :ref:`secInFrames`.

.. _figFrames:

.. figure:: figures/motioncapture/frames.*
   :width: 3.86in
   :align: center
   :target: _images/frames.png

   Diagram of the bicycle's inertial frame :math:`\mathbf{N}`, rear frame
   :math:`\mathbf{B}`, front frame :math:`\mathbf{E}` and configuration
   variables.

.. _secPca:

Principal Component Analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We used Principal Component Analysis, PCA, :cite:`Jolliffe2002` to extract and
characterize the dominant motions of the system. Calculating the principal
components effectively transforms the space of the data to a space that
maximizes the variance of the data. The typical advantage of PCA is that the
dimension of the system can be reduced while still retaining enough information
to adequately describe the system. We are primarily interested in the way that
PCA is able to extract linear components and rank them in order of variance
from the mean position. If we assume that the components with the largest
kinematic variance are motions that are the dominant motions used for control
and propulsion (which in general is not necessarily true for dynamical systems)
the comparison of these components for different riding conditions can give
insight into what motions may be important for developing a biomechanical
control model of the bicyclist.

The repaired data from the motion capture measurements contained the :math:`x`,
:math:`y`, and :math:`z` coordinates of each marker :math:`1` through :math:`l`
at each time step :math:`j=1`, :math:`2`, :math:`\ldots`, :math:`n`. Each
marker has three coordinates so there are a total of :math:`m=3l` coordinates
:math:`i=1`, :math:`2`, :math:`\ldots`, :math:`m`. The coordinates at each time
step can be collected in vector :math:`\mathbf{p}_j`.

.. math::

   \mathbf{p}_j^T
    =\left[x_{1j}\quad\ldots\quad x_{lj}\quad y_{1j}\quad\ldots\quad
    y_{lj}\quad z_{1j}\quad\ldots\quad z_{lj}\right]
    =\left[p_{1j}\quad p_{2j}\quad\ldots\quad    p_{mj}\right]

We can organize these coordinate vectors into a matrix, :math:`\mathbf{P}`,
where the rows, :math:`i`, map a single coordinate of a marker through
:math:`n` time steps.

.. math::

   \mathbf{P}=\left[ \begin{array}{cccccc}
   |              & |              &        & |              &        & |             \\
   \mathbf{p}_{1} & \mathbf{p}_{2} & \ldots & \mathbf{p}_{j} & \ldots & \mathbf{p}_{n}\\
   |              & |              &        & |              &        & |
   \end{array} \right]

The principal components were calculated for the three marker combinations as
described earlier where :math:`n=60\cdot100=6000` time steps. The number of
rows of :math:`\mathbf{P}` were (:math:`m=3\cdot31=93`),
(:math:`m=3\cdot11=33`) and (:math:`m=3\cdot20=60`) for the bicycle-rider, the
bicycle alone and the rider alone, respectively.

One method of determining the principal components is to calculate the
eigenvectors of the covariance matrix of the mean-subtracted data. We begin by
calculating the mean :math:`\mathbf{u}` Equation :eq:`eqMean` of the rows of
:math:`\mathbf{P}` and subtracting it from each column of :math:`\mathbf{P}` to
form the mean-subtracted data matrix :math:`\bar{\mathbf{P}}`, Equation
:eq:`eqB`.

.. math::
   :label: eqMean

   \mathbf{u}=\frac{1}{n}\sum_{j=1}^n\mathbf{p}_j

A vector of ones

.. math::
   :label: eqH

   \mathbf{h}^T=\left[h_1\quad h_2\quad\ldots\quad h_j\quad\ldots\quad h_n\right]
   \textrm{ where }h_j=1\textrm{ for all }j

allows us to subtract :math:`\mathbf{u}` from each column of :math:`\mathbf{P}`,

.. math::
   :label: eqB

   \bar{\mathbf{P}}=\mathbf{P}-\mathbf{u}\mathbf{h}^T

The covariance matrix :math:`\mathbf{C}` of :math:`\bar{\mathbf{P}}` can then
be calculated with Equation :eq:`eqC`.

.. math::
   :label: eqC

   \mathbf{C}=\frac{1}{n-1}\bar{\mathbf{P}}\bar{\mathbf{P}}^T

Calculating the eigenvectors :math:`\mathbf{v}_i` and eigenvalues
:math:`\lambda_i` of the covariance matrix effectively transforms the space to
one in which the variances are maximized and the covariances are zero. The
eigenvectors are the principal components of the data set and the corresponding
eigenvalues represent the variance of each principal component. The
eigenvectors are ordered by decreasing eigenvalue where :math:`\mathbf{v}_1` is
the eigenvector corresponding to the largest eigenvalue. The eigenvalues and
eigenvectors are calculated by finding the independent solutions to Equation
:eq:`eqEig`.

.. math::
   :label: eqEig

   \mathbf{C}\mathbf{v}_i=\lambda_i\mathbf{v}_i

Each time step can now be represented as a linear combination of the principal
components.

.. math::
   :label: eqLinComb

   \mathbf{p}_j=\mathbf{u}+a_{1j}\mathbf{v}_1+a_{2j}\mathbf{v}_2+
   \ldots+a_{mj}\mathbf{v}_m

The coefficients :math:`a_{ij}` can be solved for each time step :math:`j` by
reformulating Equation :eq:`eqLinComb` and solving the system of linear
equations.

.. math::
   :label: eqSystem

   \mathbf{P}-\mathbf{u}\mathbf{h}^T=
   \left[\begin{array}{cccc}
   | & | & & | \\
   \mathbf{v}_1 & \mathbf{v}_2 & \ldots & \mathbf{v}_m\\
   | & | & & |
   \end{array}\right]
   \left[\begin{array}{ccc}
   a_{11} & \ldots & a_{1n}\\
   \vdots & \ddots & \vdots\\
   a_{m1} & \ldots & a_{mn}
   \end{array}\right]
   =\mathbf{V}\mathbf{A}

   \mathbf{A}=\mathbf{V}^{-1}(\mathbf{P}-\mathbf{u}\mathbf{h}^T)

With the principal components :math:`\mathbf{v}_i` being constant, the behavior
in time is described by the coefficients :math:`a_{ij}` where the
discretization in time is indexed by :math:`j`. The order of the system can be
reduced by eliminating principal components that have little variance. We
arbitrarily decided to examine the first :math:`k=10` principal components
knowing that the first five would be based on the larger motions such as
pedaling and that the remaining five may reveal some of the motions associated
with control. The variance of each component,
:math:`\textrm{var}(\mathbf{a}_i)=\lambda_i`, is summed to determine the
cumulative percentage of variance of the principal components, :math:`g_k`.

.. math::
   :label: eqGk

   g_k=100\frac{\sum_{i=1}^k\lambda_i}{\sum_{i=1}^m\lambda_i}
   \textrm{ where }1\leq k\leq m

Highly correlated data will show that even when :math:`k<<m`, :math:`g_k` is
close to 100%. Using 10 components :math:`g_{10}` covers 100% (:math:`\sigma =
2 \cdot10^{-14}` %) of the variation in the data for the bicycle, rider and
bicycle-rider. The matrix :math:`\mathbf{A}` can then be reduced to a :math:`k
\times n` matrix and eigenvectors corresponding to eigenvalues greater than
:math:`\lambda_k` can be eliminated.

Data Visualization
~~~~~~~~~~~~~~~~~~

We developed a graphical user interface, “GUI”, in Matlab that easily allows
different trials to be compared with one another :ref:`Figure 10.6<figGUI>`.
The program loads two different trials along with information on each trial. A
graphical representation of the rider and bicycle are displayed in two adjacent
screens and can be viewed from multiple perspectives. The animations of the
runs can be played at different speeds, rewound and fast forwarded. The
principal components are shown beside the corresponding animation display and
combinations can be turned on and off for identification and comparison.
Frequency and amplitude information for the temporal coefficients
:math:`a_{ij}` can also be displayed for comparison.

.. _figGUI:

.. figure:: figures/motioncapture/pca-gui.*
   :width: 5in
   :align: center
   :target: _imags/pca-gui.png

   Screen shot of the Matlab graphical user interface (GUI) used to visualize
   principal components and compare between different components and trials.

Results
-------

Motion identification
~~~~~~~~~~~~~~~~~~~~~

The reduced set of data provides two important pieces of information for the
identification of motion: the principal components :math:`\mathbf{v}_i` and the
corresponding coefficients :math:`a_{ij}`. The principal components represent
linear trajectories of the markers and the coefficients show how the markers
follow the trajectories with time. We began processing the data by reviewing
each principal component of each trial in the GUI and noting what type of
motion we saw :ref:`Table 10.1<tabTrialDesc>`. These descriptions were subjective
because we grouped marker movement based on our preconceived understanding of
rider and bicycle motion. Some of the components displayed motions that were
not physically possible such as the upper leg stretching in length during the
knee bounce. This is possible when examining a single component but when
superimposed over the rest of the components the unrealistic motions are not
present. Furthermore, for each component we examined amplitude and frequency
content of the associated coefficients :math:`a_{ij}` as shown in Figures
:ref:`10.6<figCoef3062>` and :ref:`10.7<figFft3062>` and noted the shape of the
frequency spectrum and the frequencies at any distinct spikes.

.. _tabTrialDesc:

.. tabularcolumns:: LLLL

.. list-table:: Example raw trial description for the bicycle and rider during
   normal pedaling at 10 km/h.
   :header-rows: 1

   * - :math:`i`
     - % Variance
     - Motion Description
     - Frequency Description
   * - 1
     - 45.50
     - primarily longitudinal motion, some lateral
     - max amp = 0.6 m, most freq below 0.5 Hz, tiny spike at 1.6 Hz
   * - 2
     - 29.39
     - primarily lateral motion, some longitudinal, small feet motion
     - max amp = 0.35 m, little spike at 0.8 Hz, most freq below 0.5 Hz
   * - 3
     - 15.41
     - vertical pedaling, slight spine bend, hip/head/shoulder sway out of
       phase with pedaling
     - max amp = 0.27 m, large dominant spike at 0.8 Hz
   * - 4
     - 8.27
     - horizontal pedaling, head/shoulder sway
     - large dominant spike at 0.8 Hz with 0.19 m amp
   * - 5
     - 0.82
     - yaw, knees stay still
     - max amp = 0.04 m at 0.33 Hz, most freq below 1 Hz
   * - 6
     - 0.27
     - erratic left-hand movement
     - max amp = 0.018 m, most freq below 2 Hz
   * - 7
     - 0.21
     - steer, left-hand movement, slight roll
     - most freq below 2 Hz, spike at 0.33 Hz and 1.58 Hz
   * - 8
     - 0.07
     - knee and head bounce
     - dominant spike at 1.58 Hz
   * - 9
     - 0.04
     - lateral knee movement, head jiggle
     - spikes at 1.58 Hz and 2.37 Hz, most freq below 2.5 Hz
   * - 10
     - 0.02
     - head and knee jiggle
     - spikes at 1.58 Hz and 3.17 Hz, most freq below 3.5 Hz

.. _figCoef3062:

.. figure:: figures/motioncapture/coef3062.*
   :width: 4in
   :align: center
   :target: _images/coef3062.png

   Coefficients :math:`a_{ij}` versus time content of the first five principal
   components for normal pedaling at 10 km/h.

.. _figFft3062:

.. figure:: figures/motioncapture/fft3062.*
   :width: 4in
   :align: center
   :target: _images/fft3062.png

   The frequency content of the first five principal components for normal
   pedaling at 10 km/h. The vertical black line represents the open loop weave
   frequency (0.28 Hz) determined from :ref:`Figure 10.4<figEigPlot>` at this
   forward speed. The pedaling frequency is about 0.8 Hz at this speed, see
   :ref:`Figure 10.10<figSteerAnglePedal>`.

Several conclusions can be drawn from examining the coefficient data. First,
some of the components are linked by the frequencies of the coefficients and
describe an identifiable motion. The most obvious of these is that the vertical
and horizontal pedaling components make up the circular pedaling motion. Both
vary periodically and have a dominant frequency which is defined by the
cadence. In the example trial, :ref:`Table 10.1<tabTrialDesc>`, the upper body
motions are also linked to the pedaling. Components 8 and 9 both correspond to
a frequency that is twice the pedaling frequency, which may be due to the
forces created during each pedal stroke. Component 6 seems to be the result of
a bad marker signal. Components 5 and 7 are interesting because they display
motions of the bicycle that are not dominated by the pedaling frequency and may
be candidate control motions. The percentage variance of each component gives
an idea of the relative amplitude of the components. The descriptions of each
trial were used to compile a list of motions that contribute to the principal
components. These motions, illustrated in :ref:`Figure 10.9<figMotions>`, are:

Drift
    The bicycle and rider drift longitudinally and laterally on the surface of
    the treadmill. The motions are typically defined by two components that are
    not necessarily orthogonal or aligned with the inertial coordinate system.
    The motion is random and at low frequencies.
Steer
    Rotation of the front assembly with respect to the rear frame. The steering
    may appear linked to one of the pedaling components at the pedaling
    frequency or may be in one or more components sometimes combined with roll
    and/or yaw at more random frequencies.
Roll
    The bicycle and the rider roll with respect to the ground plane. Roll is
    typically linked with steer and/or yaw and often at the pedaling frequency.
Yaw
    The heading angle of the bicycle and rider change together with respect to
    the ground plane. This is typically linked with steer, roll and/or the
    drift.
Pedaling
    This motion is defined by two or more components, typically a vertical and
    horizontal motion of the feet, that show the feet rotating around the crank
    axle at a distinct frequency and the legs following suit.
Bend
    The spine bent laterally and was always connected with the vertical
    pedaling component.
Lean
    The upper body, shoulders and head lean laterally with respect to the rear
    frame and was always linked with the horizontal pedaling component.
Twist
    The shoulders rotate about the torso axis. This was linked to components
    that contained steering motions, both random and at the pedaling frequency.
Bounce
    The knee markers bounce up and down, the back straightens and the head nods
    at twice the pedaling frequency.
Knees
    The knees move laterally relative to the bicycle frame in both opposing
    directions and the same direction at random low frequencies.
Head
    Head twists and random head motions showed up often. These seemed to
    be due to the rider looking around randomly.

.. _figMotions:

.. figure:: figures/motioncapture/motions.*
   :width: 5.5in
   :align: center
   :target: _images/motions.png

   Diagrams of the common motions. (a) Top view of bicycle steer and roll, (b)
   bicycle yaw, (c) horizontal and vertical components of pedaling, (d) spine
   bend, (e) rider lean, (f) top view of rider twist, (g) knee bounce and (h)
   two lateral knee motions. All but pedaling (c) are exaggerated for clarity.

Motion Characterization
~~~~~~~~~~~~~~~~~~~~~~~

To identify how bicycling changes with speed it would be ideal to investigate
how the amplitude of each component varies with speed. However, the analysis
does not return the same set of components for each run so such a comparison is
typically not possible. Therefore components were grouped into classes, where
each class shows a specific physically relevant motion. The same total motion
of the class can be described by one set of components in one trial and
another, probably different, set of components in another trial. How the
amplitudes of these classes vary among experiments can be used as a measure for
how the rider and bicycle motion varies among trials.

To objectively identify which coefficients show the same type of motion and
could therefore form a class, the frequency content of each of the time
coefficients in a single trial was correlated to that of each of the other
components in that trial. Next a minimum correlation value was set to determine
which coefficients were correlated to each other. When the minimum was set at
0.9 only the coefficients making up the pedaling motion could be considered
correlated. On the other hand when a minimum level of 0.7 was used practically
every coefficient was correlated to each other. The only exception was the
coefficient that displayed the bounce. Its maximum correlation with another
coefficient was no higher than 0.4 for any of the tested speeds. The 0.8 level
gave a number of distinct classes of components and thus this level was used to
identify which coefficients were connected. Finally, the correlated
coefficients were viewed simultaneously in the GUI enabling the determination
of the motion class.

The correlated coefficients were used to form six different classes of motions,
Table :ref:`Table 10.2<tabMotionClasses>`, each made up of combinations of the
previously described motions in :ref:`Figure 10.9<figMotions>`.

.. _tabMotionClasses:

.. tabularcolumns:: LL

.. list-table:: The six primary motion classes.
   :header-rows: 1

   * - Class Name
     - Class Description
   * - Drift
     - Drift
   * - Pedaling
     - Pedaling, Bend, Lean, Twist, Steer-Yaw-Roll, Yaw
   * - Bounce
     - Bounce
   * - Knees
     - Knees
   * - Other
     - Head and components that showed noise of some sort

In most cases, the correlated coefficients described a single class. However,
in some cases, this was not the case and the coefficients were used to describe
more than one class. An example is that at low speed the components containing
the drift motions also contained large steer, yaw, and roll motions. Therefore,
the motions were placed in both the Drift and the Steer-Yaw-Roll classes.

Since the rider was not instructed to hold a specific location on the treadmill
the Drift class, which was usually the class with the largest amplitude, was
not used in further analysis of the motion and neither was the ‘Other’ class.
For each of the remaining classes, the percentages of variance of the remaining
components were recalculated without the components placed in the Drift and the
Other classes.

We also calculated various configuration variables from the bicycle marker
locations (See Section :ref:`secInFrames` independent of the PCA perspective
for more specific motion characterizations. This allowed us to investigate the
bicycle’s configuration variable time histories and frequency content
explicitly.

Characterization of motions during normal pedaling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`Figure 10.10<jellybean>` shows how the relative percent variance of the four
classes: Pedaling, Steer-Yaw-Roll, Bounce and Knees varies with speed for Rider
3 on the Batavus Browser bicycle. The percentage is the average of two runs at
speeds 5 km/h and above. From the graph, it is clear that at 10 km/h and higher
speeds practically all the motion that is taking place is the pedaling motion
class. Below 10 km/h, the Steer-Yaw-Roll class becomes increasingly active and
the relative percentage of the motion taking place in the pedaling class drops.
Also, at speeds below 10 km/h the lateral knee motion (Knees) class percentage
increases with decreasing speed. The increase is not as significant as that of
the Steer-Yaw-Roll class (increase to roughly 5% at 2 km/h), but it is
certainly visible. The spike at 4 km/h can be attributed to the fact that the
classes may contain higher variance motions because the classification method
is based on principal components that are not necessarily consistent between
runs. The Bounce roughly remains constant at all speeds.

.. _jellybean:

.. figure:: figures/motioncapture/pedaling4classes.*
   :width: 5.65667in
   :align: center
   :target: _images/pedaling4classes.png

   The relative percent variance of the four classes: Pedaling, Steer-Yaw-Roll,
   Bounce and Knees, at the different speeds when the Drift and Other classes
   were removed from the results for normal pedaling. The solid lines are
   scaled to 100% (left axis), the dotted lines are scaled to 10% (right axis).

The steer angle amplitude-frequency plot for each of the speeds calculated from
the bicycle rigid body motions is given in :ref:`Figure
10.11<figSteerAnglePedal>`. It clearly shows that the steering actions take
place at or around the pedaling frequency for high and low speeds,
respectively. It also shows that the amplitude of the steering angle increases
by 5000% when the speed decreases from 30 km/h to 2 km/h. :ref:`Figure
10.11<figSteerAnglePedal>` also shows the open loop, rigid rider, weave
eigenfrequency for each speed obtained from :ref:`Figure 10.4<figEigPlot>`.
Apparently the open loop eigenfrequency is not a frequency at which the
bicycle-rider operates.

.. _figSteerAnglePedal:

.. figure:: figures/motioncapture/steer-angle-pedal.*
   :width: 6.13in
   :align: center
   :target: _images/steer-angle-pedal.png

   Steer angle amplitude plot for the nine different speeds for normal pedaling
   experiment. Solid vertical line indicates the pedaling frequency. Dashed
   vertical gray line indicates the bicycle-rigid rider open loop weave
   eigenfrequency from :ref:`Figure 10.4<figEigPlot>`.

Characterization of motions without pedaling
--------------------------------------------

During normal pedaling, all motions, including the control tasks, are dominated
by the pedaling motions. Therefore we also looked at the motions of
bicycle-rider system without the influence of pedaling. :ref:`Figure
10.12<missjellybean>` shows how the percent variance of by Steer-Yaw-Roll,
Bounce and Knees varies with speed for Rider 3 on the Batavus Browser bicycle
without pedaling. Since the bicycle is towed and the riders feet remain in the
same, constant, position relative to bicycle, there is no pedaling class
present in analysis. Furthermore, no bend, lean or twist motions with high
variance were detected during the experiments.

.. _missjellybean:

.. figure:: figures/motioncapture/towing3classes.*
   :width: 5.65667in
   :align: center
   :target: _images/towing3classes.png

   The percent variance of each of the three classes: Steer-Yaw-Roll, Bounce
   and Knees, at the speeds at which the Drift and Other classes were removed
   from the results for trials without pedaling. The solid lines are scaled to
   100% (left axis), the dotted lines are scaled to 20% (right axis).

It is clear that at all speeds most motion takes place in the Steer-Yaw-Roll
class. Also interesting is that unlike the normal pedaling situation, the Knee
motion percentage does not increase at low speeds. This may mean that the
lateral knee motion is connected to pedaling in some way. Like for the pedaling
case, the Bounce and Knees classes may contain different principal components
and a statistical approach to evaluate the percent variance of the classes
would provide clearer results. Also note that as the bicycle becomes self
stable above 16 km/h the total variance is tiny and thus any sort of random
knee motion can be a relatively large motion.

:ref:`Figure 10.13<figSteerAngleTowing>` shows the bicycle rigid body steer
angle frequency-amplitude plot for different speeds. Compared to normal
pedaling, the amplitudes are about half the size at the low speeds and one
tenth the size at high speeds, indicating that smaller steering angles were
made. The frequency content now also shows a much wider, flatter spectrum
compared to normal pedaling. At 10 and 15 km/h, the frequency with the largest
amplitude is near the open loop weave eigenfrequency. However, at the other
speeds, this is not the case, once again indicating that the rigid body open
loop weave eigenfrequency is not the frequency at which the bicycle is
controlled.

.. _figSteerAngleTowing:

.. figure:: figures/motioncapture/steer-angle-towing.*
   :width: 6.24in
   :align: center
   :target: _images/steer-angle-towing.png

   Steer angle amplitude plot for the nine different speeds for the tasks
   without pedaling. Dashed vertical grey line indicates the bicycle-rigid
   rider open loop weave eigenfrequency obtained from :ref:`Figure
   10.4<figEigPlot>`.

Conclusions
===========

The view provided by principal component analysis into bicycle-rider
interaction, biomechanics and control has led us to several conclusions. During
normal bicycling there are several dominant upper body motions: lean, bend,
twist and bounce, all of which seem to be linked to the pedaling motion. This
is important for understanding which inputs are related to fundamental balance
control and which are reactions to pedaling. We hypothesize that lateral
control is mainly accomplished by steering since only upper body motion was
observed at the pedaling frequency. If upper body motions are used for control
then this control is carried out at the pedaling frequency. Considering
variations of motion with respect to speed, we observed that there is a great
deal of steering at low speeds but this decreases in magnitude as speed
increases. This is generally true for all motions and shows that the
bicycle-rider system becomes more stable at higher speeds with few detectable
control actions. At low speeds additional lateral knee motions are observed
which are probably more effective at augmenting steering control for lateral
balance than upper body motions.

The bicycle model predicts that the weave mode is stable above about 16 km/h
(4.4 m/s). Intuition might possibly lead one to believe that if the weave mode
is already stable, that weave frequency might be relatively undisturbed by
rider control actions and therefore present in the closed loop dynamics.
However, we found no evidence of a distinct weave frequency in the steer angle
time histories of any run. In fact the only distinct frequency that sometimes
appeared was the pedaling frequency.

Principal component analysis provided a unique view into the control actions of
a rider on a bicycle, but limitations in data reduction and motion grouping
leave room for more objective statistical views into the motion of the
bicycle-rider system.

.. _secInFrames:

Inertial frames and configuration variables
===========================================

The transformation from marker coordinates to rigid body inertial frames and
configuration variables shown in :ref:`Figure 10.5<figFrames>` is described
here. A reference frame, :math:`\mathbf{N}`, with origin :math:`n_o`
corresponding with the benchmark bicycle is defined with respect to the
Optotrak reference frame, :math:`\mathbf{M}`, Equation :eq:`eqNtoM`.

.. math::
   :label: eqNtoM

   \mathbf{N}=
   \left[
   \begin{array}{c}
   \hat{\mathbf{n}}_1\\
   \hat{\mathbf{n}}_2\\
   \hat{\mathbf{n}}_3
   \end{array}
   \right]
   =
   \left[
   \begin{array}{rrr}
   1 &  0 &  0\\
   0 & -1 &  0\\
   0 &  0 & -1
   \end{array}
   \right]
   \left[
   \begin{array}{c}
   \hat{\mathbf{m}}_1\\
   \hat{\mathbf{m}}_2\\
   \hat{\mathbf{m}}_3
   \end{array}
   \right]

Thirty-one marker locations were recorded and the vector to each is defined as
:math:`\mathbf{r}^{{m_{k}}/{n_o}}` where :math:`k=1`, :math:`2`,
:math:`\ldots`, :math:`l` for the original markers and :math:`k=l+1`,
:math:`\ldots` for any additional virtual markers. To calculate the reference
frame attached to the rear bicycle we formed a frame center plane from the seat
post marker, :math:`m_{26}`, and two new additional virtual markers at the
center of the rear wheel, :math:`m_{36}`, and the center of the head tube,
:math:`m_{33}`. For example, the center of the rear wheel was calculated by
Equation :eq:`eqRearCenter` where :math:`m_{25}` and :math:`m_{31}` are the
left and right rear wheel markers.

.. math::
   :label: eqRearCenter

   \mathbf{r}^{{m_{36}}/{n_o}} = (\mathbf{r}^{{m_{25}}/{n_o}} +
   \mathbf{r}^{{m_{31}}/{n_o}})/2

The normal vector to the plane through the rear wheel center, seat post and the
head tube center is

.. math::
   :label: eqB2

    \hat{\mathbf{b}}_2=
    \frac{\mathbf{r}^{{m_{36}}/m_{26}}\times\mathbf{r}^{{m_{33}}/m_{26}}}
    {|\mathbf{r}^{{m_{36}}/m_{26}}\times\mathbf{r}^{{m_{33}}/m_{26}}|}

The heading vector of the rear frame is then
:math:`\hat{\mathbf{b}}_1=\hat{\mathbf{b}}_2\times\hat{\mathbf{n}}_3` and
:math:`\hat{\mathbf{b}}_3=\hat{\mathbf{b}}_1\times\hat{\mathbf{b}}_2` follows.
These unit vectors define a reference frame that leans and yaws with the rear
frame. We assumed that the rear frame pitch is negligible. The marker locations
of the rider can now be expressed relative to the bicycle’s inertial frame with
reference to a point on the bicycle frame :math:`m_{36}`. Equation
:eq:`eqWrtRear` shows that the vector from any marker on the rider relative to
:math:`m_{36}` can be expressed in the bicycle reference frame,
:math:`\mathbf{B}`, rather than the inertial frame, :math:`\mathbf{N}`. This
formulation was used in the PCA of the rider-only markers to look specifically
at rider motion relative to the bicycle. The subscripts, :math:`\mathbf{N}` and
:math:`\mathbf{B}`, in Equation :eq:`eqWrtRear` signify which reference frame
the position vectors are expressed in.

.. math::
   :label: eqWrtRear

   \mathbf{r}^{{m_{k}}/m_{36}}_\mathbf{B}=
   (\mathbf{r}^{{m_{k}}/m_{36}}_\mathbf{N}\cdot\hat{\mathbf{b}}_1)\hat{\mathbf{b}}_1+
   (\mathbf{r}^{{m_{k}}/m_{36}}_\mathbf{N}\cdot\hat{\mathbf{b}}_2)\hat{\mathbf{b}}_2+
   (\mathbf{r}^{{m_{k}}/m_{36}}_\mathbf{N}\cdot\hat{\mathbf{b}}_3)\hat{\mathbf{b}}_3

A reference frame :math:`\mathbf{D}` that is aligned with the steering axis of
the rear frame can be formulated by rotation about the
:math:`\hat{\mathbf{b}}_2` axis through the steer axis angle :math:`\lambda`,
which is measured for each bicycle :cite:`Moore2009a`.

.. math::
   :label: eqDframe

   \mathbf{D}=
   \left[
   \begin{array}{c}
   \hat{\mathbf{d}}_1\\
   \hat{\mathbf{d}}_2\\
   \hat{\mathbf{d}}_3
   \end{array}
   \right]
   =
   \left[
   \begin{array}{rrr}
   \cos{\lambda} &  0 &  -\sin{\lambda}\\
   0             &  1 &  0\\
   \sin{\lambda} &  0 & \cos{\lambda}
   \end{array}
   \right]
   \left[
   \begin{array}{c}
   \hat{\mathbf{b}}_1\\
   \hat{\mathbf{b}}_2\\
   \hat{\mathbf{b}}_3
   \end{array}
   \right]

The handlebar/fork inertial frame :math:`\mathbf{E}` is then calculated by
defining :math:`\hat{\mathbf{e}}_2` to be aligned with the front wheel axle
Equation :eq:`eqE2`.

.. math::
   :label: eqE2

   \hat{\mathbf{e}}_2=\frac{\mathbf{r}^{{m_{21}}/{n_o}}-\mathbf{r}^{{m_{27}}/{n_o}}}
   { | \mathbf{r}^{{m_{21}}/{n_o}}-\mathbf{r}^{{m_{27}}/{n_o}} | }

The handlebar/fork frame rotates around
:math:`\hat{\mathbf{d}}_3=\hat{\mathbf{e}_3}` and then
:math:`\hat{\mathbf{e}}_1=\hat{\mathbf{e}}_3\times\hat{\mathbf{e}}_2`.
Equation :eq:`eqRr` gives the instantaneous rear wheel radius which is used to
formulate the vector to the rear wheel contact point Equation :eq:`eqR39`.

.. math::
   :label: eqRr

   r_\mathbf{R}=
   -\frac{\mathbf{r}^{{m_{36}}/{n_o}}\cdot\hat{\mathbf{n}}_3}
   {\hat{\mathbf{b}}_3\cdot\hat{\mathbf{n}}_3}

.. math::
   :label: eqR39

   \mathbf{r}^{{m_{39}}/{n_o}} =
   \mathbf{r}^{{m_{36}}/{n_o}}+r_\mathbf{R}\hat{\mathbf{b}}_3

This now allows us to calculate six of the eight configuration variables of the
bicycle as a function of time (:math:`q_5` and :math:`q_8` are the rear and
front wheel rotations, respectively).

.. math::
   :label: eqQ1

   \textrm{Distance to the ground contact point: }q_1 =
   \mathbf{r}^{{m_{39}}/{n_o}}\cdot\hat{\mathbf{n}}_1

.. math::
   :label: eqQ2

   \textrm{Distance to the ground contact point: }q_2 =
   \mathbf{r}^{{m_{39}}/{n_o}}\cdot\hat{\mathbf{n}}_2

.. math::
   :label: eqQ3

   \textrm{Yaw angle: }q_3 = \arccos\left(\hat{\mathbf{b}}_1
   \cdot\hat{\mathbf{n}}_1\right)

.. math::
   :label: eqQ4

   \textrm{Roll angle: }q_4 = \arccos\left(\hat{\mathbf{b}}_3
   \cdot\hat{\mathbf{n}}_3\right)

.. math::
   :label: eqQ6

   \textrm{Pitch angle: }q_6 = 0

.. math::
   :label: eqQ7

   \textrm{Steer angle: }q_7 = \arccos\left(\hat{\mathbf{d}}_1
   \cdot\hat{\mathbf{e}}_1\right)

Simple Statistics
=================

Preface
-------

Once again, we collected more data than we knew what to do with
:cite:`Moore2011` and only looked at a subset of it from one rider. I took my
first statistics class once I was back at Davis in the Fall of 2009 with the
intention of learning better ways to analyze large data sets and make more over
arching conclusions with the bicycle data. In the process, I learned about
mixed effects models and that they seemed appropriate for our data sets and
would potentially allow us to see how the kinematic motions changed with
respect to speeds, riders, maneuvers, etc. The first step in building a model
like this is to identify the independent and dependent variables. The dependent
variables can be broken up into continuous variables and factors. Speed
constitutes the continuous variable, with riders, bicycles and maneuvers as the
factors. The independent variables are trickier because we recorded time
histories, so various statistics need to be chosen. These could be things like
the results of the PCA analyses, but more concrete kinematic statistics
potentially allow for more understanding. The PCA we did assumes nothing about
the system being studied. For example, one statistic could be the standard
deviation of various generalized coordinates. I never managed to get far with
this as other things came up, but I at least started thinking about the
relevant statistics. The following is a conference paper I submitted to the
2010 International Sports Engineering Association conference in which basic
statistics of the time histories are chosen and some visualization of the
statistics with respect to speed are shown. I primarily used this data to
decide on sensor ranges when building the Davis instrumented bicycle presented
in Chapter :ref:`davisbicycle`, but I think that some better statistical models
could be derived. I also only present some of the graphs here, but the source
code can generate many more.

Abstract
--------

An overview of bicycle and rider kinematic motions from a series of
experimental treadmill tests is presented. The full kinematics of bicycles and
riders were measured with an active motion capture system. Motion across speeds
are compared graphically with box and whisker plots. Trends and ranges in
amplitude are shown to characterize the system motion. This data will be used
to develop a realistic biomechanical model and control model for the rider and
for future experimental design.

Introduction
------------

In the past decade, research has grown on single track vehicles culminating in
the recently benchmarked bicycle model :cite:`Meijaard2007`. Two other recent
papers (:cite:`Astrom2005`, :cite:`Limebeer2006`) have also presented overviews
of current and historical research in bicycle dynamics and control. These
review a plethora of dynamic models but little is known about which models are
good at representing the actual system. Very little model-validation
experimentation has been performed in the literature and many of the modeling
assumptions, especially those regarding tire and rider dynamics, remain
questionable. The most recent notable model-validation study is the
verification of the benchmark model :cite:`Kooijman2008`. Only a handful of
other good experimental studies on bicycle dynamics exist. The work
:cite:`Lunteren1970` performed some 40 years ago in the same halls as the
Kooijman experiments :cite:`Kooijman2008` included extensive efforts to
validate a human control model using a bicycle simulator paired with
statistical analysis. Also, around the same time as the first Delft experiments
:cite:`Lunteren1970`, a substantial study was done at Calspan and Schwinn
:cite:`Roland1971`.

With these studies providing some background, we have begun work to validate
the kinematics of the bicycle and rider in a way that can facilitate the
derivation of both dynamic models of the bike and rider and a rider control
model. Our work began with an instrumented bicycle :cite:`Kooijman2009a` that was
capable of measuring dynamics and collecting video of the rider’s motion. We
then used full body motion capture :cite:`Moore2009b` to quantitatively characterize
the rider and bicycle kinematics. Principal component analysis was used to
analyze the motion capture data but this proved to give less insight than
expected. These initial efforts did show that the dominant motions for control
are steering, that the rider’s motions are small for normal bicycling tasks,
and that pedaling motions are correlated with other rider motions. The present
work examines the same motion capture data from :cite:`Moore2009b` with rigid body
kinematics in mind and uses a statistical approach to identify trends with
forward speed, a strong dependency of bicycle stability.

Experimental Design
-------------------

The experiments were performed in a controlled environment while the motion of
the bicycle and rider were measured with an active motion capture system
:cite:`NorthernDigitalIncorporated2009`. The rider rode on a :math:`3\times5`
meter treadmill, (:ref:`Figure 10.1<figVrijeTreadmill>`) capable of belt speeds
up to 35 km/h. Three male riders of similar age [23, 26, 31 years] and build
[height (1.84, 1.83, 1.76 m) and mass (74, 72, 72 kg)] participated as
subjects. Each rode two different Dutch bicycles. Each rider performed all runs
in one day in the same order (no randomization) and was instructed to bicycle
comfortably at a constant speed in the range of 2 to 30 km/h for the duration
of the run. There were at least 2 repetitions of each speed with each bicycle.
A run was sampled at a frequency of 100 Hz for 60 seconds.

Bicycle markers were placed to easily extract the rigid body motion (i.e. body
orientations and locations) of the frame and fork (:ref:`Figure
10.2<figMarkers>`).  Four markers were attached to the fork and seven to the
rear frame. A marker was attached on the right and left sides of the center of
each wheel, the seat stays, the ends of the handlebars, and the head tube. A
single marker was also attached to the back of the seat post.

We recorded the locations of 20 points on the rider (:ref:`Figure
10.3<figMarkerLocation>`): left and right sides of the helmet near the temple,
back of the helmet, shoulders (greater tuberosity of the humerus), elbows
(lateral epicondyle of the humerus), wrists (pisiform of the carpus), between
the shoulder blades on the spine (T6 of the thoracic vertebrae), the tail bone
(coccyx), midpoint on the spine between the coccyx and shoulder blades (L1 on
the lumbar vertebrae), hips (greater trochanter of the femur), knees (lateral
epicondyle of the femur), ankles (lateral malleolus of the fibula) and feet
(proximal metatarsal joint).

Data Processsing
----------------

Once marker data was repaired, we calculated several generalized coordinates.
This provided a way to characterize the bicycle and rider as a system of rigid
bodies which seems to give a clearer picture of the underlying control motions
that the principal component analysis provided :cite:`Moore2009b`. The coordinates
included bicycle yaw, roll and steer angles and the locations of the wheel
ground contact points, and several coordinates to represent rider motion: the
rider’s lean and twist angles, lateral knee motion, and lateral tail bone
motion, all relative to the bicycle frame plane of symmetry. The rider lean
angle can be thought of as the angle of the rider’s spine relative to the
bicycle frame. The twist is the angle through which the torso rotates about the
spine. The knee and butt motions are the relative lateral distances from the
frame plane of symmetry for each marker. These are shown because we observed
large lateral knee movement in video footage at low speeds :cite:`Kooijman2009a`
that may be used for additional control. The butt motion is plotted to give an
idea of how the seat can potentially be shifted under the torso to control roll
angle. Figures :ref:`10.14<fig3017wheel>`, :ref:`10.15<fig3017bAng>`,
:ref:`10.16<fig3017rLat>`, and :ref:`10.17<fig3017rAng>` show examples of the
time histories of these coordinates.

.. _fig3017wheel:

.. figure:: figures/motioncapture/3017wheel.*
   :width: 3in
   :align: center
   :target: _images/3017wheel.png

   The positions of the front and rear wheel contact points throughout a single
   a normal biking run at 10 km/h.

.. _fig3017bAng:

.. figure:: figures/motioncapture/3017bAng.*
   :width: 3in
   :align: center
   :target: _images/3017bAng.png

   The bicycle yaw, roll and steer angles throughout a single a normal biking
   run at 10 km/h.

.. _fig3017rLat:

.. figure:: figures/motioncapture/3017rLat.*
   :width: 3in
   :align: center
   :target: _images/3017rLat.png

   Lateral deviations of the knees and butt from the frame plane throughout a
   single normal biking run at 10 km/h.

.. _fig3017rAng:

.. figure:: figures/motioncapture/3017rAng.*
   :width: 3in
   :align: center
   :target: _images/3017rAng.png

   Rider lean and twist angles throughout a single normal biking run at 10
   km/h.

The primary coordinates are presented in Section :ref:`secInFrames`. The
remaining are calculated as follows. The instantaneous front wheel radius is

.. math::
   :label: eqFrontRadius

   r_\mathbf{F} = \frac{-\mathbf{r}^{m_{32}/n_o} \cdot \hat{n}_3}
   {\operatorname{sin}[\operatorname{arccos}(\hat{e}_2 \cdot \hat{n}_3)]}

The front wheel contact point is then

.. math::
   :label: eqFrontWheelContact

   \mathbf{r}^{m_{40}/n_o} = \mathbf{r}^{m_{32}/n_o} + r_\mathbf{F}
   \frac{(\hat{e}_2 \times \hat{n}_3) \times \hat{e}_2}
   {|(\hat{e}_2 \times \hat{n}_3) \times \hat{e}_2|}

The coordinates to the front wheel contact points are then found by a dot
product with the lateral and longitudinal unit vectors in the ground plane

.. math::
   :label: eqFrontX

   q_8 = \hat{n}_1 \cdot \mathbf{r}^{m_{40}/n_o}

.. math::
   :label: eqFrontY

   q_9 = \hat{n}_2 \cdot \mathbf{r}^{m_{40}/n_o}

The lateral distance of the rider's knees to the bicycle frame are

.. math::
   :label: eqRightKnee

   q_{10} = \hat{b}_2 \cdot \mathbf{r}^{{m_3}/{n_o}} - \mathbf{r}^{m_{26}/n_o}

.. math::
   :label: eqLeftKnee

   q_{11} = \hat{b}_2 \cdot \mathbf{r}^{{m_7}/{n_o}} - \mathbf{r}^{m_{26}/n_o}

Simarly, the tail bone's lateral deviation from the bicycle frame is

.. math::
   :label: eqLatButt

   q_{12} = \hat{b}_2 \cdot \mathbf{r}^{{m_9}/{n_o}} - \mathbf{r}^{m_{26}/n_o}

I take the angle between a line running along the rider's back and the frame
plane to be a measure of rider lean, :ref:`Figure 10.18<figRiderLeanAngle>`.

.. _figRiderLeanAngle:

.. figure:: figures/motioncapture/rider-lean.*
   :width: 4in
   :align: center
   :target: _images/rider-lean.png

   A depiction of the rider lean angle. It is independent of the rider's
   forward lean and point 9 can be out of the plane of the bicycle. It is the
   angle of the back vector projected into a plane normal to the roll axis.

The rider's lean angle is then calculated by first finding the vector from the
butt to the upper back

.. math::
   :label: eqBackVector

   \mathbf{r}^{m_9/m_{11}} = \mathbf{r}^{m_{11}/n_o} - \mathbf{r}^{m_9/n_o}

projecting that vector into the plane normal to the roll axis

.. math::
   :label: eqBackProj

   \mathbf{v} = \frac{\mathbf{r}^{m_9/m_{11}} -
   (\mathbf{r}^{m_9/m_{11}} \cdot \hat{b}_1) \hat{b}_1}
   {|\mathbf{r}^{m_9/m_{11}} -
   (\mathbf{r}^{m_9/m_{11}} \cdot \hat{b}_1) \hat{b}_1|}

and finally calculating the angle between the projected vector and the lateral
symmetry plane

.. math::
   :label: eqLean

   q_{12} = -(\mathbf{v} \cdot b_2) \operatorname{arccos}\left(-\mathbf{v} \cdot b_3\right)

The twist is the angle of the rider is calculated by creating a vector from one
shoulder to the other

.. math::
   :label: eqShouldeVector

   \mathbf{r}^{m_{19}/m_{15}} = \mathbf{r}^{m_{15}/n_o} - \mathbf{r}^{m_{19}/n_o}

and projecting it into the plane normal to the back line

.. math::
   :label: eqShoulderProj

   \mathbf{w} = \frac{\mathbf{r}^{m_{19}/m_{15}} -
   (\mathbf{r}^{m_{19}/m_{15}} \cdot \mathbf{v}) \mathbf{v}}
   {|\mathbf{r}^{m_{19}/m_{15}} -
   (\mathbf{r}^{m_{19}/m_{15}} \cdot \mathbf{v}) \mathbf{v}|}

and finally computing the angle between it and a plane which is along the back
line and perpendicular to the bicycle lateral plane of symmetry

.. math::
   :label: eqTwist

   q_{14} = -\mathbf{w} \cdot (\mathbf{r}^{m_9/m_{11}} \times
   (\hat{b}_1 \times \mathbf{v})) \operatorname{arccos}(\mathbf{w}
   \cdot (\hat{b}_1 \times \mathbf{v}))

Results
-------

Direct examination of individual times series can be fruitful
:cite:`Doyle1987`, but it is hard to make generalizations that apply to more
that one specific case.  In our case, we have are nearly 3000 different time
histories to examine with the coordinates we've chosen. Examining the frequency
spectrum of each time history gives a different and sometimes more revealing
view. For the runs in which the rider pedals, the pedaling frequency is often
the dominant frequency, with little indication of other distinct frequencies
:cite:`Moore2009b`.

A better way to visualize how the coordinates change with speed, for example,
is to look at various statistics of the time histories. We grouped all of the
runs together for combined data sets at each speed of between 48,000 and 72,000
points, depending on how many repetitions of runs were performed (i.e. between
8 and 12). These were then plotted as separate box plots for each speed and for
each state. The box and whiskers charts plot a center line for the median of
the data, a box that bounds the 25% and 75% quartiles, whiskers that encompass
the data that falls within :math:`1.5\times(Q_{75}-Q_{25})` and crosses for
any outlier data points. Trends can be identified based on the spread and
median of the data at each speed. An offset median shows that the distribution
is skewed (e.g. steering more to the left than the right). The box and the
whiskers encompass the vast majority of the data. The whiskers can be used to
compare the coordinate excursions across speeds.

The yaw and steer plots show that the angles are small and tightly distributed
at high speeds, but that below 10 km/h the spread begins to grow. It is also
interesting that the yaw and steer graphs have very similar distributions. For
a bicycle without a rider, there is a simple linear kinematic relationship such
that yaw rate is only a function of steer rate and steer angle, which is the
likely reason for the similarity in steer and yaw. The spread of the roll angle
on the other hand stays fairly constant regardless of speed. The butt lateral
distance has somewhat constant distributions across speeds and it is also
apparent that the rider generally sits about one centimeter off the center
plane of the bicycle. The lateral knee distances are interesting in the fact
that spreads increase with lower speeds. We were able to visually detect large
knee movements in the video data at low speeds and hypothesized about the role
the knees could possibly play in control of the bicycle (:cite:`Kooijman2009a`,
:cite:`Moore2009b`). The rider lean angles are very small and do not show much
change with speed. This continues to support our hypotheses that riders do not
make use of leaning for control in normal bicycling. The rider twist angles
show a little more spread at low speeds. This could be tied to the fact that
you twist more when you steer more.

.. _figYawAngleNb:

.. figure:: figures/motioncapture/YawAngleNb.*
   :width: 3in
   :align: center
   :target: _images/YawAngleNb.png

   Box and whiskers plots of the yaw angle data from all riders and bicycles
   versus speed.

.. figure:: figures/motioncapture/RollAngleNb.*
   :width: 3in
   :align: center
   :target: _images/RollAngleNb.png

   Box and whiskers plots of the roll angle data from all riders and bicycles
   versus speed.

.. _figSteerAngleNb:

.. figure:: figures/motioncapture/SteerAngleNb.*
   :width: 3in
   :align: center
   :target: _images/SteerAngleNb.png

   Box and whiskers plots of the steer angle data from all riders and bicycles
   versus speed.

.. figure:: figures/motioncapture/RightKneeLateralDistanceNb.*
   :width: 3in
   :align: center
   :target: _images/RightKneeLateralDistanceNb.png

   Box and whiskers plots of the right knee lateral distance data from all
   rider and bicycles versus speed.

.. figure:: figures/motioncapture/LeftKneeLateralDistanceNb.*
   :width: 3in
   :align: center
   :target: _images/LeftKneeLateralDistanceNb.png

   Box and whiskers plots of the left knee lateral distancee data from all
   riders and bicycles versus speed.

.. figure:: figures/motioncapture/ButtLateralDistanceNb.*
   :width: 3in
   :align: center
   :target: _images/ButtLateralDistanceNb.png

   Box and whiskers plots of the butt lateral distance data from all riders and
   bicycles versus speed.

.. figure:: figures/motioncapture/LeanAngleNb.*
   :width: 3in
   :align: center
   :target: _images/LeanAngleNb.png

   Box and whiskers plots of the lean angle data from all riders and bicycles
   versus speed.

.. figure:: figures/motioncapture/TwistAngleNb.*
   :width: 3in
   :align: center
   :target: _images/TwistAngleNb.png

   Box and whiskers plots of the twist angle data from all riders and bicycles
   versus speed.

Conclusions
-----------

The box and whisker plots are a method of visualizing a more statistically
valid view of the kinematics of the bicycle and rider during stabilization
tasks. General trends in how states change with speed were shown and can be
utilized for rider bicycle dynamic and control model design. This is only one
of the first steps toward understanding how particular motions vary with speed,
maneuvers, bicycles, riders, and even the correlations among the motions. The
source code also computes statistics for the rates, accelerations, and
frequency content of the coordinates. The numerical values presented also
provide a framework for design of measurement techniques needed in experimental
studies.

Conclusions
===========

The PCA data decomposes the motion into a collection of linear motions, with
the dominant ones being exposed. We'd hoped that we would be able to apply a
second PCA in much the same fashion as :cite:`Troje2002` did with the walkers,
but bicycling doesn't produce clean periodic motion like walking does.
:cite:`Troje2002` was able to apply the second PCA across second independent
variables to characterize the change in motion with respect to the variables.
We are most interested in dynamical changes with respect to speed for the
bicycle-rider system, but also in how different bicycle designs affect the
control and dynamics. Our attempt at tracking how the principal components
changed with respect to speed, was somewhat flawed due to the difficulty in
matching components from run to run. It correctly shows the increased motions
at low speeds, but the information from the principal components became less
and less relevant as we continued to work with it. This is what led me to
transform the marker data into more concrete coordinates that have more meaning
and connection to the kinematics we typically examine in the bicycle-rider
system. I think the data set can provide some more concrete conclusions about
how we balance a bicycle. Another thing that I thought about pursuing was
making use of scaling with respect to mass in the principal component analysis.
It is possible to applying weighting to the coordinates such that the principal
components can be formulated with respect to a momentum-like quantity. This
could reveal the motions that effect the dynamics rather than simply the
primary kinematics.
