#!/usr/bin/env bash
tmpdir=$1
simulations_path=$2
parameter_set=$3
plot_directory=$4

shift 1

echo "--------------------------------------------"
echo "Running InvasionPlotting.sh"
echo "Parameters:"
echo " - simulations path = ${simulations_path}"
echo " - parameter set = ${parameter_set}"
echo " - plots directory = ${plot_directory}"
echo " - Rest of parameters = $@"
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
# cp ${SCRIPTS_DIR}/utils.py ./

python generate_plots.py ${simulations_path} ${parameter_set} ${plot_directory}

cd ${CURRENT_DIR}
