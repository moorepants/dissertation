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
model parameters to such things as handleability, stability and controllability
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
most encompassing conclusions, but the complicated form of the equations
typically lead researchers to numerical studies. [PapadapoulusXXXX]_ has made
the most progress analytical studies and solves for Routh's stability criteria
for the capsize mode. [Franke1990]_ and [Astrom2005]_ examine the effect of
stable speed range with respect to independently varying wheel inertia and find
that for their parameter sets both the weave and capsize critical speeds
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

.. todo:: Cite Zytveld1975 as doing early parameter studies with trail, front
   wheel moment of inertia and rider position. He also did it analyticall and
   with Routh's, like Jim. He also did a basic sensitity sutdy like Tak.

.. todo:: cite Lai2003

.. todo:: cite Sharp1971 as he discusses effects of parameter variations.

.. todo:: maybe cite Sharp1994

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
builder interested the effects of fork alignment on handling and wrote a small
piece on bicycle geometry for the 2007 North American Handbuilt Bicycle show
[Calfee2007]_. He claims that minute misalignments in the fork geometry can
cause undesirable handling. Finally, Jan Heine has written extensively in his
Vintage Bicycle Quarterly about handling with subject and objective measures by
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
the nominal configuration change with respect to independently varying the
essential geometry: trail, head tube angle, wheelbase and front wheel diameter.
Unlike in many other parameter studies, the physical associated with the
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

.. todo:: Add the time to double below.

At speeds greater than the capsize critical speed, the capsize mode is unstable
with a time to double of about XX seconds. Thus the instability can be assumed
to be relatively easy to stabilize with a simple control, especially since the
weave mode provides rapid roll damping. That implies that the stable speed
range and capsize critical speed may be of less importance to actual stability,
leaving the weave critical speed as the defining characteristic.

.. _figHeadTubeAngle:

.. figure:: figures/parameterstudy/head-tube-angle.png
   :width: 5in

   figHeadTubeAngle

   The change in stable speed range as a function of head tube angle.

A slack head tube angle (< 72 degrees) has a higher weave critical speed than a
larger head tube angle but the capsize critical speed varies very little with
changing head tube angle. Slack head tube angles are found on many utility
bicycles. I've founded that these bicycles feel very unresponsive at low speeds
and typically do not feel stable until moderate speeds are reached. The head
tube angle results are in agreement with this anecdotal evidence in so far as
the weave critical speed increases with decreasing head tube angle. The head
tube angle results are interesting because the weave speed can be decreased
using a steeper head tube angle without adversely affecting the capsize
critical speed, thus simultaneously increasing the stable speed range and
decreasing the weave speed. This is ideal if it is assumed that a low weave
critical speed is beneficial for take off and a broad stable speed range is
beneficial for cruising with little control input.

.. _figTrail:

.. figure:: figures/parameterstudy/trail.png
   :width: 5in

   figTrail

Trail is typically of particular interest, with many bicycle designers claiming
that it is the most important parameter affecting handling qualities. As trail
increases, the stable speed range broadens and the weave critical velocity
increases. As trail approaches zero the stable speed range diminishes to zero.
It is obvious that increasing trail will decrease the caster mode eigenvalue,
but un-intuitively it increases the weave eigenvalue. The yellow bicycle
[Ruina2011]_ and the silver bicycle [Kooijman2006]_ both have their forks
flipped for increase trail with the intent on the bicycles being stable at the
speeds tested. According to the data I'm not sure the flipped fork actually
helps this though.

.. _figWheelbase:

.. figure:: figures/parameterstudy/wheelbase.png
   :width: 5in

   figWheelbase

Long bicycles such as tandems and some recumbents are often hard to start and
have slower response. As wheelbase increases the stable speed range stays
constant as both weave and capsize critical speeds increase linearly at the
with the same slope rate. The weave critical speed increases as wheelbase
increases which may correlates with the difficulty in starting long wheelbase
bicycles.

.. _figFrontWheelDiameter:

.. figure:: figures/parameterstudy/front-wheel-diameter.png
   :width: 5in

   figFrontWheelDiameter

