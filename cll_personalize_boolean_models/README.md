# Building Block cll_personalize_boolean_models

This package provides the cll_personalize_boolean_models **Building Block (BB)** using the **HPC/Exascale Centre of Excellence in Personalised Medicine**
([PerMedCoE](https://permedcoe.eu/)) base Building Block.

## Table of Contents

- [Building Block cll\_personalize\_boolean\_models](#building-block-cll_personalize_boolean_models)
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

This building block is responsible for building patient-specific boolean models by employing the PROFILE tool and input RNA-Seq data.

## User instructions

### Requirements

- Python >= 3.6
- [Singularity](https://singularity.lbl.gov/docs-installation)
- `permedcoe` base package: `python3 -m pip install permedcoe`

In addition to the dependencies, it is necessary to generate the associated
singularity image ([`cll_personalize_boolean_models.singularity`](../Resources/images/cll_personalize_boolean_models.singularity)),
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

The `cll_personalize_boolean_models` package provides a clear interface that allows
it to be used with multiple workflow managers (e.g. PyCOMPSs, NextFlow and
Snakemake).

It can be imported from python and invoked directly from a **PyCOMPSs**
application, or through the command line for other workflow managers
(e.g. Snakemake and NextFlow).

The command line is:

```bash
cll_personalize_boolean_models_BB -d \
    --tmpdir <working_directory> \
    --sif <sif> \
    --norm_exp <norm_exp> \
    --metadata <metadata> \
    --group <group> \
    --outdir <outdir>
```

Where the parameters are:

|        | Flag       | Parameter            | Type   | Description                         |
|--------|------------|----------------------|--------|-------------------------------------|
|        | --tmpdir   | \<working_directory> | Folder | Working directory (temporary files) |
| Input  | --sif      | \<sif>               | File   | Inferred network (in sif format)    |
| Input  | --norm_exp | \<norm_exp>          | File   | Normalized expression file          |
| Input  | --metadata | \<metadata>          | File   | Sample metadata                     |
| Input  | --group    | \<group>             | String | Group variable                      |
| Output | --outdir   | \<outdir>            | Folder | Output folder                       |


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
