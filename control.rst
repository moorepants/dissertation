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

You can control a bicycle in a million ways. If you believ the system is of
certain order, then a variety of control structures can place the poles into
the same place. But not all gains may be needed to make the bicycle stable and
perfrom well. Human probably choose a robust system vs a high performance
system.

There are thes control catergories: let's stablize and control the bicycle with
any means possible or lets limit the controller to how the human can actually
sense and actuate. Then there are the ones in the middle. There are models and
then people who try to actually balance a robotic device.

There is a mean human controller for tight tasks. For loose tasks, it is more
ambigous.

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
tracked itself using a lateral deviation at a preview time and roll angle
feedback and a simple bicycle dynamical model with good agreement bewteen
experiment and the model predictions, with the expection of countersteer
predictions. [Forouhar1992]_ studied the robust stabilization of the wobble
mode in motorcycles. [Getz1994]_ uses a simple bicylce model that exhibit
non-minimum phase behavior and tracks roll angle and forward velocity using
proportional and derivative control. One year later, Getz adds pathing tracking
to his model ([Getz1995]_, [Getz1995a]_). [Kageyama1996]_ uses a neural network
model to balance a two wheeled vehicle. [Cloyd1996]_ use the same simple
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

.. todo:: talk about learned control, unconscious vs conscious, upper cortex

van Lunteren and Stassen did some the earliest work on the subject. They were
primarily interested in identifying the human control system in the bicycle
riding task. Their studies spanned several years in the late 60s and early 70s.
[Lunteren1967]_, [Lunteren1969]_, [Lunteren1970]_, [Lunteren1970a]_,
[Stassen1973]_, [Lunteren1973]_ uses a bicycle roll angle feedback with PID
control that drives the rider's lean angle and steer angle. The bicycle model
they employ is is quite simple (it models their simulator more than a real
bicycle) and does not exhibit coupling in steer and roll. The model also has
steer and lean angle input as opposed to input torques. They also mention that
the control structure was chosen because of equipment limitations and cite
recent manual control models [McRuerXXXX]_ as being probably being preferable.
None-the-less the studies were before their time and quite impressive. They
concluded that roll angle control was more reflexive and that the steer angle
control was more cerebral based on identified time delays. [Lange2011]_
develops a more up-to-date model with the same type of structure as van
Lunteren and Stassen, where he feeds back roll angle and steer angle, and
drives steer torque with PID controllers. He also points out a sign error in
van Lunteren and Stassen's work.

Weir worked with McRuer on some manual control papers prior to his PhD thesis
[Weir1972]_, where he employed a crossover model along side a motorcycle model
which is based on Sharp's early motorcycle model [Sharp1971]_ to evaluate the
controller used by humans. This is the most likely the first complete attempt
at analyzing the rider-motorcycle control system. Weir determined that roll
angle feedback combined with a basic human model and a simple gain controlling
steer torque was the most effective control mechanism. In particular, he showed
how steer angle control was poor and he even examined rider lean angle control
using a pseudo rider lean model similar to [Hess2012]_. Rider lean could
succesfully control the system, but required large lean angles. He also worked
with mutliple loop closures and found that roll angle fed back to control steer
torque with heading and lateral deviation fed back to control rider lean angle
presented the best control strategy for the human rider. He only did his
studies at a single high speed with a motorcycle model which only required
stablization of the capsize mode. It is highly likely that these control
strategies could vary with speed, especially at low speed where the weave mode
is the dominant instability. Weir and Zellner went on to complete several more
important studies involing manual control of the motorcycle [Weir1978]_,
[Weir1979]_, including a detailed technical report for the U.S. Department of
Transportation [Weir1979a]_ in which much experimental work was done verifying
their mathematical models.

.. todo:: There are some other Weir papers I could cite, and I should look over
   Weir1979a again to get the main conclusions.

A recently uncovered study by Doyle ([Doyle1987]_, [Doyle1988]_), thanks to
Google's book scanning endeavors and Jim's persistance in searching, presents a
slow speed view for bicylce control in much contrast to the Weir studies, not
only because of the speed and vehicle differences, but because it is from the
view of a psychologist. We engineeres are quick to model the human sensory and
actuation system, with little understanding of the intricucies of the human
brain. Doyle's treatise gives a refreshing look from outside the engineering
box. Doyle's control model is fundamentally a sequential loop closure with the
inner most loop being roll control and the outer two being heading and path
deviation. He says that the outer loops are highly dependent on the inner loop.
For the inner loop he determines that continously feeding back both roll
accleration with integral and proportional gains adjusted by the human as the
crossover model dictates will stabilize the bicycle at non intended roll
angles. To control roll angle, he claims that we do not do this in a continous
but that we apply discrete pulses when the roll angle meets a threshhold. This
model has similar form to the one developed by us in the next section.

