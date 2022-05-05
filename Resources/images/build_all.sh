# Required for UC5 - Covid19
sudo /usr/local/bin/singularity build MaBoSS.sif MaBoSS.singularity
sudo /usr/local/bin/singularity build PhysiCell-COVID19.sif PhysiCell-COVID19.singularity
sudo /usr/local/bin/singularity build single_cell.sif single_cell.singularity
sudo /usr/local/bin/singularity build meta_analysis.sif meta_analysis.singularity

# Required for UC2 - Drug synergies (also requires PhysiCell-COVID19 container).
sudo /usr/local/bin/singularity build printResults.sif printResults.singularity
sudo /usr/local/bin/singularity build MaBoSS_sensitivity.sif MaBoSS_sensitivity.singularity
sudo /usr/local/bin/singularity build FromSpeciesToMaBoSSModel.sif FromSpeciesToMaBoSSModel.singularity

# Required for UC2 - Single drug prediction
## Download new BB singularity files
wget https://github.com/saezlab/permedcoe/archive/refs/heads/master.zip
unzip master.zip
cd permedcoe-master/containers

# TODO: Add building the containers for single-drug-prediction.

cd ../..
## Cleanup
rm -rf permedcoe-master
rm master.zip