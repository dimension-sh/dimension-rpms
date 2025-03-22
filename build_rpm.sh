#!/bin/bash
spec="SPECS/${1}.spec"

cd $(dirname $0)
mkdir -p {BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}

spectool -g --all -C SOURCES "${spec}"
rpmbuild -bs --define "_topdir `pwd`" --nodebuginfo "${spec}"
rpmbuild -bb --define "_topdir `pwd`" --nodebuginfo "${spec}"
