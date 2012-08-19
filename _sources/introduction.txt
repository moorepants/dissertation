============
Introduction
============

Preface
=======

The bicycle is indeed a curious contraption that has greatly affected the lives
of human's since the early 19th century. There are probably more bicycles in
the world than any other kind of vehicle. The bicycle has a notable history and
it helped pave the way for the industrial revolution, the automobile, the
airplane and even played a role in the emancipation of western women. Yet it is
often an overlooked item in this day and age, especially in the United States
of America, where the automobile is the dominant form of transportation and the
bicycle is mostly considered a child's toy. But in other parts of the world the
bicycle can be viewed as a person's stepping stone to progress or the most
convenient way to get around. And what may be even more special about the
bicycle is that in its elegant simplicity it still embodies the solutions to
many of the world's transportation problems, whether it be on the congested 12
lane freeways of Los Angeles or in a rural African village.

In my life, I have become an ever stronger proponent of the use of the bicycle
as an appropriate mode of transportation. It is the most energy efficient way
for a human to travel :cite:`Wilson2004`. It has crept into all parts of my life
with much of my time being spent thinking about different aspects of bicycles
and bicycling. But this dissertation is concerned with how we actually balance
on the blasted thing. Balancing, in general, may seem like a trivial task
because we can all do it without consciously thinking about it, but the fact
that the best engineers in the world are still baffled by the intricacies of
balancing human-like robots give an idea of the difficulty of the subject. And
to muddle it even more, humans are capable of much more advanced balancing
acts like tight rope walking in which we invoke our *very* active control.
Riding a bicycle falls somewhere between simply standing and these more extreme
acts. The bicycle effectively disconnects us from the ground and forces us to
use different control strategies to stay upright. The bicycle's complex
dynamics, the difficulty of the task, limited control actuation methods, and
the ubiquity of the machine make the bicycle an ideal candidate platform for
human control studies.

The Bicycle and Rider as a Dynamic System
=========================================

The bicycle can be classified as a lightweight single track vehicle that is
fundamentally made up of four components: two wheels, a front frame, and a rear
frame. The wheels are connected to the respective frames by revolute joints and
the two frames are connected to one another by a revolute joint such that the
wheels are in-line with one another. This revolute joint between the two frames
is necessary for balance and directional control of the vehicle. It is easy to
show that locking the steering on a bicycle almost completely removes its
ability to balance or be balanced, and certainly to be guided in a desired
direction, no matter how the rider moves their body.

The bicycle has been studied by many scientists over the years. It is a rich
dynamic system that is difficult to model accurately. :cite:`Meijaard2007` did an
excellent job of sorting through 140 years of bicycle dynamics papers and
providing a benchmarked bicycle model that finally verified the correct
linearized equations of motion of the basic model, usually attributed as the
Whipple Model :cite:`Whipple1899`. The model is able to predict both the non-minimum
phase behavior and speed dependent stability and is now considered the
foundation to all more detailed models.

I'll briefly mention some of the common bicycle models and do so by dividing
them into two main categories: models that do not exhibit open loop stability
and models that do. All of these models can be extended by adding additional
dynamics such as tire-road interactions, frame flexibility, and human
biomechanics. These extensions can have effects on the stability and control of
the complete system.

Simple Models
-------------

Typically a one degree of freedom model that produces a roll equation of motion
is used to model a bicycle in its most basic form. This model has been derived
and analyzed by many including, but not limited to, :cite:`Timoshenko1948`,
:cite:`Karnopp2004`, and :cite:`Astrom2005`. These models do not have great fidelity with
regard to predicting the bicycle's open-loop, speed-dependent stability but
they are able to predict the non-minimum phase behavior. This situates them to
be good candidates for basic control studies (:cite:`Getz1994`, :cite:`Cloyd1996`,
:cite:`Karnopp2004`, :cite:`Astrom2005`, :cite:`Limebeer2006`) as they predict the necessity
of steering into the roll for stabilization and control. Controllers based on
these models have also been successfully implemented on actual experimental
control models :cite:`Suryanarayanan2002` with some success. Beyond this paragraph,
I will not be discussing these low order models any further.

