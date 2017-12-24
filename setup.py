"""
The latest version of this package is available at:
<http://github.com/jantman/python-package-skeleton>

##################################################################################
Copyright 2017 Jason Antman <jason@jasonantman.com> <http://www.jasonantman.com>

    This file is part of python-package-skeleton, also known as python-package-skeleton.

    python-package-skeleton is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    python-package-skeleton is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with python-package-skeleton.  If not, see <http://www.gnu.org/licenses/>.

The Copyright and Authors attributions contained herein may not be removed or
otherwise altered, except to add the Author attribution of a contributor to
this work. (Additional Terms pursuant to Section 7b of the AGPL v3)
##################################################################################
While not legally required, I sincerely request that anyone who finds
bugs please submit them at <https://github.com/jantman/python-package-skeleton> or
to me via email, and that you send any contributions or improvements
either as a pull request on GitHub, or to me via email.
##################################################################################

AUTHORS:
Jason Antman <jason@jasonantman.com> <http://www.jasonantman.com>
##################################################################################
"""

from setuptools import setup, find_packages
from python_package_skeleton.version import VERSION, PROJECT_URL

with open('README.rst') as file:
    long_description = file.read()

requires = [
    'something'
]

# @TODO - see: https://pypi.python.org/pypi?%3Aaction=list_classifiers
classifiers = [
    'Development Status :: 1 - Planning',
    'License :: OSI Approved :: GNU Affero General Public License '
    'v3 or later (AGPLv3+)',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
]

setup(
    name='python-package-skeleton',
    version=VERSION,
    author='Jason Antman',
    author_email='jason@jasonantman.com',
    packages=find_packages(),
    url=PROJECT_URL,
    description='Description here.',
    long_description=long_description,
    install_requires=requires,
    keywords="",
    classifiers=classifiers
)
