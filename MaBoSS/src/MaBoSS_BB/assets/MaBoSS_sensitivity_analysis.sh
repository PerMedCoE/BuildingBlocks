#!/usr/bin/env bash

CURRENT_DIR=$(pwd)
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

cd "${SCRIPT_DIR}/MaBoSS_sensitivity_analysis"

python3 sensitivity_analysis.py $@

cd ${CURRENT_DIR}
