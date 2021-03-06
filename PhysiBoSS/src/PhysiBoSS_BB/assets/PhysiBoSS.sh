#!/usr/bin/env bash

CURRENT_DIR=$(pwd)
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd $SCRIPT_DIR

sample=$1
repetition=$2
prefix==$3
bnd_file=$4
cfg_file=$5
out_file=$6
err_file=$7
results_dir=$8
parallel=$9
max_time=${10}

# Do a copy of PhysiBoSS folder for the current execution
user=$(whoami)
physiboss_folder="PhysiBoSS_${sample}_${prefix}_${repetition}_${user}"
cp -r /usr/local/scm/COVID19/PhysiCell/ ${physiboss_folder}

# Update the number of threads
sed -i "s/<omp_num_threads>6/<omp_num_threads>${parallel}/g" "${physiboss_folder}/config/PhysiCell_settings.xml"
echo "USING:"
grep "omp_num_threads" "${physiboss_folder}/config/PhysiCell_settings.xml"

# Update the maxtime
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
myproj > ${out_file} 2> ${err_file}
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
