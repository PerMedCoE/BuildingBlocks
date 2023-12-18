# Building Block cll_combine_models

This package provides the cll_combine_models **Building Block (BB)** using the **HPC/Exascale Centre of Excellence in Personalised Medicine**
([PerMedCoE](https://permedcoe.eu/)) base Building Block.

## Table of Contents

- [Building Block cll\_combine\_models](#building-block-cll_combine_models)
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

This building block combines patient or group-specific results from MaBoSS, assessing whether the obtained profiles are appropriately clustered and can serve as predictors of disease subtype.

## User instructions

### Requirements

- Python >= 3.6
- [Singularity](https://singularity.lbl.gov/docs-installation)
- `permedcoe` base package: `python3 -m pip install permedcoe`

In addtion to the dependencies, it is necessary to generate the associated
singularity image ([`cll_combine_models.singularity`](../Resources/images/cll_combine_models.singularity)),
located in the **Resources** folder of this repository.

They **MUST be available and exported in the following environment variable**
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

The `cll_combine_models` package provides a clear interface that allows
it to be used with multiple workflow managers (e.g. PyCOMPSs, NextFlow and
Snakemake).

It can be imported from python and invoked directly from a **PyCOMPSs**
application, or through the command line for other workflow managers
(e.g. Snakemake and NextFlow).

The command line is:

```bash
CLL_COMBINE_MODELS_ASSETS=$(python3 -c "import cll_combine_models_BB; import os; print(os.path.dirname(cll_combine_models_BB.__file__))")

cll_combine_models_BB -d \
    --mount_point ${CLL_COMBINE_MODELS_ASSETS}/assets:${CLL_COMBINE_MODELS_ASSETS}/assets,<working_directory>:<working_directory> \
    --runs <runs> \
    --metadata <metadata> \
    --group <group> \
    --outdir <outdir> \
    --working_directory <working_directory>
```

Where the parameters are:

|        | Flag       | Parameter   | Type   | Description                                             |
|--------|------------|-------------|--------|---------------------------------------------------------|
| Input  | --runs     | \<runs>     | Folder | Folder containing group and patient boolean models runs |
| Input  | --metadata | \<metadata> | File   | Sample metadata                                         |
| Input  | --group    | \<group>    | String | Group variable                                          |
| Output | --outdir   | \<outdir>   | Folder | Output folder                                           |

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