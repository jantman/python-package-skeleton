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

function movefile {
    src=$1
    dst=$2
    sed "s/python-package-skeleton/${projname}/g" ${srcdir}/${src} | sed "s/python_package_skeleton/${projname_underscored}/g" > ${projname}/${dst}
}

mkdir -p $projname/.github $projname/docs/source/_static ${projname}/${projname_underscored}/tests

for fname in .coveragerc .github/ISSUE_TEMPLATE.md .github/PULL_REQUEST_TEMPLATE.md .gitignore CHANGES.rst LICENSE MANIFEST.in setup.cfg setup.py tox.ini docs/Makefile docs/source/changes.rst docs/source/conf.py docs/source/index.rst docs/source/modules.rst
do
    movefile $fname $fname
done

touch $projname/docs/source/_static/.gitkeep

sed "s/python-package-skeleton/${projname}/g" ${srcdir}/README_skeleton.rst > README.rst

for fname in __init__.py version.py tests/__init__.py tests/test_version.py
do
    movefile python_package_skeleton/${fname} ${projname_underscored}/${fname}
done

echo "Done."
