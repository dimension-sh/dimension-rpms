#!/bin/bash

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
