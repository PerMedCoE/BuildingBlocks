# Required for UC5 - Covid19
sudo /usr/local/bin/singularity build --sandbox MaBoSS MaBoSS.singularity
sudo chown -R javier:users MaBoSS
tar czf MaBoSS.tar.gz MaBoSS
rm -rf MaBoSS
sudo /usr/local/bin/singularity build --sandbox PhysiCell-COVID19 PhysiCell-COVID19.singularity
sudo chown -R javier:users PhysiCell-COVID19
tar czf PhysiCell-COVID19.tar.gz PhysiCell-COVID19
rm -rf PhysiCell-COVID19
sudo /usr/local/bin/singularity build --sandbox single_cell single_cell.singularity
sudo chown -R javier:users single_cell
tar czf single_cell.tar.gz single_cell
rm -rf single_cell
sudo /usr/local/bin/singularity build --sandbox meta_analysis meta_analysis.singularity
sudo chown -R javier:users meta_analysis
tar czf meta_analysis.tar.gz meta_analysis
rm -rf meta_analysis


## Required for UC2 - Drug synergies (also requires PhysiCell-COVID19 container).
sudo /usr/local/bin/singularity build --sandbox printResults printResults.singularity
sudo chown -R javier:users printResults
tar czf printResults.tar.gz printResults
rm -rf printResults
sudo /usr/local/bin/singularity build --sandbox MaBoSS_sensitivity MaBoSS_sensitivity.singularity
sudo chown -R javier:users MaBoSS_sensitivity
tar czf MaBoSS_sensitivity.tar.gz MaBoSS_sensitivity
rm -rf MaBoSS_sensitivity
sudo /usr/local/bin/singularity build --sandbox FromSpeciesToMaBoSSModel FromSpeciesToMaBoSSModel.singularity
sudo chown -R javier:users FromSpeciesToMaBoSSModel
tar czf FromSpeciesToMaBoSSModel.tar.gz FromSpeciesToMaBoSSModel
rm -rf FromSpeciesToMaBoSSModel

# Required for UC2 - Single drug prediction  ---- BUILT SANDBOXES FROM SIF FILES
## Download new BB singularity files
wget https://github.com/saezlab/permedcoe/archive/refs/heads/master.zip
unzip master.zip
cd permedcoe-master/containers

cd toolset
sudo /usr/local/bin/singularity build toolset.sif toolset.singularity
mv toolset.sif ../../../
cd ..
sudo /usr/local/bin/singularity build --sandbox toolset toolset.sif
sudo chown -R javier:users toolset
tar czf toolset.tar.gz toolset
rm -rf toolset

cd carnivalpy
sudo /usr/local/bin/singularity build carnivalpy.sif carnivalpy.singularity
mv carnivalpy.sif ../../../
cd ..
sudo /usr/local/bin/singularity build --sandbox carnivalpy carnivalpy.sif
sudo chown -R javier:users carnivalpy
tar czf carnivalpy.tar.gz carnivalpy
rm -rf carnivalpy

cd ml-jax
sudo /usr/local/bin/singularity build ml-jax.sif ml-jax.singularity
mv ml-jax.sif ../../../tf-jax.sif
cd ..
sudo /usr/local/bin/singularity build --sandbox tf-jax tf-jax.sif
sudo chown -R javier:users tf-jax
tar czf tf-jax.tar.gz tf-jax
rm -rf tf-jax

cd ../..
## Cleanup
rm -rf permedcoe-master
rm master.zip
