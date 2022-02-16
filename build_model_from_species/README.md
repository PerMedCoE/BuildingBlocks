# Build Model From Genes Building Block

This package provides the Build Model From Genes **Building Block (BB)**.

## Table of Contents

  - [Build Model From Genes Building Block](#build-model-from-genes-building-block)
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
singularity image ([`FromSpeciesToMaBoSSModel.singularity`](path/to/singularity.file))
and the building block asset ([`FromSpeciesToMaBoSSModel`](path/to/asset.folder)
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

The `build_model_from_species` package provides a clear interface that allows
it to be used with multiple workflow managers (e.g. PyCOMPSs, NextFlow and
Snakemake).

It can be imported from python and invoked directly from a **PyCOMPSs**
application, or through the command line for other workflow managers
(e.g. Snakemake and NextFlow).

The command line is:

```bash
build_model_from_species_BB -d \
    -i <input_file> \
    -o <output_bnd_file> <output_cfg_file> \
    -c <config_file>
    --mount_point ${PERMEDCOE_ASSETS}/FromSpeciesToMaBoSSModel:${PERMEDCOE_ASSETS}/FromSpeciesToMaBoSSModel
```

Where the parameters are:

|        | Parameter          | Type | Description                                             |
|--------|--------------------|------|---------------------------------------------------------|
| Input  | \<input_file>      | File | [TO BE COMPLETED]                                       |
| Output | \<output_bnd_file> | File | [TO BE COMPLETED]                                       |
| Output | \<output_cfg_file> | File | [TO BE COMPLETED]                                       |
| Config | \<config_file>     | File | Configuration file. Must include the **build_model_from** key with a value that can be **genes** or **sif** |

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
