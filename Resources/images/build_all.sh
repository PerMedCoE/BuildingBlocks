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

cd toolset
sudo /usr/local/bin/singularity build toolset.sif toolset.singularity
mv toolset.sif ../../../
cd ..

cd carnivalpy
sudo /usr/local/bin/singularity build carnivalpy.sif carnivalpy.singularity
mv carnivalpy.sif ../../../
cd ..

cd ml-jax
sudo /usr/local/bin/singularity build ml-jax.sif ml-jax.singularity
mv ml-jax.sif ../../../tf-jax.sif
cd ..

cd ../..
## Cleanup
rm -rf permedcoe-master
rm master.zip