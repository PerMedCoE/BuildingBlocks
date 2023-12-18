# Building Block cll_prepare_data

This package provides the cll_prepare_data **Building Block (BB)** using the **HPC/Exascale Centre of Excellence in Personalised Medicine**
([PerMedCoE](https://permedcoe.eu/)) base Building Block.

## Table of Contents

- [Building Block cll\_prepare\_data](#building-block-cll_prepare_data)
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

This building block involves an in-house script for the primary analysis of the input RNA-Seq data, focusing on tasks such as differential expression analysis and batch effect correction.

## User instructions

### Requirements

- Python >= 3.6
- [Singularity](https://singularity.lbl.gov/docs-installation)
- `permedcoe` base package: `python3 -m pip install permedcoe`

In addtion to the dependencies, it is necessary to generate the associated
singularity image ([`cll_prepare_data.singularity`](../Resources/images/cll_prepare_data.singularity)),
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

The `cll_prepare_data` package provides a clear interface that allows
it to be used with multiple workflow managers (e.g. PyCOMPSs, NextFlow and
Snakemake).

It can be imported from python and invoked directly from a **PyCOMPSs**
application, or through the command line for other workflow managers
(e.g. Snakemake and NextFlow).

The command line is:

```bash
CLL_PREPARE_DATA_ASSETS=$(python3 -c "import cll_prepare_data_BB; import os; print(os.path.dirname(cll_prepare_data_BB.__file__))")

cll_prepare_data_BB -d \
    --mount_point ${CLL_PREPARE_DATA_ASSETS}/assets:${CLL_PREPARE_DATA_ASSETS}/assets,<working_directory>:<working_directory> \
    --exp <exp> \
    --metadata <metadata> \
    --group <group> \
    --treatment <treatment> \
    --control <control> \
    --xref <xref> \
    --batch <batch> \
    --outdir <outdir> \
    --working_directory <working_directory>
```

Where the parameters are:

|        | Flag        | Parameter    | Type   | Description               |
|--------|-------------|--------------|--------|---------------------------|
| Input  | --exp       | \<exp>       | File   | Expression file           |
| Input  | --metadata  | \<metadata>  | File   | Sample metadata           |
| Input  | --group     | \<group>     | String | Group variable            |
| Input  | --treatment | \<treatment> | String | Label of treated subgroup |
| Input  | --control   | \<control>   | String | Label of control subgroup |
| Input  | --xref      | \<xref>      | File   | Xref translation file     |
| Input  | --batch     | \<batch>     | String | Batch variable            |
| Output | --outdir    | \<outdir>    | Folder | Output folder             |


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
