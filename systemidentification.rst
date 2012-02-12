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

Vehicle
-------

[Weir1979a]_
   He may have done some id like work.
[Biral2003]_
   Motorcycle transfer functions.

Kooijman
--------

[Kooijman2006]_, [Kooijman2008]_
   Simple ID of a riderless bicycle.

Lange
-----

[Lange2011]_

Doria2011

Experimental Design
===================

Environments
------------

* Treadmill
* Gym

Manuevers
---------

* Balance
* Track Line
* Disturbance
* Blind
* Riders

Whipple Model Validity
======================

[Biral2003]_ and [Teerhuis2010]_ do a feed forward sim of their models with the
measured steering torque.
