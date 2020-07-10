#!/bin/bash
cd $(dirname $0)
mkdir -p {BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}

for spec in SPECS/*.spec; do
    spectool -g -A -C SOURCES "${spec}"
    rpmbuild -bs --define "_topdir `pwd`" --nodebuginfo "${spec}"
    rpmbuild -bb --define "_topdir `pwd`" --nodebuginfo "${spec}"
done


mkdir REPO
cp -R RPMS/* REPO/
for arch in REPO/*; do
  createrepo $arch
done

for arch in REPO/*; do
    echo "${arch} Packages"
    echo ""
    ls -il $arch
done