.. todo:: Cerebellum is the lower brain (learend control). High cortical
   regions and outer cortex is the higher brain. Under-conscious control or sub
   conscious.

I'll mention briefly some about modeling the human with fuzzy control. I have
little understanding of fuzzy control but [Cloud1994]_ says that fuzzy control
methodologies fundamentally let one translate linguistic rules from a an expert
in controlling the particular system into a control logic algorthm. This seems
like it may certainly be valualbe for conscius control efforts, but may have
definicies when trying to determine the control stragetly of unconscious
control. But a conbimnation of fuzzy logic and crossover type control may prove
useful in describing the human control system. Liu and Wu have done extensive
work applying fuzzy control to single track vehicles ([Liu1994]_, [Wu1994]_,
[Wu1995]_, [Wu1996]_, [Wu1996a]_, [Wu1996b]_, [Wu1996c]_).

.. todo:: Read some of the Wu and Liu stuff and say something about it.

More recently, [Lange2011]_ wrote his master's thesis on identifying the human
controller in the bicycle-rider system. He employed a controller which fed back
roll angle and steer angle with PID plus second derivative control and time
delays to command a neurmuscular model which in turn commanded steer torque of
the Whipple model. The model is similar in flavor to van Lunteren and Stassens,
but more up-to-date and uses more feedback loops. He chose eight gains plus
time delays and attempted to identify which loops were not important from our
experimental data. He finds that the critical feedback variables for a stable
model were roll angle, roll rate, steering rate and the integral of the steer
angle, claiming the last one in is proportional to heading thus controlling
heading with steer. He also finds the time delays to be stabilizing and removes
them.

Finally, we've developed a control model with Ron Hess [Hess2012]_ that is used
later this dissertation for human operator identification. The following
section gives a brief synopsis, but one should refer to the published paper for
more detail.

Hess Manual Control Model
=========================

Many control model architectures can be used to attempt to identify the human
control system while riding the bicycle. We are only limited by the type of
sensory information a human rider can sense and the actuation means. The human
operator has been modeled with simple models like the crossover model, to more
complex neuromuscular dynamics and even fuzzy and optimal control. Some of the
controllers are essentially equivalent placing the closed loop poles in the
same place, but make use of different techniques to get to the end result. The
models may also be different in complexity. In general finding the simplest
mathematical model capable of capturing the dynamics one is interested is a
good goal. With this in mind, my advisor Ron Hess developed a controller based
on the Whipple bicycle model and his previous successful human operator models.
We present the control model and the loop closure procedure for selecting the
five model gains in [Hess2012]_. This model is fundamentally similar in nature
to Weir's work and has the same roots through the work of McRuer. We similarly
found steer angle based control to be troublesome and had success across a
broad range of speeds and selection of bicycles with steer torque control. We
also employed a similar method of evaluating rider lean control with
introducing an extra degree of freedom. It also has semblance to the work of
[Doyle1987]_ with the inner loop structure dedicated to roll stablization and
the outer loops to high congintive control in heading and path tracking.

Basics of manual control theory
-------------------------------

Manual control, or human operator control, was primarily bithed from control
engineers after world war two. The requirements for machine designs in which
humans were the principal control element, such as artillery guns and aricraft,
led to human control modeling. Theorecital work by [Tustin1947]_ theorized
early on that a human control systems could be modeled simlirly to automatic
feedback systems. This was followed by experimentl work by [McRuer1965]_ mostly
confirming these hypotheses.

It turns out that humans adjust their control such that the combine human and
plant dynamics behave with desireable closed loop dynamics. This phenomena can
be captured by a variety of theorectical control structures from simple
dynamics to complex neuromuscular models [Hess1997]_. Fortunately, the simple
models can capture much of the dynamics in systems such our bicycle-rider
system. Here after we make use of the crossover model [McRuer1974]_. The reason
for this is multi-fold. It allows us to stick with a simple system which has
been applied to numerous man-machine systems with good results.

