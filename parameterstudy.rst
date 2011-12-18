.. _parameterstudy:

=================
Parameter Studies
=================

.. warning::

   This document is a draft which is updated regularly (Last updated |today|).
   Once I submit if for my doctoral degree at UC Davis, it will be done. So for
   now use at your own risk. The information may or may not be correct.
   Reviews, comments and suggestions are welcome.

Introduction
============

Investigation of the effects of changes in the model parameters are natural
place to start once the various bicycle models are available. For the bicycle
designer, understanding how changing the parameters effects the dynamic
characteristics is something of a holy grail. If connections can be drawn from
model parameters to such things as handleability, stabilty and contrablity
bicycle designs could be tuned with these things mind. In the aircraft design
world correlations have been drawn from open loop dynamics to handling
qualities. It is highly likely that open loop dynamics can be predictors of the
handling of a bicycle, but there are large differences in aircraft, ground
vehicles and bicycles. The most glaring is the size of the rider with respect
to the vehicle and the fact that the rider's biomechanics, which are not
trivial contribute to the open loop dynamics of the entire system.

The eigenmodes of the Whipple model and the stability regime are prime targets
for initial parameter studies and there are many papers that deal with various
aspects. An analytical view of the parameter relationships would provide the
most encompassing conclusiong, but the complicated form of the equations
typically lead researchers to numerical studies. [PapadapoulusXXXX]_ has made
the most progress analitical studies and solves for Routh's stability criteria
for the capsize mode. [Franke1990]_ and [Astrom2005]_ examine the effect of
stable speed range with respect to independently varying wheel inertia and find
that for their parmater sets both the weave and capsize critical speeds
decrease with increase in spin moment of inertia. [Franke1990]_ also shows that
as trail increases both the critical speeds and the stable speed range
increase. This conclusion is counter intuitive, as many seem to believe that an
increase in trail lowers the weave critical speed, thus making the bicycle more
stable [Kooijman2008]_. [Stevens2009]_ examines experimentally and numerically
the effects of the front end geometry on eigenvalues, with some similar results
as [Kooijman2008]_. [Tak2010]_ examines the derivatives of the critical speeds
with respect to the benchmark parameters for a nominal parameter set. Tak's
method allows one to quickly visualize the independent parameter change which
affects the stable speed range the most for a given bicycle.

.. todo:: There are more examples of parameters studies that should be added
   I need to look through my references and any suggestions for inclusion would
   be appreciated. [Limebeer2006]_ may be one.

Numerical parameters studies were the first thing I did once I had a working
Whipple model [Moore2008]_ and I've explored some other studies over the years.
The following sections provide some the results.

Geometric Variation
===================

My first curiosities about bicycle handling arose when I was designing the
frame geometry of a recumbent bicycle for my bachelor's senior design project
and this seems to be continually the main interest among bicycle enthusiasts
and designers. Many bicycle designers focus on the geometry as the primary
design criteria for handling, in particular the head tube angle and trail (or
rake). But wheelbase, front wheel diameter, frame/wheel alignment and even
handlebar geometry rider position are considered too. A browse through bicycle
magazines and frame builder literature provide a wide range of opinions what
how geometry affects the handling. For example, Tim Paterek, an expert frame
builder, claims that the comfort zone for trail falls between 0.05 m and 0.065
m for most bicycles [Paterek2004]_. Craig Calfee is another prominent frame
buileder interested the effects of fork alignment on handling and wrote a small
piece on bicycle geometery for the 2007 North American Handbuilt Bicycle show
[Calfee2007]_. He claims that minute misaligments in the fork geometry can
cause undesireable handling. Finally, Jan Heine has written extensively in his
Vintage Bicycle Quarteley about handling with subject and objective measures by
experienced riders to the handling differences in real bicycles.

.. figure:: figures/parameterstudy/bicycle-geometry.png

   figBicycleGeometry

   The essential geometry of a bicycle parameterized with variables typically
   of interest to bicycle designers.

