from setuptools import setup
from sys import version_info
from python-package-skeleton.version import VERSION

with open('README.rst') as file:
    long_description = file.read()

requires = ['something']

classifiers = [
    'Development Status :: 1 - Planning',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
]

setup(
    name='python-package-skeleton',
    version=VERSION,
    author='Jason Antman',
    author_email='jason@jasonantman.com',
    packages=['python-package-skeleton', 'python-package-skeleton.tests'],
    url='http://github.com/jantman/pypuppetdb-daily-report/',
    description='Description here.',
    long_description=long_description,
    install_requires=requires,
    keywords="",
    classifiers=classifiers
)