The weave critical speed decreases as front wheel diameter increases but the
capsize critical speed decreases even faster so the size of the stable speed
envelope also decreases. The results show that the weave critical speed
decreases with a larger front wheel which provides stability at low speeds.
This correlates with the findings for the flywheel bicycle presented in Chapter
:ref:`extensions`.

I have made some conclusions about the stability of the Whipple model and
made some subjective conclusions on the potentially relationship of the critical
speeds with geometry changes. This gives some idea of how one may begin
connecting handling to the bicycle's dynamics.

Bicycle Comparison
==================

I present the physical parameters of ten bicycles in Chapter
:ref:`physicalparameters`. There are variety of bicycles from commuter bicycles
to road racing and mountain to a child's bicycle and some instrumented
bicycles.  Here I will present some comparisons of the linear dynamics of the
different bicycles and try to make some conclusions about their dynamics. The
"normal" diamond frame bicycle is very similar from bicycle to bicycle with
very little variation in the essential geometry. More variation is seen in the
mass and inertia.

Benchmark validity
------------------

The benchmark bicycle parameters in [Meijaard2007]_ are representative of a
real bicycle but where manipulated so that each parameter was guaranteed a
detectable role in numerical studies. Figure :ref:`figBenchmarkReal` compares
the eigenvalues of the benchmark bicycle with those of two ordinary bicycles,
the Batavus Browser and Batavus Stratos including the rider, Jason, seated on
the bicycles. The eigenvalues are qualitatively similar, but the stable speed
range is both lower and narrower. The weave frequency also diverts from the
real bicycles at higher speeds, but other than that the benchmark parameters
are within realistic bounds for a normal style bicycle.

.. _figBenchmarkReal:

.. figure:: figures/parameterstudy/benchmark-real.png
   :width: 6in

   figBenchmarkReal

   The real and imaginary parts of the eigenvalues as a function of speed for
   three bicycles including the benchmark bicycle from [Meijaard2007]_ and two
   bicycles and riders presented in Chapter :ref:`physicalparameters`.

Rider-less bicycles
-------------------

There are relatively few datasets with where real bicycle parameters were
measured as described in Chapter :ref:`physicalparameters`. Figure
:ref:`silverCompare` plots one such parameter set, labeled Silver, from
[Kooijman2008]_ and compares it to several of the rider-less bicycles I
measured using almost identical techniques. Notice that all of the bicycles I
measured show a bifurcation in the caster and capsize modes at lower speeds
which produces second oscillatory mode not necessarily seen in the parameter
sets with a rigid rider. Figures :ref:`figCresEvecWeave` and
:ref:`figCresEvecOsc` give a look at the eigenvector components for the two
oscillatory modes for the Crescendo bicycle at 1.5 m/s. They turn out to be
similar modes in that they oscillatory in roll and steer, with steer being
dominant in magnitude and the phase shifts slightly larger for the weave mode.
But the new mode is stable as opposed to the weave mode being unstable. The
bicycles measured in [Stevens2009]_ and [Escalonas2011]_ measured bicycles both
exhibit this mode, but Steven's parameters are estimated from a CAD drawing,
which may not be that accurate. Steven's does show that this mode disappears
with very steep or very slack head tube angles. The diagrams for very slack
head angles more qualitatively resemble the Silver bicycle from
[Kooijman2008]_. But it is still odd that the Silver bicycle is that different
than all the other bicycles, with the only major difference being a flipped
fork form more trail and a larger yaw and roll moment of inertia due to the
outriggers.

.. _figSilverCompare:

.. figure:: figures/parameterstudy/silver-compare.png
   :width: 6in

   figSilverCompare

   The real and imaginary parts of the eigenvalues as a function of speed for
   four bicycles including the silver bicycle from [Kooijman2008]_ and three
   bicycles and riders presented in Chapter :ref:`physicalparameters`.

.. _figCresEvecWeave:

.. figure:: figures/parameterstudy/cres-evec-1.5-1.png

   figCresEvecWeave

   The eigenvector components for roll rate, :math:`u_4`, and steer rate,
   :math:`u_9`, for the Crescendo parameter set weave mode at 1.5 m/s.

.. _figCresEvecOsc:

