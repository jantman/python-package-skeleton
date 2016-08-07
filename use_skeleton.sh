#!/bin/bash -ex
#
# python-package-skeleton install script
#
# <https://github.com/jantman/python-package-skeleton>
#

if [ $# -eq 0 ]
then
  echo "USAGE: use_skeleton.sh <project name>"
  exit 1
fi

# directory where this script lives
srcdir=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

projname=$1
projname_underscored=${projname//-/_}

mkdir -p $projname
cd $projname

function movefile {
    src=$1
    dst=$2
    sed "s/python-package-skeleton/${projname}/g" ${srcdir}/${src} | sed "s/python_package_skeleton/${projname_underscored}/g" > $dst
}

mkdir -p .github docs/source

for fname in .coveragerc .github/CONTRIBUTING.md .github/ISSUE_TEMPLATE.md .github/PULL_REQUEST_TEMPLATE.md .gitignore .landscape.yaml .travis.yml CHANGES.rst LICENSE MANIFEST.in pytest.ini setup.cfg setup.py tox.ini docs/Makefile docs/source/changes.rst docs/source/conf.py docs/source/index.rst docs/source/modules.rst
do
    movefile $fname $fname
done

mkdir docs/source/_static
touch docs/source/_static/.gitkeep

sed "s/python-package-skeleton/${projname}/g" ${srcdir}/README_skeleton.rst > README.rst

mkdir -p ${projname}/tests
for fname in __init__.py version.py tests/__init__.py tests/test_version.py
do
    movefile python-package-skeleton/${fname} ${projname}/${fname}
done

echo "Done."
