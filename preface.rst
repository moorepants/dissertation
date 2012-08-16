=======
Preface
=======

.. warning::

   This document is a draft which is updated regularly (Last updated |today|).
   Once I submit if for my doctoral degree at UC Davis, it will be done. So for
   now use at your own risk. The information may or may not be correct.
   Reviews, comments and suggestions are welcome.

Introduction
============

The typical conversation with someone I've met over the past years that I've
been a graduate student inevitably comes to this: "So what do you do in
graduate school?". My reply is "I study how people balance on bicycles". This
is a great conversation starter as almost everyone recalls learning how to ride
a bicycle. It is something we weren't born to do and we almost always remember
the feeling of learning the skill. It is typically quite a momentous occasion
in most folks' lives. Usually everyone thinks the research is cool and can
identify with it, but the next question (as with most research), is "What
application is that good for?". As an engineer, we are trained to be
application minded. It is certainly what drove me to start down this path in
the first place. There is an answer to this second question, but over the years
I've gotten less enthusiastic about trying to justify why I'm working on this
project with respect to an immediate application. In many ways this is simply
the reality for the growing scientist. It becomes obvious that basic science
simply needs to be performed, without regard to what it may or may
not accomplish. The benefits down the road are inevitable and there is a large
body of evidence to support that. But nonetheless my initial curiosity about bicycle
dynamics is rooted in application and it still is in many ways. But I'm content
with understanding difficult problems for basic progression in learning and
science.

