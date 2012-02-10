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

I've located very few explicit examples of identifying the vehicle and/or the
bicycle

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

.. todo:: read the third Eaton paper

.. todo:: find the name of the michigan institute

.. todo:: show block diagram of his controller

Vehicle
-------

[Weir1979a]_
   He may have done some id like work.
[Biral2003]_
   Motorcycle transfer functions.
[Kooijman2006]_
   Simple ID of a riderless bicycle.

Human
-----

[Lunteren]_
   Online id routines in the 
[Lange2011]_

[Mammar]_

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
