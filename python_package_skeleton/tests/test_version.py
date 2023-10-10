"""
The latest version of this package is available at:
<http://github.com/jantman/python-package-skeleton>

##################################################################################
Copyright 2023 Jason Antman <jason@jasonantman.com> <http://www.jasonantman.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the “Software”), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

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

import python_package_skeleton.version as version

import re
import sys


class TestVersion(object):

    def test_project_url(self):
        expected = 'https://github.com/jantman/python-package-skeleton'
        assert version.PROJECT_URL == expected

    def test_is_semver(self):
        # see:
        # https://github.com/mojombo/semver.org/issues/59#issuecomment-57884619
        semver_ptn = re.compile(
            r'^'
            r'(?P<MAJOR>(?:'
            r'0|(?:[1-9]\d*)'
            r'))'
            r'\.'
            r'(?P<MINOR>(?:'
            r'0|(?:[1-9]\d*)'
            r'))'
            r'\.'
            r'(?P<PATCH>(?:'
            r'0|(?:[1-9]\d*)'
            r'))'
            r'(?:-(?P<prerelease>'
            r'[0-9A-Za-z-]+(\.[0-9A-Za-z-]+)*'
            r'))?'
            r'(?:\+(?P<build>'
            r'[0-9A-Za-z-]+(\.[0-9A-Za-z-]+)*'
            r'))?'
            r'$'
        )
        assert semver_ptn.match(version.VERSION) is not None