But the reality is that it is difficult to make any conclusive connections to
handling and geometry in a broad sense using rigorous dynamic and control
theory. Little progress has been made on this front. None-the-less parameter
studies can still be done with the models we have available. The following
results show how the stable speed range of the Whipple model linearized about
the nominal configuration change with respect to indepently varying the
essential geometry: trail, head tube angle, wheelbase and front wheel diameter.
Unlike in many ofther parameter studies, the physical associated with the
rider's position and the bicycle's parameters other than the essential geometry
are interdependent (i.e. adjusting the front wheel diameter changes the wheel’s
mass and moment of inertia together with the bicycle’s frame geometry and
adjusting the wheelbase causes the rider to reach further forward). The rider
parameters are estimated using a method which was a slight precursor to the
simple geometry method presented in Chapter :ref:`physicalparameters` [#]_ and
where based off of a 72 kg, 182 cm tall adult male. The rear frame and fork
were modelled as a collection of uniform steel tubes and the wheels as simple
tori. This allowed one to estimate the inertial properties of a bicycle as a
function of geometry. It assumed a normal diamond frame bicycle and the base
geometry of the bicycle was measured from a 58 cm 1982 Schwinn LeTour steel
road bike.

.. todo:: I've never documented the method to calculate the bicycle parameters
   besides in my code. I think I'll leave it at that, but can document it the
   phyical parameter chapter if desired.

The stable speed range for the nominal configuration was between about 3.59 m/s
and 4.88 m/s. Changes in the stable speed range were calculated by varying each
parameter over a realistic range for a bicycle of this nature. Each figure
shows a depiction of the maximal and minimal geometry configurations and the
nominal stable speed range is shown with a vertical line.

.. _figHeadTubeAngle:

.. figure:: figures/parameterstudy/head-tube-angle.png
   :width: 5in

   figHeadTubeAngle

.. _figTrail:

.. figure:: figures/parameterstudy/trail.png
   :width: 5in

   figTrail

.. _figWheelbase:

.. figure:: figures/parameterstudy/wheelbase.png
   :width: 5in

   figWheelbase

.. _figFrontWheelDiameter:

.. figure:: figures/parameterstudy/front-wheel-diameter.png
   :width: 5in

   figFrontWheelDiameter

Some obeservations from the plots follow.   As trail increases, the stable speed range broadens and the weave
critical velocity increases. As wheelbase increases the stable speed range
stays constant as both weave and capsize critical speeds increase at about the
same rate.

.. todo:: Add the time to double.

At speeds greated than the capsize critical speed, the capsize mode is unstable
with a time to double of about XX seconds. Thus the instability can be assumed
to be realitevly easy to stablize with a simple control, especially since the
weave mode provides rapid roll damping. That implies that the stable speed
range and capsize critical speed maybe of less importance to actual stability,
leaving the weave critical speed as the more important value considered in
stability.

The weave critical speed decreases as front wheel diameter increases but the
capsize critical speed decreases even faster so the size of the stable speed
envelope also decreases. The results show that the weave critical speed
decreases with a larger front wheel which will provide stability at low speeds.

A slack head tube angle (< 72 degrees) has a higher weave critical speed than a
larger head tube angle but the capsize critical speed varies very little with
changing head tube angle.Slack head tube angles are found on many utility
bicycles. These bicycles subjectively feel very unresponsive at low speeds and
typically do not feel stable until moderate speeds are reached. The head tube
angle results are in agreement with this anecdotal evidence in so far as the
weave critical speed increases with decreasing head tube angle (Figure 7). The
head tube angle results are interesting because the weave speed can be
decreased with a steep head tube angle without adversely affecting the capsize
critical speed, thus simultaneously increasing the stable speed range and
decreasing the weave speed. This is ideal if it is assumed that a low weave
critical speed is beneficial for take off and a broad stable speed range is
beneficial for cruising with little control input.

Trail is typically of
particular interest, with many bicycle designers claiming that it is the most
important parameter affecting handling qualities. Tim Paterek, an expert frame
builder, claims that the comfort zone for trail falls between 0.05 m and 0.065
m for most bicycles (Paterek 2004). Whether Paterek's claims have anything to
do with the stable speed range or the open loop eigenvalues can not be drawn.
Thus a more robust assessment of handling qualities is
needed. As trail approaches zero the stable speed range diminishes and this
follows the observed instability of a caster with negative trail (the caster
will always flip around to the stable configuration).

Long bicycles such as tandems and some recumbents are typically hard to start,
but handle better at higher speeds. The weave critical speed increases as
wheelbase increases (Figure 9) which correlates with the difficulty in starting
long wheelbase bicycles.


* Variation of parameters and effects to linear stability
* Comparison of the linear properties of real bicycles
* Note that flipping fork around raises the weave speed.
* Parameter studies are suited to a small range because most bicycles are the
  same design.
* Note that a bicycle without rider has two oscillatory modes as some point and
  explain them.

.. rubric:: Footnotes

.. [#] The original method modeled the legs with a two cuboids instead of four
   cylinders.
