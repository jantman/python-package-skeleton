python-package-skeleton
========================

.. image:: https://img.shields.io/pypi/v/python-package-skeleton.svg?maxAge=2592000
   :target: https://pypi.python.org/pypi/python-package-skeleton
   :alt: pypi version

.. image:: https://img.shields.io/github/forks/jantman/python-package-skeleton.svg
   :alt: GitHub Forks
   :target: https://github.com/jantman/python-package-skeleton/network

.. image:: https://img.shields.io/github/issues/jantman/python-package-skeleton.svg
   :alt: GitHub Open Issues
   :target: https://github.com/jantman/python-package-skeleton/issues

.. image:: http://www.repostatus.org/badges/latest/wip.svg
   :alt: Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.
   :target: http://www.repostatus.org/#wip

Introduction here.

Requirements
------------

* Python 3.7+
* ``pip`` (recommended installation method; your OS/distribution should have packages for these)

Installation
------------

It's recommended that you install into a virtual environment (virtualenv /
venv). See the `virtualenv usage documentation <http://www.virtualenv.org/en/latest/>`_
for information on how to create a venv.

.. code-block:: bash

    pip install python-package-skeleton

Configuration
-------------

Something here.

Usage
-----

Something else here.

Bugs and Feature Requests
-------------------------

Bug reports and feature requests are happily accepted via the `GitHub Issue Tracker <https://github.com/jantman/python-package-skeleton/issues>`_. Pull requests are
welcome. Issues that don't have an accompanying pull request will be worked on
as my time and priority allows.

Development
===========

To install for development:

1. Fork the `python-package-skeleton <https://github.com/jantman/python-package-skeleton>`_ repository on GitHub
2. Create a new branch off of master in your fork.

.. code-block:: bash

    $ python -mvenv python-package-skeleton
    $ cd python-package-skeleton && source bin/activate
    $ pip install -e git+git@github.com:YOURNAME/python-package-skeleton.git@BRANCHNAME#egg=python-package-skeleton
    $ cd src/python-package-skeleton

The git clone you're now in will probably be checked out to a specific commit,
so you may want to ``git checkout BRANCHNAME``.

Guidelines
----------

* pep8 compliant with some exceptions (see pytest.ini)
* 100% test coverage with pytest (with valid tests)

Testing
-------

Testing is done via `pytest <http://pytest.org/latest/>`_, driven by `tox <http://tox.testrun.org/>`_.

* testing is as simple as:

  * ``pip install tox``
  * ``tox``

* If you want to pass additional arguments to pytest, add them to the tox command line after "--". i.e., for verbose pytext output on py27 tests: ``tox -e py27 -- -v``
