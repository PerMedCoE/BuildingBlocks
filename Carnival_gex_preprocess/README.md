# Carnival Gex Preprocess Building Block

This package provides the Carnival Gex Preprocess **Building Block (BB)**.

## Table of Contents

- [Carnival Gex Preprocess Building Block](#carnival-gex-preprocess-building-block)
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

This building block processes (reshapes and scales) gene expression data from the [Genomics of Drug Sensitivity in Cancer (GDSC)](https://www.cancerrxgene.org/) database for use by other building blocks.

## User instructions

### Requirements

- Python >= 3.6
- [Singularity](https://singularity.lbl.gov/docs-installation)
- `permedcoe` base package: `python3 -m pip install permedcoe`

In addition to the dependencies, it is necessary to generate the associated
singularity image ([`toolset.singularity`](../Resources/images/toolset.singularity)),
located in the **Resources** folder of this repository.

They **MUST be available and exported respectively in the following environment variable**
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

The `Carnival_gex_preprocess_BB` package provides a clear interface that allows
it to be used with multiple workflow managers (e.g. PyCOMPSs, NextFlow and
Snakemake).

It can be imported from python and invoked directly from a **PyCOMPSs**
application, or through the command line for other workflow managers
(e.g. Snakemake and NextFlow).

The command line is:

```bash
CARNIVAL_GEX_PREPROCESS_ASSETS=$(python3 -c "import Carnival_gex_preprocess_BB; import os; print(os.path.dirname(Carnival_gex_preprocess_BB.__file__))")

Carnival_gex_preprocess_BB -d \
    --mount_point ${CARNIVAL_GEX_PREPROCESS_ASSETS}/assets:${CARNIVAL_GEX_PREPROCESS_ASSETS}/assets, <working_directory>:<working_directory> \
    --input_file <input_file> \
    --col_genes <col_genes> \
    --scale <scale> \
    --exclude_cols <exclude_cols> \
    --tsv <tsv> \
    --remove <remove> \
    --verbose <verbose> \
    --output_file <output_file> \
    --working_directory <working_directory>
```

Where the parameters are:

|        | Flag                | Parameter            | Type   | Description                                                              |
|--------|---------------------|----------------------|--------|--------------------------------------------------------------------------|
| Input  | --input_file        | \<input_file>        | File   | csv/url with the GDSC gene expression data                               |
| Input  | --col_genes         | \<col_genes>         | String | Name of the column containing the gene symbols. Default = `GENE_SYMBOLS` |
| Input  | --scale             | \<scale>             | String | Normalize genes across samples (TRUE/FALSE)                              |
| Input  | --exclude_cols      | \<exclude_cols>      | String | Exclude columns containing the given string. Default = `GENE_title`      |
| Input  | --tsv               | \<tsv>               | String | Import as TSV instead of CSV (TRUE/FALSE)                                |
| Input  | --remove            | \<remove>            | String | Remove the given substring from columns. Default = `.DATA`               |
| Input  | --verbose           | \<verbose>           | String | Verbose output (TRUE/FALSE)                                              |
| Output | --output_file       | \<output_file>       | File   | Processed csv file                                                       |
| Output | --working_directory | \<working_directory> | Folder | Working directory (temporary files)                                      |

Here is an example from https://github.com/saezlab/permedcoe/blob/master/containers/workflow_bb.sh preprocessing GDSC data:

```bash
wget -O gdsc_gex.zip https://www.cancerrxgene.org/gdsc1000/GDSC1000_WebResources/Data/preprocessed/Cell_line_RMA_proc_basalExp.txt.zip
unzip gdsc_gex.zip
Carnival_gex_preprocess_BB \
    --input_file Cell_line_RMA_proc_basalExp.txt \
    --col_genes GENE_SYMBOLS \
    --scale FALSE \
    --exclude_cols GENE_title \
    --tsv TRUE \
    --remove DATA. \
    --verbose TRUE \
    --output_file gex.csv
```

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

This software has been developed for the [PerMedCoE project](https://permedcoe.eu/), funded by the European Commission (EU H2020 [951773](https://cordis.europa.eu/project/id/951773)).

![](https://permedcoe.eu/wp-content/uploads/2020/11/logo_1.png "PerMedCoE")
