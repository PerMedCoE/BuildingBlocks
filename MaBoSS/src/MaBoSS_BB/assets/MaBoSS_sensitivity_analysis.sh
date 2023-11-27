#!/usr/bin/env bash

tmpdir=$1

shift 1

echo "--------------------------------------------"
echo "Running MaBoSS_sensitivity_analysis.sh"
echo "Parameters:"
echo " - tmpdir = ${tmpdir}"
echo " - Rest of parameters = $@"
echo "--------------------------------------------"

CURRENT_DIR=$(pwd)
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
# Directory where the scripts used by this script are located in the installation folder
SCRIPTS_DIR="${SCRIPT_DIR}/MaBoSS_sensitivity_analysis"

# This is the directory where the auxiliary or temporary files will be written and from where the execution will be done
if [ "${tmpdir}" = "pycompss_sandbox" ]; then
    tmpdir=${CURRENT_DIR}
    echo "Using PyCOMPSs sandbox directory as temporary: ${tmpdir}"
else
    echo "Using temporary directory: ${tmpdir}"
    cd ${tmpdir}
fi

# Copy all modifiable files to working directory
cp ${SCRIPTS_DIR}/sensitivity_analysis.py ./

if [ -z ${PYTHONHOME+x} ]; then
    echo "No PYTHONHOME set"
else
    unset PYTHONHOME
fi

python3 sensitivity_analysis.py $@

cd ${CURRENT_DIR}
