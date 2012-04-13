.. _systemidentification:

=====================
System Identification
=====================

.. warning::

   This document is a draft which is updated regularly (Last updated |today|).
   Once I submit if for my doctoral degree at UC Davis, it will be done. So for
   now use at your own risk. The information may or may not be correct.
   Reviews, comments and suggestions are welcome.

Outline
=======

* Preface
* Introduction
* Literature review

  * Passive model identification
  * Rider control model identification

* Experimental Description
  * Answer question about whether bicycle dynamics are same on and off
    treadmill
* Data Description

  * Processing methods

* Parameter identification versus model identification

  * Identifiability

* Identification model structures

  * Black Box

    * Basic
    * State Space
    * Canonical Form

  * Grey Box

    * Structured State Space
    * Structured Canonical Form
    * Parameterized State Space

* Passive Model Identification

  * Black box ID

    * SISO (ARX, ARMAX, State Space)
    * System order

  * Grey box ID

    * Talk some about the identifiability of individual parameters.

  * Structured State Space ID

    * Coefficient plots

  * Canonical Form ID

    * Comparison of derived models with respect to rider and environment
    * Quality of models with respect to variance explained by the data

  * Comparison of identified models to first principle models

    * Structured state space per run
    * Regression results of general model
    * Benchmark canonical form identification for sets of runs

* Rider Controller identification

  * Grey box identification of the 6 parameter control model
  * Comparison of riders on the pavilion floor for different speed bins

* Discussion of results
* Conclusion

Preface
=======

The work presented in this Chapter is intended to be the icing on the cake that
takes into account all of the theory presented in the previous chapters and
evaluates it with a large set of data taken with the instrumented bicycle. I
started to think about system identification when I arrived at Delft and the
discussions began with Arend and Jodi. I hadn't much clue about the formal
field and theory on system identification. My first look at it was when Arend
presented me with a light introduction by Ljung. We talked about it here and
there but never really put together a solid experimental plan to do anything
about it. Karl Astrom visited us in Delft in late 2008 and we talked some with
him about ideas. I mainly recal him focusing on how to excite the system in a
very controlled manner with an oscilating mass on the bicycle. Some of these
ideas propogated through Arend to Peter and can be seen in the final sections
of his thesis [Lange2011]_. Many of these ideas influenced our NSF proposal and
ultimately the final portion of what I was to do for my dissertation work.

Once I had gotten back to Davis we now had the resources availabe from NSF
funding to make something happen. My goal had basically formalized into
creating a instrumented bicycle to be controlled by person that was capable of
measuring all of the kinematics and kinetics involved seen in regulated control
tasks. We also orginally had hoped to be able to vary the dynamics of the
bicycle, but the reduced funding nixed that idea. It took some time into the
project to really understand what we may be able to accomplish with that but it
finally materialized into validating Ron's theoretic control model which is
discussed in Chapter :ref:`control` with data collected via the instrumented
bicycle. After our first experiments, over a year into the project timeline it
became apparent that simple tasks with measured lateral perturbations would
provide the best chance of us validating his model. Unfortunately, I had not
thought a great deal about how to provide and measure these lateral
perturbations but the manually exticed perturbations seemed to to trick.

We ran a lot of preliminary system identifcation analyses on the first set of
trial data, but it quickly became apparent that we had little understanding in
the subject. The early analyses did give confidence that data was of good
enough quality to do something with, but our goal of identifying the parameter
of the controller were still far from our reach.

We performed the final set of experiments around August and September of 2011
to get a large sample of data for the final analyses. The NSF grant was to end
at the end of September and I still had to figure out how to analsize all of
the data, not to mention write up a ton of work for my dissertation. We ended
up extending the NSF grant another year (as seems to be typical with these
things). I look back to our original proposal and in hindsight the scope was
way too large (accurately predicted by Arend). We nixed the handling qualities
parts when the funding was lowered, but I now see that what we intended to do
really took another 6-12 months than we had intended.

The final analses has forced me to figure out what system identification is all
about and I've learned a great deal rapidly and much on my own. At this stage
we weren't able to find any local experts on the subject to help us along but
I've gotten some great insight from both the single track vehicle dynamics
email list and in particular from personal communication with Karl Astrom. I
still feel veyr weak in the subject but it is more clear how difficult
identifcying complex systems is, expecially trying to identify physical
parameters.

As many doctoral students probably hope when starting their long trek to the
PhD, I hoped for some grand findings to arise from this work. But I've been
humbled a lot in that quest. I present here the work I've done with regards to
identifying the bicycle and rider system with what I think are pretty good
results, but I hope that it is more of guide for others to see some of the
difficulties in excuting this kind of analyses with some ideas to better
structure it.

Introduction
============

This chapter details system identification of the 

Literature
==========

Identification of the vehicle/rider dynamical model and identifcation of
rider's controller have been studied several times in the past for single track
vehicles.

.. todo:: cite the british psycologist

van Lunteren and Stassen
------------------------

At Delft University of Technology in the Man-Machines research group, van
Lunteren and Stassen began work in 1962 to identify the human controller for a
normal population of subjects and report on their work into the early 70's
([Lunteren1967]_, [Lunteren1969]_, [Stassen1969]_, [Lunteren1970]_,
[Lunteren1970a]_, [Lunteren1970b]_, [Luntern1973]_, [Stassen1973]_). They chose
a bicycle simulator because it was a common task that average people could do
and their studies could focus on a wider population of individuals as compared
to most previous work based around trained pilots. The bicycle simulator did
not capture all of the essential dynamics of a real bicycle as it's operation
was based on only the simplified roll dynamics of Whipple's model, but
nonetheless offered a similarly complex roll stabilization control task. The
simulator is controlled by both the steering angle and the rider's lean angle,
both of which are questionable as realistic inputs.

They assumed the rider's control actions can be described with PID control with
time delays and mention that this controller was chosen instead of a McRuer
style controller primarily due to limitations of their computational equipment.
The error in the roll angle is fed into two PID controllers each with a time
delay: one to output the corrective steer angle and the other to output the
corrective lean angle. They introduce a remnant term for each control action
and the external disturbances to the bicycle model. The identification goal was
to find the six gains and two times delays which for the controller. The
preferred method was a real time estimation routine due to the speed of
computations and reasonable agreement their correlation method. The results
indicated that no integral control was used (i.e. only position and rate
feedback). They could identify a bandwidth of about 2 Hz and noticed that when
the system was undisturbed their was a 0.5 Hz dominant frequency in the rider's
control actions. The rate feedback was more dominant in generating the lean
control input than it was for the steer control input. Also, the found the time
delay for lean to be larger than the steer time delay and postulate that the
steer action is a result of cerebral activity while the lean is more of reflex
pattern. Another finding resulting from analysis of Nyquist plots of different
rider's identified control actions showed that riders chose different control
actions. They attribute this to the roll stabilization being a sub-critical
task (i.e. a more difficult task may force different riders to adopt similar
control behavior). They also investigated the effects of drugs, such as
alcohol, to the riders control behavior. They found correlations from drug dose
to time delays and the error in the control actions. Their later studies
introduced better identification methods and they found discrepancies in the
identified time delays of the later work as compared to the newer work. For
example, the steer control time delay was originally found to be around 1.5
seconds and the improved methods found the delay to be around 0.7 seconds, and
the discrepancy attributed to the bias due to remnant in their early work. They
also introduced a visual tracking task into the simulator but had difficulties
in getting reliable transfer function identification as compared to the roll
stabilization transfer functions which improved in quality due with longer
trials of 35 minutes.

