# Single-Cell Processing Building Block

This package provides the Single-Cell Processing **Building Block (BB)**.

## Table of Contents

- [Single-Cell Processing Building Block](#single-cell-processing-building-block)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [User instructions](#user-instructions)
    - [Requirements](#requirements)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Uninstall](#uninstall)
  - [Contact](#contact)

## Description

This building block enables the processing and analysis of single-cell RNA-Seq data from each patient in a sample. The first step of the protocol includes quality control, filtering and normalisation of the count matrices at the cellular level. Next, the number of variable genes in each individual is determined and the corresponding scaled matrices are obtained, allowing in the next step the application of dimensionality reduction techniques such as PCA, T-SNE and UMAP.

Finally, cells are clustered using graph-based techniques and annotated to their corresponding cell type, enabling subsequent building blocks to select and work with the set of cells that are relevant to the disease under study (e.g. epithelial cells in COVID19 disease).

## User instructions

### Requirements

- Python >= 3.6
- [Singularity](https://singularity.lbl.gov/docs-installation)
- `permedcoe` base package: `python3 -m pip install permedcoe`

In addtion to the dependencies, it is necessary to generate the associated
singularity image ([`single_cell.singularity`](../Resources/images/single_cell.singularity)),
located in the **Resources** folder of this repository.

They **MUST be available and exported in the following environment variable**
before its usage:

```bash
export PERMEDCOE_IMAGES="/path/to/images/"
```

### Installation

This package provides an automatic installation script:

```bash
./install.sh
```

### Usage

The `single_cell_processing_BB` package provides a clear interface that allows
it to be used with multiple workflow managers (e.g. PyCOMPSs, NextFlow and
Snakemake).

It can be imported from python and invoked directly from a **PyCOMPSs**
application, or through the command line for other workflow managers
(e.g. Snakemake and NextFlow).

The command line is:

```bash
SINGLE_CELL_ASSETS=$(python3 -c "import single_cell_processing_BB; import os; print(os.path.dirname(single_cell_processing_BB.__file__))")

single_cell_processing_BB -d \
    --mount_points ${SINGLE_CELL_ASSETS}/assets/:${SINGLE_CELL_ASSETS}/assets/,<working_directory>:<working_directory> \
    --p_id <p_id> \
    --p_group <p_group> \
    --p_file <p_file> \
    --parallelize <parallelize> \
    --norm_data <norm_data> \
    --raw_data <raw_data> \
    --scaled_data <scaled_data> \
    --cells_metadata <cells_metadata> \
    --outdir <outdir> \
    --working_directory <working_directory>
```

Where the parameters are:

|        | Flag                | Parameter            | Type    | Description                         |
|--------|---------------------|----------------------|---------|-------------------------------------|
| Input  | --p_id              | \<p_id>              | String  | Patient ID                          |
| Input  | --p_group           | \<p_group>           | String  | Patient's group label               |
| Input  | --p_file            | \<p_file>            | File    | scRNA-Seq patient's counts          |
| Input  | --parallelize       | \<parallelize>       | Integer | Internal parallelism                |
| Output | --norm_data         | \<norm_data>         | File    | Normalized counts output filename   |
| Output | --raw_data          | \<raw_data>          | File    | Raw counts output filename          |
| Output | --scaled_data       | \<scaled_data>       | File    | Scaled counts output filename       |
| Output | --cells_metadata    | \<cells_metadata>    | File    | Cells' metadata output filename     |
| Output | --outdir            | \<outdir>            | Folder  | Output folder                       |
| Output | --working_directory | \<working_directory> | Folder  | Working directory (temporary files) |

### Uninstall

Uninstall can be achieved by executing the following scripts:

```bash
./uninstall.sh
./clean.sh
```

## Contact

<https://permedcoe.eu/contact/>

This software has been developed for the [PerMedCoE project](https://permedcoe.eu/), funded by the European Commission (EU H2020 [951773](https://cordis.europa.eu/project/id/951773)).

![](https://permedcoe.eu/wp-content/uploads/2020/11/logo_1.png "PerMedCoE")
