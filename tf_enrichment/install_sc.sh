#!/usr/bin/env bash

echo "Installing..."

version=$(python -c "import sys; version = sys.version_info; print('%d.%d' % (version[0], version[1]))")
path="$1/python${version}/"

mkdir -p ${path}

python3 -m pip install . --target=${path}

echo "----- Installation finished -----"
