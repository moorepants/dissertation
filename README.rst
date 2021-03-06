This is a dissertation.

The output can be found here: http://moorepants.github.com/dissertation

Copyright (c) Jason K. Moore 2012

The text and figures are licensed under the Creative Commons Attribution 3.0
Unported License and the source code is licensed under the BSD license (see
LICENSE.txt).

Building the Document
=====================

First clone the dissertation repository::

   $ git clone git://github.com/moorepants/dissertation.git

Install the Sphinx 1.1.3::

   $ pip install sphinx==1.1.3

Install the latest pybtex development version and merge in two branches::

   $ bzr branch lp:pybtex
   $ cd pybtex
   $ bzr merge lp:~matthias-troffaes/pybtex/label-alpha
   $ bzr commit -m "Merged label-alpha."
   $ bzr merge lp:~matthias-troffaes/pybtex/sorting-bugfix
   $ bzr commit -m "Merged sorting-bugfix."
   $ python setup.py install
   $ cd ..

Install the development version of Matthias Troffaes's bibtex Sphinx
extension::

   $ git clone git://github.com/mcmtroffaes/sphinxcontrib-bibtex.git
   $ cd sphinxcontrib-bibtex
   $ python setup.py install
   $ cd ..

The easy method to obtain *all* of the figures and tables is to download the
data file with the pre-generated figures and tables (see below for instructions
on generating the figures and tables from source). This should be extracted
into the ``dissertation`` directory.::

   $ cd dissertation
   $ wget http://mae.ucdavis.edu/~biosport/jkm/dissertation/dissertation-data.tar.bz2 # 73 mb
   $ tar -xjf dissertation-data.tar.bz2

Now build the website::

   $ make html

And the pdf documents::

   $ make webpdf # colored hyperlinks

or::

   $ make printpdf # this one gives black text and inline urls

Open the website in your browser and the pdf in your pdf viewer::

   $ firefox _build/html/index.html
   $ evince _build/latex/HumanControlofaBicycle.pdf

Build Dependencies
------------------

- Sphinx 1.1.3
  [`web <http://sphinx.pocoo.org>`_]
  [`src <https://bitbucket.org/birkenfeld/sphinx>`_]
  [`docs <http://sphinx.pocoo.org/contents.html>`_]
- sphinxcontrib.bibtex dev
  [`web <https://github.com/mcmtroffaes/sphinxcontrib-bibtex>`_]
  [`src <https://github.com/mcmtroffaes/sphinxcontrib-bibtex>`_]
  [`docs <http://sphinxcontrib-bibtex.readthedocs.org/en/latest/index.html>`_]
- pybtex dev
  [`web <http://pybtex.sourceforge.net>`_]
  [`src <https://code.launchpad.net/pybtex>`_]
  [`docs <http://pybtex.sourceforge.net/manual.html>`_]

Generating Figures and Tables From Source
=========================================

I've attempted to generate all of the figures and tables\ [#all]_ in the
dissertation from raw data and scripts. They can be generated by running all of
the scripts in the ``src`` directory. These scripts require several Python,
Matlab, and R based software.

Main Python Dependencies
------------------------

- Python 2.7.3
  [`web <http://www.python.org>`_]
  [`src <http://hg.python.org/cpython>`_]
  [`docs <http://www.python.org/doc>`_]
- setuptools
- NumPy 1.6.2
  [`web <http://www.numpy.org>`_]
  [`src <https://github.com/numpy/numpy>`_]
  [`docs <http://docs.scipy.org/doc/>`_]
- SciPy 0.10.1
  [`web <http://www.scipy.org>`_]
  [`src <https://github.com/scipy/scipy>`_]
  [`docs <http://docs.scipy.org/doc/>`_]
- PyTables 2.4.0
  [`web <http://www.pytables.org>`_]
  [`src <https://github.com/PyTables/PyTables>`_]
  [`docs <http://pytables.github.com/>`_]
- Matplotlib 1.1.1
  [`web <http://matplotlib.sourceforge.net>`_]
  [`src <https://github.com/matplotlib/matplotlib>`_]
  [`docs <http://matplotlib.sourceforge.net>`_]
- IPython 0.13
  [`web <http://ipython.org>`_]
  [`src <https://github.com/ipython/ipython>`_]
  [`docs <http://ipython.org/documentation.html>`_]
- Pandas 0.8.1
  [`web <http://pandas.pydata.org>`_]
  [`src <https://github.com/pydata/pandas>`_]
  [`docs <http://pandas.pydata.org/pandas-docs/stable>`_]
- uncertainties 1.8
  [`web <http://packages.python.org/uncertainties/>`_]
  [`src <https://github.com/lebigot/uncertainties>`_]
  [`docs <http://packages.python.org/uncertainties/>`_]
- SymPy 0.7.1
  [`web <http://www.sympy.org>`_]
  [`src <https://github.com/sympy/sympy>`_]
  [`docs <http://docs.sympy.org>`_]

Main Matlab Dependencies
------------------------

- Matlab 7.10.0.499 (R2010a)
- Matlab Simulink 7.5
- Matlab Control System Toolbox 8.5
- Matlab System Identification Toolbox 7.4

.. note:: Older and newer versions of Matlab and the toolboxes may work, I've
   only tested the code with these versions.

Main R Dependencies
-------------------

- R 2.14.1

Python Development Dependencies
-------------------------------

