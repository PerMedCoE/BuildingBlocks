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
    -i <input_file> <weight_col> <source> <id_col> <tsv> <minsize> <confidence> <verbose>
    -o <output_file>
```

Where the parameters are:

|        | Parameter          | Type      | Description                                                                                                             |
|--------|--------------------|-----------|-------------------------------------------------------------------------------------------------------------------------|
| Input  | \<input_file>      | String    | Input gene expression data. Genes should be normalized across samples.                                                  |
| Input  | \<weight_col>      | String    | Name of the column containing differential expression values (e.g t-statistic from DESeq2) between a control/treatment condition for example, or just log-fold change. |
| Input  | \<source>          | String    | Column with the TFs. Default = `tf`                                                                                     |
| Input  | \<id_col>          | String    | Name of the column for gene ids.                                                                                        |
| Input  | \<tsv>             | String    | Import data as TSV instead of CSV (True/False)                                                                          |
| Input  | \<minsize>         | Integer   | Minimum size for regulons. E.g 10.                                                                                      |
| Input  | \<confidence>      | String    | Level of confidence to be used for regulons. E.g.: `A,B,C`. (see https://saezlab.github.io/dorothea/ for documentation) |
| Input  | \<verbose>         | String    | Verbose output (True/False).                                                                                            |
| Output | \<output_file>     | String    | Result csv file with estimated TF activities.                                                                           |


Example from normalized GEX data from GDSC using `preprocess_bb` on sample `DATA.906826`. Note that here we assume that genes are normalized across columns and so the control vs condition is the given column against the other conditions as control:

```bash
tfenrichment_BB -i gex.csv DATA.906826 GENE_SYMBOLS tf FALSE 10 'A,B,C' TRUE -o 906826_tf.csv
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
