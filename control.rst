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

I have shown that a basic bicycle model can exhibit stability when linearized
about the nominal configuration for a range of speeds, Chapter :ref:`eom`.
Stability is a strong function of the parameters of the bicycle and it turns
out that for standard bicycle designs, they typically exhibit a speed dependent
stability where the bicycle becomes stable at some speed threshold, Chapter
:ref:`parameterstudy`. Based on the damping of the weave mode, one may also
even claim that the bicycle becomes  *more* stable as speed increases,
neglecting the very slow capsize instability. I've also shown that stability
can be enhanced or defeated by extending the Whipple model with a flywheel or
rider degrees of freedom, Chapter :ref:`extensions`. In Chapter
:ref:`motioncapture`, I've examined the kinematics of the rider to see if the
rider's motion during a control task has any correlation to the kinematics of
the Whipple model and identified the dominant rider motions during
stabilization.

As far as roll stability is concerned, it is highly probable that a human must
enact active control at *all* times while balancing. I reason this, because
posture control directly affects the bicycle's roll angle. But the stability
exhibited of the almost always present weave mode may alleviate the need for
primary roll control provided by the rider. And even if the bicycle-rider
system is open loop unstable at a given speed, the question arises of *how*
instable is it or *how* controllable is it. Classic controllability is simply a
binary test to determine whether or not it is possible for a system to be
controlled, whereas there must be some measure variable measure of
controllability that is more relevant to the proposed questions. [Seffen2001]_
studies how parameter changes affect controllability, and concludes XXX.
[Schwab2010a]_ also determines the controllability of several bicycle models
and uses the eigenmode rate magnitude as an example variable measure of the
controllability. The pole locations of an open loop system can also give a
general sense of how easy it can be to control with roots in the far right
plane likely being hard to stabilize.

One can work with different bicycle models (simple/complex [or low/high order]
and linear/non-linear), different control structures and different ways to
identify the optimal numerical values for the controller. For a given order
model most good controllers can place the closed loop poles in the same place
regardless of the control structure. Controllers designed for low order or
linear models are even likely to work with higher order models and non-linear
models.  But depending on the controller structure they can provide more or
less physical insight to the control happening, in particular what a human
might be doing. The human most likely choses robustness over performance.
...Expand this.

The bicycle-rider system presents both a theoretical and experimentally rich
dynamical system for control studies. It is very tractable in the sense that
most people are familiar with controlling a bicycle and that it is a *simple*
machine which is readily available for experimental use. And thirdly, control
of the bicycle is not necessarily trivial due to it's complex dynamics and
provides a platform for testing many strategies. Past control studies tend to
be framed in two different but overlapping frameworks. The first is to simply
control a bicycle (model or real) with any control algorithms and mechanisms
available. Both the simple roll stabilization task and more complex path
tracking tasks have been examined. The results show that bicycles are readily
controllable by a variety of means, from a simple steer in the direction of the
rate of fall to full state feedback with preview of future path variations.
Depending on the sensing and actuation methods chosen these controllers range
in their resemblance to how a human may actually control a bicycle. This leads
into a second framework in which the researcher is explicitly trying to
determine the how a human balances and controls a bicycle.  Basic understanding
of the limited sensory input and actuation available to a human give
constraints on what control structures are adopted. Both frameworks are
motivated by many things such as desire for to implement automatic control,
improving simulation for vehicle design, handling qualities inquiries, control
system testing, etc.

My intention of the work presented in this dissertation falls in the second
framework, where we are most concerned with  identifying the human controller.

Single Track Vehicle Control Models
===================================

Once you dig around in the literature enough you will find many studies on the
control of a bicycle. I've split the review of control models into three
sections. The first are about controllers which have actually be implemented on
robotic bicycles. The second are theoretic controllers that weren't
necessarily introduced to identify the human control system and the final
section details efforts that explicitly work with controllers that mimic the
human controller.

Bicycle Robots
--------------

[Zytveld1975]_
   van Zytveld was one of the first to explore the automatic stabilization of the
   bicycle that was not explicitly in the human control framework, although he
   did chose feedback variables that he believed a human rider could sense. He
   attempted to control a robot bicycle with only a leaning rider (inverted
   pendulum) through proportional and derivative feedback of rider lean angle
   and bicycle roll angle. He made use of a linear model with a rider lean
   degree of freedom which was the same as the one presented Chapter
   :ref:`extensions`.  His controller worked on paper, but he wasn't able to
   ever balance the robot bicycle, with the suspected problems being the
   limitations of the hardware he used.
