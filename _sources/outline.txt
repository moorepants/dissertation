=======
Outline
=======

Preface
=======

* Introduction
* Reproducibility
* Host while I write

Acknowledgements
================

* Hubbard
* Luke
* Arend
* Jodi
* Jim
* Grad interns: Danique, Peter, Chris, Gilbert
* Undergrad interns
* Others...

Abstract
========

Introduction
============

* The bicycle as a dynamic system
* Motivation
* General literature review

Bicycle Equations of Motion
===========================

* Overview of general types of bicylce models

  * Simple bicycle models
  * Bicycle models with stability
  * Complex models (motorcycle)

    * Tire models
    * Flexible rider
    * Shocks and flexible frames

* Derivation of the Whipple model

  * Geometry and positions

    * Parameter choice
    * Symmetry

  * Inertial

    * Mass
    * Center of mass
    * Inertia

  * Velocities

    * Mass centers
    * Contact points

  * Accelerations

    * Mass centers

  * Holonomic constraint
  * Non-holonomic constraints
  * Fr + Fr* = 0
  * Non-linear simulation
  * Linearization
  * Linear simulation
  * Comparison to benchmarks

    * Meijaard 2007
    * Basu-Mandal 2007

Extensions and modifcations to the Whipple Model
================================================

* Addition of a lateral force input
* Leaning rider extension
* David de Lorenzo extension (3 rider dof)
* Addition of rider arms

  * Addition holonomic contraints
  * Linearization
  * Comparison to Arend's model

* Flywheel in the front wheel
* Swing bike
* Flexible rider (hip rotation, back lean and twist)
* Roll angle trailer

Measurement and Calculation of Physical Parameters
==================================================

* Introduction

  * Motivation
  * Literature review

* Bicycle parameters

  * Measurement methods and experimental setup
  * Bicycles

    * Fisher
    * Batavus Browser
    * Instrumented Batavus Browser
    * Bianchi Pista
    * Yellow bike
    * Yellow bike with reversed fork
    * Batavus Crescendo
    * Batavus Stratos
    * UCD Instrumented Bicycle
    * Gyrobike

  * Calculations

    * Uncertainties in parameters
    * Geometry
    * Mass
    * Center of mass
    * Inertia

* Human Parameters

  * Simple geometrical method by Moore
  * Complex geometrical method by Yeadon

* Combining bike and rider
* Extracting different parameters for different models (rider parameters)
* Parameter conversions
* Comparison to other measured bikes

Parameter Studies
=================

* Variation of parameters and effects to linear stability
* Comparison of the linear properties of real bicycles

Delft Instrumented Bicycle
==========================

* Sensor and instrumentation design
* Experiment design

  * Treadmill
  * Around town

* Data visualization GUI
* Data analysis
* Results

Motion Capture
==============

* Experiment design

  * Equipment
  * Manuevers
  * Riders

* Principal Component Analysis
* Simple Statistics

Davis Instrumented Bicycle
==========================

* Instrumentation design

  * Bicycle frame
  * Steer torque
  * Rates and accelerations
  * Lateral Force
  * Rider rigidification
  * Wiring diagram
  * Data aquisition
  * Time sychronization
  * Roll angle trailer

* DAQ Software

Control
=======

* Review of control models
* Review of manual control
* Our manual control model
* Manuevers

  * Single and double lane change
  * Lateral disturbance

Handling
========

* Review of handling
* Thoughts on bicycle handling
* Ron's analytical method
* Comparison of different bicycles

Davis Experiments
=================

* Experimental Design

  * Environments

    * Treadmill
    * Gym

* Manuevers

  * Balance
  * Track Line
  * Disturbance
  * Blind
  * Riders

System Identification
=====================

* Introduction and review
* Model fitting
* Control parameter estimation
* Effects of rider, environment, speed and manuever to human control