My first inquiries about bicycle dynamics came from my attempts to design a
recumbent bicycle frame for my senior design project at Old Dominion
University. Recumbents are notorious for not being that easy to ride and we
were building one for the annual ASME Human Powered Vehicle challenge which
would be especially unusual with an extremely low center of gravity. It needed
to be suitable for novice riders to control. I found myself in the design
process where one needs to choose the wheel sizes, front end geometry and
location and seating position of the rider. As a young engineer is taught, I
went looking for technical guidelines to choose these parameters for our
bicycle design. But all I came back with were many conflicting ideas from
various bicycle fabricators and the book Bicycling Science 2nd Ed :cite:`Whitt1982`
which gave a synopsis of Jones' :cite:`Jones1970` conclusions from his famous study
on the stability of bicycles. I studied this in detail and designed my bicycle
geometry to be exactly what was specified as good handling by Jones.\ [#tubes]_
The bicycle turned out to be rideable (after lots of practice), but this was
probably the first time I realized in my engineering career that there isn't a
formula for everything.

These particulars fell onto the back burner as I finished my work at the
Langley Full Scale Tunnel and did not re-emerge until a few classes at UC Davis
brought these concepts back into my picture. In particular, I attempted to
derive the equations of motion of the bicycle in Mont Hubbard's multi-body
dynamics class at the beginning of 2006 and the power to potentially properly
answer the questions I had back at Old Dominion seemed to be at my finger tips.
Little did I realize that those answers simply introduced more difficult
questions and a research project was born.

This dissertation documents most of the work I've done and my thoughts on
bicycle dynamics, control, and handling at UC Davis and TU Delft since around
December 2006.

Reproducibility
===============

Over the past few years, I've begun realize how reproducibility is crucial for
science to improve and grow rapidly, all the while building a deeply intact and
strong foundation for future researchers and that it may not be as reproducible
as we may all think. With that in mind, I have put a great deal of effort into
making my work more accessible, reusable, and ultimately reproducible, which is
the cornerstone of all scientific understanding. For the type of work presented
here, the majority is computational and the computer along with software have
enabled our generation to make the work reproducible without too much extra
effort. My intention is provide enough information in the form of data, source
code, and writing, that others will have a *relatively* easy time reproducing
my work. This has been mostly possible in the time frame that I've had to
complete the thesis, but there are some holes in particular with respect to the
work done in the earlier years of the project.

Literature
----------

I really enjoy reading older dissertations and technical reports because they
typically have so much detail, much more than any journal paper will ever have.
I find these details to be invaluable for developing new research plans and
understanding. This is especially true when the null science is reported, which
gives a much better idea of what not to do. My dissertation is modeled after
these longer documents and I've attempted to include as much detail in the
decision making processes, methods, and results as possible.

This dissertation is partly original work that has not been published in any
form and partly based on several journal and conference papers that I have
written or co-authored over the years. I've given an outline below of the
papers which have been subsumed into this thesis.

:cite:`Findlay2006`
   This is an internal report done with two other students in my modern
   controls class. We developed several controllers for a simple bicycle model.
   Some elements of this paper influenced Chapter :ref:`control`.
:cite:`Moore2006`
   This is the internal report which described my first effort at deriving the
   equations of motion of the bicycle\ [#equations]_, estimating the physical
   parameters of the bicycle/rider, and running a numerical parameter study.
:cite:`Moore2007`
   Luke Peterson and I wrote this short paper for the 11th International
   Symposium on Computer Simulation in Biomechanics in Tainan, Taiwan. We
   presented a basic rider biomechanic extension to the Whipple model which I
   had developed in :cite:`Moore2006`. This contributes directly to Chapter
   :ref:`extensions`.
:cite:`Moore2008`
   This is the polished and corrected version of :cite:`Moore2006` which was
   submitted to the 2008 International Sports Engineering Conference in
   Biarritz, France. The model derivation is written out thoroughly in Chapter
   :ref:`eom`, the physical parameter estimation in Chapter
   :ref:`physicalparameters`, and the parameter studies in Chapter
   :ref:`parameterstudy`.
:cite:`Kooijman2008a`
   Jodi Kooijman presented this paper at a conference in Hungary not long after
   I had been in the Netherlands. It contained the results from the
   experimental studies we did during my first few months in Delft.
:cite:`Moore2009b`
   I presented this paper at the 2009 Multibody Dynamics conference in Warsaw,
   Poland. This work focused on the motion identification experiments we did
   early in 2009.
:cite:`Moore2009a`
   This paper presented a combination of the bicycle measurement technique used
   in :cite:`Kooijman2006` and an improved version of the human inertia estimation
   technique developed in :cite:`Moore2006`. I presented it at the 2009 ASME
   conference in San Diego, CA.\ [#sandiego]_
:cite:`Kooijman2009a`
   This is a polished version of :cite:`Kooijman2008a`. Jodi Kooijman presented it
   at the 2009 ASME conference. This work is presented in Chapter
   :ref:`delftbicycle`.
:cite:`Moore2010`
   This is a report on the work I did in the last few months I spent in Delft
   in which I used a modified technique from :cite:`Kooijman2006` to more accurately
   measure the physical parameters of a variety of bicycles. I presented it as
   a poster at the first Bicycle and Motorcycle Dynamics Conference in 2010.
:cite:`Moore2010a`
   Jodi Kooijman presented this paper for me at the International Sports
   Engineering Conference in 2010. It was about simple statistical analyses
   of the data we collected in :cite:`Moore2009a`. This work can be found in Chapter
   :ref:`motioncapture`.
:cite:`Peterson2010`
   Dr. Hubbard presented this paper for us at the ISEA conference in 2010. It
   gave a preliminary look at the instrumented/robot bicycle we were developing.
:cite:`Moore2011`
   The paper written for the conference in Warsaw, :cite:`Moore2009b`, was accepted
   to be published in Multibody System Dynamics. It is a polished version of
   :cite:`Moore2009b` and is presented in Chapter :ref:`motioncapture`.
:cite:`Hess2012`
   This work was originally presented at the Bicycle and Motorcycle Dynamics
   conference in 2010 and eventually published by IEEE in 2012. The work is
   expanded on and detailed in Chapter :ref:`control`.

Source Code
-----------

It is very possible to code every computation that an engineer does and in many
ways the most preferable method to record it. It is not only a record of the
working computation that contains all of the details needed but an executable
source that can be reused. But this doesn't mean one can simply drop all of
their undocumented scripts into a folder, publish it to the web and expect
anyone to ever be able to decipher it and actually use it. It takes much more
effort to document the source code and to put it into a usable form. These
techniques are very rarely, if at all, taught to engineers. Once I got a
taste of the development methods of software engineers and computer scientists
I couldn't believe how poorly we engineers execute our code. Not only does
creating usable and well documented code help others to use it, but it helps
you to know what it is and be able to reuse it yourself. It is documented proof
of working methods. I have no idea how much code "waste" is on my hard drive
that I will never have the time to decipher again and make use of it.

I have several layers of code that supports this document. In general, all of
the figures and tables are generated by scripts in the `src` directory included
with the source to this dissertation. These scripts access a variety packages
in my software stack with most of them being open source packages that I or
some of my collaborators have written. The following gives a list of the
packages we've developed:

.. todo:: include the git commit hashes for the version that works with the
   theses data

`AutolevToolKit <https://github.com/moorepants/AutolevToolKit>`_ (Python)
   A collection of tools which parse `Autolev <http://www.autolev.com>`_
   output for extracting the equations of motion and some basic tool to
   convert them to LaTeX. It has a prototype of a numerical dynamic system
   class with accompanying linear dynamic system class to make basic analysis
   quick and painless.
`BicycleDAQ <https://github.com/moorepants/BicycleDAQ>`_ (Matlab)
   A GUI tool that collects time series and meta data from the instrumented
   bicycle via the NI USB-6218 data acquisition board and the VectorNav VN-100.
   It has tools for also collecting calibration data for the various sensors.
`BicycleDataProcessor <https://github.com/moorepants/BicycleDataProcessor>`_ (Python)
   A tool that stores all of the data collected from the instrumented bicycle
   in a database for easy retrieval and manipulation. It also processes the
   raw data into the variables of interest, so you can directly compare it
   with models.
`BicycleID <https://github.com/moorepants/BicycleID>`_ (Python
   A GTK GUI for visualizing the bicycle model identification data.
`BicycleParameters <http://pypi.python.org/pypi/BicycleParameters>`_ (Python)
   A program that generates the physical parameters of a bicycle and rider
   from experimental measurements. It also allows for basic manipulation and
   analysis with some widely used models.
`BicycleSystemID <https://github.com/moorepants/BicycleSystemID>`_ (Matlab & Python)
   A set of tools for interacting with the Matlab System ID toolbox. It has
   functions built around the grey and black box identification of several
   bicycle, rider and control models.
`CanonicalBicycleID <https://github.com/moorepants/CanonicalBicycleID>`_ (Python)
   A module for identifying a 4th order bicycle model from the canonical form.
`DelftBicycleDataViewer <https://github.com/moorepants/DelftBicycleDataViewer>`_ (Matlab)
   A prototype video and data viewer for the Delft instrumented bicycle data.
`DynamicistToolKit <https://github.com/moorepants/DynamicistToolKit>`_ (Python)
   A clearing house for all the generic functions and classes that I write
   that may be useful across all the work I do.
`HumanControl <https://github.com/moorepants/HumanControl>`_ (Matlab)
   An implementation of our bicycle human control model from :cite:`Hess2012` and
   Chapter :ref:`control`. It computes the controller parameters for most
   bicycles and most speeds, simulates the model during lane changes, and
   computes a handling quality metric.
`MotionCapture <https://github.com/moorepants/DynamicistToolKit>`_ (Python & Matlab)
   A Matlab GUI tool for interactively exploring the data from the bicycle
   motion capture experiments and python tools for basic statistics.
`Yeadon <http://pypi.python.org/pypi/yeadon>`_ (Python)
   A program that computes the inertia of a human using the method from
   :cite:`Yeadon1990`.

This software stack is built upon several languages and software packages
including: Python_, NumPy_, SciPy_, Matplotlib_, PyTables_, Pandas_, Uncertainties_,
SymPy_, Autolev_, Matlab_.

.. _Python: http://www.python.org
.. _NumPy: http://www.numpy.org
.. _SciPy: http://www.scipy.org
.. _Matplotlib: http://matplotlib.sourceforge.net/
.. _PyTables: http://www.pytables.org
.. _Pandas: http://pandas.pydata.org/
.. _Uncertainties: http://pypi.python.org/pypi/uncertainties/
.. _SymPy: http://www.sympy.org
.. _Autolev: http://www.autolev.com
.. _Matlab: http://www.mathworks.com/products/matlab/

.. todo:: Make proper citations to all of these pieces of software and put them
   in the bibiliography.

Data
----

During the experimental studies, I've collected a fair amount of data and have
worked to provide at least the raw data from the experimental studies with
enough meta data for it to be reusable. Also, the data is used directly with
the software packages above. All of the data described below is accessible
through the bicycle data page on our lab website:
`<http://biosport.ucdavis.edu/research-projects/bicycle/data>`_.

.. todo:: Add direct links to the data sets and videos if available before
   publishing.

Physical Parameters
   The physical parameter data consists of measured values, such as geometry
   and mass, of both the bicycles and the riders.
Delft Instrumented Bicycle
   This data is in the form of comma separated text files with the time
   histories of the sensors and accompanying meta data in the header of each
   file. The various treadmill experiments with two riders are included. This
   includes video data for each of the runs.
Motion Capture
   This data set includes Matlab mat files for each run for several days of
   experimenting with several riders on the treadmill. There is also video data
   for a good portion of the runs.
`Steer Torque Experiments <http://archive.org/details/BicycleSteerTorqueExperiment01>`_
   There is video data for each run and also the manually derived comma
   separated value text file with the torque values determined from the video.
Identification Experiments
   This data is available both as raw data mat files with included meta data
   for each run and as a single HDF5 database which stores the time histories
   of the sensors in multiple arrays and the meta data in tables. Video data of
   all the runs were also recorded.
Photos
   I've taken extensive photo documentation of the instrumentation construction
   and the experiments. The albums are divided into ones of the work done at
   `UC Davis <http://picasaweb.google.com/moorepants/BicycleDynamics#>`_ and
   the work done at `TU Delft
   <http://picasaweb.google.com/moorepants/BicycleDynamicsTUDelft>`_.

Dissertation website
====================

I decided to publish my dissertation publicly on the internet from the day I
started writing it. The first reason for this is that I want to take full
advantage of the ability the web offers for conveying ideas and information,
whether it be a video or an interactive program. Paper-based publication is a
thing of the past and is an unbelievably limited form of sharing, especially in
science. Secondly, I want the process of writing my dissertation to be in the
open with the ability for anyone to offer comments, suggestions and edits.
Dissertations are traditionally considered to be the work of a single
individual, but that is never true. All the research we do as scientists is
built upon the works of others and rarely does anyone produce their work
without the help of others. Dissertations in the USA are typically very
individualistically oriented but I've begun to believe that we should strive to
move away from the idea that some work is only due to one person and embrace
the fact that we need help from many people to complete something like a
dissertation for a doctoral degree. So it is best to be collaborative from the
beginning with a sufficient mechanism to provide credit where credit is due. I
also want this work to be the best it can be, and if others are interested in
helping me make it that way then an interactive website is a platform that is
capable of promoting this.

I desired to follow these basic rules when writing my dissertation:

- The content should be written presentation format neutral.
- The primary presentation view is through a web browser, but a static PDF
  version is also available to suit UCD's archaic submission rules.
- The source code for all the figures, animations, and interactive bits should
  be included with the dissertation.
- The experimentally collected data should all be available for download and
  use by others.
- Software tools should be developed if at all possible, instead of
  disconnected scripts.

Based on these goals, I choose the `Sphinx <http://sphinx.pocoo.org/>`_
publishing platform for my dissertation. The text source, which is written in
reStructuredText, is available along with the source code for the figures at
`<https://github.com/moorepants/dissertation>`_. The HTML version can be viewed
and the PDF version downloaded at
`<http://moorepants.github.com/dissertation>`_

Writing Style
=============

I generally find scientific writing in my field to be extremely dry. We've
developed a collective style that removes any material that isn't technical
from the articles and this in turn causes us to gloss over the fact that people
are behind all of the reported research. These people have ideas, struggles,
mishaps, revelations, and sometimes even fun. But these things weren't always
hidden. Early engineering articles ended with lengthy personal conversations
between the reviewers and the authors (:cite:`Wilson-Jones1951`,
:cite:`Kondo1955`) and include much more artistic and beautiful illustrations.
Page limits in journal and conference articles force today's writer to make
their writing as dry as possible to maximize the amount of technical content.
I'm no writing ace, but have decided to inject some of the humanism that comes
along with a project than spans seven years of ones life into this text. I
mostly corralled these ramblings in the prefaces and footnotes of the chapters,
but some has sneaked into the drier areas too. I hope that these asides give
some idea of how all of this work developed and who to attribute the ideas and
labor to along with breaking up the monotony of the technical parts of the
text. I figured that a dissertation will be one of the few writings in my
career that provides a chance to do this.

Attribution
===========

As a child, I was programmed to think that any form of plagiarism was evil: you
shouldn't copy anything. But how would we ever make any progress if we didn't
copy and improve on what others have done in the past? The work presented here
is mostly based on the work that I have done in the past several years, but
there are many other people's work that is wrapped up in it. Their
writings and thoughts will inevitably be present in this text. I do not claim
these as my own, but they will be required to tell the story of the research. I
will do my best to acknowledge everyone's work in this thesis, but there will
surely be some that I have forgotten. Please let me know if that is so, and I
will remedy it.

Notation
========

I attempt to keep notation consistent throughout each chapter, with much of the
notation being consistent throughout the dissertation. The extensions chapter
has different notation for each model. The notation for the Chapter is given at
the end of each Chapter. There are ultimately two notations forms for the
bicycle: mine which follows a Kane-like syntax and the one adapted from
:cite:`Meijaard2007`.

License
=======

The written work and data are licensed under the `Creative Commons Attribution
3.0 Unported License <http://creativecommons.org/licenses/by/3.0/>`_.

You may share, rework, and use any of the materials provided you cite this work

*Moore, J. K., Human Control of a Bicycle, UC Davis Doctoral Dissertation, 2012*

All of the source code is licensed explicitly in the src directory under a BSD
license.

.. rubric:: Footnotes

.. [#tubes] It was not untill after welding the bicycle frame together that I
   realized that I'd cut a tube too long and the geometry was very different
   than I'd planned.

.. [#equations] The equations derived here are slightly incorrect.

.. [#sandiego] I remember this being a poor presentation on my part. I arrived in San
   Diego after living for a year in the Netherlands. My mind was lost in
   experiencing everything I missed about my home country and I couldn't focus
   on properly preparing for the presentation.