[Nagai1983]_
   They constructed a robot bicycle which balanced and tracked itself by
   feeding back lateral deviation at a previewed time and the current roll
   angle. He was successful at stabilizing his robot. His bicycle model was
   much simpler than the Whipple model but he found good agreement between
   experiment and the model predictions, with the exception of counter-steer
   predictions.
[Beznos1998]_
   Find and read.
[Berriah1999]_
   They developed a digital fuzzy controller to stabilize a remote controlled
   bicycle robot. They do not seem to demonstrate the robot actually balancing
   but only bench tests of the sensors and actuators.
[Gallaspy2000]_
   He designed a robot balancing bicycle which controls a gimbaled gyroscope to
   apply a restoring torque with respect to the sensed roll angle, but was not
   successful at balancing the real robot.
[Sooraksa2000]_, [Sooraksa2000a]_
   Read
[Muraoka2002]_
   bicycle robot (MS thesis in Japanese).
[Oda2002]_
   I do not have this paper, Google doesn't give any hits.
[Miyagishi2003]_
   This is the same Kageyama Honda robot, they say that the model the
   controller after a human.
[Kageyama2004]_
   Motorcycle robot with Honda (need to find this paper!). Probably in
   Japanese. He's got a bunch of papers that I don't have.
[Tanaka2004]_
   They successfully balances a bicycle on rollers with a PD roll angle to
   steer angle controller with a disturbance observer.
[Muhich2004]_
   graduate project or something, read
[Iuchi2005]_
   They use PD control on the bicycle roll angle to control steer angle and
   rider lean angle. The controller is implemented on a bicycle robot, of which
   they are able to balance on rollers.
[Iuchi2006]_
   They use the same model base as [Iuchi2005]_ except they now add in a human
   torque estimator, so that the controller will not treat the human's steer
   torque as a disturbance if the controller is activated while a rider is also
   trying to control the bicycle. They show some crude experimental results, of
   which I assume are of a rider controlling the bicycle with and without the
   automatic controller activated. Their human torque accounting is based off
   of a estimation of the human torque from the steer motor torque, rather than
   explicitly measuring the human's torque input.
[Miyagishi2006]_
   Another one on the Honda robot, but probably in Japanese.
[Yamakita2006]_
   implements a modified controller from the one presented in [Yamakita2005]_
   with an additional :math:`H_\inf` controller. They show some successful roll
   stabilization of a robot scooter in which they only implement the roll
   stabilization control.
[Micchini2006]_
   constructed a robot bicycle (I've asked him for more info on this one).
[Suprapto2006]_
   Find and read.
[Taura2007]_
   master's thesis on acrobatic bike robot..maybe a wheely (need to find this
   one). Probably in Japanese.
[Murayama2007]_
   uses the same vehicle and control model as in [Yamakita2006]_ and a new two
   degree of freedom "rider" pendulum. They demonstrate roll stability of the
   robot at both zero forward speed up to 2 m/s.
[Solveberg2007]_
   Read. MS thesis on controlling a bicycle robot.
[Thanh2008]_
   Thanh designs a controller with :math:`H_2/H_\inf` techniques and applies it
   to a bicycle robot which uses a flywheel for stabilization. He compares it
   to a PD controller and a genetic algorithm and shows that it is more robust.
[Tanaka2009]_
   tracking and posture control electric bicycle
[Mutsaerts2010]_
   designed a Lego NXT bicycle robot with a simple proportional steer into the
   direction of roll rate controller and `demonstrates
   <http://youtu.be/VxiOy4QzD7I>`_ the bicycle roll stability in crude turns
   and straight ahead running.
[Brekke2010]_
   Read. MS thesis on controlling a bicycle robot.
[Cerone2010]_
   Read
[Keo2011]_
   Read
[Murata2011]_
   The Murata Manufacturing company designed a bicycle robot to demonstrate the
   utility of their sensors which debuted sometime in 2006 [Murata2011]_.
   There is little published detail on the control techniques but they seem to
   primarily make use of a roll rate gyro with steering and a gyro actuator.
   They also have other sensors such as ultrasonic sensors for obstacle
   detection. They demonstrate stability at zero, reverse and forward speeds,
   stopping for obstacles, and tracking a narrow s-curve.
