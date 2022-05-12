#!/usr/bin/env bash

echo "Installing..."

path=$1
mkdir -p ${path}

python3 -m pip install . --target=${path}

echo "----- Installation finished -----"
