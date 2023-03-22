#!/usr/bin/env bash

tmpdir=$1

shift 1

echo "--------------------------------------------"
echo "Running single_cell_processing_individual.sh"
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

# Copy all modifiable files to working directory
cp ${SCRIPTS_DIR}/single_cell_processing_individual.R ./
# cp ${SCRIPTS_DIR}/single_cell_processing_individual.sh ./

Rscript ./single_cell_processing_individual.R $@

cd $CURRENT_DIR
