#!/usr/bin/env bash

CURRENT_DIR=$(pwd)
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd $SCRIPT_DIR

/opt/miniconda/bin/python /opt/carnival/carnivalpy/carnival.py $@

cd $CURRENT_DIR
