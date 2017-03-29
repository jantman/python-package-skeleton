python-package-skeleton
========================

.. image:: http://www.repostatus.org/badges/0.1.0/active.svg
   :alt: Project Status: Active - The project has reached a stable, usable state and is being actively developed.
   :target: http://www.repostatus.org/#active

Skeleton for a python package, complete with tox/Travis-CI, Landscape.io, codecov, etc.

Usage
------

Run:

    /path/to/python-package-skeleton/use_skeleton.sh <project name>

This will create a ``project name`` directory under your pwd and populate it with the skeleton.

You'll then need to make some updates in many of the files, but it's a good starting point.

For people other than me, you'll probably want to do the following in the resulting directory:

.. code-block:: bash

    find ./ -type f -exec sed -i -e 's/Jason Antman/Your Name/g' -e 's/jason@jasonantman\.com/YOUR_EMAIL/g' -e 's|http://www\.jasonantman\.com|YOUR_WEBSITE|g' -e 's/jantman/YOUR_GITHUB_USERNAME/g' {} \;

Actions
--------

See ``use_skeleton.sh``, it's simple enough.