Whipple Model
-------------

The lowest order model that has had some reasonable experimental validation
:cite:`Kooijman2008` is one which is able to predict speed dependent stability,
and includes a complete physical description of the four basic rigid bodies
that constitute a bicycle. The model is now typically referred to as the
"Whipple Model". This is in honor of Francis J. W. Whipple, the first author to
publish a correct derivation of the linear equations of motion of this
particular bicycle model :cite:`Whipple1899`. This model will be used as the
basis for all further studies proposed in this dissertation. Many researchers
over the past century have attempted to derive and analyze this model but very
few have been successful. :cite:`Meijaard2007` give a complete historical
review of uncontrolled bicycle research which made use of the historical
comparisons in the thesis by :cite:`Hand1988`. :cite:`Meijaard2007` also
benchmarked the Whipple Model by deriving the linearized equations of motion by
using four independent methods (two independent pen and paper calculations and
two different dynamic software packages). Furthermore, :cite:`Basu-Mandal2007`
benchmarked various torque-free circular motions in the non-linear case with
two additional independent derivations of the equations of motion. There has
been a series of recent validation attempts (:cite:`Kooijman2006`,
:cite:`Kooijman2008`, :cite:`Kooijman2009`, :cite:`Stevens2009`,
:cite:`Escalona2010`, :cite:`Escalona2011`) for the Whipple model in particular
and the evidence for it's ability to describe the motion of the bicycle with no
rider around the stable speed range is strong. This is important because it may
be the lowest order model with the ability to predict the dynamics. In this
dissertation, I make use of both the :cite:`Meijaard2007` model and my own
derivation of the Whipple Model.

Complex Models
--------------

With modern dynamic tools it is relatively easy to add more degrees of freedom,
flexible bodies, and more detailed forcing functions to the Whipple model with
the intent of pushing the model's ability to accurately predict bicycle and
motorcycle motion. For example, the typical motorcycle is modeled with more
realistic empirically derived tire-road interactions and a full suspension.

The most cited models typically have some reference to the model developed by
Robin S. Sharp :cite:`Sharp1971`. This model extends the Whipple model concepts to
include tire compliance and side slip. The model has been refined over the
years to improve accuracy by adding frame flexibility, rider models and
improving the tire models :cite:`Sharp1999` , :cite:`Sharp2001`, :cite:`Sharp2004`
with Pacejka-style :cite:`Pacejka2006` tire models being a popular choice. Sharp
was also the first to give names to the eigenmodes of the Whipple Model
:cite:`Sharp1975`. He and David Limebeer give a review of bicycle and motorcycle
modeling in :cite:`Limebeer2006` covering much of their work. Other notable studies
include ones developed by :cite:`Koenen1983` and the Italian group lead by Vittore
Cossalter :cite:`Cossalter2002`.

The motorcycle researchers have more experimental data validation of their
models than in bicycle studies, and their more complicated models in general do
a very good job of predicting the high speed motorcycle dynamics\ [#example]_.
This is due to the fact that more work has been done to understand and measure
the phenomena, that the high speed dynamics are easier to predict, and that the
human's biomechanical motions play a smaller role in the vehicle motion.

Conclusion
==========

Albert Einstein once said "Any intelligent fool can make things bigger, more
complex, and more violent. It takes a touch of genius - and a lot of courage -
to move in the opposite direction." With the wide variety of models available,
I've generally taken the approach of trying to use the simplest models possible
to predict the measured motion in my experiments rather than adding great
complexity. In my case, this model is often the Whipple model\ [#complex]_ with
or without various rider biomechanical models which attempt to account for the
large affect the rider's freedom of movement can contribute to the system
dynamics.

.. rubric:: Footnotes

.. [#example] For example, :cite:`Biral2003` is great example.

.. [#complex] Not to say that the Whipple Model is not complex, au contraire.