Eaton
-----

David Eaton's work ([Eaton1973]_, [Eaton1973a]_, [Eaton1973b]_) may be the
closest example to the work presented in this chapter. He wrote did his PhD
work at the University of Michigan under the Highway Safety Research Institute.
His PhD focused on the experimental validation of the motorcycle modeling work
of [Sharp1971]_ and the human controller modeling work of [Weir1972]_. He did
this with two sets of experiments 1) identification of the uncontrolled
dynamics of the motorcycle under perturbations and 2) identification of the
rider controller during roll stabilization tasks.

During the first experiments his subjects road a motorcycle with their bodies
rigidly braced to the frame and hands-free at speeds of 15, 30, and 45 mph
(6.7, 13.4, and 20.1 m/s) along side a pace car which recorded the output from
roll angle, roll rate and steer angle sensors. Weights were dropped from one
side of the motorcycle to induce a step roll torque and the rider used a single
pulse in steering torque to the handlebars to right the motorcycle in roll.
These were unbelievable and dangerous experiments and would be hard pressed for
approval by the Institutional Review Board if done today. The resulting time
histories were compared to simulations of Sharp's model augmented with a
variety of tire models. He found good agreement between the experiments and the
model for higher speeds, but felt that a more robust tire model was needed to
predict the wobble mode in slower speed runs.

The second set of experiments were more tame. The riders simply balanced the
motorcycle on a straight path at two speeds, 15 mph and 30 mph, for three
riders, a total of 38 runs. He added a steer torque bar above the handlebars
which the rider controlled the motorcycle with one hand and rider applied
torque was recorded with the other signals. No pertubations were necessary, as
the rider's remnant excited the system enough. From this data he was able to
identify the motorcycle steer torque to roll angle transfer function by
dividing the cross spectrum of the roll angle and steer torque signal by the
power spectrum of the steer torque. The identified transfer functions show
good agreement with the augmented Sharp motorcycle model at the 30 mph speeds,
less so for the 15 mph runs. Then he made use of the Wingrove-Edwards method
in tandem with an impulse identification to identify the human controller. The
remnant element was large with respect to the torque that was linearly
correlated with the roll angle, but the human control element was identified
with a simple gain and time delay for most of the high speed runs. The time delay
identification was very repeatable across all runs. Furthermore, he
demonstrated that the crossover model was evident in the resulting rider and
motorcycle transfer function.

Eaton is one of very few who have identified the rider controller

.. todo:: .3 sec time delay

.. todo:: show block diagram of his controller

Aoki
----

[Aoki1979]_

James
-----

Stephen James's study published in 2002 [James2002]_ attempted to identify the
linear dynamics of an off road motorcycle. He measured steering torque, steer
angle, speed, roll rate and yaw rate while manually exciting the vehicle
through steer torque during runs at various speeds on a straight single lane
road. He made use of black box ARX SIMO identification routines of 6th and 7th
order (his and others motocycles models are usually 10th+ order) to tease out
the weave and wobble eigenvalues. He compares the identified eigenvalues,
eigenvectors and frequency responses to his motorcycle model and claims good
fits based on visual interpretation of the plots. The agreement is questionable
especially since no statistics on the fits were given, but this certainly shows
that there is the possibilty of identification of multiple modes of motion with
simple manual exctation of the handlebars.

Biral et al
-----------

[Biral2003]_ performed a nice study to identify the motorcycle dynamics under
an osciallotpry steer torque input. They measured steer torque, roll rate,
steer angle and yaw rate with an instrumented motorcycle. They performed slalom
manuevers at speeds from 2 to 30 m/s at three sets of cone spacings in the slalom
course. The data ended up being very sinusoidal and curves could be easily fit
and amplitude and phase relatoinships among the measure signals could be
plotted on Bode plots for comparison to the model generated Bode curves. The
models end up reasonably predicting the data, although they only asses this by
eye instead of presenting any fit percentages. This technique is more of an ad
hoc method of system identification of the vehicle dyanmics but seems to be
effective. Making use of modern system identification techinques could
potentially give more reliable results.

Kooijman
--------

My collegauge at Delft, Jodi Kooijman, worked on experimental validation of the
benchmark bicycle [Meijaard2007]_ linear equations of motion for a riderless
bicycle [Kooijman2006]_, [Kooijman2008]_, [Kooijman2009]_. His instrumented
bicycle measured the steer angle, forward speed, roll rate and yaw rate.
Because the bicycle can be stable at certain speeds he was able to launch the
bicycle in and around the stable speed range and perturb the bicycle with a
lateral impulse and record the decay in the steer, roll and yaw rates. The data
after the perturbations gave nice decaying oscillations and curves could be fit
to find the time constant and frequency of oscillation. These were then
compared to the model predicted weave response based on the measured physical
parameters of the bicycle with good agreement between 4 and 6 m/s. The
comparisons were by eye with no predictions in the error in the parameter
measurements or that of the dynamic measurements. His methods were also not
able to predict the heavily damped caster mode nor the capsize mode. He also
demonstrated that the dynamics were the same when the experiments were
performed on a treadmill.

In [Kooijman2011]_, Jodi constructed a bicycle with very unusual physical
characteristics including negative trail and canceled angular momentum of the
wheels. He performed similar experiments as his Master's thesis work. They show
the comparison of a stable single experiment in which the yaw and roll rates
were measured and compared it to the predictions of the benchmark bicycle.

[Stevens2009]_ and [Escolana2011]_ both perform experiments similar to
Kooijman's with similar results, althought Steven's results are poor for some
of his bicycle configurations.

These were also more ad hoc system identification techinques that took
advantage of very particulry behaving motions and little to no discussion of
the prediction errors are discussed.

Chen and Doa
------------

[Chen2010]_ developed a non-linear bicycle model and uses it to generate
controlled simulations of stable response for various speeds. He then does a
grey box identification on the resulting data with respect to the non-zero and
non-unity entries of the state, input and output matrices (i.e. just the
entries of the acceleration equations). No details of the identification noise
model were given. The identification is done for a discrete number of speeds in
the range 1 to 15 m/s. The eigenvalues are calculated of the resulting speed
dependent A matrices and the root loci plotted versus speed. The resulting
eigenvalues do not match the benchmark bicycle and the capsize mode is shown to
go unstable breifly before the stable speed range. This method of calcaulting
the linear model has much room for error due to the system identification
method and also that their non-linear bicycle equations of motion [Chen2006]_
were never validated against any other verifeid models. But they do show that
system identification can be used with somewhat noisy data to get good
estimates of a linear model of the vehicle alone, regardless of the controller
which stablizes the vehicle.

Lange
-----

[Lange2011]_