.. figure:: figures/parameterstudy/cres-evec-1.5-2.png

   figCresEvecWeave

   The eigenvector components for roll rate, :math:`u_4`, and steer rate,
   :math:`u_9`, for the Crescendo parameter set new mode at 1.5 m/s.

Riders
------

There are some potentially significant differences in the Whipple model
dynamics for a riderless bicycle and a bicycle with a rider rider. Figure
:ref:`figCompareRiderEig` gives an example of how the eigenvalues change when a
rider is added to the Stratos bicycle. The stable speed range broadens and the
weave critical speed increases by over 1 m/s. The second oscillatory mode
dissapaers and the caster mode has higher damping. The weave bifurcation point
occurs at a lower speed. And finally the natural frequency of the weave mode
for the rider and bike is much lower for speeds above 3 m/s. The changes in
dynamics are enough that conclusions made about bicycles without rigid riders
don't necessarily extend to bicycles with rigid riders.

.. _figCompareRiderEig:

.. figure:: figures/parameterstudy/compare-rider-eig.png
   :width: 6in

   figCompareRiderEig

   The root loci with respec to speed for the Stratos bicycle with and without
   a rider.

Yellow bicycle
--------------

I measured the parameters of the "Yellow" bicycle at TU Delft, which was a
replica of the Yellow bike from Cornell which demonstrates stability so well. I
measured the bicycle in two configurations, one with the fork in the normal
position and the second with the fork flipped 180 degrees about the steer axis
to exaggerate trail. Figure :ref:`figYellowCompare` plots the root loci with
respect to speed for the two yellow bicycle configuration and the silver
bicycle which also has a reversed fork. As was mentioned in the previous
section the weave critical speed increases as the trail increases and this is
clearly shown for the yellow bicycle with a reversed fork. But maybe more
interestingly  the capsize critical speed increases dramitcally with the
revesred fork.

.. todo:: Include the yellow bicycle video from Cornell.

.. _figYellowCompare:

.. figure:: figures/parameterstudy/yellow-compare.png
   :width: 6in

   figYellowCompare

   The root loci with respect to forward speed for the yellow bicycle in both
   configurations and the silver bicycle which also has a reversed fork.

Rear weight
-----------

Another fruitful comparison can be gathered from the Batavus Browser as we
measured both the instrumented configuration and the factory version. The
fundamental difference in the two configuration is that the instrumented
version has a large weight atop the rear rack. Bicycle tourists are some of the
first to mention the effects on handling due to weight on the front and rear
racks of a bicycle, so this comparison examines that to some degree. Figure
:ref:`figBrowserCompare` once again shows the root loci with respect to speed
for the two bicycles. The second bifurcation points for the second oscillatory
mode are affected and the weave critical speed is slightly lower for the
factory version. If a rider is added, Figure :ref:`figBrowserRiderCompare`,
shows that the added rear weight makes little difference in the linear
dynamics.

.. _figBrowserCompare:

.. figure:: figures/parameterstudy/browser-compare.png
   :width: 6in

   figBrowserCompare

   The root loci with respect to forward speed for the factory Browser and the
   instrumented version which has a large weight on the rear rack.

.. _figBrowserRiderCompare:

.. figure:: figures/parameterstudy/browser-rider-compare.png
   :width: 6in

   figBrowserRiderCompare

   The root loci with respect to forward speed for the factory Browser and the
   instrumented version which has a large weight on the rear rack and a rider.

Uncertainty
===========

.. todo:: This maybe belong in the previous chapter and may need to be removed
   together. I'm not sure where I want to go with it.

I had intended to calculate the uncertainty in the eigenvalue predictions
based on the error propagation from the raw measurements, but I never quite
figured it out. It would be interesting to draw error bars on around the modes
in the eigenvalue plots. I think it maybe revealing with respect to the
experiments that are done which try to estimate the eigenvalues of a stable
bicycle [Kooijman2008]_, [Kooijman2009]_, [Stevens2009]_, [Escalona2010]_. All
of the these except for [Kooijman2009]_ experiments plot a predicted eigenvalue
for a speed range because the bicycle doesn't have way of maintaining forward
speed, but beyond that the uncertainty in the eigenvalue estimates are not
reported. It would be interesting account for the uncertainties in both methods
of predicting the eigenvalues. Because the eigenvalues seem to be rather
sensitive to change in some parameters, the may be an important issue to
address.

