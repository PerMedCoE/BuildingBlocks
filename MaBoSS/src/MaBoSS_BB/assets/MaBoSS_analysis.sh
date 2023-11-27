#!/usr/bin/env bash

projectname=$1
data_folder=$2
ko_file=$3
parallel=$4
tmpdir=$5

echo "--------------------------------------------"
echo "Running MaBoSS_analysis.sh"
echo "Parameters:"
echo " - projectname = ${projectname}"
echo " - data_folder = ${data_folder}"
echo " - ko_file = ${ko_file}"
echo " - parallel = ${parallel}"
echo " - tmpdir = ${tmpdir}"
echo "--------------------------------------------"

CURRENT_DIR=$(pwd)
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
# Directory where the scripts used by this script are located in the installation folder
SCRIPTS_DIR="${SCRIPT_DIR}/MaBoSS_analysis"

# This is the directory where the auxiliary or temporary files will be written and from where the execution will be done
if [ "${tmpdir}" = "pycompss_sandbox" ]; then
    tmpdir=${CURRENT_DIR}
    echo "Using PyCOMPSs sandbox directory as temporary: ${tmpdir}"
else
    echo "Using temporary directory: ${tmpdir}"
    cd ${tmpdir}
fi

# Copy all modifiable files to working directory
cp ${SCRIPTS_DIR}/analysis.py ./

if [ -z ${PYTHONHOME+x} ]; then
    echo "No PYTHONHOME set"
else
    unset PYTHONHOME
fi

python3 analysis.py ${projectname} ${data_folder} ${ko_file} ${parallel}

cd ${CURRENT_DIR}
