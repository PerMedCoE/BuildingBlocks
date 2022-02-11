#!/usr/bin/env bash

CURRENT_DIR=$(pwd)
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd $SCRIPT_DIR

sample=$1
repetition=$2
prefix==$3
model_dir=$4
out_file=$5
err_file=$6
results_dir=$7
parallel=$8

bnd_file=${model_dir}/${prefix}.bnd
cfg_file=${model_dir}/${prefix}.cfg

# Do a copy of PhysiBoSS folder for the current execution
physiboss_folder="PhysiBoSS_${sample}_${prefix}_${repetition}"
cp -r PhysiBoSS ${physiboss_folder}

# Update the number of threads
sed -i "s/<omp_num_threads>6/<omp_num_threads>${parallel}/g" "${physiboss_folder}/config/PhysiCell_settings.xml"
echo "USING:"
grep "omp_num_threads" "${physiboss_folder}/config/PhysiCell_settings.xml"

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
./myproj > ${out_file} 2> ${err_file}
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
