# Building Block cll_network_inference

This package provides the cll_network_inference **Building Block (BB)** using the **HPC/Exascale Centre of Excellence in Personalised Medicine**
([PerMedCoE](https://permedcoe.eu/)) base Building Block.

## Table of Contents

- [Building Block cll\_network\_inference](#building-block-cll_network_inference)
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

This building block involves network inference with CARNIVAL, leveraging Omnipath, as well as DecoupleR and PROGENY results as constraints within the linear programming problem.

## User instructions

### Requirements

- Python >= 3.6
- [Singularity](https://singularity.lbl.gov/docs-installation)
- `permedcoe` base package: `python3 -m pip install permedcoe`

In addtion to the dependencies, it is necessary to generate the associated
singularity image ([`cll_network_inference.singularity`](../Resources/images/cll_network_inference.singularity)),
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

The `cll_network_inference` package provides a clear interface that allows
it to be used with multiple workflow managers (e.g. PyCOMPSs, NextFlow and
Snakemake).

It can be imported from python and invoked directly from a **PyCOMPSs**
application, or through the command line for other workflow managers
(e.g. Snakemake and NextFlow).

The command line is:

```bash
CLL_NETWORK_INFERENCE_ASSETS=$(python3 -c "import cll_network_inference_BB; import os; print(os.path.dirname(cll_network_inference_BB.__file__))")

cll_network_inference_BB -d \
    --mount_point ${CLL_NETWORK_INFERENCE_ASSETS}/assets:${CLL_NETWORK_INFERENCE_ASSETS}/assets,<working_directory>:<working_directory> \
    --cplex_bin <cplex_bin> \
    --activities <activities> \
    --omnipath_database <omnipath_database> \
    --outdir <outdir> \
    --sif <sif> \
    --working_directory <working_directory>
```

Where the parameters are:

|        | Flag                | Parameter            | Type   | Description                      |
|--------|---------------------|----------------------|--------|----------------------------------|
| Input  | --cplex_bin         | \<cplex_bin>         | String | CPLEX binary path                |
| Input  | --activities        | \<activities>        | File   | TF inferred activities file      |
| Input  | --omnipath_database | \<omnipath_database> | File   | Pre-fetched Omnipath database    |
| Output | --outdir            | \<outdir>            | Folder | Output folder                    |
| Output | --sif               | \<sif>               | File   | Inferred network (in sif format) |

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
