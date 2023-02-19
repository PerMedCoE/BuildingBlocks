#!/usr/bin/env bash

CURRENT_DIR=$(pwd)
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd ${SCRIPT_DIR}/invasion_analysis

python collect_data.py "$@"

cd ${CURRENT_DIR}
