#!/usr/bin/env bash

./build.sh

echo "Installing..."

python3 setup.py install --record installed_files.txt --user

# Avoid to remove the permedcoe launcher
sed -i '/permedcoe/d' ./installed_files.txt

echo "----- Installation finished -----"