Peter de Lange's recent Master thesis work focused on identifying the rider
controller from the data that he helped us collect while interning at our lab.
He used the Whipple bicycle model, a simplifed second order representation of
the human's nueromuscular dynamics (natural frequency 2.17 rad/s and damping
ratio of 1.414) and a PID like controller with a 0.03 second time delay. The
controller strucute had gains proportional to the integral of the angle, the
angle, the angular rate and the angular acceleration for roll and steer. The
task was defined as simple roll stabilization (i.e. track a roll angle of zero
degrees). He made use of the finite impulse response method for system
identification and a SISO fit (lateral pertubation force input and steer angle
as output) and reduced the human remnant by identifying the average of many
perturbations during a single experiment. He parameterized the rider controller
with eight gains and a time delay and was able to identify the gains, but the
time delay always gave a resulting unstable model, so he dropped it. All of the
gains were not necessary for a good fitting model, so he reduced the structure
to find the critical feedback elements which were roll angle, roll rate, steer
rate and the integral of the steer angle. He concludes that the steer angle
integral could be equated to yaw angle feedback since they are proportional in
the linear sense.

Doria
-----

[Doria2012]_ A motorcycle rider excites the steering with a pulse and lets the motorcycle
oscilate with the rider's hands on the handlebars (as opposed to Eaton's
hands-free experiments). The resutling dynamical measurements are nice
sinusiodal motions of which the authors fit ideal curves to the data and
extract the eigenvalues and eigenvectors of the excited mode. The eigenvectors
show resemblance to the model's predictions.


[Weir1979a]_
   He may have done some id like work.

.. todo:: a hard copy mcruer automobile paper...look around the office for
   those papers.

It is somewhat easy enough to theorize models of both the vehicle system
dynamics and the rider's control, but often proving that those models are good
representations of real physical phenoma is difficult. These examples that I've
presented have various similarities to the methods I've chosen to use to
explore some of our models. They've basically come in a few flavors

Vehicle Indetification
   Mode Excitation
      This involves identifing particular modes of motion by forcing the system
      such that those modes are excited. The input to the vehicle is typically
      limited in frequency content. The forcing can be from human control to
      a particular manuever or by external pertubations and uncontrolled
      osciallations. The technique is to typically fit decaying osciallation
      functions to the data and to extract time constants, frequency and phase
      shift for the outputs. These techniques have given some good results, but
      formal system identifcation techniques may offer better results with more
      statiscal information. These techinques have been limited to identifying the
      vehicle dynamics.
   Excitation
      All modes can be excited if proper inputs to the vehicle are chosen, giving
      the opportunity to identify all models of a model. Freqency sweeps, white
      noise, and sum of sines are good candidates for a broad input spectrum. The
      remnant associated with human control also provides a good input as shown in
      [Eaton1973]_ and [James2002]_.
Rider Control Identification
   Few have attemted to identify the rider as a control element, but similar
   external excitation techniques for a broad frequency spectrum are needed.
   The control structure is harded to deduce from first principles, as the
   theories are much younger as compared to classical mechanics which governs
   the vehicles dynamics.

Experimental Design
===================

Our main experimental designs were focused around reasonable ways to excite the
rider/bicycle system to identify the rider control system. I started by simply
repeating some of the experiments from Chapters :ref:`delftbicycle` and
:ref:`motioncapture`, but measuring the lateral perturbation force and the
steer torque. We also tried out a single lane change manuever because we'd been
using a lane change as our objective criteria in our simulations [Hess2012]_.
It turned out that we were able to get reasonable results with preliminary
system identification with the lateral perturbation runs and did not pursue
the lane change data. The lane changes were especially difficult on the
treadmill.

We chose three riders of similar age (28-29, 32, 34) (J, L, C), mass () and
bicycling ability although Luke has more technical mountatin biking skill. Each
rider's inertial properties were computed with Yeadon's method.

Environments
------------

Treadmill
   Dr. James Jones at the vetinary school at here at Davis graciously let us use
   their horse treadmill during their downtime. The treadmill is 1 meter wider and
   5 meters long and has a speed range from 0.5 m/s to 17 m/s. This was only a
   third of the width treadmill at Vrije Univertiet, but after some practice runs
   we felt that narrow lane changes and the lateral perturbations could be
   successfully performed. We wanted to use the treadmill because the environment
   was very controllable, in particular fixed speeds,  and very long runs at
   constant speed could be done.
Pavilion
   The bicycle had all of the data collection equipment on board and is suitable
   for data collection non fixed enviroments. After lengthy beucratic negotiations
   we were able to make use of the UCD pavilion floor for the experiments. The
   floor was made of a stiff rubber and provided a rectangular wind free space of
   about 100' by 180'. We road around the perimeter to build up speed and did our
   manuevers on a straight section about 100 feet long. We were not able to travel
   at speeds higher than about 7 m/s as tires would slip in the final turn into
   the test section. This in door enviroment provided a wind free area.

.. todo:: find out what the floor was made of

.. todo:: Add some images of the treadmill and pavilion floor

Manuevers
---------

System Test
   This is a generic label for data collected during various system tests.
Balance
   The rider is instructed to simply balance the bicycle and keep a relatively
   straight heading. They were instructed to focus one some point in the far
   distance. There was an open door infront of the treadmill which allowed the
   rider to look to a point outside. In the pavilion, the rider looked into the
   rafters of the builing or at the furthest wall. We may have given slightly
   different instructions to the riders and at least one did not understand the
   instructions exactly during some of the earlier runs, but nonetheless these
   can be analyzed with a control model that only has the roll and heading
   loops closed and maybe with only the roll loop closed. We had a line taped
   to the pavilion floor during these runs that was still in the periphery of
   the rider's vision. This may have affected their heading control.
Balance With Disturbance
   Same as 'Balance' except that a lateral force perturbation is applied just
   under the seat of the bicycle. On the treadmill, we sample for 60 to 90
   minutes with five to eleven pertubations per run. On the pavilion floor we
   were able to apply two to four perturbations per run due to the length of
   the track. In the early runs (< 204), the lateral force was applied only in
   the negative direction and the perturber decided when to apply the
   pertubations. For the later runs, we applied a random sequence of positive
   and negative perturbations. On the treadmill, the rider signaled when they
   felt stable and the perturbation was applied at a random time between 0 and
   1 second based on a simple computer program. On the pavilion floor, we
   simply applied the pertubations as soon as the rider felt stable so that we
   could get in as many as possible during each run.
Track Straight Line
   The rider was instructed to focus on a straight line that is on the ground
   and attempt to keep the front wheel on the line. The line of site from the
   rider's eyes to the the line on the ground was esentially tangent the top of
   the front wheel. In the pavilion the line could be seen up to 100 feet
   ahead, so there was a little perphiral view of the line. On the treadmill,
   there was from 0.5 to 1.5 meters of preview line available.
Track Straight Line With Disturbance
   Same as "Track Straight Line" except that a lateral perturbation force is
   applied to the seat of the bicycle. This was done in the same fashion as
   described in "Balance With Disturbance".
Lane Change
   The rider attempted to track a line in the same fashion as "Track Straight
   Line" except that the line was a single lane change. On the pavilion floor,
   the line was taped on the ground and the rider was instructed to do whatever
   feels best to stay on the line. They can use full preview looking ahead,
   focus on the front wheel and line, or a combination of both. We also tried
   some lane changes on the treadmill but the lack of preview of the line made
   it especially difficult. We were able to manage it by marking a count down
   on the belt so that the rider new when the lane change would arrive. The
   rider also new the direction of lane change before hand for all the
   scenarios.
Blind With Disturbance
   We did a run or two for each rider on the pavilion floor with the rider's
   eyes closed to attempt to completely open the heading loop.

.. todo:: dimensions of the lane changes

