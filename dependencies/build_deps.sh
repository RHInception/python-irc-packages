#!/usr/bin/env bash

rm -fR results rpm-build;
mkdir -p results

make -f ./Makefile.jaraco rpm
find rpm-build -name '*.rpm' -exec cp '{}' results/ \;

make -f ./Makefile.itertools rpm
find rpm-build -name '*.rpm' -exec cp '{}' results/ \;

rm -fR rpm-build;
