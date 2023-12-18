# Building Block cll_tf_activities

This package provides the cll_tf_activities **Building Block (BB)** using the **HPC/Exascale Centre of Excellence in Personalised Medicine**
([PerMedCoE](https://permedcoe.eu/)) base Building Block.

## Table of Contents

- [Building Block cll\_tf\_activities](#building-block-cll_tf_activities)
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

This building block entails the inference of transcription factor (TF) activities using DecoupleR and the quantification of molecular pathways through PROGENY.

## User instructions

### Requirements

- Python >= 3.6
- [Singularity](https://singularity.lbl.gov/docs-installation)
- `permedcoe` base package: `python3 -m pip install permedcoe`

In addtion to the dependencies, it is necessary to generate the associated
singularity image ([`cll_tf_activities.singularity`](../Resources/images/cll_tf_activities.singularity)),
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

The `cll_tf_activities` package provides a clear interface that allows
it to be used with multiple workflow managers (e.g. PyCOMPSs, NextFlow and
Snakemake).

It can be imported from python and invoked directly from a **PyCOMPSs**
application, or through the command line for other workflow managers
(e.g. Snakemake and NextFlow).

The command line is:

```bash
CLL_TF_ACTIVITIES_ASSETS=$(python3 -c "import cll_tf_activities_BB; import os; print(os.path.dirname(cll_tf_activities_BB.__file__))")

cll_tf_activities_BB -d \
    --mount_point ${CLL_TF_ACTIVITIES_ASSETS}/assets:${CLL_TF_ACTIVITIES_ASSETS}/assets,<working_directory>:<working_directory> \
    --norm_exp <norm_exp> \
    --metadata <metadata> \
    --dea <dea> \
    --group <group> \
    --treatment <treatment> \
    --control <control> \
    --collectri_database <collectri_database> \
    --progeny_database <progeny_database> \
    --outdir <outdir> \
    --activities <activities> \
    --working_directory <working_directory>
```

Where the parameters are:

|        | Flag                 | Parameter             | Type   | Description                        |
|--------|----------------------|-----------------------|--------|------------------------------------|
| Input  | --norm_exp           | \<norm_exp>           | File   | Normalized expression file         |
| Input  | --metadata           | \<metadata>           | File   | Sample metadata                    |
| Input  | --dea                | \<dea>                | File   | Differential expression analysis   |
| Input  | --group              | \<group>              | String | Group variable                     |
| Input  | --treatment          | \<treatment>          | String | Label of treated subgroup          |
| Input  | --control            | \<control>            | String | Label of control subgroup          |
| Input  | --collectri_database | \<collectri_database> | File   | Pre-fetched Collectri database     |
| Input  | --progeny_database   | \<progeny_database>   | File   | Pre-fetched Progreny database      |
| Output | --outdir             | \<outdir>             | Folder | Output folder                      |
| Output | --activities         | \<activities>         | File   | Output TFs infered activities file |


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