Frequency Response
==================

The eigenvalues give a complete of the linear systems open loop dynamics, but
one can also examine the system's response to various inputs. The frequency
response is good way to examine how the system responds to a sinusoidal input.
The transfer function from steer torque to the roll rate of a bicycle is
particularly interesting because it captures what the essential steering action
needed to induce a turn.

Figure :ref:`figBodeSpeeds` shows the transfer function for Jason seated on the
Browser for several different speeds. The speeds correspond to before the first
weave bifurcation, unstable weave, stable speed range and unstable capsize. The
roll rate amplitudes somewhat increase with speed, with the 6 m/s showing
larger output amplitudes than the more well damped 10 m/s. The phase plot shows
similarity in the higher speeds and similarity in the lower speeds.  Both plots
show differences at lower frequencies and seem to tend to the same response at
higher frequencies.

.. todo:: I need some help talking about what these graphs mean, as my Bode
   diagram language is weak.

.. _figBodeSpeeds:

.. figure:: figures/parameterstudy/bode-speeds.png
   :width: 5in

   figBodeSpeeds

   The steer torque to roll rate transfer function frequency response for
   various speeds.

Figure :ref:`figBodeWeight` shows the transfer function for the same rider
(same configuration with respect to the rear wheel contact point) seat on a
light bicycle, Bianchi Pista, and very heavy bicycle, the Davis instrumented
bicycle. Notice that the light bicycle has an under-damped weave mode which is
stable, while the heavy bikes weave mode is well damped and unstable. Once
again, differences in the frequency response are less apparent at high
frequencies.

.. _figBodeWeight:

.. figure:: figures/parameterstudy/bode-weight.png
   :width: 5in

   figBodeWeight

   The steer torque to roll rate transfer function frequency response for a
   heavy and light bicycle at 5 m/s.

.. todo:: There are many of these plots I can make. Can you think of any others
   that might be worth showing?

Conclusions
===========

Parameter studies can reveal allow one to explore the effects of design
parameters on the system dynamics. The eigenvalue provide a way to transform of
the parameters of a complex system into a minimum characteristic set of
parameters that completely characterize the open loop input ignorant dynamics.
And other views such as the frequency response provide input/output
characteristics of the system's transfer functions. System stability, time to
double/half, natural frequency and frequency responses. There are most likely
correlations from the open loop dynamics to handling, as has been demonstrated
in aircraft control literature, but those correlations are mostly speculation
and anecdotal at this point.

For basic diamond frame bicycle, large changes in parameters seem to be needed
for large changes in the dynamics. Most bicycle design parameters are such that
they are within a tight bound in dynamic behavior and differences may not be
readily detectable by the human. Even if they are, we are extremely adaptable
to minor bicycle design variations in term of controllability and handling. The
seems evident even in the front end geometry such as trail, which countless
debates have ensued over the effect of this parameter. Negative trail recumbent
have been designed and the rider can learn ride them, but they provide a higher
learning curve, see the Python Lowracer for an example. These bikes can often
be easily ridden with no hands. With this in mind and the scalability rules
[HandXXXX]_, most bicycles don't really vary much, but this surely doesn't
include tandems, large two wheel cargo bicycles, recumbent designs, etc. And
not to mention the differences in dynamics from a riderless bicycle one with a
rigid rider.  Parameter studies may let us find bicycle designs that don't fit
the normal mold but may still have good handling, see [Kooijman2011]_ for some
examples of exploring the extremes of the parameter space.

I've shown some qualitative comparisons for real and realistic bicycles. I
believe that the open loop weave eigenvalue and the critical speed (if there is
one) does have correlation to what a rider feels when riding a bicycle.
Everyone can agree that balance is more difficult when starting up than we
cruising at speed. The dynamics show that the system becomes more stable and
more controllable (in the control system's sense) as the speed increases. The
weave eigenvalue and critical speed can probably be a good indicator of
stability of normal bicycle designs.

.. rubric:: Footnotes

.. [#] The original method modeled the legs with a two cuboids instead of four
   cylinders.