compensatory: controller uses the error only to make control
pursuit: both error and input information is available for the controller

.. todo:: read Ron's work on manual control again and write a summary here.

Jim - Isn't it true that the crossover model is only a representation of human
behavior near the limit of performance?

Ron - I can describe the dynamics of the human at various "crossover" frequencies
 and various performance levels.  It's true, that it has been verified in many
 laboratory and vehicle control tasks were good performance was required.

Model Description 
-----------------

The multiloop model we use is constructed with a sequential loop closure
technique that sets the model up to follow the dictates of the crossover model.
The three inner loops manage the roll stablization task and the outer two loops
manage the path following. We include a simple model of the humans
neuromuscular dynamics which produces a steer torque from the steer angle
error.

.. math::
   :label: eqNeuromuscular

   G_{nm} = \frac{\omega_{nm}^2}{s^2 + 2\zeta_{nm}\omega_{nm}s + \omega_{nm}}

The neuromuscular parameters, :math:`\zeta_{nm},\omega_{nm}`, were chosen to
such that the innermost loop gave a typical response for a human operator.

The bicycle is modeled using the Whipple model linearized about the nominal
configuration with the primary control input being steer torque. The inner
loops are closed with sequential gains starting with the proprioceptive steer
angle loop, followed by the vestibular roll rate loop and the visual roll angle
loop [#]_, Figure :ref:`figInnerLoops`. The steer angle loop in essense
captures the force/feel or haptic feedback we use while interacting with the
handlebars. The need for this loop is readily apparent when trying to control a
bicycle simulation with a joystick or steering wheel with no haptic feedback as
demonstrated in [Lange2011]_; the difficultly level is high without it. The
outer loops are also visual, heading and lateral path deviation, Figure
:ref:`figOuterLoops`.

.. _figInnerLoops:

.. figure:: figures/control/inner-loops.png
   :width: 5in

   figInnerLoops

   The inner loop structure of the control system.

.. _figOuterLoops:

.. figure:: figures/control/outer-loops.png
   :width: 4in

   figOuterLoops

   The outer loop structure of the control system with the inner loops closed.

The control structure is simply a function of five gains, which the human
adjusts under the dictates of the crossover model to get good overall system
performance. The two inner most loop gains are chosen such that all of the
oscillatory roots of the closed loop have at least a 0.15 damping ratio.
Whereas the three outer loop gains are chosen such that the open loop crossover
frequencies are half the previous.

Traditionally, sequential loop closure methods are performed on a case by case
basis and involve some subjectiveness in applying the rules of thumb. This is
time consuming and error prone when you have to find the gains for many systems
as in our bicycles and riders at various speeds. We automated the technique
described in [Hess2012]_ can be automated to alleviate this.

The closed roll angle loop should be stable, as stability in roll is critical
for the path tracking in the outer two loops. To get there, the closure of the
proprioceptive and vestibular loops must push the poles to a favorable spot for
application of the crossover model on the roll angle loop. To do this, the
first two loop closure require that all of the oscialltory modes have a minimum
damping ratio of 0.15. We first use the proprioceptive gain, :math:`k_\delta`
to push the poles orginating at the bicycle weave eigenvalue to a higher
frequency with 0.15 damping. The closed loop transfer function for the steer
loop is

.. math::
   :label: eqDeltaLoop

   G_{\delta c} = \frac{\delta}{\delta_c} =
   \frac{ G_{\delta o}}{1 + G_{\delta o}}

   G_{\delta o} = k_\delta G_{nm} \left(\frac{\delta}{T_\delta}]\right)_b

To set the damping ratio multiple approaches can be take, here I'll show a Bode
design and a root locus based design. For the Bode design, this can be enforced
by finding the gain such that the dominant pole has a 10db peak. This dominant
pole is the neuromuscular mode created when combing the neuromuscular model
with the bicycle plant. For this bicycle and speed, a gain of ~45.9 will set
the inner loop as desired.

.. _figDeltaBode:

.. figure:: figures/control/delta-bode.*
   :width: 4in

   figDeltaBode

   The Bode plots of the closed steer loop with various gains. Notice how the
   higher gains push the neuromuscular peak to a frequency typical of human
   operator and plant dynamics [Hess2012]_.

