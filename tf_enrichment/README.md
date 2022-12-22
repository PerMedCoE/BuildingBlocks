# TF Enrichment Building Block

This package provides the TF Enrichment **Building Block (BB)**.

## Table of Contents

- [TF Enrichment Building Block](#tf-enrichment-building-block)
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

The `TF Enrichment` building block uses [DecoupleR](https://saezlab.github.io/decoupleR/) and [Dorothea](https://saezlab.github.io/dorothea/) to estimate transcription factor activities from perturbational data.

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

The `tf_enrichment_BB` package provides a clear interface that allows
it to be used with multiple workflow managers (e.g. PyCOMPSs, NextFlow and
Snakemake).

It can be imported from python and invoked directly from a **PyCOMPSs**
application, or through the command line for other workflow managers
(e.g. Snakemake and NextFlow).

The command line is:

```bash
tf_enrichment_BB -d \
    --input_file <input_file> \
    --weight_col <weight_col> \
    --source <source> \
    --id_col <id_col> \
    --tsv <tsv> \
    --minsize <minsize> \
    --confidence <confidence> \
    --verbose <verbose> \
    --output_file <output_file>
```

Where the parameters are:

|        | Flag              | Parameter          | Type    | Description                                                                                                             |
|--------|-------------------|--------------------|---------|-------------------------------------------------------------------------------------------------------------------------|
| Input  | --input_file      | \<input_file>      | File    | Input gene expression data. Genes should be normalized across samples.                                                  |
| Input  | --tsv             | \<tsv>             | String  | Import data as TSV instead of CSV (True/False)                                                                          |
| Input  | --weight_col      | \<weight_col>      | String  | Name of the column containing differential expression values (e.g t-statistic from DESeq2) between a control/treatment condition for example, or just log-fold change. |
| Input  | --id_col          | \<id_col>          | String  | Name of the column for gene ids.                                                                                        |
| Input  | --minsize         | \<minsize>         | Integer | Minimum size for regulons. E.g 10.                                                                                      |
| Input  | --source          | \<source>          | String  | Column with the TFs. Default = `tf`                                                                                     |
| Input  | --confidence      | \<confidence>      | String  | Level of confidence to be used for regulons. E.g.: `A,B,C`. (see https://saezlab.github.io/dorothea/ for documentation) |
| Input  | --verbose         | \<verbose>         | String  | Verbose output (True/False).                                                                                            |
| Input  | --pval_threshold  | \<pval_threshold>  | Float   | Filter out TFs with adj. p-val above the provided value.                                                                |
| Input  | --export_carnival | \<export_carnival> | String  |  Export a table with the results with two columns (id, value) only (for CARNIVAL)(TRUE/FALSE).                          |
| Output | --output_file     | \<output_file>     | File    | Result csv file with estimated TF activities.                                                                           |


Example from normalized GEX data from GDSC using `preprocess_bb` on sample `DATA.906826`. Note that here we assume that genes are normalized across columns and so the control vs condition is the given column against the other conditions as control:

```bash
tf_enrichment_BB \
    --input_file gex_n.csv \
    --weight_col 906826 \
    --source tf \
    --id_col GENE_SYMBOLS \
    --tsv FALSE \
    --minsize 10 \
    --confidence 'A,B,C' \
    --verbose TRUE \
    --output_file 906826/measurements.csv
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