[BicyRobo2011]_
   In 2011 the first `BicyRobo Thailand student competition
   <http://bicyrobo.ait.ac.th/>`_ occurred and many videos on the internet
   demonstrate the successful design of some teams. The full size bicycle
   robots have roll stability and even path following. One video demonstrates
   students riding the robot bicycle and simultaneously applying manual steer
   torques.
[Yamaguchi2011]_ `<http://ai2001.ifdef.jp/>`_
   `<http://www.youtube.com/watch?v=mT3vfSQePcs>`_ demonstrates an impressive
   remote controlled mini robot bicycle that is similar in nature to the
   [Berriah1999]_ design with remote control. He uses a commercially available
   bipedal robot seated on a small bicycle. A gyro detects the systems roll
   rate and he uses a PID controller to applied the correct steering for roll
   stabilization. The remote control is employed to control the heading.

The limited success of most of the various bicycle robots demonstrates that the
actual implementation of single track vehicle control is not trivial. Some of
the robots could demonstrate basic roll stability and some even capable of path
tracking ability but many didn't quite work either. The Murata Boy robot is
quite impressive in its abilities but it uses control outside of what humans
are capable of. The motorcycle robot by Kageyama is probably the most
successful demonstration of a full sized vehicle with control of only steering.
The vehicle dynamic models and control methodologies are varied, implying that
many techniques may be applicable.

Theoretic Control Models
-------------------------

It is far easier to develop theoretic control models than taking them as far as
implementation. There are many more successfully designed models on paper than
implemented. These models in this section are more in the realm of general
control, than human operator control.

