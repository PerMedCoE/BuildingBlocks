#!/usr/bin/env bash

parameter_set=$1
repetition=$2
out_file=$3
err_file=$4
results_dir=$5
parallel=$6
max_time=$7
tmpdir=$8

echo "--------------------------------------------"
echo "Running PhysiBoSS.sh"
echo "Parameters:"
echo " - parameter_set = ${parameter_set}"
echo " - repetition = ${repetition}"
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
physiboss_folder="${tmpdir}/PhysiBoSS_${repetition}_${user}"
cp -r /usr/local/scm/Invasion_model_PhysiBoSS/ ${physiboss_folder}
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
sed -i "s/<omp_num_threads>10/<omp_num_threads>${parallel}/g" "${physiboss_folder}/data/PhysiCell_settings_2D.xml"
echo "USING:"
grep "omp_num_threads" "${physiboss_folder}/data/PhysiCell_settings_2D.xml"

# Update the maxtime
sed -i "s/<max_time units=\"min\">4500<\/max_time>/<max_time units=\"min\">${max_time}<\/max_time>/g" "${physiboss_folder}/data/PhysiCell_settings_2D.xml"
echo "MAX TIME:"
grep "max_time" "${physiboss_folder}/data/PhysiCell_settings_2D.xml"

while read -r line || [ -n "$line" ]
do
  param=$(echo ${line} | cut -f1 -d,)
  value=$(echo ${line} | cut -f2 -d,)
  sed -i -E "s|>.*</${param}|>${value}</${param}>|" "${physiboss_folder}/data/PhysiCell_settings_2D.xml"
  echo "${param}: "
  grep "${param}" "${physiboss_folder}/data/PhysiCell_settings_2D.xml"
done < "${parameter_set}"

# # Prepare patient execution
# cp ${bnd_file} ${physiboss_folder}/data/boolean_network/intracellular_model.bnd
# cp ${cfg_file} ${physiboss_folder}/data/boolean_network/intracellular_model.cfg

# Execute PhysiBoss
# Prepare output folder (hardcoded into config.xml)
cd ${physiboss_folder}/bin/
if [ ! -d "output" ]
then
  mkdir output
else
  rm -rf output/*
fi
# Execution
cat "${physiboss_folder}/data/PhysiCell_settings_2D.xml"

myproj "${physiboss_folder}/data/PhysiCell_settings_2D.xml" > ${out_file} 2> ${err_file}
# Move results to the final directory
if [ ! -d ${results_dir} ]
then
  mkdir -p ${results_dir}
else
  rm -rf ${results_dir}/*
fi

ls ${results_dir}
mv output/* ${results_dir}/.
ls ${results_dir}
cd ..

# Clean
rm -rf $physiboss_folder

cd $CURRENT_DIR
