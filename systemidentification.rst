.. _systemidentification:

=====================
System Identification
=====================

.. warning::

   This document is a draft which is updated regularly (Last updated |today|).
   Once I submit if for my doctoral degree at UC Davis, it will be done. So for
   now use at your own risk. The information may or may not be correct.
   Reviews, comments and suggestions are welcome.

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

The predictor can be written as follows

.. math::

   \hat{y}(t|\theta) = \mathbf{C}(\theta) \left[qI - \mathbf{A}(\theta) +
   \mathbf{K}(\theta) \right]^{-1} \left[\mathbf{B}(\theta) u(t) +
   \mathbf{K}(\theta)y(t) \right]

:math:`Y_N` is an :math:`pN x 1` vector

.. math::

   \left[y_1(1) \ldots y_1(N) \ldots y_p(1) \ldots y_p(N) \right]^T

where :math:`p` are the number of outputs and :math:`N` is the number of samples.
:math:`\hat{Y}_N(\theta)` is then the one step ahead prediction of :math:`Y_N`
given :math:`y(s)` and :math:`u(s)` where :math:`s \leq t - 1`

.. math::

   \left[\hat{y}_1(1) \ldots \hat{y}_1(N) \ldots \hat{y}_p(1) \ldots \hat{y}_p(N) \right]^T

The cost function is then the magnitude of the squares of the difference of
:math:`Y_N` and :math:`\hat{Y}_N(\theta)`.

.. math::

   V_N(\theta) = \frac{1}{pN}|Y_N - \hat{Y}_N(\theta)|^2

The value of :math:`\theta` which minimizes cost function is the best
prediction

.. math::

   \hat{\theta}_N = \underset{x}{\operatorname{argmax}} V_N(\theta, Z^N)

We made use of the Matlab System Identification Toolbox for the identification of
the parameters :math:`\theta` in each run of this output error model structure.

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