Data
====

The experimental data was collected on seven different days. The first few days
were mostly trials to test out the equipment, procedures and different
maneuvers. The data from the trial days is valid data and we ended up using it
in our analysis.

February 4 2011 Runs 103-109
   First trials on the treadmill to test things out. Only Jason rode. Bike fell
   over, broke and we had to cut it short.
February 28, 2011 Run 115-170
   First trials in the at the pavilion. Jason rode. Tried lane changes, track
   straight line and track straight line with disturbance.
March 9, 2011 Runs 180-204
   Second go at the treadmill, still just testing out things. Jason rode. Tried
   track and balance with disturbance and some lane changes. Did the highest
   speed during any trials 9 m/s.
August 30, 2011 Runs 235-291
   Jason and Luke rode and performed balance and tracking tasks with and
   without perturbations at three speeds. On the treadmill.
September 6, 2011 Runs 295-318
   Charlie on the treadmill. Did balance and tracking with and without
   perturbations.
September 9, 2011 Runs 325-536
   Luke, Charlie and Jason on the Pavilion floor for balance and tracking with
   and without perturbations. Most of Luke and Charlie's runs are corrupt due
   to the time synchronization issues.
September 21, 2011 Runs 538-706
   Luke and Charlie repeated the runs from September 9th. We added a couple of
   blind runs for each of them.

We recorded a large set of meta data for each run to help with parsing during
analyses. We also video recorded all of the runs (minus a few video mishaps).
I coded each run based on the notes, data quality and viewing the video for
potential or definite corrupted data.

Corrupt
   If the data is completely unusable due to time synchronization issues or
   other then this is set to true.
Warning
   Runs with a warning flag are questionable and potentially not usable.
Knee
   The rider's knees would sometimes de-clip from the frame during a
   perturbation. This potentially invalidates the rigid rider assumption. An
   array of 15 boolean values are stored for each run and each true value
   represents a perturbation where a knee came off.
Handlebar
   On the treadmill the bicycle handlebars occasionally connected with the side
   railings. Each perturbation during the run which this happen was recorded.
Trailer
   On the treadmill the roll trailer occasionally connected with the side of
   the treadmill. Each perturbation during the run which this happened was
   recorded.

.. _figDataBarPlots:

.. figure:: figures/systemidentification/raw-data-bar-plot.*
   :width: 7in

   figDataBarPlot

   Four bar charts showing the number of runs that are potentially usable for
   model identification. These include runs from the treadmill and pavilion,
   one of the four primary maneuvers, and were not corrupt.

.. _figTreadmillTimeHistory:

.. figure:: figures/systemidentification/time-history-treadmill.*
   :width: 7in

   figTreadmillTimeHistory

   The time histories of the computed signals for a typical treadmill run after
   processing and filtering. Only a portion of the 90 second run is shown for
   clarity.

.. _figPavilionTimeHistory:

.. figure:: figures/systemidentification/time-history-pavilion.*

   figPavilionTimeHistory

   The time histories of the computed signals for a typical pavilion run after
   processing and filtering.

System Identification
=====================

The primary goal in the analyses of the data is to identify the human control
system. I will start by limiting the search with the control structure
described in [Hess2012]_ and in Chapter :ref:`control`. We've shown that this
control structure is robust for a range of speeds and lends itself to the
dictates of the crossover model and thus common human operator modeling. But
regardless of the control structure used we need to be confident that the plant
(i.e. the bicycle) is well described by our choice of bicycle model. There is
actually very little experimental validation of the passive dynamics of the
bicycle and rider biomechanics and taking the various theorectical models for
granted is potentially dangerous and will inevitably result in poor estimations
of the controller. There is good reason to question some of assumptions such as
knife, no side slip wheels. Using Eaton's [Eaton1973]_ lead, I will first attempt to
identify the bicycle model and then proceed to the onto the controller.
Preliminary attempts at identifying the controller with the Whipple model in
place as the plant have underestimated the steer torque needed for a given
trajectory and point to the need for a more in depth look at the validity of
our bicycle models.

Bicycle Model Validity
======================

The first topic to examine is the validity of our open loop bicycle and rider
biomechanic models. We will need a realistic model to have any hope of
identifying the human controller. During all of the experiments we
fundamentally have one or two external or exogneous inputs: the steer torque
and the lateral force. Both inputs are generated from manually control, the
first from the rider nd the second from the person applying the pulsive
perturbation. The outputs can be any subset of the measured kinematical
variables. The problem can then be formulated as such: given the inputs and
outputs of the system and some system structure, what model gives the best
prediction of the output given the measured input. This a classic system
identification problem and we will treat it as such.

For this analysis, we limit our inputs to steer torque and lateral force and
our outputs which are equal to the states as roll angle, steer angle, roll rate
and steer rate. This ideal fourth order system can be described by the
following continuous state space description.

.. math::

   \dot{x}(t) = \mathbf{F}(\theta)x(t) + \mathbf{G}(\theta)u(t)\\

   \begin{bmatrix}
     \dot{\phi} \\
     \dot{\delta} \\
     \ddot{\phi} \\
     \ddot{\delta}
   \end{bmatrix}
   =
   \begin{bmatrix}
     0 & 0 & a_{\dot{\phi}\phi} & 0\\
     0 & 0 & 0 & a_{\dot{\delta}\delta}\\
     a_{\ddot{\phi}\phi} & a_{\ddot{\phi}\delta} &
     a_{\ddot{\phi}\dot{\phi}} & a_{\ddot{\phi}\dot{\delta}}\\
     a_{\ddot{\delta}\phi} & a_{\ddot{\delta}\delta} &
     a_{\ddot{\delta}\dot{\phi}} & a_{\ddot{\delta}\dot{\delta}}
   \end{bmatrix}
   \begin{bmatrix}
     \phi \\
     \delta \\
     \dot{\phi} \\
     \dot{\delta}
   \end{bmatrix}
   +
   \begin{bmatrix}
     0 & 0 \\
     0 & 0\\
     b_{\ddot{\phi}T_\delta} & b_{\ddot{\phi}F_{c_l}}\\
     b_{\ddot{\delta}T_\delta} & b_{\ddot{\delta}F_{c_l}}
   \end{bmatrix}
   \begin{bmatrix}
     T_\delta\\
     F_{c_l}
   \end{bmatrix}

   \eta(t) & = \mathbf{H}x(t)\\

   \begin{bmatrix}
     \phi \\
     \delta \\
     \dot{\phi} \\
     \dot{\delta}
   \end{bmatrix}
   =
   \begin{bmatrix}
      1 & 0 & 0 & 0 \\
      0 & 1 & 0 & 0 \\
      0 & 0 & 1 & 0 \\
      0 & 0 & 0 & 1
   \end{bmatrix}
   \begin{bmatrix}
     \phi \\
     \delta \\
     \dot{\phi} \\
     \dot{\delta}
   \end{bmatrix}

Assuming that this model structure can adequately capture the dynamics of
interest in the bicycle/rider system, our goal is to accurately identify the
unknown parameters :math:`\theta` which are made up of all or a subset of the
unspecified entries in the :math:`\mathbf{F}` and :math:`\mathbf{G}` matrices.
This continuous formulation is not easily used with noisy discrete data and the
following difference equation can be assumed if we sample at :math:`t=kT`,
:math:`k=1,2,\cdots` and that the values are constant over the sample period
(i.e. zero order hold).