[Forouhar1992]_
   studied the robust stabilization of the wobble mode in motorcycles (I
   haven't read this one, should be able to get it from Berkeley).
[Getz1994]_, [Getz1995]_, [Getz1995a]_
   uses a simple bicycle model that exhibits non-minimum phase behavior and is
   able to track roll angle and forward velocity using proportional and
   derivative control. One year later, Getz adds path tracking to his model.
[Kageyama1996]_
   uses a neural network model to balance a two wheeled vehicle (don't have
   this one).
[Cloyd1996]_
   use the same simple bicycle model and tracking variables as [Nagai1983]_,
   but controlled it with linear quadratic regulator.
[Nakano1997]_
   (in japanese).
[Yavin1997]_ and [Yavin1998]_
   study path tracking of a simple bicycle model using some kind of generalized
   control structure, with a bicycle model similar to [Getz1995]_.
[Chen2000]_
   fuzzy training.
[Sharp2001a]_
   They stabilize the roll angle of a motorcycle with a PID controller which
   operates on the error in roll angle to provide a steer torque. The gains for
   the controller are chosen by trial and error. The gains are difficult to
   find for low speed high roll angle scenarios.
[Park2001]_
   (do not have paper) can't find it yet with basic google searches
[Suryanarayanan2002]_
   uses a simple bicycle model to build a roll rate feedback controller for a
   high speed recumbent bicycle. They use proportional feedback of the roll
   rate to control the steer angle.
[Lee2002]_
   develops a control model based on something akin to sliding mode control to
   stabilize the bicycle and track a path.
[Frezza2003]_
   Read
[Kamata2003]_
   Download and read.
[Chidzonga2003]_
   Chidzonga uses the simple point mass bicycle model with a load sharing
   controller to demonstrate a track stand around zero forward speed. Although,
   it might have just been due to a miracle from Jesus.
[Yamakita2004]_
   setups a linear trajectory tracking control model and non-linear
   stabilization control by controlling steer torque, rider lean torque and rear
   wheel torque. They demonstrate the control in a simulation of a bicycle jump
   maneuver.
[Karnopp2004]_
   Karnopp uses a very simply bicycle model and basic proportional control to
   demonstrate the counter steering require to balance the bicycle. He also
   examines rear steered bicycles.
[Niki2005a]_
   Handlebar control..don't have paper.
[Niki2005]_
   This follows the [Tanaka2004]_ and [Iuchi2005]_ work, but adds in velocity
   tracking.
[Huyge2005]_
   He makes use of the [Cossalter2002]_ motorcycle model with a eighth body
   rider bio-mechanical model. He stabilizes the bodies and tracks a path using
   LQR control.
[Astrom2005]_
   They apply simple proportional control of a point mass type bicycle model to
   stabilize the roll angle with a steer angle input.
[Sharma2006]_
   They stabilize a simple bicycle model using fuzzy control rules to provide a
   desired roll correction based on the current steer and roll angles. The
   simulations show stability but with very erratic control that seem like it
   would be poor for a real controller.
[Saccon2006]_
   some kind of controller for a simulator or something.
[Limebeer2006]_
   They implement a PD controller on roll rate to stabilize the Whipple bicycle
   model outside the stable speed range.
[Findlay2006]_
   A simple point mass bicycle is stabilized by steer angle using three
   methods: a classical lead/lag compensator design, Ackerman pole placement
   and LQR optimal control.
[Bjermeland2006]_
   a masters these on controlling a bicycle, I don't have it.
[Sharp2007a]_
   He develops a path tracking controller for the benchmark bicycle
   [Meijaard2007]_ based on full state feedback and optimal control (LQR). He
   explores tight to loose control and shows how the gains vary with speed. He
   also include a preview model of which the tight control needs 2.5s of
   preview and the loose control needs at least 12.5 s. It is interesting to
   note that he found little change in computed gains for 20% variations in the
   various model parameters, leading him to conclude that the rider would be
   robust to various bicycle designs. His controllers show good performance for
   randomly generated paths.
[Sharp2007]_
   Here Sharp extends his LQR control method with preview from [Sharp2007a]_ to
   the motorcycle with the addition of rider lean torque control. He says that
   the objective was to develop a control scheme that *somewhat* represents a
   rider which is simple and effective. His controller inputs are the rider's
   upper-body absolute and relative lean angles and the path tracking error. He
   claims that riders control the motorcycle at the weave frequency at high
   speeds. He is able successfully stabilize and track a path and determines
   optimal preview gains. He also finds that the rider lean torque control is
   relatively ineffective and even with high weighting in the LQR formulation,
   the steer torque input dominates the optimal solution.
[Sharp2008a]_
   Sharp applies his LQR based preview model control model from [Sharp2007]_ to
   the benchmark bicycle. His findings are somewhat similar. His bicycle model
   is 6th order (he includes heading and path deviation) and he sets up the
   optimal control problem on full state feedback including varying numbers of
   path preview points. The bicycle tracks a path well and he shows high,
   medium and low authority control by changing the LQR weightings. In general
   the bicycle roll angle and rate gains are the largest, with rider lean gains
   following, and steer related gains being the smallest. His leaning rider is
   initially stabilized by a passive spring and damper, and he finds that the
   lean torque control is minor when paired with steer torque control. Lean
   torque alone requires very high gains.
[Marumo2007]_
   Marumo and Nagai design both a PD controller with respect to roll angle and
   an LQR controller with full state feedback to stabilize the roll of Sharp's
   basic motorcycle model through steer torque. The intention is to have a
   steer-by-wire system so the rider can specify the desired roll angle with
   something like a joystick, thus alleviating the need for the human to learn
   to counter steer. They include an additional torque to the controller output
   computed from the steady state inverse steer torque to roll angle transfer
   function. (this last sentence it weak).
[Chidzonga2007]_
   Chidzonga expands on the work in [Chidzonga2007]_ by once again managing a
   track stand with a load sharing control scheme.
[Peterson2008a]_
   Peterson designs a yaw rate and rear wheel speed tracking controller based
   on full state feedback and LQR control. He uses a non-linear Whipple like
   model with rider lean torque as the control input. His simulation required
   30 Nm of rider lean torque for a 0.3 rad/sec and 1 rad/sec step in yaw rate
   and rear wheel rate respectively.
[Keo2008]_
   They stabilize a bicycle model with a leaning "rider" pendulum and track a
   path.
[Connors2009]_
   Connors adds moving legs to the Whipple bicycle model and uses parameters to
   simulate a low slung recumbent bicycle. He designs an LQR full state
   feedback controller to stabilize the bicycle.

.. todo:: Kondo may be good to cite, but I haven't none of the papers.

.. todo:: Does Cangley have a control model?

.. todo:: Roland simulate a bicycle in a slalom some how

.. todo:: Doesn't Tak have a robot bicycle?

.. todo:: Check through the needswork folder for other papers and also the BMD
   conference proceedings for other examples.

Variations on PID control of steer angle or steer torque with feedback of the
roll angle are the most popular controller designs, many them being successful.
LQR type follow close behind. H_inf and other more modern control designs make
up the rest. It is clear that roll stabilization is the critical task and must
be conquered before path tracking can be employed.

Human Operator Control
----------------------

There are very fewer studies focusing on human control of a bicycle or
motorcycle with the intent of identifying the human controller or controlling
the vehicle with a human-like controller.

.. todo:: talk about learned control, unconscious vs conscious, upper cortex

van Lunteren and Stassen
~~~~~~~~~~~~~~~~~~~~~~~~

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

Weir and Zellner
~~~~~~~~~~~~~~~~

Weir worked with McRuer on some manual control papers prior to his PhD thesis
[Weir1972]_, where he employed a crossover model along side a motorcycle model
which is based on Sharp's early motorcycle model [Sharp1971]_ to evaluate the
controller used by humans. This is the most likely the first complete attempt
at analyzing the rider-motorcycle control system. Weir determined that roll
angle feedback combined with a basic human model and a simple gain controlling
steer torque was the most effective control mechanism. In particular, he showed
how steer angle control was poor and he even examined rider lean angle control
using a pseudo rider lean model similar to [Hess2012]_. Rider lean could
successfully control the system, but required large lean angles. He also worked
with multiple loop closures and found that roll angle fed back to control steer
torque with heading and lateral deviation fed back to control rider lean angle
presented the best control strategy for the human rider. He only did his
studies at a single high speed with a motorcycle model which only required
stabilization of the capsize mode. It is highly likely that these control
strategies could vary with speed, especially at low speed where the weave mode
is the dominant instability. Weir and Zellner went on to complete several more
important studies involving manual control of the motorcycle [Weir1978]_,
[Weir1979]_, including a detailed technical report for the U.S. Department of
Transportation [Weir1979a]_ in which much experimental work was done verifying
their mathematical models.

.. todo:: There are some other Weir papers I could cite, and I should look over
   Weir1979a again to get the main conclusions.

Doyle
~~~~~

A recently uncovered study by Doyle ([Doyle1987]_, [Doyle1988]_), thanks to
Google's book scanning endeavors and Jim Papadopoulus persistence in searching, presents a
slow speed view for bicycle control in much contrast to the Weir studies, not
only because of the speed and vehicle differences, but because it is from the
view of a psychologist. We engineers are quick to model the human sensory and
actuation system, with little understanding of the intricacies of the human
brain. Doyle's treatise gives a refreshing look from outside the engineering
box. Doyle's control model is fundamentally a sequential loop closure with the
inner most loop being roll control and the outer two being heading and path
deviation. He says that the outer loops are highly dependent on the inner loop.
For the inner loop he determines that continuously feeding back both roll
acceleration with integral and proportional gains adjusted by the human as the
crossover model dictates will stabilize the bicycle at non intended roll
angles. To control roll angle, he claims that we do not do this in a continuous
but that we apply discrete pulses when the roll angle meets a threshold. This
model has similar form to the one developed by us in the next section.

.. todo:: Cerebellum is the lower brain (learned control). High cortical
   regions and outer cortex is the higher brain. Under-conscious control or sub
   conscious.

Wu and Liu
~~~~~~~~~~

I'll mention briefly some about modeling the human with fuzzy control. I have
little understanding of fuzzy control but [Cloud1994]_ says that fuzzy control
methodologies fundamentally let one translate linguistic rules from an expert
in controlling the particular system into a control logic algorithm.
[Tagaki1983]_ discussed developing fuzzy control rules from the human
operator's actions (find this and read it). This parallels how the PID
controller was developed based on a ship's helmsman's decision structure. IT
seems like it may certainly be valuable for conscious control efforts, but may
have deficiencies when trying to determine the control strategy of unconscious
control. But a combination of fuzzy logic and crossover type control may prove
useful in describing the human control system. Liu and Wu have done extensive
work applying fuzzy control to single track vehicles ([Liu1994]_, [Wu1994]_,
[Wu1995]_, [Wu1996]_, [Wu1996a]_, [Wu1996b]_, [Wu1996c]_).

.. todo:: Read some of the Wu and Liu stuff and say something about it.

Mammar
~~~~~~

[Mammar2005]_ developed a motorcycle control scheme based on a motorcycle
dynamics model similar to Robin Sharp's work with steer torque and rider lean
angle as the model inputs. He includes human model with four elements: a simple
second order neuromuscular model similar to [Hess2012]_, a time delay, gain,
and a first order lead filter for a mental workload model. His control elements
include a roll angle feedback gain, a reference signal prefilter, and a
compensator with proportional, integral and lead control terms. The proportional
term in the compensator is the only speed dependent term. They select the
numerical values for the control elements using :math:`H_\infinity` loop
shaping. They finally show simulation results with good performance with
regards to disturbance rejection and roll tracking.

de Lange
~~~~~~~~

More recently, [Lange2011]_ wrote his master's thesis on identifying the human
controller in the bicycle-rider system. He employed a controller which fed back
roll angle and steer angle with PID plus second derivative control and time
delays to command a neuromuscular model which in turn commanded steer torque of
the Whipple model. The model is similar in flavor to van Lunteren and Stassen's,
but more up-to-date and uses more feedback loops. He chose eight gains plus
time delays and attempted to identify which loops were not important from our
experimental data. He finds that the critical feedback variables for a stable
model were roll angle, roll rate, steering rate and the integral of the steer
angle, claiming the last one in is proportional to heading thus controlling
heading with steer. He also finds the time delays to generally destabilize his
model and removes them.

Finally, we've developed a control model with Ron Hess [Hess2012]_ that is used
later this dissertation for human operator identification. The following
section gives a brief synopsis, but one should refer to the published paper for
more detail.

Conclusion
~~~~~~~~~~

A single track vehicle can be stabilized and controlled by a variety of means.
Controllers based on simplified dynamical models can potentially control more
advanced linear and nonlinear models and/or real systems (i.e. steer into the
fall). The roll stabilization is the critical tasks, as path following can't
happen if the bicycle is unstable in roll. Few people have demonstrated robust
control of a real system which stabilizes in roll at a variety of speeds. Even
fewer have added path tracking abilities. It doesn't seem like anyone has
stabilized a robotic bicycle with a controller that has the limitations of a
human built in.

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
[Doyle1987]_ with the inner loop structure dedicated to roll stabilization and
the outer loops to high cognitive control in heading and path tracking.

Basics of manual control theory
-------------------------------

Manual control, or human operator control, was primarily birthed from control
engineers after world war two. The requirements for machine designs in which
humans were the principal control element, such as artillery guns and aircraft,
led to human control modeling. Theoretical work by [Tustin1947]_ theorized
early on that a human control systems could be modeled similarly to automatic
feedback systems. This was followed by experimental work by [McRuer1965]_ mostly
confirming these hypotheses.

It turns out that humans adjust their control such that the combine human and
plant dynamics behave with desirable closed loop dynamics. This phenomena can
be captured by a variety of theoretical control structures from simple
dynamics to complex neuromuscular models [Hess1997]_. Fortunately, the simple
models can capture much of the dynamics in systems such our bicycle-rider
system. Here after we make use of the crossover model [McRuer1974]_. The reason
for this is multi-fold. It allows us to stick with a simple system which has
been applied to numerous man-machine systems with good results.

compensatory: controller uses the error only to make control
pursuit: both error and input information is available for the controller

The basic idea of the crossover model is that the when the human is paired
with the plant which she is trying to control that the combined open loop
transfer function conforms to the dictates of a sound control system design
around the crossover frequency [Hess1997]_. The form of this transfer function
for many control tasks takes the form

.. math::
   :label: crossover

   G_{human}G_{plant}(s) = \frac{\omega_c e^{-\tau_e s}}{s}

The model is governed by only two parameters: the cross over frequency,
:math:`\omega_c` and the effective time delay, :math:`\tau_e`. The simplicity
of this model and its ability to describe many human in the loop systems is
powerful.

.. todo:: read Ron's work on manual control again and write a summary here.

Jim - Isn't it true that the crossover model is only a representation of human
behavior near the limit of performance?

Ron - I can describe the dynamics of the human at various "crossover" frequencies
 and various performance levels.  It's true, that it has been verified in many
 laboratory and vehicle control tasks were good performance was required.

Model Description
-----------------

The design of the control structure was design to meet these requirements:

1. Roll stabilization is the primary task, with path following in the outer
   loop. The roll should be stabilize before closing the path following loops.
2. The input to the bicycle and rider biomechanic model is steer torque.
3. The neuromuscular mode of the closed system should have a natural frequency
   around 10 rad/s to match laboratory tracking tasks of a human operator.
4. The system should be simple in such that only simple gains are needed to
   stabilized the system and close all the loops.
5. We should see evidence of the crossover model in the open roll, heading and
   lateral deviation loops.

The multi-loop model we use is constructed with a sequential loop closure
technique that sets the model up to follow the dictates of the crossover model.
The three inner loops manage the roll stabilization task and the outer two
loops manage the path following. We include a simple second order model of the
human's neuromuscular dynamics which produces a steer torque from the steer
angle error.

.. math::
   :label: eqNeuromuscular

   G_{nm} = \frac{\omega_{nm}^2}{s^2 + 2\zeta_{nm}\omega_{nm}s + \omega_{nm}}

The neuromuscular parameters, :math:`\zeta_{nm},\omega_{nm}`, were chosen to
such that the innermost loop gave a typical response for a human operator.

.. todo:: Why is that the proprioception is required?? Is it a function of
   adding the neuromuscular model, cause people can stablize roll with P, D or
   PD on roll angle.

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

.. todo:: Why do we need the proprioceptive loop?

Traditionally, sequential loop closure methods are performed on a case by case
basis and involve some subjectiveness in applying the rules of thumb. This is
time consuming and error prone when you have to find the gains for many systems
as in our bicycles and riders at various speeds. We automated the technique
described in [Hess2012]_ can be automated to alleviate this.

The closed roll angle loop should be stable, as stability in roll is critical
for the path tracking in the outer two loops. To get there, the closure of the
proprioceptive and vestibular loops must push the poles to a favorable spot for
application of the crossover model on the roll angle loop. To do this, the
first two loop closure require that all of the oscillatory modes have a minimum
damping ratio of 0.15. We first use the proprioceptive gain, :math:`k_\delta`
to push the poles originating at the bicycle weave eigenvalue to a higher
frequency with 0.15 damping. The closed loop transfer function for the steer
loop is

.. math::
   :label: eqDeltaLoop

   G_{\delta c} = \frac{\delta}{\delta_c} =
   \frac{ G_{\delta o}}{1 + G_{\delta o}}

   G_{\delta o}(s) = k_\delta G_{nm} \left(\frac{\delta}{T_\delta}]\right)_b

