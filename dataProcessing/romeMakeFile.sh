#!/usr/bin/env bash
# shellcheck disable=SC2164
cd "$1"
make clean
rm Makefile
rm -rf testAnswerDir/
rm -rf numpyDataDir/