.. math::

   x(kT + T) & = \mathbf{A}(\theta)x(kT) + \mathbf{B}(\theta)u(kT) + w(kT)

   y(kT) & = \mathbf{C}(\theta)x(kT) + v(kT)

Where :math:`w` is the process noise which we assume is zero and :math:`v` is
the measurement noise, which is assumed to be white and Gaussian with zero mean
and known variance.Where :math:`w` is the process noise and :math:`v` is the measurement noise,
both of which are assume to be white with zero mean and known covariances. This
can finally be transformed by making use of the Kalman filter to get the
optimal estimate of the states :math:`\hat{x}`

.. math::

   \hat{x}(kT + T, \theta) & = \mathbf{A}(\theta)\hat{x}(kT) +
   \mathbf{B}(\theta)u(kT) + \mathbf{K}(\theta)e(kT)\\

   y(kT) & = \mathbf{C}(\theta)\hat{x}(kT) + e(kT)

where :math:`\mathbf{K}` is the Kalman gain matrix which is directly
parameterized by \theta. This equation is called the directly parameterized
innovations form and will be used in the identification process. The
:math:`\mathbf{A}` and :math:`\mathbf{B}` matrices are related to
:math:`\mathbf{F}` and :math:`\mathbf{G}` by

.. math::

   \mathbf{A}(\theta) = e^{\mathbf{F}(\theta)T}

   \mathbf{B}(\theta) = \int_{\tau=0}^T e^{\mathbf{F}(\theta)\tau} \mathbf{G}(\theta) d\tau

The one step ahead predictor for this system is

.. math::

   \hat{y}(t|\theta) = \mathbf{C}(\theta) \left[qI - \mathbf{A}(\theta) +
   \mathbf{K}(\theta) \right]^{-1} \left[\mathbf{B}(\theta) u(t) +
   \mathbf{K}(\theta)y(t) \right]

where :math:`q` is the forward shift operator (:math:`q u(t) = u(t+1)`)
[Ljung1999]_. The predictor is a vector of length :math:`p` where each entry is
a ratio of polynomials in :math:`q`. These are transfer functions from the
previous inputs and outputs to the current output. In general, the coefficients
of :math:`q` are non-linear functions of the parameters :math:`\theta`.

We can now construct the cost function, which will enable the computation of
the parameters which give the best fit.

:math:`Y_N` is an :math:`pN x 1` vector containing all of the current outputs

.. math::

   \left[y_1(1) \ldots y_p(1) \ldots y_1(N) \ldots y_p(N) \right]^T

where :math:`p` are the number of outputs and :math:`N` is the number of samples.
:math:`\hat{Y}_N(\theta)` is then the one step ahead prediction of :math:`Y_N`
given :math:`y(s)` and :math:`u(s)` where :math:`s \leq t - 1`

.. math::

   \left[\hat{y}_1(1) \ldots \hat{y}_p(1) \ldots \hat{y}_p(N) \ldots \hat{y}_p(N) \right]^T

The cost function is then the magnitude of the squares of the difference of
:math:`Y_N` and :math:`\hat{Y}_N(\theta)`.

.. math::

   V_N(\theta) = \frac{1}{pN}|Y_N - \hat{Y}_N(\theta)|^2

.. todo:: do I need the 1/pN? I'm just copying that from the book somewhere.

The value of :math:`\theta` which minimizes cost function is the best
prediction

.. math::

   \hat{\theta}_N = \underset{x}{\operatorname{argmax}} V_N(\theta, Z^N)

where :math:`Z^N` are all the measured inputs and outputs.

I made use of the Matlab System Identification Toolbox for the identification
of the parameters :math:`\theta` in each run of this output error model
structure. In particular a structured `idss` object was built for 

I further processed all of the signals that were generally symmetric about zero
by subtracting the means. For some of the pavilion runs, this may actually
introduce a small bias, especially in the roll angle.

.. todo:: I should probably make use of the static measurements I did each day
   to get a better idea of the roll angle bias.

It turns out that finding a model than which meets the criterion isn't too
difficult when the output error form is considered (:math:`K=0`). This model
may be able to explain the data well, but the parameter estimation could be
poor. Global minima in the search routine are quickly found when the number of
parameters are 10-14. When the :math:`\mathbf{K}` matrix is added the number of
unknown parameters increases by 16 and the global minima becomes more difficult
to find, but if found the parameters identification seems to be a better and
more repeatable estimate across runs.

Figure \ref{fig:exampleFit} shows the example input and output data for a
single run with both steer torque and lateral force as inputs. Notice that the
identified model predicts the trajecotry extremely well and similar results are
found for the majority of the runs. The Whipple model predicts the trajectory
directions but the magnitudes are large, meaning that for a given trajectory,
the Whipple model requires less torque than what was measured. The Whipple
model with the arm inertial effects does a better job than the Whipple model,
but still has some magnitude differences.

.. todo:: Compare the fit from a k=0 fit and one without, note how we aren't
   getting to the global minima

\begin{figure}
	\includegraphics{figures/example-fit.pdf}
	\caption{The example results for the identification of a single run. The
	experimentally measured steer torque and lateral force are shown in the top
	two graphs. All of the signals were filtered with a 2nd order 15 hertz low
	pass Butterworth filter. The remaining four graphs show the simulation
	results for the Whipple model (W), Whipple model with the arm inertia (A),
	and the identified model for that run (I) plotted with the measured data (M).
	The percentages give the percent of variance explained by the model.}
	\label{fig:exampleFit}
\end{figure}

[Biral2003]_ and [Teerhuis2010]_ do a feed forward sim of their models with the
measured steering torque.

Canonical Identification
------------------------

Model structure
~~~~~~~~~~~~~~~

The identification of the linear dynamics of the bicycle can be formulated with
respect to the benchmark canonical form realized in [Meijaard2007]_. If the
time varying quantities in the equations are all known at each time step, the
coefficients of the linear equations can be estimated given enough time steps.

.. math::

   M \ddot{q} + v C_1 \dot{q} + [g K_0 + v^2 K_2] q = T

where the time varying states roll and steer are collected in the vector
:math:`q = [\phi \quad \delta]^T` and the time varying inputs roll torque and
steer torque are collected in the vector :math:`T = [T_\phi \quad T_\delta]^T`.
This equation form assumes that the velocity is constant with respect to time
as the model was linearized about a constant velocity equilibriumm, but the
velocity can be treated as a time varying parameter if the acceleration is
relatively small. I extend the equations to properly account for the lateral
perturbation force, :math:`F`, which was the actual input we delivered during
the experiments. It contributes to both the roll torque and steer torque
equations.

.. math::

   M \ddot{q} + v C_1 \dot{q} + [g K_0 + v^2 K_2] q = T + H F

where :math:`H = [H_{\phi F} \quad H_{\delta F}]^T` is a vector describing the
linear contribution of the lateral force to the roll and steer torque
equations. :math:`H_{\phi F}` is approximately the distance from the ground to
the force application point. :math:`H_{\delta F}` is a distance that is a
function of the bicycle geometry (trail, wheelbase) and the longitudinal
location of the force application point. For our normal geometry bicycles,
including the one used in the experiments, :math:`H_{\delta F} << H_{\phi F}`.
I compute :math:`H` for each rider/bicycle from the state space form of the
linear equations of motion calculated in Chapter :ref:`extensions`.