A numerical example of Charlie on the Rigidcl bicycle at 5 m/s gives

.. math::

   G_{\delta o}(s)|_{k_\delta = 1} = \frac{4990.0342 (s+2.934) (s-2.934)}
   {(s+17.08) (s+2.56) (s^2 - 1.306s + 5.18) (s^2 + 43.02s + 900)}

The characteristic equation is 6th order and the caster, capsize and
nueromuscular modes are all stable and weave model is unstable. The first loop
closure will drive the unstable weave pole out  such that the interaction of
the original nueromuscular poles and weave poles give the new nueromuscular
mode about 0.15 damping at about 10 rad/s natural frequency. This is typical
neuromuscular/machine interaction seen in human operator control.

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

With the loop closed the transfer function takes the form

.. math::

   G_{\delta c}(s) = \frac{229042.5688 (s+2.934) (s-2.934)}
   {(s+2.998) (s-2.333) (s^2 + 4.292s + 205.2) (s^2 + 56.4s + 1232)}

Notice the single unstable poll at :math:`s=2.333`.

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

Notice that setting the phi loop gain affects the closed loop poles little, but
moves the right half plane zero to the left half plane

.. math::

   G_{\dot{\phi} c} = \frac{243.1658 s (s+77.09) (s+14.79)}
   {(s+3.572) (s-1.905) (s^2 + 2.936s + 208.7) (s^2 + 56.75s + 1244)}

leaving the single unstable poll in need of stabilization.

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

As can be surmised from the Bode diagram we've now stabilized the system in
roll by forcing the system to behave like the crossover model around the
crossover frequency, 2 rad/s.

.. math::

   G_{\phi c} = \frac{2504.8689 (s+77.09) (s+17.08)^2 (s+14.79) (s+2.56)^2 (s^2 - 1.306s + 5.18)^2}
   {(s+17.08)^2 (s+2.56)^2 (s^2 + 2.049s + 4.53) (s^2 - 1.306s + 5.18)^2 (s^2 + 2.657s + 193.7) (s^2 + 56.65s + 1242)}

The remaining loops are closed using the rule of thumb [Hess1997]_ of crossing
over at half the previous loops crossover frequency.

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
