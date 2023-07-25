#!/usr/bin/env bash

tmpdir=$1
path_models=$2
list_druggable=$3
nodes_quantify=$4
results_file=$5
mode=$6

echo "--------------------------------------------"
echo "Running MaBoSSG_sensitivity_analysis.sh"
echo "Parameters:"
echo " - tmpdir = ${tmpdir}"
echo " - path_models = ${path_models}"
echo " - list_druggable = ${list_druggable}"
echo " - nodes_quantify = ${nodes_quantify}"
echo " - results_file = ${results_file}"
echo " - mode = ${mode}"
echo "--------------------------------------------"

CURRENT_DIR=$(pwd)
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
# Directory where the scripts used by this script are located in the installation folder
SCRIPTS_DIR="${SCRIPT_DIR}/MaBoSSG_sensitivity_analysis"

# This is the directory where the auxiliary or temporary files will be written and from where the execution will be done
if [ "${tmpdir}" = "pycompss_sandbox" ]; then
    tmpdir=${CURRENT_DIR}
    echo "Using PyCOMPSs sandbox directory as temporary: ${tmpdir}"
else
    echo "Using temporary directory: ${tmpdir}"
    cd ${tmpdir}
fi

CURRENT_DIR=$(pwd)

cp -r /opt/MaBoSSG ${CURRENT_DIR}
cd MaBoSSG

cp -r ${SCRIPT_DIR}/make_model.py .
python3 make_model.py ${path_models} ${list_druggable} ${nodes_quantify}

sed -i "s/1E308/3E38/g" "${path_models}/mutable_model.bnd"

python3 gen/generator.py --runtime-variables ${path_models}/mutable_model.bnd ${path_models}/mutable_model.cfg ${path_models}/settings.json

if [ -d ./build ]; then
    rm -fr ./build
fi  
cmake -DCMAKE_BUILD_TYPE=Release -B build .
cmake --build build

cp -r ${SCRIPT_DIR}/run_mutants_analysis.py .
python3 run_mutants_analysis.py ${list_druggable} ${nodes_quantify} ${path_models}/settings.json ${results_file}
