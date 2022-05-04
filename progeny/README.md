# PROGENy Building Block

This package provides the PROGENy **Building Block (BB)**.

## Table of Contents

- [PROGENy Building Block](#progeny-building-block)
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

The `PROGENy` building block uses PROGENy to extract pathway activities from gene expression data. Further information on PROGENy can be found on the [Saez Laboratory website](https://saezlab.github.io/progeny/).

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

The `progeny_BB` package provides a clear interface that allows
it to be used with multiple workflow managers (e.g. PyCOMPSs, NextFlow and
Snakemake).

It can be imported from python and invoked directly from a **PyCOMPSs**
application, or through the command line for other workflow managers
(e.g. Snakemake and NextFlow).

The command line is:

```bash
progeny_BB -d \
    -i <input_file> organism> <ntop> <col_genes> <scale> <exclude_cols> <tsv> <perms> <zscore> <verbose>
    -o <output_file>
```

Where the parameters are:

|        | Parameter          | Type      | Description                                                                                                            |
|--------|--------------------|-----------|------------------------------------------------------------------------------------------------------------------------|
| Input  | \<input_file>      | String    | CSV with gene expression data, where rows are genes and columns are samples.                                           |
| Input  | \<organism>        | String    | Human/Mouse                                                                                                            |
| Input  | \<ntop>            | Integer   | Number of top genes used to estimate pathway activities.                                                               |
| Input  | \<col_genes>       | String    | Name of the column containing gene IDs.                                                                                |
| Input  | \<scale>           | String    | Scale data (True/False)                                                                                                |
| Input  | \<exclude_cols>    | String    | Columns containing this string will be removed.                                                                        |
| Input  | \<tsv>             | String    | Import input data as TSV                                                                                               |
| Input  | \<perms>           | String    | Number of permutations to estimate the null distribution. For default usage of PROGENy, just pass 1 to skip this step. |
| Input  | \<zscore>          | String    | If True, the z-scores will be returned for the pathway activity estimations. Else, the function returns a normalized z-score value between -1 and 1 |
| Input  | \<verbose>         | String    | Verbose output (True/False)                                                                                            |
| Output | \<output_file>     | String    | File with the results containing pathway activities.                                                                   |

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
