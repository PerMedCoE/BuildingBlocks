#!/usr/bin/env bash

repetitions=$1
replicates_folder=$2
prefix=$3
out_file=$4
err_file=$5
results_dir=$6
parallel=$7
tmpdir=$8

echo "--------------------------------------------"
echo "Running PhysiBoSS_analyse_replicates.sh"
echo "Parameters:"
echo " - repetitions = ${repetitions}"
echo " - replicates_folder = ${replicates_folder}"
echo " - prefix = ${prefix}"
echo " - out_file = ${out_file}"
echo " - err_file = ${err_file}"
echo " - results_dir = ${results_dir}"
echo " - parallel = ${parallel}"
echo " - tmpdir = ${tmpdir}"
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

mkdir ${replicates_folder}/${prefix}_data

python3 ${SCRIPTS_DIR}/ParseReplicates.py --folder ${replicates_folder} --prefix ${prefix} --cores ${parallel} --first 1 --replicates ${repetitions} --out_folder ${replicates_folder}/${prefix}_data 1> ${out_file} 2> ${err_file}
ls -al ${replicates_folder}
python3 ${SCRIPTS_DIR}/ParseReplicatesDat.py --folder ${replicates_folder} --prefix ${prefix} --first 1 --replicates ${repetitions} --out_folder ${replicates_folder}/${prefix}_data 1>> ${out_file} 2>> ${err_file}
ls -al ${replicates_folder}
python3 ${SCRIPTS_DIR}/ParseReplicatesStates.py --folder ${replicates_folder} --prefix ${prefix} --cores ${parallel} --first 1 --replicates ${repetitions} --out_folder ${replicates_folder}/${prefix}_data 1>> ${out_file} 2>> ${err_file}
ls -al ${replicates_folder}
python3 ${SCRIPTS_DIR}/plotReplicates.py --folder ${replicates_folder}/${prefix}_data --replicates ${repetitions} --out_folder ${replicates_folder}/${prefix}_data 1>> ${out_file} 2>> ${err_file}
ls -al ${replicates_folder}

# Move results to the final directory
if [ ! -d ${results_dir} ]
then
  mkdir -p ${results_dir}
else
  rm -rf ${results_dir}/*
fi
mv ${replicates_folder}/${prefix}_data/* \
   ${results_dir}/.
cd ..

cd $CURRENT_DIR