By plotting the damping ratio of the closed loop poles as a function of
:math:`k_\delta` the desired gain can also easily be picked off on a root locus
diagram. The bicycle-rider system is similar enough in nature for speeds above
2 m/s that this always works. [Lange2011]_ reported difficulties stabilizing
his system below about 2 m/s too. We've found that relaxing the 10db peak
requirement such that the neuromuscular mode is more damped, will allow for
successive closure and a stable system for lower speeds. But as we all know,
the bicycle is very difficult for a human to balance at extremely low speeds.
The fast time constants compounded with human neuro processing delays makes
this true. There are even slow bicycle competitions that take advantage of this
fact to test the balancing skill of the rider.

.. _figDeltaLocus:

.. figure:: figures/control/delta-locus.*
   :width: 4in

   figDeltaLocus

   The root locus of the closed delta loop poles.

The root locus of the closed delta loop poles as a function of :math:`k_\delta`
gives an idea where we can push the poles for the next loop closure. Notice
that the poles associated with the weave mode at :math:`k_\delta=0` are pushed
into the stable regime and back out, crossing the 0.15 damping ratio line
twice. There is a range of gains between about 3.1 and 44.0 which cause all of
the oscillatory modes to have at least 0.15 damping ratio. This is very clear
when plotting the damping ratio versus gain in Figure :ref:`figDeltaDamp`.  The
best choice is typically to set the gain such that the pole is at the highest
frequency allowable with minimum damping, to give typical human operator
behavior. This will set up the bandwith of the sub sequent loops to be high
enough for good system performance.

.. _figDeltaDamp:

.. figure:: figures/control/delta-damp.*
   :width: 4in

   figDeltaDamp

   The damping ratio of the poles as a function of gain. Note that there are
   gains such that all the roots are stable and the damping ratio is at least
   0.15, although inner loop stability is not a requirement for total system
   stability.

The roll rate loop closure is trickier to set. We want to maintain the 10db
peaking on the neuromuscular mode that we just set, but select a roll rate gain
such that any other new oscillatory mode also have a minimum damping ratio of
0.15, but from Figure :ref:`figPhiDotDamp` we see that we are already in good
shape. Since the bicycle with steer control exhibits non-minimum behavior, we
need to introduce a positive feedback on roll rate. So it turns out that with
a slight negative gain we can maintain the neuromuscular mode behavior but
introduce the require sign change for stability.

.. math::
   :label: eqPhiDotLoop

   G_{\dot{\phi} c} = \frac{\dot{\phi}}{\dot{\phi}_c} =
   \frac{G_{\dot{\phi} o}}{1 + G_{\dot{\phi} o}}

   G_{\dot{\phi} o} = k_\dot{\phi} k_\delta G_{nm} \left(\frac{\dot{\phi}}{T_\delta}\right)_b
   [1 - G_{\delta c}]

.. figure:: figures/control/phiDot-damp.*
   :width: 4in

   figPhiDotDamp

   The damping ratio of all roots to the closed loop roll rate loop as a
   function of gain.

.. todo:: I don't know how to explain the choice in gain for the roll rate loop
   in terms of the Bode diagram. Some help please!

.. figure:: figures/control/phiDot-bode.*
   :width: 4in

   The closed loop Bode plot of the roll rate loop. The neuromuscular mode
   peaks with a 10db magnitude.

With the roll rate loop closed, the final three loops can be closed by setting
the gain such that the crossover frequency of the roll most loop is 2 rad/s
and the outer loops crossover at half the previous frequency. This is easily
set by measuring the gain of transfer function at the desired crossover
frequency and realizing that a unit change in gain will raise or lower the gain
curve.

.. math::
   :label: eqPhiLoop

   G_{\phi c} = \frac{\phi}{\phi_c} =
   \frac{G_{\phi o}}{1 + G_{\phi o}}

   G_{\phi o} = k_\phi k_\dot{\phi} k_\delta G_{nm}
   \left(\frac{\phi}{T_\delta}\right)_b
   [1 - G_{\dot{\phi} c}] [1 - G_{\delta c}]

.. math::
   :label: eqKPhi

   k_\phi = \frac{1}{|G_{\phi o}(2j)|}

.. _figPhiBode:

.. figure:: figures/control/phi-bode.*

   figPhiBode

   The open loop frequency response for the roll angle loop. Blue is gain of
   unity and the green line is uses the gain to give desired crossover.

