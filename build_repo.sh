#!/bin/bash

mkdir REPO
cp -R RPMS/* REPO/
createrepo REPO/

for arch in REPO/*; do
    echo "${arch} Packages"
    echo ""
    ls -il $arch
done
