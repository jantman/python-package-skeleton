#!/bin/bash -ex
#
# python-package-skeleton install script
#
# <https://github.com/jantman/python-package-skeleton>
#

if [ $# -eq 0]
then
  echo "USAGE: use_skeleton.sh <project name>"
  exit 1
fi

projname=$1

# directory where this script lives
srcdir=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

for fname in .coveragerc .landscape.yaml .travis.yml CHANGES.rst MANIFEST.in pytest.ini setup.py tox.ini
do
  sed "s/python-package-skeleton/${projname}/g" ${srcdir}/${fname} > $fname
done

sed "s/python-package-skeleton/${projname}/g" ${srcdir}/README_skeleton.rst > README.rst

mkdir -p ${projname}/tests
touch ${projname}/__init__.py
touch ${projname}/tests/__init__.py

echo "# ${projname}" > ${projname}/version.py
echo "VERSION = '0.0.1'" >> ${projname}/version.py

echo "Done."
