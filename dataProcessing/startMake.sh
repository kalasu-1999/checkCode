#!/usr/bin/env bash
# shellcheck disable=SC2164
cd "$1"
make clean
make
if [ -d "testAnswerDir" ]; then
    rm -rf "testAnswerDir/"
fi
if [ -d "numpyDataDir/" ]; then
    rm -rf "numpyDataDir/"
fi
mkdir "testAnswerDir"
mkdir "numpyDataDir"
