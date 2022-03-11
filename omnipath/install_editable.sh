#!/usr/bin/env bash

./build.sh

echo "Installing in editable mode..."

python3 -m pip install --editable .

echo "----- Installation finished -----"
