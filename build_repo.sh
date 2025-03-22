#!/bin/bash

for release in 8 9; do
    mkdir -p REPO/$release/{noarch,x86_64}
    for arch in noarch x86_64; do
        cp RPMS/$arch/*el$release* REPO/$release/$arch/
    done
    createrepo REPO/$release
done