.. math::
   :label: eqPsiLoop

   G_{\psi c} = \frac{\psi}{\psi_c} =
   \frac{G_{\psi o}}{1 + G_{\psi o}}

   G_{\psi o} = k_\psi k_\phi k_\dot{\phi} k_\delta G_{nm}
   \left(\frac{\psi}{T_\delta}\right)_b
   [1 - G_{\phi c}] [1 - G_{\dot{\phi} c}] [1 - G_{\delta c}]

.. math::
   :label: eqKPsi

   k_\psi = \frac{1}{|G_{\psi o}(1j)|}

.. _figPsiBode:

.. figure:: figures/control/psi-bode.*

   figPsiBode

   The open loop frequency response for the yaw angle loop. Blue is gain of
   unity and the green line is uses the gain to give desired crossover.

.. math::
   :label: eqYqLoop

   G_{y_q c} = \frac{y_q}{{y_q}_c} =
   \frac{G_{y_q o}}{1 + G_{y_q o}}

   G_{y_q o} = k_{y_q} k_\psi k_\phi k_\dot{\phi} k_\delta G_{nm}
   \left(\frac{y_q}{T_\delta}\right)_b
   [1 - G_{\psi c}] [1 - G_{\phi c}] [1 - G_{\dot{\phi} c}] [1 - G_{\delta c}]

.. math::
   :label: eqKYq

   k_{y_q} = \frac{1}{|G_{y_q o}(0.5j)|}

.. _figYqBode:

.. figure:: figures/control/yq-bode.*

   figYqBode

   The open loop frequency response for the front wheel lateral deviation loop.
   Blue is gain of unity and the green line is uses the gain to give desired
   crossover.

The gains can be computed across a relevant speed range for the bicycle. Figure
:ref:`figGains` shows how the gains vary with respect to speed for a particular
bicycle and rider. Notice that at higher speeds the gains change linearly, but
at speeds below 3 m/s there is non-linear variation. These gains give a stable
system which is capable of the lane change manuever, but due to the
difficulties in selecting the gains with rules above the algorthm may be making
poor choices, especially for :math:`k_\dot{\phi}`.

.. _figGains:

.. figure:: figures/control/gains.*
   :width: 3in

   figGains

   The auto computed gains as a function of speed for the Davis instrumented
   biycle with Jason as the rider.

We automated this method based on the Bode design guidelines. The gain choices
for proper neuromuscular peaks in the inner most loops require good initial
guesses, as there is often multiple solutions. The correct solution puts the
neuromusclar natural frequency at a typical value for human operators.

Software
--------

I designed a software suite in Matlab to implement the automated gain selected
for various bicycles, riders, and speeds. The software was constructed around a
simulink model of the model describe above and offers this functionality:

#. It generates the state space form of the linear Whipple model for any
parameter sets and speeds. The outputs include all eight of the configuration
variables and their derivatives reported in Chapter :ref:`eom` with the
addition of the front contact point. This includes the lateral force input
described in Chapter :ref:`extensions`.

#. It generates the state space form of the closed loops system as a function
of the bicycle-rider parameters, the speed, the five gains and the
neuromuscular frequency.

#. It computes the gains with the sequential loop closure guidelines described
above for any give bicycle-rider and speed. (Very low speeds may require some
hand modification.) The open and closed loop transfer functions for each loop
can be returned and or plotted. It can also do this for roll torque as the
input as described in [Hess2012]_.

#. It simulates the system performing a single or double lane change with a
given or computed set of gains and plots the results.

#. It computes the lateral force input transfer functions.

#. It computes the handling quality metric described in [Hess2012]_.

#. It plots the gains versus speed.

The software was used to generate most of the results and plots in [Hess2012]_
and the source code for doing so is included.

Notation
========

:math:`T_\delta`
   Steer torque.
:math:`T_\phi`
   Roll torque.
:math:`x_p,y_p`
   Rear wheel contact point.
:math:`x_q,y_q`
   Front wheel contact point.
:math:`\psi`
   Yaw angle.
:math:`\phi`
   Roll angle.
:math:`\delta`
   Steer angle.
:math:`G_{nm}`
   Human neuromuscular transfer function.
:math:`G_{xo}`
   The open loop transfer function of loop :math:`x`.
:math:`G_{xc}`
   The closed loop transfer function of loop :math:`x`.

.. rubric:: Footnotes

.. [#] [Doyle1988]_ notes that his riders can balance even while blindfolded.
   This is even true for people who've been blind since birth. So the roll
   angle dectection, must not necessarily be all visual based.
