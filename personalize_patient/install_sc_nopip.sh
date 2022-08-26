#!/usr/bin/env bash

echo "Installing..."

path=$1
mkdir -p ${path}

python3 setup.py install --prefix ${path}

echo "----- Installation finished -----"