.. todo:: Calculate what H_{\delta F\) actually is by hand.

.. math::

   \dot{x} = A x + B u

where :math:`x = [\phi \quad \delta \quad \dot{\phi} \quad \dot{\delta}]^T` and
:math:`u = [F \quad T_\phi \quad T_\delta]^T`. The state and input matrices can
be sectioned.

.. math::

   A =
   \begin{bmatrix}
     0 & I \\
     A_l & A_r
   \end{bmatrix}

.. math::

   B =
   \begin{bmatrix}
     0 & 0\\
     B_F &  B_T
   \end{bmatrix}

where :math:`A_l` and :math:`A_r` are the 2 x 2 submatrices corresponding to the states
and their derivatives, respectively. :math:`B_F` and :math:`B_T` are the 2 x 1 and 2 x
2 submatrices corresponding to the lateral force and the torques, respectively.
The benchmark canonical form can now be written as

.. math::

   B_T^{-1} [ \ddot{q} - A_r \dot{q} - A_l q] = T + B_T^{-1} B_F F

where

.. math::

   M = B_T^{-1}

.. math::

   vC_1 = -B_T^{-1} A_r

.. math::

   [gK_0 + v^2K_2] = -B_T^{-1} A_l

.. math::

   H = B_T^{-1} B_F

.. list-table::

   * - Rider
     - :math:`H`
   * - Charlie
     - :math:`[0.9017 \quad 0.01121716]^T` m
   * - Jason
     - :math:`[0.942975 \quad 0.01062231]^T` m
   * - Luke
     - :math:`[0.9017 \quad 0.01121716]^T` m

The location of the lateral force application point is the same for Charlie an
Luke because they used the same seat height. The force was applied just below
the seat, which was adjustable in height for different riders.

Data processing
~~~~~~~~~~~~~~~

Chapter :ref:`davisbicycle` details how each of the signals were measured and
processed to obtain

For the following analysis, all of the signals were filtered with a second
order low pass Butterworth filter at 15 Hz. The roll and steer accelerations
were computed by numerically differentiating the roll and steer rate signals
with a central differencing except for the end points being handled by forward
and backward differencing. The mean was subtracted from all the signals except
the lateral force.

Identification
~~~~~~~~~~~~~~

A simple analytic identification problem can be formulated from the canonical
form. If we have good measurements of :math:`q`, their first and second
derivatives, forward speed :math:`v`, and the inputs :math:`T_\delta` and
:math:`F`, the entries in the :math:`M`, :math:`C1`, :math:`K0`, :math:`K2` and
:math:`H` matrices can be identified by forming two simple regressions, one for
each equation in the canonical form. I use the instantaneous speed at each time
step rather than the mean over a run to improve accuracy with respect to the
speed parameter as it has some variablity.

.. todo:: calculate the variablity in the forward speed measurement for each
   run

The roll and steer equation each can be put into a simple linear form

.. math::

   \Gamma \Theta = Y

where :math:`\Theta` are the unknown coefficients and :math:`\Gamma` and
:math:`\Theta` are made up of the inputs and outputs measured during a run.
:math:`\Theta` can be all or a subset of the entries in the canonical matrices.
If there are :math:`N` samples in a run and we desire to find :math:`M` entries
in the equation, then :math:`\Gamma` is an :math:`N \times M` matrix and
:math:`Y` is an :math:`N \times 1` vector. The Moore-Penrose puesdo inverse can
be employed to solve for :math:`\Theta` analytically. The estimate of the
unknown parameters is then

.. math::

   \hat{\Theta} = [\Gamma^T\Gamma]^{-1}\Gamma^T Y

For example if we fix the mass terms in the steer torque equation and let the
rest be free the linear equation is

.. math::

   \begin{bmatrix}
      v(1) \dot{\phi}(1) & v(1) \dot{\delta}(1) & g \phi(1) & g \delta(1) &
      v(1)^2 \phi(1) & v(1)^2 \delta(1) & - F(1)\\
      \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots\\
      v(N) \dot{\phi}(N) & v(N) \dot{\delta}(N) & g \phi(N) & g \delta(N) &
      v(N)^2 \phi(N) & v(N)^2 \delta(N) & - F(N)\\
   \end{bmatrix}
   \begin{bmatrix}
     C_{1\delta\phi}\\
     C_{1\delta\delta}\\
     K_{0\delta\phi}\\
     K_{0\delta\delta}\\
     K_{2\delta\phi}\\
     K_{2\delta\delta}\\
     H_{\delta F}
   \end{bmatrix}
   =
   \begin{bmatrix}
     T_\delta(1) - M_{\delta\phi} \ddot{\phi}(1) -
     M_{\delta\delta} \ddot{\delta}(1)\\
     \vdots\\
     T_\delta(N) - M_{\delta\phi} \ddot{\phi}(N) -
     M_{\delta\delta} \ddot{\delta}(N)
   \end{bmatrix}

The error in the fit is

.. math::

   \epsilon = \hat{Y} - Y = \Gamma \hat{\Theta} - Y

.. todo:: discuss how this solves for noise

This equation can be solved for each run individually, a portion of a run or if
there are :math:`P` runs then they can be all collected in :math:`\Gamma` for
best fit over multiple runs. If all the runs have the same number of time
steps, :math:`\Gamma` then becomes an :math:`NP \times M` matrix and :math:`Y`
an :math:`NP\times 1` vector if each run is the same length.

The covarance of the parameter estimatations can be computed with respect to
the error.

.. math::

   \sigma^2 = \frac{\epsilon^T\epsilon}{N - d}

.. math::

   U = \sigma^2 (\Gamma^T \Gamma)^{-1}

Secondly, all of the parameters in the canonical matrices need not be
estimated. The analytical benchmark bicycle model [Meijaard2007]_ gives a good
idea of which entries in the matrices we may be more certain about from our
physical parameters measurements in Chapter :ref:`physicalparameters`. I went
through the benchmark formulation and fixed the parameters based on these
rules:

- If the parameter is greatly affected by trail, leave it free.
- If the parameter is greatly affected by the front assembly moments and
  products of inertia, leave it free.
- If the parameter is equal or near to zero, fix it.

For the roll equation this leaves :math:`M_{\phi\delta}`,
:math:`C_{1\phi\delta}`, and :math:`K_{0\phi\delta}` as free parameters. And
for the steer equation this leaves :math:`M_{\delta\phi}`,
:math:`M_{\delta\delta}`, :math:`C_{1\delta\phi}`, :math:`C_{1\delta\delta}`,
:math:`K_{0\delta\phi}`, :math:`K_{0\delta\delta}`, :math:`K_{2\delta\delta}`,
and :math:`H_{\delta F}` as free. The choice of fixing the majority of the roll
equation is also justified by the smaller variance seen in the state space
estimation of the roll acceleration equation.

I start by identifying the three coefficeints of the roll equation for the
given time steps due to having much more certainty in the roll equation
estimates from first principles.

