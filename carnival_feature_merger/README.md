# Carnival Feature Merger Building Block

This package provides the Carnival Feature Merger **Building Block (BB)**.

## Table of Contents

- [Carnival Feature Merger Building Block](#carnival-feature-merger-building-block)
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
singularity image ([`carnivalpy.singularity`](../Resources/images/carnivalpy.singularity)).

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

The `carnival_feature_merger_BB` package provides a clear interface that allows
it to be used with multiple workflow managers (e.g. PyCOMPSs, NextFlow and
Snakemake).

It can be imported from python and invoked directly from a **PyCOMPSs**
application, or through the command line for other workflow managers
(e.g. Snakemake and NextFlow).

The command line is:

```bash
carnival_feature_merger_BB -d \
    -i <input_file>
```

Where the parameters are:

|        | Parameter           | Type      | Description                                             |
|--------|---------------------|-----------|---------------------------------------------------------|
| Input  | \<input_file>       | String    | [TO BE COMPLETED]                                       |
| Output | \<output_file>      | String    | [TO BE COMPLETED]                                       |
| Input  | \<feature_file>     | String    | [TO BE COMPLETED]                                       |
| Input  | \<merge_csv_file>   | String    | [TO BE COMPLETED]                                       |
| Input  | \<merge_csv_index>  | String    | [TO BE COMPLETED]                                       |
| Input  | \<merge_csv_prefix> | String    | [TO BE COMPLETED]                                       |

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