# Single Cell Processing Building Block

This package provides the Single Cell Processing **Building Block (BB)**.

## Table of Contents

- [Single Cell Processing Building Block](#single-cell-processing-building-block)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [User instructions](#user-instructions)
    - [Requirements](#requirements)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Uninstall](#uninstall)
  - [License](#license)
  - [Contact](#contact)

## Description

This BB performs the processing and analysis of single-cell RNA-Seq data from each patient in the sample.  The first step of the protocol includes quality control, filtering and normalisation of the count matrices at the cellular level. Next, the number of variable genes in each individual is determined and the corresponding scaled matrices are obtained, allowing in the next step the application of dimensionality reduction techniques such as PCA, T-SNE and UMAP. Finally, cells are clustered using graph-based techniques and annotated to their corresponding cell type, enabling subsequent BBs to select and work with the set of cells that are relevant to the disease under study (e.g. epithelial cells in COVID19 disease).

## User instructions

### Requirements

- Python >= 3.6
- [Singularity](https://singularity.lbl.gov/docs-installation)
- `permedcoe` base package: `python3 -m pip install permedcoe`

In addtion to the dependencies, it is necessary to generate the associated
singularity image ([`single_cell.singularity`](../Resources/images/single_cell.singularity))
and the building block asset ([`single_cell`](../Resources/assets/single_cell)
folder), located in the **Resources** folder of this repository.

They **MUST be available and exported in the following environment variables**
before its usage:

```bash
export PERMEDCOE_IMAGES="/path/to/images/"
export PERMEDCOE_ASSETS="/path/to/assets/"
```

### Installation

This package provides an automatic installation script:

```bash
./install.sh
```

This script creates a file `installation_files.txt` to keep track of the
installed files.
It is used with the `uninstall.sh` script to uninstall the Building Block
from the system.

### Usage

The `single_cell_processing` package provides a clear interface that allows
it to be used with multiple workflow managers (e.g. PyCOMPSs, NextFlow and
Snakemake).

It can be imported from python and invoked directly from a **PyCOMPSs**
application, or through the command line for other workflow managers
(e.g. Snakemake and NextFlow).

The command line is:

```bash
single_cell_processing -d \
    -i <metadata_file(tsv)> \
    -o <result_folder> \
    --mount_points ${COVID19_BB_ASSETS}/single_cell/:${COVID19_BB_ASSETS}/single_cell/
```

Where the parameters are:

|        | Parameter        | Type      | Description                                             |
|--------|------------------|-----------|---------------------------------------------------------|
| Input  | \<metadata_file> | File      | Sample information                                      |
| Output | \<result_folder> | Directory | Output folder                                           |

### Uninstall

Uninstall can be achieved by executing the following scripts:

```bash
./uninstall.sh
./clean.sh
```

## License

[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)

## Contact

<https://permedcoe.eu/contact/>
