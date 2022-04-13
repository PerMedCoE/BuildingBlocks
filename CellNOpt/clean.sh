#!/usr/bin/env bash

echo "Cleaning..."

rm -rf -v build/
rm -rf -v dist/
rm -rf -v src/*.egg-info

echo "----- Cleaning finished -----"
