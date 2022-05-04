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
Carnival_gex_preprocess_BB -d \
    -i <input_file> <col_genes> <scale> <exclude_cols> <tsv> <remove> <verbose>
    -o <output_file>
```

Where the parameters are:

|        | Parameter           | Type      | Description                                                                |
|--------|---------------------|-----------|----------------------------------------------------------------------------|
| Input  | \<input_file>       | String    | csv/url with the GDSC gene expression data                                 |
| Output | \<output_file>      | String    | processed csv file                                                         |
| Input  | \<col_genes>        | String    | Name of the column containing the gene symbols. Default = `GENE_SYMBOLS`.  |
| Input  | \<scale>            | String    | Normalize genes across samples (True/False)                                |
| Input  | \<exclude_cols>     | String    | Exclude columns containing the given string. Default = `GENE_title`        |
| Input  | \<tsv>              | String    | Import as TSV instead of CSV (True/False)                                  |
| Input  | \<remove>           | String    | Remove the given substring from columns. Default = `.DATA`                 |
| Input  | \<verbose>          | String    | Verbose output (True/False)                                                |

Here is an example from https://github.com/saezlab/permedcoe/blob/master/containers/workflow_bb.sh preprocessing GDSC data:

```bash
wget -O ${tmpdir}/gdsc_gex.zip https://www.cancerrxgene.org/gdsc1000/GDSC1000_WebResources/Data/preprocessed/Cell_line_RMA_proc_basalExp.txt.zip
unzip gdsc_gex.zip -d ${tmpdir}/
carnival_gex_preprocess_bb -i ${tmpdir}/Cell_line_RMA_proc_basalExp.txt GENE_SYMBOLS GENE_title FALSE TRUE TRUE DATA. -o ${tmpdir}/gex.csv
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
