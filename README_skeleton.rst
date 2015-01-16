python-package-skeleton
========================

.. image:: https://pypip.in/v/python-package-skeleton/badge.png
   :target: https://crate.io/packages/python-package-skeleton

.. image:: https://pypip.in/d/python-package-skeleton/badge.png
   :target: https://crate.io/packages/python-package-skeleton

.. image:: https://landscape.io/github/jantman/python-package-skeleton/landscape/landscape.svg
   :target: https://landscape.io/github/jantman/python-package-skeleton/landscape
   :alt: Code Health

.. image:: https://secure.travis-ci.org/jantman/python-package-skeleton.png?branch=master
   :target: http://travis-ci.org/jantman/python-package-skeleton
   :alt: travis-ci for master branch

.. image:: https://codecov.io/github/jantman/python-package-skeleton/coverage.svg?branch=master
   :target: https://codecov.io/github/jantman/python-package-skeleton?branch=master
   :alt: coverage report for master branch

.. image:: http://www.repostatus.org/badges/0.1.0/active.svg
   :alt: Project Status: Active - The project has reached a stable, usable state and is being actively developed.
   :target: http://www.repostatus.org/#active

Introduction here.

Requirements
------------

* Python 2.7+ (currently tested with 2.7, 3.2, 3.3, 3.4)
* Python `VirtualEnv <http://www.virtualenv.org/>`_ and ``pip`` (recommended installation method; your OS/distribution should have packages for these)

Installation
------------

It's recommended that you install into a virtual environment (virtualenv /
venv). See the `virtualenv usage documentation <http://www.virtualenv.org/en/latest/>`_
for information on how to create a venv. If you really want to install
system-wide, you can (using sudo).

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

    $ virtualenv python-package-skeleton
    $ cd python-package-skeleton && source bin/activate
    $ pip install -e git+git@github.com:YOURNAME/python-package-skeleton.git@BRANCHNAME#egg=python-package-skeleton
    $ cd src/python-package-skeleton

The git clone you're now in will probably be checked out to a specific commit,
so you may want to ``git checkout BRANCHNAME``.

Guidelines
----------

* pep8 compliant with some exceptions (see pytest.ini)
* 100% test coverage with pytest (with valid tests) (note that until
  https://github.com/lemurheavy/coveralls-public/issues/31 is fixed, you
  need to check the ``cov`` output for branch coverage, coveralls can't
  be relied on).

Testing
-------

Testing is done via `pytest <http://pytest.org/latest/>`_, driven by `tox <http://tox.testrun.org/>`_.

* testing is as simple as:

  * ``pip install tox``
  * ``tox``

* If you want to see code coverage: ``tox -e cov``

  * this produces two coverage reports - a summary on STDOUT and a full report in the ``htmlcov/`` directory

* If you want to pass additional arguments to pytest, add them to the tox command line after "--". i.e., for verbose pytext output on py27 tests: ``tox -e py27 -- -v``

Release Checklist
-----------------

1. Open an issue for the release; cut a branch off master for that issue.
2. Confirm that there are CHANGES.rst entries for all major changes.
3. Ensure that Travis tests passing in all environments.
4. Ensure that test coverage is no less than the last release (ideally, 100%).
5. Increment the version number in python-package-skeleton/version.py and add version and release date to CHANGES.rst, then push to GitHub.
6. Confirm that README.rst renders correctly on GitHub.
7. Upload package to testpypi, confirm that README.rst renders correctly.

   * Make sure your ~/.pypirc file is correct
   * ``python setup.py register -r https://testpypi.python.org/pypi``
   * ``python setup.py sdist upload -r https://testpypi.python.org/pypi``
   * Check that the README renders at https://testpypi.python.org/pypi/python-package-skeleton

8. Create a pull request for the release to be merge into master. Upon successful Travis build, merge it.
9. Tag the release in Git, push tag to GitHub:

   * tag the release. for now the message is quite simple: ``git tag -a vX.Y.Z -m 'X.Y.Z released YYYY-MM-DD'``
   * push the tag to GitHub: ``git push origin vX.Y.Z``

11. Upload package to live pypi:

    * ``python setup.py sdist upload``

10. make sure any GH issues fixed in the release were closed.
