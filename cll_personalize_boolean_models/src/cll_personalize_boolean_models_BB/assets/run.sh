#!/usr/bin/env bash

tmpdir=$1

shift 1

echo "--------------------------------------------"
echo "Running run.sh from cll_personalize_boolean_models_BB"
echo "Parameters:"
echo " - tmpdir = ${tmpdir}"
echo " - Rest of parameters = $@"
echo "--------------------------------------------"

CURRENT_DIR=$(pwd)
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
# Directory where the scripts used by this script are located in the installation folder
SCRIPTS_DIR="${SCRIPT_DIR}/"

# This is the directory where the auxiliary or temporary files will be written and from where the execution will be done
if [ "${tmpdir}" = "pycompss_sandbox" ]; then
    tmpdir=${CURRENT_DIR}
    echo "Using PyCOMPSs sandbox directory as temporary: ${tmpdir}"
else
    echo "Using temporary directory: ${tmpdir}"
    cd ${tmpdir}
fi

cd ${CURRENT_DIR}

if [ -z ${PYTHONHOME+x} ]; then
    echo "No PYTHONHOME set"
else
    unset PYTHONHOME
fi

cd /home/permed
Rscript personalize_boolean_models.R $@

cd $CURRENT_DIR
