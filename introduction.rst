============
Introduction
============

The bicycle is indeed a curious contraption. There are probably more bicycles
in the world that any other kind of vehicle. The bicycle has a notable history
and helped pave the way for the industrial revolution, the automobile, the
airplane and some say the emancipation of western women. But it is
often an overlooked item in this day an age, especially in the United States of
America, where the automobile is the dominant form of transportation and the
bicycle is mostly considered a child's toy. But in other parts of the world
the bicycle can be viewed as a person's stepping stone to progress or the
most convenient way to get around. And what may be even more special about the
bicycle is that in its elegenat simplicity it embodies the solutions to many
of the world's transporation problems, whether it be in the congested 12 lane
freeways of Los Angeles or in a rural African village.

In my life, I have become an ever strong proponent of the use of the bicycle as
an appropriate mode of transportation. It is in fact the most energy efficient
way for a human to travel [Wilson2004]_. It has crept into all parts of my
life with much of my time being spent thinking about different aspects of
bicycles and bicycling. But this disseration is concerened with how we
actually balance on the blasted thing. Balancing, in general, may seem like a
trivial task because we can all do it without consciously thinking about it, but
the fact that the best engineers in the world are still baffled by the
intricancies of balancing human-like robots shows the difficulty of the subject. 
And to muddle it even more, humans can do advanced balancing acts like tight rope 
walking in which we invoke our *very* active control. Riding a bicycle falls somewhere 
between normal balancing and these more extreme acts. It effectively disconnects us 
from the ground and forces us to use somewhat different control implements to stay upright.

The Bicycle and Rider as a Dynamic System
=========================================

The bicycle is fundamentally a lightweight single track vehicle with two wheels
and a revolute joint between the frame and fork. This revolute joint is
necessary for balance. It is easy to show that locking the steering on a
bicycle almost completely removes its ability to balance or be balanced, and
certainly can't be guided in a desired direction, no matter how the rider moves
their body.

Introduction
============

As was mentioned in the introduction, the bicycle has been studied by many
scientists over the years. The bicycle is a rich dynamic system that is
difficult to model accurately.  [Meijaard2007]_ did an excellent job of sorting
through 140 years of bicycle dynamics papers and providing a benchmarked
bicycle that finally verified the correct equations of the linearized Whipple
Model [Whipple1899]_. Bicycle-only models can be divided into two main
categories: models that do not exhibit open loop stability and models that do.
All of these models can be extended by adding additional dynamics such as
tire-road interactions, frame flexibility, and human biomechanics. These
extensions can have effects on the stability and control of the bicycle.

Simple Models
-------------

Typically a one degree of freedom model that produces a roll equation of motion
is used to model a bicycle in its most basic form. This model has been derived
and analyzed by many including, but not limited to, [Timoshenko1948]_,
[Karnopp2004]_ and [Astrom2005]_. These models do not have enough fidelity to
predict a real bicycle's uncontrolled motion and do not predict the speed
dependent stability that higher order models can. These models have been used
for control studies [Getz1994,CloydHubbardAlaways1996,Karnopp2004]_ as they
exhibit the non-minimum phase behavior that predicts the necessity of steering
into the roll for stabilization. Controllers based on these models have also
been used on actual experimental control models [Suryanarayanan2002]_. This
type of model will not be used in my studies.

Whipple Model
-------------

The lowest order model that has had some experimental validation
[Kooijman2008]_, is able to predict speed dependent stability and includes a
complete physical description of the four rigid bodies is typically referred to
as the "Whipple Model". This is in honor of Francis J. W. Whipple, the first
author to publish a correct derivation of the linear equations of motion of
this particular bicycle model [Whipple1899]_.  This model will be used as a
basis for all further studies proposed herein. Many researchers over the past
century have attempted to derive and analyze this model but very few have been
successful. [Meijaard2007]_ give a complete historical review of uncontrolled
bicycle research which made use of the historical comparisons in the thesis by
[Hand1988]_. [Meijaard2007]_ also benchmarked the Whipple Model by deriving the
linearized equations of motion by four independent methods (two independent pen
and paper calculations and two different dynamic software packages).
Furthermore, [Basu-Mandal2007]_ benchmarked various torque free circular
motions in the non-linear case with two additional independent derivations of
the equations of motion. [Kooijman2006]_ has verified by experiment that the
linearized Whipple Model does in fact predict the uncontrolled motion of a
normal bicycle in a speed range of about 3 to 6 m/s.  These papers and my own
derivation of the Whipple Model are the basis for using this model in my
research.

Motorcycle Models
-----------------

The motorcycle is modeled in much the same fashion as the bicycle except that
tire-road interactions and suspension are included.  Also, the human's
biomechanical motions play a smaller role because the motorcycle typically
weighs more than the rider. The most cited models are those developed by Robin
S. Sharp. His first model [Sharp1971]_ includes tire compliance and side slip.
The model has been refined over the years to improve accuracy by adding frame
flexibility, rider models and improving the tire models
[SharpLimebeerGani1999,SharpLimebeer2001,SharpEvangelouLimebeer2004]_.  He was
also the first to give names to the eigenmodes of the Whipple Model
[Sharp1975]_. He and David Limebeer give a review of bicycle and motorcycle
modeling in [LimebeerSharp2006]_ covering much of their work. Other notable
studies include ones developed by [Koenen1983]_ and [CossalterLot2002]_.


* The bicycle as a dynamic system
* Motivation
* General literature review
* Syntax and variables
* Overview of general types of bicylce models

  * Simple bicycle models
  * Bicycle models with stability
  * Complex models (motorcycle)

    * Tire models
    * Flexible rider
    * Shocks and flexible frames
