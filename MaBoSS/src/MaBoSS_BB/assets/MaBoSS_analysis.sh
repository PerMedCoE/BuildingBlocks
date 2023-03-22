#!/usr/bin/env bash

projectname=$1
data_folder=$2
ko_file=$3
parallel=$4
tmpdir=$5

echo "--------------------------------------------"
echo "Running MaBoSS_analysis.sh"
echo "Parameters:"
echo " - projectname = ${projectname}"
echo " - data_folder = ${data_folder}"
echo " - ko_file = ${ko_file}"
echo " - parallel = ${parallel}"
echo " - tmpdir = ${tmpdir}"
echo "--------------------------------------------"

CURRENT_DIR=$(pwd)
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
# Directory where the scripts used by this script are located in the installation folder
SCRIPTS_DIR="${SCRIPT_DIR}/MaBoSS_analysis"

# This is the directory where the auxiliary or temporary files will be written and from where the execution will be done
if [ "${tmpdir}" = "pycompss_sandbox" ]; then
    tmpdir=${CURRENT_DIR}
    echo "Using PyCOMPSs sandbox directory as temporary: ${tmpdir}"
else
    echo "Using temporary directory: ${tmpdir}"
    cd ${tmpdir}
fi

echo "1, run MaBoSS instance"
if [ -d "$projectname" ]
then
  echo "WARNING: removing existing MaBoSS folder"
  rm -r $projectname
fi

# Copy all modifiable files to working directory
cp ${data_folder}/{"$projectname".bnd,"$projectname".cfg} ./
cp ${data_folder}/inputs.txt ./
cp ${data_folder}/outputs.txt ./
cp ${SCRIPTS_DIR}/* ./

# Adapt the number of computing units for parallel execution:
updated_projectname="${projectname}_updated"
cp "${projectname}.bnd" "${updated_projectname}.bnd"
sed "s/thread_count=4/thread_count=${parallel}/g" "${projectname}.cfg" > "${updated_projectname}.cfg"
projectname=${updated_projectname}
echo "USING:"
grep "thread_count" "${projectname}.cfg"

./run_MaBoSS_Unix_Stew.sh ${projectname}

echo "2, Predict genetic interactions of the model"
if [ -d "$projectname"_epistasis ]
then
  echo "WARNING: removing existing epistasis folder"
  rm -r "$projectname"_epistasis
fi
./1-4_epistasis_Stew.sh ${projectname} "-onlyko"

# TODO: AVOID TO SED THE R SCRIPT AND USE A PARAMETER FOR projectname
echo "3, Analyse genetic interactions of the model"
sed "s/projectname/"${projectname}"/g" Analyses_of_genetic_interactions_Stew_workflow.R > Analyses_of_genetic_interactions_Stew_workflow_post.R
chmod 755 Analyses_of_genetic_interactions_Stew_workflow_post.R
Rscript Analyses_of_genetic_interactions_Stew_workflow_post.R

########################################################
# WARNING: Do not modify code on the fly. For example: #
########################################################
# sed "s/projectname/"$projectname"/g" run_MaBoSS_Unix_Stew.sh > run_MaBoSS_Unix_Stew_post.sh
# chmod 755 run_MaBoSS_Unix_Stew_post.sh
# ./run_MaBoSS_Unix_Stew_post.sh
#
# echo "2, Predict genetic interactions of the model"
# if [ -d "$projectname"_epistasis ]
# then
#   echo "WARNING: removing existing epistasis folder"
#  rm -r "$projectname"_epistasis
# fi
# sed "s/projectname/"$projectname"/g" 1\-4_epistasis_Stew.sh > 1\-4_epistasis_Stew_post.sh
# sed -i "s/ -single / -single -onlyko /g" 1\-4_epistasis_Stew_post.sh
# chmod 755 1\-4_epistasis_Stew_post.sh
# ./1-4_epistasis_Stew_post.sh
#
# echo "3, Analyse genetic interactions of the model"
# sed "s/projectname/"$projectname"/g" Analyses_of_genetic_interactions_Stew_workflow.R > Analyses_of_genetic_interactions_Stew_workflow_post.R
# chmod 755 Analyses_of_genetic_interactions_Stew_workflow_post.R
# Rscript Analyses_of_genetic_interactions_Stew_workflow_post.R
########################################################

echo "4, Cleaning"
rm -rf ./${projectname}*
rm ./inputs.txt
rm ./outputs.txt
rm ./*.sh
rm ./*.pl
rm ./*.R


if [ ! -f "${ko_file}" ]
then
    echo "ko file copy to final destination needed"
    cp --no-preserve=mode,ownership ./ko_file.txt ${ko_file}
    # rm ./ko_file.txt
else
    echo "ko file already in final destination"
fi

cd ${CURRENT_DIR}