These are all of the Python packages we've developed for the analysis in the
dissertation. They are required to run many of the Python scripts in the
``src`` directory.

- AutolevToolKit
  [`src <https://github.com/moorepants/AutolevToolKit>`_]
- DynamicistToolKit
  [`src <https://github.com/moorepants/DynamicistToolKit>`_]
- BicycleParameters
  [`src <https://github.com/moorepants/BicycleParameters>`_]
- BicycleDataProcessor
  [`src <https://github.com/moorepants/BicycleDataProcessor>`_]
- CanonicalID
  [`src <https://github.com/moorepants/CanonicalID>`_]
- BicycleID
  [`src <https://github.com/moorepants/BicycleID>`_]
- Yeadon
  [`src <https://github.com/fitze/yeadon>`_]

Matlab Development Dependencies
-------------------------------

These are the Matlab packages we've developed. They are required to run many of
the m-files in the ``src`` directory.

- HumanControl
  [`src <https://github.com/moorepants/HumanControl>`_]
- BicycleSystemID
  [`src <https://github.com/moorepants/BicycleSystemID>`_]

Optional Dependencies
---------------------

My workflow also includes these helpful tools but they are not necessary to
build the dissertation.

- git (http://git-scm.com/)
- pip (http://pypi.python.org/pypi/pip): Useful for pulling releases from PyPi.
- virtualenv (http://pypi.python.org/pypi/virtualenv)
- Autolev 4.1 (http://www.autolev.com/): This software is no longer available,
  but can be used to process the ``.al`` scripts.

Installation
------------

Install main Python dependencies to the system. It is easiest to simply use
your system's package manager (e.g. apt-get) to install all of the
dependencies. For example::

   apt-get install git python-setuptools python-virtualenv python-numpy python-scipy ipython python-matplotlib python-pandas python-sphinx python-tables python-uncertainties

.. warning:: The package manager may not have the latest software versions, so
   you may have to build from source or locate the correct binaries.

To install packages from source use ``pip`` or ``easy_install`` or  download
the source and use ``python setup.py install``.

Now create a directory to house all of the development software.

::

   $ mkdir bicycle-dissertation

Clone all of the python packages developed by us (if you use Github, you should
fork the code in the web interface and then clone from your fork, for easy pull
requests).

::

   $ cd bicycle-dissertation
   $ git clone git://github.com/moorepants/AutolevToolKit.git
   $ git clone git://github.com/moorepants/DynamicistToolKit.git
   $ git clone git://github.com/moorepants/BicycleParameters.git
   $ git clone git://github.com/moorepants/BicycleDataProcessor.git
   $ git clone git://github.com/moorepants/CanonicalID.git
   $ git clone git://github.com/moorepants/BicycleID.git
   $ git clone git://github.com/fitze/yeadon.git

I typically set up a virtual environment for the Python development workflow.
I usually install the main Python dependencies to the system files as they are
typically used by other virtual environments and outside virtual environments,
but it is also possible to install them in the virtual environment which is a
good idea if you need to pin the versions. The virtual environment is not
required but is recommended if you are hacking on the development dependencies.

::

   $ # --system-site-packages allows use of packages installed to the system
   $ # (i.e. access to NumPy, SciPy, IPython, etc
   $ virtualenv --system-site-packages bicycle

Activate the virtual environment.

::

   $ source bicycle/bin/activate

Checkout the dissertation tag in each of the repositories. The dissertation tag
pins the software used when version 1.0 of the dissertation was built, but
future versions of each software package may work too (as long as I keep things
backward compatible).

For example::

   $ cd AutolevToolKit
   $ git checkout dissertation

Then install::

   python setup.py install

or::

   python setup.py develop # do this if hacking on the code

::

   $ cd ..

Repeat for all six Python repositories.

Matlab Install
--------------

Clone the two repositories into the ``bicycle-dissertation`` directory.

::

   $ git clone git://github.com/moorepants/HumanControl.git
   $ git clone git://github.com/moorepants/BicycleSystemID.git

Data
----

The scripts access several sets of data:

- Physical Parameters: The ``data`` directory in the ``BicycleParameters``
  repository has the necessary data to load in the bicycles and riders.
- The Davis bicycle run database can be downloaded here
  http://mae.ucdavis.edu/~biosport/InstrumentedBicycleData/InstrumentedBicycleData.h5.bz2
  [310mb].  To build from raw data files see the ``BicycleDataProcessor``
  README.

.. warning:: The scripts in the ``src`` directory do not create all of the
   figures in the dissertation. Some figures were generated during older
   studies before I had strict coding practices and reproducibility on my mind.
   But all of these figures can be produced from other source code. They just
   aren't that user friendly. Contact me if you want to build those figures.

Paths
-----

This is an absolute mess so far. A lot of the scripts have explicit paths to
the data files which are referenced to my file system. They will have to be
manually changed to reflect the locations on the system you install to.

Generate Figures and Tables
---------------------------

At this point the figures and tables can be generated by running all of the
scripts in the ``src`` directory. The figures and tables are all stored in the
``figures`` and ``tables`` directory and most are auto-generated with the
source code in the ``src`` directory and data stored in the ``data`` directory.

.. rubric:: Footnotes

.. [#all] Most of the figures are generated by the source but some are not. The
   others are either svg figures or created from other source code that hasn't
   been consolidated into the dissertation files.
