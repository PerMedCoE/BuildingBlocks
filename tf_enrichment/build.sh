#!/usr/bin/env bash

echo "Building..."

python3 setup.py build

python3 setup.py sdist

echo "----- Building finished -----"
