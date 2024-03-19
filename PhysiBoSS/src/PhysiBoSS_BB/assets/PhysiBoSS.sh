#!/usr/bin/env bash

sample=$1
repetition=$2
prefix=$3
bnd_file=$4
cfg_file=$5
out_file=$6
err_file=$7
results_dir=$8
parallel=$9
max_time=${10}
tmpdir=${11}

echo "--------------------------------------------"
echo "Running PhysiBoSS.sh"
echo "Parameters:"
echo " - sample = ${sample}"
echo " - repetition = ${repetition}"
echo " - prefix = ${prefix}"
echo " - bnd_file = ${bnd_file}"
echo " - cfg_file = ${cfg_file}"
echo " - out_file = ${out_file}"
echo " - err_file = ${err_file}"
echo " - results_dir = ${results_dir}"
echo " - parallel = ${parallel}"
echo " - max_time = ${max_time}"
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

# Do a copy of PhysiBoSS folder for the current execution
user=$(whoami)
physiboss_folder="${tmpdir}/PhysiBoSS_${sample}_${prefix}_${repetition}_${user}"
if [ -d "/usr/local/scm/COVID19/PhysiCell" ]; then
  echo "Using /usr/local/scm/COVID19/PhysiCell/ folder"
  cp -rL /usr/local/scm/COVID19/PhysiCell/ ${physiboss_folder}
else
  echo "Using /usr/local/src/covid19/PhysiCell/ folder"
  cp -rL /usr/local/src/covid19/PhysiCell/ ${physiboss_folder}
fi
chmod -R 755 ${physiboss_folder}
echo "COPY OF PhysiBoSS:"
echo "${physiboss_folder}"
echo "PhysiBoSS executable:"
ls -l ${physiboss_folder}
echo "--------------------------------------"
echo "Working directory content:"
ls -l ${tmpdir}
echo "--------------------------------------"

# Update the number of threads
sed -i "s/<omp_num_threads>6/<omp_num_threads>${parallel}/g" "${physiboss_folder}/config/PhysiCell_settings.xml"
echo "USING:"
grep "omp_num_threads" "${physiboss_folder}/config/PhysiCell_settings.xml"

# Update the maxtime
sed -i "s/<max_time units=\"min\">21600<\/max_time> <\!-- 8640, 5 days \* 24 h \* 60 min -->/<max_time units=\"min\">${max_time}<\/max_time>/g" "${physiboss_folder}/config/PhysiCell_settings.xml"
sed -i "s/<max_time units=\"min\">14400<\/max_time> <\!-- 5 days \* 24 h \* 60 min -->/<max_time units=\"min\">${max_time}<\/max_time>/g" "${physiboss_folder}/config/PhysiCell_settings.xml"
sed -i "s/<max_time units=\"min\">8640<\/max_time> <\!-- 5 days \* 24 h \* 60 min -->/<max_time units=\"min\">${max_time}<\/max_time>/g" "${physiboss_folder}/config/PhysiCell_settings.xml"
echo "MAX TIME:"
grep "max_time" "${physiboss_folder}/config/PhysiCell_settings.xml"

# Prepare patient execution
cp ${bnd_file} ${physiboss_folder}/config/boolean_network/personalized_epithelial_cell.bnd
cp ${cfg_file} ${physiboss_folder}/config/boolean_network/personalized_epithelial_cell.cfg

# Execute PhysiBoss
# Prepare output folder (hardcoded into config.xml)
cd ${physiboss_folder}
if [ ! -d "output" ]
then
  mkdir output
else
  rm -rf output/*
fi
# Execution
if [ -f "$(pwd)/myproj" ]; then
  myproj > ${out_file} 2> ${err_file}
else
  COVID19 > ${out_file} 2> ${err_file}
fi
# Move results to the final directory
if [ ! -d ${results_dir} ]
then
  mkdir -p ${results_dir}
else
  rm -rf ${results_dir}/*
fi
mv output/* ${results_dir}/.
cd ..

# Clean
rm -rf $physiboss_folder

cd $CURRENT_DIR
