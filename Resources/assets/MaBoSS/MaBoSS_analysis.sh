#!/usr/bin/env bash

projectname=$1
data_folder=$2
ko_file=$3
parallel=$4

CURRENT_DIR=$(pwd)
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

cd ${SCRIPT_DIR}/"MaBoSS_analysis"

echo "1, run MaBoSS instance"
if [ -d "$projectname" ]
then
  echo "WARNING: removing existing MaBoSS folder"
  rm -r $projectname
fi

cp ${data_folder}/{"$projectname".bnd,"$projectname".cfg} ./
cp ${data_folder}/inputs.txt ./
cp ${data_folder}/outputs.txt ./

# Adapt the number of computing units for parallel execution:
sed -i "s/thread_count=4/thread_count=${parallel}/g" "${data_folder}/${projectname}.cfg"
echo "USING:"
grep "thread_count" "${data_folder}/${projectname}.cfg"

./run_MaBoSS_Unix_Stew.sh $projectname

echo "2, Predict genetic interactions of the model"
if [ -d "$projectname"_epistasis ]
then
  echo "WARNING: removing existing epistasis folder"
 rm -r "$projectname"_epistasis
fi
./1-4_epistasis_Stew.sh ${projectname} "-onlyko"

# TODO: AVOID TO SED THE R SCRIPT AND USE A PARAMETER FOR projectname
echo "3, Analyse genetic interactions of the model"
sed "s/projectname/"$projectname"/g" Analyses_of_genetic_interactions_Stew_workflow.R > Analyses_of_genetic_interactions_Stew_workflow_post.R
chmod 755 Analyses_of_genetic_interactions_Stew_workflow_post.R
Rscript Analyses_of_genetic_interactions_Stew_workflow_post.R

##########################################
# WARNING: Do not modify code on the fly #
##########################################
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

echo "4, Cleaning"
rm -rf ./${projectname}*
rm inputs.txt
rm outputs.txt

mv ./ko_file.txt ${ko_file}
cd ../
cd ${CURRENT_DIR}
