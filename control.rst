.. _control:

=======
Control
=======

.. warning::

   This document is a draft which is updated regularly (Last updated |today|).
   Once I submit if for my doctoral degree at UC Davis, it will be done. So for
   now use at your own risk. The information may or may not be correct.
   Reviews, comments and suggestions are welcome.

Introduction
============

I have shown that a basic bicycle model can demonstrate stability when
linearized about the nominal configuration for ranges of speeds. This stablity
is a strong function of the parameters of the bicycle and it turns out that for
general bicycle designs, they exhibit stability. I've also shown that stability
can be enhanced or defeated by extending the Whipple model with things such as
the a flywheel or rider degrees of freedom. I've also examined the kinematics
of the rider to see if the rider attempts to control the bicycle at the
eigenfrequencies of the Whipple model, and this doesn't seem to be the case. As
far as roll stability is concerned, it is highly probable that a human must
enact active control at all times while balancing a bicycle, but the stablity
exhibited by the Whipple model may allieviate the control needed by the rider.
enact active control at all times while balancing a bicycle. One hypothesis is
that the stablity exhibited by the Whipple model may allieviate the rider from
having to control the bicycle. And even if the bicycle is unstable at a given
speed, the question arise of *how* instable or *how* controllable is the
bicycle. Classic controlability and observability simply tests whether or not
it is possible for a system to be controlled, whereas the difficultly of these
two may be more relevant to the human controller. [Seffen2001]_ studies how
parameter changes affect controlability. [Schwab2010a]_ touches on
controlability of severl bicycle models and uses the eigenmode rate magnitude
to try to look at how controllable the system is. The damping ratio and natural
frequency of the mode can also give a general sense of how easy it can be to
control.

The bicycle presents both theorectical and experimentally rich dynamical system
for control studies. This tends to be framed in two different ways certainly
with overlap. The first is simply controlling the bicycle with general types of
controllers and mechanisims which invloves simple stablization to path
tracking. The second way is trying to control the bicycle as a human does,
limiting sensory input and actuation to the human system. The motivation ranges
from desire for automatic control, improving simulation for vehicle design,
handling qualities enquires, control system testing, ....


Pure stabilization (eyes closed, big open flat area).

General Single Track Vehicle Control Models
===========================================

Many authors have controlled the bicycle with various schemes ranging from
optimal control to H inifitiy. Some models are concerned only with balancing
the bicycle (roll control) and others are concerned with tracking either
heading and lateral deviation.

[Zytveld1975]_ was one of the first to explore the automatic stablization of
the bicycle outside of a human control framework, although he did chosen
feedback variables that he believe a human rider could sense. He attempted to
control a robot bicycle with a leaning rider (no steer control) through
proportional and derivative feedback of rider lean angle and bicycle roll
angle. His controller worked on paper, but he wasn't able to get the robot
bicylce working. [Nagai1983]_ constructed a robot bicycle which balanced and
trackeditself using a lateral deviation at a preview time and roll angle
feedback and a simple bicycle dynamical model  with good agreement bewteen
experiment and the model predictions, with the expection of countersteer
predictions. [Forouhar1992]_ studied the robust stabilization of the wobble
mode in motorcycles. [Getz1994]_ uses a simple bicylce model that exhibit
non-minimum phase behavior and tracks roll angle and forward velocity using
proportional and derivative control. One year later, Getz adds pathing tracking
to his model ([Getz1995]_, [Getz1995a]_). [Kageyama1996]_ uses a neural network
model to balance a tow wheeled vehicle. [Cloyd1996]_ use the same simple
bicycle model as [Nagai1983]_, but control it with a linear quadratic
regulator. [Yavin1997]_ studies path tracking of a simpel bicyle model.
[Berriah1999]_ remote control a bicycle robot. [Gallaspy200]_ designed a robot
balancing bicycle which uses a gimabled gyroscope to apply a restoring torque
to the sensed lean angle, but was not successful at balancing the real robot.
[Suryanarayanan2002]_ uses a simple bicycle model to build a roll rate feedback
controller for high speed recumbent bicycle. They use proportional feedback on
the steer angle for a front steered bicycle. [Lee2002]_ mass balancer.
[Tanaka2004]_. [Yamakita2005]_ has robot bicycle. [Mammar2005]_ uses H
inifinity. [Iuchi2005]_. [Huyge2005]_. [Astrom2005]_ proportional lean angle to
steer torque. [Yamakita2006]_. [Sharma2006]_ fuzzy control. [Saccon2006]_ some
kind of controller for a simulator or something. [Micchini2006]_ the MIT bike?
[Limebeer2006]_ implements a control model. [Liang2006]_ fuzzy. [Findlay2006]_
the model we did for Joshi's class. [Bjermeland2006]_ a masters these on
controlling a bicycle, I don't have it. [Shaprp2007a]_, [Sharp2007]_, and
[Sharp2008a]_ presents optimal control methods with detailed preview models for
motorcycle and bicycle control. He exploress both steer torque and rider lean
torque control, comparing the effectiveness of both. [Murayama2007}_ robot
balancer.  [Marumo2007]_ steer by wire of motorcycle. [Chidzonga2007]_.
[Baslamisli2007]_ gain scheduled steering control. [Thanh2008]_ particle swarm
bicycle robo balancing. [Peterson2008a]_ yaw rate and velocity tracking with
rider lean torque. [Keo2008]_ trajectory control for auto bicycle with
balancer.  [Connors2009]_ LQR control recumbent leg masses. [Tanaka2009]_
tracking and posture control electric bicycle.  [MurataBoy]_ gyro balancing
bicycle.  [Baslamisli2009]_ gain scheduling.  [Cerone2010]_. [Keo2011]_.

.. todo:: Kondo may be good to cite, but I haven't none of the papers.

.. todo:: Does Cangley have a control model?

Single Track Vehicle Human Operator Control Models
==================================================

There are very fewer studies focusing on human control of a bicycle or
motorcycle with the intent of identifying the human controller or controlling
the vehicle with a human-like controller.

van Lunteren and Stassen did some the earliest work on the subject. They were
primarily interested in identifying the human control system in the bicycle
riding task. Their studies spanned several years in the late 60s and early 70s.
[Lunteren1967]_, [Lunteren1969]_, [Lunteren1970]_, [Lunteren1970a]_,
[Stassen1973]_, [Lunteren1973]_ uses a
bicycle roll angle feedback with PID control that drives the rider's lean angle
and steer angle. The bicycle model they employ is is quite simple and does not
exhibit coupling in steer and roll. The model also has steer and lean angle
input as opposed to input torques. They also mention that the control structure
was chosen because of equipment limitations and cite recent manual control
models [McRuierXXXX]_ as being probably being preferable.  None-the-less the
studies were before their time and quite impressive. They concluded that roll
angle control was more reflexive and that the steer angle control was more
cerebral based on identified time delays.

, Weir, Doyle
[Liu1993]_ used fuzzy control
[Wu1994]_
[Cloud1994]_ fuzzy control kids
[Wu1995]_

[Lange2011]_
Lots of Wu articles.
[Hess2012]_

Our manual control model
========================

Basics of manual control theory
-------------------------------

Isn't it true that the crossover model is only a representation of human behavior near the limit of performance?

 I can describe the dynamics of the human at various "crossover" frequencies
 and various performance levels.  It's true, that it has been verified in many
 laboratory and vehicle control tasks were good performance was required.

Model Description
-----------------

- Cite the journal paper.
- Model block diagram
- Basic model description
- Automation of the loop closure
- Software

Plots
-----
- plots of the gains versus speed
- Single and double lane change
- Lateral disturbance
