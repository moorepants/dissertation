.. _systemidentification:

=====================
System Identification
=====================

* Introduction and review
* Model fitting
* Control parameter estimation
* Effects of rider, environment, speed and manuever to human control
* State space form of control system
* Fitting data
* Estimation and/or calculation of the K matrix
* Identify which parameters can be identified on the given data
* Relationship between speed and gains
* Whipple model versus whipple model with arms

Literature
==========

Identification of the vehicle/rider dynamical model and identifcation of
rider's controller have been studied several times in the past for single track
vehicles.

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
system identification with the lateral pertubation runs and did not work with
the lane change data. The lane changes were especially difficult on the
treadmill.

We chose three riders of similar age (28-29, 32, 34) (J, L, C), mass () and
bicycling ability although Luke has more technical mountatin biking skill. Each
rider's inertial properties were computed with Yeadon's method.

Enviroments
-----------

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
   eyes closed to attempt to compeletely open the heading loop.

.. todo:: dimensions of the lane changes

Whipple Model Validity
======================

The first topic to examine is the validity of our open loop bicycle and rider
biomechanic's models. We will need a realistic model to have any hope of
identifying the human controller. During all of the experiments we
fundamentally have one or two external inputs, the steer torque and the lateral
perturbation. The outputs can be any number of the measured quantities.

[Biral2003]_ and [Teerhuis2010]_ do a feed forward sim of their models with the
measured steering torque.
