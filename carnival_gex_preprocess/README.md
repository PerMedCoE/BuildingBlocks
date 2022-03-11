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

[TO BE COMPLETED]

## User instructions

### Requirements

- Python >= 3.6
- [Singularity](https://singularity.lbl.gov/docs-installation)
- `permedcoe` base package: `python3 -m pip install permedcoe`

In addition to the dependencies, it is necessary to generate the associated
singularity image ([`toolset.singularity`](../Resources/images/toolset.singularity)).

They **MUST be available and exported respectively in the following environment variables**
before its usage:

```bash
export PERMEDCOE_IMAGES="/path/to/images/"
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

The `carnival_gex_preprocess_BB` package provides a clear interface that allows
it to be used with multiple workflow managers (e.g. PyCOMPSs, NextFlow and
Snakemake).

It can be imported from python and invoked directly from a **PyCOMPSs**
application, or through the command line for other workflow managers
(e.g. Snakemake and NextFlow).

The command line is:

```bash
carnival_gex_preprocess_BB -d \
    -i <input_file> <col_genes> <scale> <exclude_cols> <tsv> <remove> <verbose>
    -o <output_file>
```

Where the parameters are:

|        | Parameter           | Type      | Description                                             |
|--------|---------------------|-----------|---------------------------------------------------------|
| Input  | \<input_file>       | String    | [TO BE COMPLETED]                                       |
| Output | \<output_file>      | String    | [TO BE COMPLETED]                                       |
| Input  | \<col_genes>        | String    | [TO BE COMPLETED]                                       |
| Input  | \<scale>            | String    | [TO BE COMPLETED]                                       |
| Input  | \<exclude_cols>     | String    | [TO BE COMPLETED]                                       |
| Input  | \<tsv>              | String    | [TO BE COMPLETED]                                       |
| Input  | \<remove>           | String    | [TO BE COMPLETED]                                       |
| Input  | \<verbose>          | String    | [TO BE COMPLETED]                                       |

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