.. math::

   \begin{bmatrix}
      \ddot{\delta}(1) &
      v(1) \dot{\delta}(1) &
      g \delta(1) \\
      \vdots & \vdots & \vdots\\
      \ddot{\delta}(N) &
      v(N) \dot{\delta}(N) &
      g \delta(N) \\
   \end{bmatrix}
   \begin{bmatrix}
     M_{\phi\delta} \\
     C_{1\phi\delta} \\
     K_{0\phi\delta}
   \end{bmatrix}
   =
   \begin{bmatrix}
     H_{\phi F} F(1)
     - M_{\phi\phi} \ddot{\phi}(1)
     - C_{1\phi\phi} v(1) \dot{\phi}(1)
     - K_{0\phi\phi} g \phi(1)
     - K_{2\phi\phi} v(1)^2 \phi(1)
     - K_{2\phi\delta} v(1)^2 \delta(1) \\
   \vdots\\
     H_{\phi F} F(N)
     - M_{\phi\phi} \ddot{\phi}(N)
     - C_{N\phi\phi} v(N) \dot{\phi}(N)
     - K_{0\phi\phi} g \phi(N)
     - K_{2\phi\phi} v(N)^2 \phi(N)
     - K_{2\phi\delta} v(N)^2 \delta(N) \\
   \end{bmatrix}

I then I enforce the assumptions that :math:`M_{\phi\delta} = M_{\delta\phi}`
and :math:`K_{0\phi\delta} = K_{0\delta\phi}` to fix these values in the steer
equation to the ones identified in the roll equation, leaving less free
parameters in the steer equation. This matrix symmetry is likely enforced in
reality due to the simple coupling of the front and rear frames by a revolute
joint. It is also possible to solve the roll and steer equations simultaneously
and enforce the symmetry but this was the easier solution. Finally, I identify
the remaining steer equation coefficients.

.. math::

   \begin{bmatrix}
     \ddot{\delta}(1) &
     v(1) \dot{\phi}(1) &
     v(1) \dot{\delta}(1) &
     g \phi(1) &
     v(1)^2 \delta(1) &
     - F(1)\\
     \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
     \ddot{\delta}(N) &
     v(N) \dot{\phi}(N) &
     v(N) \dot{\delta}(N) &
     g \phi(N) &
     v(N)^2 \delta(N) &
     - F(N)\\
   \end{bmatrix}
   \begin{bmatrix}
     M_{\delta\delta} \\
     C_{1\delta\phi} \\
     C_{1\delta\delta} \\
     K_{0\delta\phi} \\
     K_{2\delta\delta} \\
     H_{\delta F}
   \end{bmatrix}
   =
   \begin{bmatrix}
     T_\delta(1)
     - \hat{M}_{\delta\phi} \ddot{\phi}(1)
     - K_{0\delta\delta} g \delta(1)
     - \hat{K}_{2\delta\phi} v(1)^2 \phi(1) \\
     \vdots\\
     T_\delta(N)
     - \hat{M}_{\delta\phi} \ddot{\phi}(N)
     - K_{0\delta\delta} g \delta(N)
     - \hat{K}_{2\delta\phi} v(N)^2 \phi(N) \\
   \end{bmatrix}

Results
-------

I selected data for three riders on the same bicycle, performing two maneuvers,
on two different environments. I have little reason to believe the dynamics of
the passive system should vary much with respect to different maneuvers, but
there is potentially a small variation across riders primarily due to their
inertial properties and there may be variation across environments because of
the differences in the wheel to floor interaction. I opted to compute the best
fit model across series of runs to benefit from the large dataset. This leaves
these four scenarios:

- All riders in both environments (n=1)
- All riders in each environment (n=2)
- Each rider in both environments (n=3)
- Each rider in each environment (n=6)

.. list-table::

   * - Rider
     - Environment
     - Runs
     - N
   * - C
     - H
     - 24
     - 267773
   * - C
     - P
     - 87
     - 118700
   * - C
     - A
     - 111
     - 386473
   * - J
     - H
     - 57
     - 804995
   * - J
     - P
     - 93
     - 112582
   * - J
     - A
     - 150
     - 917577
   * - L
     - H
     - 25
     - 272719
   * - L
     - P
     - 88
     - 125878
   * - L
     - A
     - 113
     - 398597
   * - A
     - H
     - 106
     - 1345487
   * - A
     - P
     - 268
     - 357160
   * - A
     - A
     - 374
     - 1702647

A total of 12 different models can be derived from this perspective.

Computing the estimate for riders: Charlie and environments: Horse Treadmill
Number of runs: 24
Shape of A: (267773, 3)
Number of runs: 24
Shape of A: (267773, 6)
Done.
Computing the estimate for riders: Charlie and environments: Pavillion Floor
Number of runs: 87
Shape of A: (118700, 3)
Number of runs: 87
Shape of A: (118700, 6)
Done.
Computing the estimate for riders: Charlie and environments: All
Number of runs: 111
Shape of A: (386473, 3)
Number of runs: 111
Shape of A: (386473, 6)
Done.
Computing the estimate for riders: Jason and environments: Horse Treadmill
Number of runs: 57
Shape of A: (804995, 3)
Number of runs: 57
Shape of A: (804995, 6)
Done.
Computing the estimate for riders: Jason and environments: Pavillion Floor
Number of runs: 93
Shape of A: (112582, 3)
Number of runs: 93
Shape of A: (112582, 6)
Done.
Computing the estimate for riders: Jason and environments: All
Number of runs: 150
Shape of A: (917577, 3)
Number of runs: 150
Shape of A: (917577, 6)
Done.
Computing the estimate for riders: Luke and environments: Horse Treadmill
Number of runs: 25
Shape of A: (272719, 3)
Number of runs: 25
Shape of A: (272719, 6)
Done.
Computing the estimate for riders: Luke and environments: Pavillion Floor
Number of runs: 88
Shape of A: (125878, 3)
Number of runs: 88
Shape of A: (125878, 6)
Done.
Computing the estimate for riders: Luke and environments: All
Number of runs: 113
Shape of A: (398597, 3)
Number of runs: 113
Shape of A: (398597, 6)
Done.
Computing the estimate for riders: All and environments: Horse Treadmill
Number of runs: 106
Shape of A: (1345487, 3)
Number of runs: 106
Shape of A: (1345487, 6)
Done.
Computing the estimate for riders: All and environments: Pavillion Floor
Number of runs: 268
Shape of A: (357160, 3)
Number of runs: 268
Shape of A: (357160, 6)
Done.
Computing the estimate for riders: All and environments: All
Number of runs: 374
Shape of A: (1702647, 3)
Number of runs: 374
Shape of A: (1702647, 6)
Done.

All riders in both environments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here I'll make the assumption that the best fit model doesn't vary much across
riders or environments. The assumption that the passive model of the bicycle
and rider are similar with respect to rider can be justified by recognizing
that the Whipple model predicts little difference in the dynamics with respect
to the three bicycle/rider combinations. On the other hand, I have little
reason to believe the enviromenters are the same except that both floors are
made of a rubber like material. I calculated the best fit over 374 runs giving
about 142 minutes of data sampled at 200 Hz, :math:`N=1720000`.

.. figure:: figures/systemidentification/A-A-rlocus.*

   The root locus of the identified model (circle), the Whipple model
   (diamond), and the arm model (triangle) with respect to speed.

