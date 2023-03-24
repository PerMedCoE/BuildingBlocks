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

This building block performs automatic network construction using OmniPath and pypath. This enables the generation of a Boolean model in MaBoSS format. It takes a list of genes of interest and returns either a simple network as a SIF file or a MaBoSS network as a BND and CFG files.

## User instructions

### Requirements

- Python >= 3.6
- [Singularity](https://singularity.lbl.gov/docs-installation)
- `permedcoe` base package: `python3 -m pip install permedcoe`

In addtion to the dependencies, it is necessary to generate the associated
singularity image ([`FromSpeciesToMaBoSSModel.singularity`](../Resources/images/FromSpeciesToMaBoSSModel.singularity)),
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

The `build_model_from_species` package provides a clear interface that allows
it to be used with multiple workflow managers (e.g. PyCOMPSs, NextFlow and
Snakemake).

It can be imported from python and invoked directly from a **PyCOMPSs**
application, or through the command line for other workflow managers
(e.g. Snakemake and NextFlow).

The command line is:

```bash
BUILD_MODEL_FROM_SPECIES_ASSETS=$(python3 -c "import build_model_from_species_BB; import os; print(os.path.dirname(build_model_from_species_BB.__file__))")

build_model_from_species_BB -d \
    --mount_point ${BUILD_MODEL_FROM_SPECIES_ASSETS}/assets:${BUILD_MODEL_FROM_SPECIES_ASSETS}/assets,<working_directory>:<working_directory> \
    --build_model_from <genes | sif>
    --input_file <input_file> \
    --output_bnd_file <output_bnd_file> \
    --output_cfg_file <output_cfg_file> \
    --working_directory <working_directory>
```

Where the parameters are:

|        | Flag                | Parameter            | Type    | Description                            |
|--------|---------------------|----------------------|---------|----------------------------------------|
| Input  | --build_model_from  | \<genes|sif>         | String  | Build model from genes or sif          |
| Input  | --input_file        | \<input_file>        | File    | List of genes as a CSV file            |
| Output | --output_bnd_file   | \<output_bnd_file>   | File    | BND file of the generated MaBoSS model |
| Output | --output_cfg_file   | \<output_cfg_file>   | File    | CFG file of the generated MaBoSS model |
| Output | --working_directory | \<working_directory> | Folder  | Working directory (temporary files)    |

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
