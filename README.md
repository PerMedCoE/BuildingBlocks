# PerMedCoE Building Blocks' Catalogue

This repository contains the **Building Blocks** developed within the **HPC/Exascale Centre of Excellence in Personalised Medicine** (PerMedCoE).

## Table of Contents

- [PerMedCoE Building Blocks' Catalogue](#permedcoe-building-blocks-catalogue)
  - [Table of Contents](#table-of-contents)
  - [List of Building Blocks](#list-of-building-blocks)
  - [License](#license)
  - [Contact](#contact)

## List of Building Blocks

1. [**Carnival**](Carnival/)

    This building block uses the accelerated CARNIVAL simulator with OpenMP and ACO solver with MPI which can be used in a HPC system.

2. [**CarnivalPy**](CarnivalPy/)

   This building block uses the normal version of CARNIVAL for Python with support for different open-source and commercial MPI solvers.

3. [**Carnival_feature_merger**](Carnival_feature_merger/)

   This building block merges the results of CARNIVAL.

4. [**Carnival_gex_preprocess**](Carnival_gex_preprocess/)

    This building block downloads GEX data from GDSC and applies minimal transformations required for other building blocks.

5. [**CellNOpt**](CellNOpt/)

    This building block uses the accelerated CellNopt simulator with OpenMP and the ACO solver.

6. [**MaBoSS**](MaBoSS/)

    This building block uses MaBoSS to screen all the possible knock outs of a given Boolean model.

7. [**PhysiBoSS**](PhysiBoSS/)

    This building block performs a multiscale simulation of a population of cells using PhysiBoSS.

8. [**Build Model From Species**](build_model_from_species/)

    This building block generates a boolean model of interest from a list of genes.

9. [**Export Solver HDF5**](export_solver_hdf5/)

   This building block exports the CSV files defining the problem of CARNIVAL/CellNopt to a R format file required for the simulators.

10. [**Meta-analysis of PhysiBoSS Output**](meta_analysis/)

    This building block performs a meta-analysis to determine which parameters of interest in PhysiBoSS are distributed differently among the patient subgroups.

11. [**ML Jax Drug Prediction**](ml_jax_drug_prediction/)

    This building block implementing the ML strategy for prediction of drug responses on cell lines, accelerated with JAX.

12. [**Omnipath**](omnipath/)

    This building block downloads the latest prior knowledge network (PKN) from the whole database from a predefined list of genes and can be reduced to a subset of selected public databases. It can be extended to provide more options to pre-filter genes for example.

13. [**Personalize Patient**](personalize_patient/)

    This building block tailors a given MaBoSS Boolean model to a given RNAseq dataset of interest, for instance from the "Single-cell Processing" building block.

14. [**Print Drug Results**](print_drug_results/)

    This building block generates report from raw simulation results of large drug screening.

15. [**Progeny**](progeny/)

    This building block computes a matrix of samples x pathways with pathway activities given gene expression data. This is required to compute cell features summarising gene expressions into a vector of 11 pathway activities that is useful to predict drug responses for any cell.

16. [**Single-cell Processing**](single_cell_processing/)

    This building block performs the processing and analysis of the single-cell RNA-Seq data from the patients included in the sample.

17. [**TF Enrichment**](tf_enrichment/)

    This building block uses the tool Dorothea to calculate the TF activities from changes in downstream gene targets. This is required by CARNIVAL in order to extract a subnetwork from the PKN connecting perturbations to TFs.


## License

[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)

## Contact

<https://permedcoe.eu/contact/>
