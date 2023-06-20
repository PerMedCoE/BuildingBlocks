#!/usr/bin/env bash
tmpdir=$1
parameter_set=$2
plot_directory=$3
shift 3
simulations_paths=$@

echo "--------------------------------------------"
echo "Running InvasionPlotting.sh"
echo "Parameters:"
echo " - parameter set = ${parameter_set}"
echo " - plots directory = ${plot_directory}"
echo " - simulations path = ${simulations_paths}"
echo "--------------------------------------------"

CURRENT_DIR=$(pwd)
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
# Directory where the scripts used by this script are located in the installation folder
SCRIPTS_DIR="${SCRIPT_DIR}/invasion_analysis/"

# This is the directory where the auxiliary or temporary files will be written and from where the execution will be done
if [ "${tmpdir}" = "pycompss_sandbox" ]; then
    tmpdir=${CURRENT_DIR}
    echo "Using PyCOMPSs sandbox directory as temporary: ${tmpdir}"
else
    echo "Using temporary directory: ${tmpdir}"
    cd ${tmpdir}
fi

# Copy all modifiable files to working directory
cp ${SCRIPTS_DIR}/generate_plots.py ./

python generate_plots.py ${parameter_set} ${plot_directory} ${simulations_paths}

cd ${CURRENT_DIR}
