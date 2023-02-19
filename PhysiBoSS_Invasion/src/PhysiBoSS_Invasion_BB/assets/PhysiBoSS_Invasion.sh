#!/usr/bin/env bash

CURRENT_DIR=$(pwd)
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

cd $SCRIPT_DIR

parameter_set=$1
repetition=$2
out_file=$3
err_file=$4
results_dir=$5
parallel=$6
max_time=$7

# Do a copy of PhysiBoSS folder for the current execution
user=$(whoami)
physiboss_folder="PhysiBoSS_${repetition}_${user}"

cp -r /usr/local/scm/Invasion_model_PhysiBoSS/ ${physiboss_folder}

# Update the number of threads
sed -i "s/<omp_num_threads>12/<omp_num_threads>${parallel}/g" "${physiboss_folder}/data/PhysiCell_settings_2D.xml"
echo "USING:"
grep "omp_num_threads" "${physiboss_folder}/data/PhysiCell_settings_2D.xml"

# Update the maxtime
#sed -i "s/<max_time units=\"min\">8640<\/max_time> <\!-- 5 days \* 24 h \* 60 min -->/<max_time units=\"min\">${max_time}<\/max_time>/g" "${physiboss_folder}/config/PhysiCell_settings_2D.xml"
sed -i "s/<max_time units=\"min\">7500<\/max_time>/<max_time units=\"min\">${max_time}<\/max_time>/g" "${physiboss_folder}/data/PhysiCell_settings_2D.xml"
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
cat "${SCRIPT_DIR}/${physiboss_folder}/data/PhysiCell_settings_2D.xml"

myproj "${SCRIPT_DIR}/${physiboss_folder}/data/PhysiCell_settings_2D.xml" > ${out_file} 2> ${err_file}
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
