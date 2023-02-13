#!/usr/bin/env bash

working_directory=$1

shift 1

echo "--------------------------------------------"
echo "Running print_result_drugs.sh"
echo "Parameters:"
echo " - working_directory = ${working_directory}"
echo " - Rest of parameters = $@"
echo "--------------------------------------------"

CURRENT_DIR=$(pwd)
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
# Directory where the scripts used by this script are located in the installation folder
SCRIPTS_DIR="${SCRIPT_DIR}/"

# This is the directory where the auxiliary or temporary files will be written and from where the execution will be done
if [ "${working_directory}" = "pycompss_sandbox" ]; then
    working_directory=${CURRENT_DIR}
    echo "Using PyCOMPSs sandbox directory: ${working_directory}"
else
    echo "Using working directory: ${working_directory}"
    cd ${working_directory}
fi

# Copy all modifiable files to working directory
cp ${SCRIPTS_DIR}/print_result_drugs.py ./

python3 print_result_drugs.py $@

cd $CURRENT_DIR
