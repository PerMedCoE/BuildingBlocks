# Personalize Patient Building Block

This package provides the Personalize Patient **Building Block (BB)**.

## Table of Contents

  - [Personalize Patient Building Block](#personalize-patient-building-block)
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

In addtion to the dependencies, it is necessary to generate the associated
singularity image ([`personalize_patient.singularity`](path/to/singularity.file))
and the building block asset ([`personalize_patient`](path/to/asset.folder)
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

The `personalize_patient` package provides a clear interface that allows
it to be used with multiple workflow managers (e.g. PyCOMPSs, NextFlow and
Snakemake).

It can be imported from python and invoked directly from a **PyCOMPSs**
application, or through the command line for other workflow managers
(e.g. Snakemake and NextFlow).

The command line is:

```bash
personalize_patient_BB -d \
      -i <normalized_data_file> <cells_metadata> <data_folder> <model_prefix> <prefix> <ko_file> \
      -o <result_folder> \
      --mount_points ${COVID19_BB_ASSETS}/personalize_patient/:${COVID19_BB_ASSETS}/personalize_patient/,<data_folder>:<data_folder>
```

Where the parameters are:

|        | Parameter               | File      | Description                                             |
|--------|-------------------------|-----------|---------------------------------------------------------|
| Input  | \<normalized_data_file> | File      | tsv [TO BE COMPLETED]                                   |
| Input  | \<cells_metadata>       | File      | tsv [TO BE COMPLETED]                                   |
| Input  | \<data_folder>          | Directory | [TO BE COMPLETED]                                       |
| Input  | \<model_prefix>         | String    | [TO BE COMPLETED]                                       |
| Input  | \<prefix>               | String    | [TO BE COMPLETED]                                       |
| Input  | \<ko_file>              | File      | [TO BE COMPLETED]                                       |
| Output | \<result_folder>        | Directory | [TO BE COMPLETED]                                       |

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