The eigenvalues as a function of speed of the identified model can be compared
to those of the Whipple and arm models. Figure :ref:`figAARloc` shows the root
locus of the three models. We see clearly that the weave mode exists in all
three models, with it being always stable in the arm model and with it being
unstable at lower speeds in the other two models. The identified model is
unstable over most of the shown speed range. Above 3 m/s or so, the Whipple
model's weave mode diverges from the identified model to different asymptotes.
The arm model weave mode diverges somewhere in between. Note that the arm model
has an unstable real mode for all speeds. Figure :ref:`figAAEig` gives a
different view of the root locus allowing one to more easily compare the real
eigenvalues. The imaginary parts of the weave mode have similar curavture with
respect to speed for all the models, with the identified model having about 1
rad/s larger frequency of osciallation for all speeds. The identified model
does have a stable speed range with the Whipple model underpredicting the weave
critical speed by almost 2 m/s. The identifed caster mode is much faster than
the one predicted by the Whipple model.

.. figure:: figures/systemidentification/A-A-eig.*

   Real and imaginary parts of the eigenvalues as a function of speed for model
   identified from all runs, the Whipple model and the arm model.

The identification process is structured around identifiying the input/output
relationship among measured varibles. The frequency response provides a view
into these relationships. Figures :ref:`fig` to :ref:`fig` give a picture of
how the first principles models compare to the identified model with respect to
frequency response. The frequency band from 1 rad/s to 12 rad/s is of most
concern as it is the range the human operates in.

The roll torque to roll angle shows that at 2 m/s the response if predicted
well at high frequencies by all the models and that the Whipple model predicts
the response well across all frequencies. At 4 m/s the two models only predict
the high frequency behavior (>4 rad/s) with the arm model being slightly better

.. figure:: figures/systemidentification/A-A-Tphi-Phi.*

   Frequency response of the three models at four speeds. The color indicates
   the model and the line type indicates the speed.

.. figure:: figures/systemidentification/A-A-Tphi-Del.*

   Frequency response of the three models at four speeds. The color indicates
   the model and the line type indicates the speed.

The steer torque to roll angle transfer function may be the most important to
model accurately as it is the primary method of controlling the bicycle's
direction. At 2 m/s the Whipple model magnitude matches at lower frequencies
better and the arm model better at higher frequencies. At all higher speeds the
Whipple and arm models don't match well at low frequencies.

.. figure:: figures/systemidentification/A-A-Tdel-Phi.*

   Frequency response of the three models at four speeds. The color indicates
   the model and the line type indicates the speed.

The steer torque to steer angle shows that speeds above 2 m/s the first
principle models do not predict the response well at low frequencies.

.. figure:: figures/systemidentification/A-A-Tdel-Del.*

   Frequency response of the three models at four speeds. The color indicates
   the model and the line type indicates the speed.

The response changes more drastically with respect to speed for the first
principles models than the identified model.

.. include:: tables/systemidentification/canonical-id-table-one.rst

.. include:: tables/systemidentification/canonical-id-table-two.rst

.. todo:: add this caption to the tables

Table Caption: Identified coefficients of the benchmark bicycle model for
various sets of data. The first column indicates which rider's runs were used:
(C)harlie, (J)ason, (L)uke or (A)ll. The second column indicates which
environment's runs were used: (P)avilion Floor, (H)orse Treadmill, or (A)ll.
The remaining columns give the resulting numerical value of the identified
parameter, its standard deviation with respect to the model fit, and the
percent difference with respect to the value predicted by the Whipple model.

Each rider in both environments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. todo:: Show the differences in the three rider models and point out that
   Charlie seems more different.

Comparison of identified models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The identified models in Tables X and X have differences in their dynamics. The
measurement errors, model structure and order dictate how well the models can
predict the input-output behavior of each run or even each perturbation. I
would ultimately like to select one or a small set of models that generally do
a good job at predicting the measured behavior for each run. I have shown that
the Whipple and arm models may not give good enough predictions.

Figures X through X plot the steer torque to roll angle frequency response for
three speeds: 2 m/s, 5.5 m/s and 9.0 m/s for each of the models in Tables X and
X. At the lowest speed, all of the models have a similar frequency response,
especially in the frequency band between about 1 an 20 rad/s. At 5.5 m/s the
models are similar at a higher bandwith, 4 to 30 rad/s. At 9.0 m/s even higher,
10 to 50 rad/s. For all speeds the variation among the response is most likely
   well within the uncertainty of the models as group. The model derived from
   all of the data (all rider and all runs), gives somewhat of a mean model and
   if this model is significantly better at predicting the measured behavior of
   the Whipple and arm models, it may be a good general candidate model for
   this bicycle.

.. todo:: Make a plot showing how all of the identified models frequency
   responses compared at a single speed (could do multiple graphs. This would
   hopefully support choosing the one identified model for all runs.

.. figure:: figures/systemidentification/compare-id-bode-2.0.*

   Steer torque to roll angle frequency responses at 2.0 m/s for all the
   identified models in Tables X and X.

.. figure:: figures/systemidentification/compare-id-bode-5.5.*

   Steer torque to roll angle frequency responses at 5.5 m/s for all the
   identified models in Tables X and X.

.. figure:: figures/systemidentification/compare-id-bode-9.0.*

   Steer torque to roll angle frequency responses at 9.0 m/s for all the
   identified models in Tables X and X.

The predictive capability of a given model can be quantified by mutliple
methods. I've made use of two criterion to judge the quality of a model with
respect to given data. The first is to simulate the system given the measured
inputs.  This method works well when the open loop system is stable, but if it
is unstable as so in the case of the bicycle, it may be difficult to simulate.
Searching for initial conditions that give rise to a stable model for the
duration of the run or simulating by weighting the future error less may
relieve the instability issues. Another option is to see how well the inputs
are predicted given the measured outputs. The canonical form of the equations
lend themselves to this check and only two inputs per run need be checked.

We designated the predicted torques on the system to be

.. math::

   y_p = M \ddot{q] + C \dot{q} + K q

and the measured torques to be

.. math::

   y_m = T + H F

:math:`y_p` and :math:`y_m` can be computed for each run along with the percent
variance explained by the model for both the total roll torque and the steer
torque

.. math::

   var = 1 - \frac{||y_p - y_m||}{||y_m - \bar{y}_m}}}

This percentage can be used as criterion of which to judge the ability of model
versus another to predict the measurement.

I compute the percent variance for each of the 374 runs used in the canonical
identification outlined earlier using each of the 12 identified models and both
the Whipple and Arm models. This percentage can be used ascriterion of which to
judge the ability of model versus another to predict the measurement.

I compute the percent variance for each of the 374 runs used in the canonical
identification outlined earlier using each of the 12 identified models and both
the Whipple and Arm models. I then take the median of the percent variances
over 12 sets of runs corresponding, each set corresponding to the set of runs
used in computing the various identified models. The results give an idea of
how well the various models are able to predict the data for all of the runs in
a given set.

.. include:: tables/systemidentification/median-roll.rst

.. include:: tables/systemidentification/median-steer.rst

.. todo:: Evaluate the model quality for each run (or a portion of each run).
   This can be done by seeing how well the predicted inputs fit with respect to
   the measured outupts or how well the outputs fit with respect to the
   measured inputs.

.. todo:: Plot the identified model A and B coefficients on the coefficient
   plots from the previous section.

Discussion
----------

- All identified models are unstable until very high speeds.
- I'm not sure if the rider's arm stiffness can affect these results. Or how
  much the different riders can effect this if we are only searching for the
  passive bicycle-rider model. Why is there difference in the riders?
