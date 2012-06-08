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
identify with it, but the next question (as is with most research), is "What
application is that good for?". As an engineer, we are trained to be
application minded. It is certainly what drove me to start down this path in
the first place. There is an answer to this second question, but over the years
I've gotten less enthusiastic about trying to justify why I'm working on this
project with respect to an immediate application. An many ways this is simply
the reality for the growing scientist. It becomes obvious that basic science
simply needs to be performed, other even without regards to what it may or may
not accomplish. The benefits down the road are inevitable and there is a large
body of evidence to support that. But nonetheless my initial curiosity of bicycle
dynamics is rooted in application and still is in many ways but I'm content
with understanding difficult problems for basic progression in learning and
science.

My first inquiries about bicycle dynamics came from my attempts to design a
recumbent bicycle frame for my senior design project at Old Dominion
University. Recumbents are notorious for not being that easy to ride and we
were building one for the annual ASME Human Powered Vehicle challenge which
would be especially unusual with the extremely low center of gravity. It needed
to be suitable for novice riders to control. I found myself in the design
process where one needs to choose the wheel sizes, front end geometry and
location and seating position of the rider. As a young engineer is taught, I
went looking for technical guidelines to choose these parameters for our
bicycle design. But all I came back with were many conflicting ideas from
various bicycle fabricators and the book Bicycling Science 2nd Ed [WilsonXXXX]_
which gave a synopsis of Jones', [Jones1970]_, conclusions from his famous
study on the stability of bicycles. I studied this in detail and designed my
bicycle geometry to be exactly what was specified as good handling by Jones.
[#tubes]_ The bicycle turned out to be rideable (after lots of practice), but
this was probably the first time I realized in my engineering career that there
wasn't a formula for everything.

These particulars fell onto the back burner as I finished out my work at the
Langley Full Scale Tunnel and did not re-emerge until a few classes at UC Davis
brought these concepts back into my picture. In particular, I attempted to
derive the equations of motion of the bicycle in Mont Hubbard's multi-body
dynamics class in the beginning of 2006 and the power to potentially properly
answer the questions I had back at Old Dominion seemed to be at my finger tips.
Little did I realize, that those answers simply introduce more difficult
questions and a research project is born.

I hope that this dissertation will document the majority of work I've done and
my thoughts on bicycle dynamics, control, and handling at UC Davis and TU Delft
since around December 2006. I of course won't be able to add it all, especially
since most of it has been written at the end of the project rather than as I
went along, but this should be a good picture of what all transpired.

Reproducibility
===============

Over the past few years, I've begun realize how reproducibility is crucial for
science to improve and grow rapidly all the while building a deeply intact and
strong foundation for future researchers and that it may not be as reproducible
as we may all think it is. With that in mind, I have put a great deal of effort
into making my work more accessible, reusable and ultimately reproducible which
is the cornerstone of all scientific understanding. For the type of work
presented, the majority is computational and the computer along with software
have enabled our generation to make the work reproducible without too much
extra effort. My intention is provide enough information in the form of data,
source code, and writing, that others will have a *relatively* easy time
reproducing my work. This has been mostly possible in the time frame that I've
had to complete the work, but there are some holes in particular with respect
to the work done in the earlier years of the project.

Literature
----------

I really enjoy reading older dissertations and technical reports because they
typically have so much detail. Much more than any journal paper will ever have.
I find these details to be invaluable for developing new research plans and
understanding. This is especially when the null science is reported, which
gives you a much better idea of what not to do. My dissertation is modeled
after these type of longer documents and I've attempted to include as much
detail in the decision making processes, methods and results as possible in
the allowable time.

This dissertation is partly original work that had not been published in any
form yet and partly based on several journal and conference papers that I have
written or co-authored over the years. I've given an outline below of the
papers which have been subsumed into this thesis.

[Findlay2006]_
   This is an internal report I worked on with two other students in my
   controls class. We developed several controllers for a simple bicycle model.
   Some elements of this paper influenced Chapter :ref:`control`.
[Moore2006]_
   This is the internal report I wrote which described my first effort at
   deriving the equations of motion of the bicycle [#]_, estimating the physical
   parameters of the bicycle/rider, and running a numerical parameter study.
[Moore2007]_
   Luke and I wrote this short paper for the 11th International Symposium on
   Computer Simulation in Biomechanics in Tainan, Taiwan. We presented a basic
   rider biomechanic extension to the Whipple model which I had developed in
   [Moore2006]_. This work contributes to Chapter :ref:`extensions`.
[Moore2008]_
   This is the polished and corrected version of my work I did in [Moore2006]_
   which I submitted to the 2008 International Sports Engineering Conference in
   Biarritz, France. The model derivation is written out thoroughly in Chapter
   :ref:`eom`, the physical parameter estimation in Chapter
   :ref:`physicalparameters`, and the parameter studies in Chapter
   :ref:`parameterstudy`.
[Kooijman2008a]_
   Jodi presented this paper at a conference in Hungary not long after I had
   been in the Netherlands. It contained the results from the experimental
   studies we'd done during my first few months in Delft.
[Moore2009b]_
   I presented this paper at the 2009 Multibody Dynamics conference in Warsaw,
   Poland. This work focused on the motion identification experiments we did
   early in 2009.
[Moore2009a]_
   This paper presented a combination of the bicycle measurement technique used
   in [Kooijman2006]_ and an improved version of the human inertia estimation
   technique I developed in [Moore2006]_. I presented it at the 2009 ASME
   conference in San Diego, CA. [#]_
[Kooijman2009a]_
   This is a polished version of [Kooijman2008a]_. Jodi presented it at the
   2009 ASME conference. This work is presented in Chapter :ref:`delftbicycle`.
[Moore2010]_
   This is a report on the work I did in the last few months I spent in Delft
   in which I used a modified technique from [Kooijman2006]_ to more accurately
   measure the physical parameters of a variety of bicycles. I presented it as
   a poster at the first Bicycle and Motorcycle Dynamics Conference in 2010.
[Moore2010a]_
   Jodi presented this paper for me at the International Sports Engineering
   Conference in 2010. It was about some extra statistical analyses of the data
   we collected in [Moore2009a]_. This work can be found in Chapter
   :ref:`motioncapture`.
[Peterson2010]_
   Dr. Hubbard presented this paper for us at the ISEA conference in 2010. It
   gave a premature look at the instrumented/robot bicycle we were developing.
[Moore2011]_
   The paper we wrote for the Warsaw conference, [Moore2009b]_, was accepted to
   be published in Multibody System Dynamics. This is mostly a polished version
   of [Moore2009b]_. This work is presented in Chapter :ref:`motioncapture`.
[Hess2012]_
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
techniques are very rarely, if at all, taught to engineers and once I got a
taste of the development methods of software engineers and computer scientists
I couldn't believe how poorly we engineers execute our code. Not only does
creating usable and well documented code help others to use it, it helps you to
know what it is an be able to use it and is documented proof of working
methods. I have no idea how much code "waste" is on my hard drive that I will
never have the time to decipher again and make use of it.

I have several layers of code that supports this document. In general all of
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
   A GTK Gui for visualizing the bicycle model identification data.
`BicycleParameters <http://pypi.python.org/pypi/BicycleParameters>`_ (Python)
   A program that generates the physical parameters of a bicycle and rider
   from experimental measurements. It also allows for basic manipulation basic
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
   An implementation of our bicycle human control model from [Hess2012]_ and
   Chapter :ref:`control`. It computes the controller parameters for most
   bicycles and most speeds, simulates the model during lane changes, and
   computes a handling quality metric.
`MotionCapture <https://github.com/moorepants/DynamicistToolKit>`_ (Python & Matlab)
   A Matlab GUI tool for interactively exploring the data from the bicycle
   motion capture experiments and python tools for basic statistics.
`Yeadon <http://pypi.python.org/pypi/yeadon>`_ (Python)
   A program that computes the inertia of a human using the method from
   [Yeadon1990]_.

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

.. todo:: Maybe do proper citations to these in the bibliography

Data
----

During the experimental studies, I've collected a fair amount of data. I've
worked to provide at least the raw data from the experimental studies with
enough meta data for it to be reusable. Also, the data is used directly with
the software packages above.

I've taken extensive photo documentation of the instrumentation construction
and the experiments. The albums are divided into ones of the work done at `UC
Davis <http://picasaweb.google.com/moorepants/BicycleDynamics#>`_ and the work
done at `TU Delft
<http://picasaweb.google.com/moorepants/BicycleDynamicsTUDelft>`_.

I've made several data sets available from all of the experimentation.

.. todo:: add the links to the data sets and videos

Physical Parameters
   The physical parameter data consists of measured values such as geometry
   and mass of both the bicycles and the riders.
Delft Instrumented Bicycle
   This data is in the form of comma separated text files with the time
   histories of the sensors and accompanying meta data in the header of each
   file. The various treadmill experiments with two riders are included. This
   includes video data for each of the runs
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
   of the sensors in multiple arrays and the meta data in tables. There is
   video data of all the runs.

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

- The content should be written presentation neutral.
- The primary presentation view is through a web browser, but a static PDF
  version is also available to suit UCD's archaic submission rules.
- The source code for all the figures, animations, and interactive bits should
  be included with the dissertation.
- The experimentally collected data should all be available for download and
  use by others.
- Software tools should be developed if at all possible, instead of
  disconnected scripts.

I've made use of the `Sphinx <http://sphinx.pocoo.org/>`_ publishing platform
to write my dissertation and meet these goals. The source, which is written in
reStructuredText, is available along with the source code for the figures at

`<https://github.com/moorepants/dissertation>`_

and the HTML version can be viewed and the PDF version downloaded at

`<http://moorepants.github.com/dissertation>`_

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
bicycle: mine which follows a Kane-like syntax and the one adopted from
[Meijaard2007]_.

License
=======

The written work and data are licensed under the `Creative Commons Attribution
3.0 Unported License <http://creativecommons.org/licenses/by/3.0/>`_.

You may share, rework, and use any of the materials provided you cite this work

*Moore, J. K., Human Control of a Bicycle, UC Davis Doctoral Dissertation, 2012*

All of the source code is licensed explicitly in the src directory under a BSD
license.

.. rubric:: Footnotes

.. [#tubes] It wasn't till after welding the bicycle frame together did I
            realize that I'd cut a tube too long and the geometry was very
            different than I'd planned.
.. [#] The equations derived here are slightly incorrect.
.. [#] This was a poor presentation as I arrove in San Diego after living for a
   year in the Netherlands. My mind was lost in experiencing everything I
   missed about my home country and I couldn't focus on getting the
   presentation done.
