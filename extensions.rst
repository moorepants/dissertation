.. _extensions:

================================================
Extensions and modifcations to the Whipple Model
================================================

I present several bicycle models based off of the basic formulation of the
Whipple model in this Chapter. Various combinations of these model extensions
are used in the later Chapters for analysis.

Addition of a lateral force input
=================================

The Whipple model has three input forces roll torque :math:`T_4`, rear wheel
torque :math:`T_6` and steer torque :math:`T_7`. Here I add a lateral force
which acts on a point on the bicycle frame. The force is defined such that is
is always in the :math:`n_2` direction and acts on a point located in the
midplane of the bicycle frame. We make use of this in the analyses in later
chapters because we perturb the bicycle/rider system with an external lateral
force. The vector from the rear wheel center to the point is:

.. math::
   :label: lateralForcePoint

   \bar{r}^{P/D_o} = l_5\hat{c}_1 + l_6\hat{c}_3

The generalized active forces become

.. math::
   :label: lateralForce

   \bar{R}^{D_o} = m_Dg\hat{n}_3 + F^P\hat{n}_2

   \bar{T}^D = T_6\hat{c}_2 + F^P something

The equations of motion can then be formulated with the additional forcing
term. This new input creates a very similar dynamics as the roll torque.

Leaning rider extension
=======================

A typical assumption is that a rider can control a bicycle by leaning their
body relative to the bicycle frame. This is especially drawn for the no-hands
riding case. A simple leaning rider can be modeled by adding an additional
rider lean degree of freedom.

David de Lorenzo extension (3 rider dof)
========================================

Addition of rider arms
======================

Addition holonomic contraints
-----------------------------

Linearization
-------------

Comparison to Arend's model
---------------------------

Flywheel in the front wheel
===========================

Swing bike
==========

Flexible rider (hip rotation, back lean and twist)
==================================================

Roll angle trailer
==================
