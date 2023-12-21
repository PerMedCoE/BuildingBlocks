# PhysiBoSS Building Block

This package provides the PhysiBoSS **Building Block (BB)**.

## Table of Contents

- [PhysiBoSS Building Block](#physiboss-building-block)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [User instructions](#user-instructions)
    - [Requirements](#requirements)
    - [Installation](#installation)
    - [Usage](#usage)
      - [Default](#default)
      - [physiboss\_model](#physiboss_model)
      - [analyse\_replicates](#analyse_replicates)
    - [Uninstall](#uninstall)
  - [License](#license)
  - [Contact](#contact)

## Description

This building block is used to perform a multiscale simulation of a population of cells using PhysiBoSS. The tool uses the different Boolean models personalised by the `Personalise patient` building block and with the mutants selected by the `High-throughput mutant analysis` building block. More information on this tool can be found in [Ponce-de-Leon et al. (2022)](https://www.biorxiv.org/content/10.1101/2022.01.06.468363v1) and the [PhysiBoSS GitHub repository](https://github.com/PhysiBoSS/PhysiBoSS).

## User instructions

### Requirements

- Python >= 3.6
- [Singularity](https://singularity.lbl.gov/docs-installation)
- `permedcoe` base package: `python3 -m pip install permedcoe`

In addition to the dependencies, it is necessary to generate the associated
singularity image ([`PhysiCell-COVID19.singularity`](../Resources/images/PhysiCell-COVID19.singularity)),
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

The `PhysiBoSS` package provides a clear interface that allows
it to be used with multiple workflow managers (e.g. PyCOMPSs, NextFlow and
Snakemake).

It can be imported from python and invoked directly from a **PyCOMPSs**
application, or through the command line for other workflow managers
(e.g. Snakemake and NextFlow).

Supports 3 different operations modes:

- default
- physiboss_model
- analyse_replicates

#### Default

The command line is:

```bash
PhysiBoSS_BB -d \
    --tmpdir PhysiBoSS_wd \
    default \
    --sample <sample> \
    --repetition <repetition> \
    --prefix <prefix> \
    --bnd_file <bnd_file> \
    --cfg_file <cfg_file> \
    --out_file <out_file> \
    --err_file <err_file> \
    --results_file <results_file> \
    --parallel <parallel> \
    --max_time <max_time>
```

Where the parameters are:

|        | Flag                | Parameter            | Type    | Description                          |
|--------|---------------------|----------------------|---------|--------------------------------------|
| Input  | --sample            | \<sample>            | String  | Patient's identifier                 |
| Input  | --repetition        | \<repetition>        | Integer | Number of repetition to be performed |
| Input  | --prefix            | \<prefix>            | String  | Name of the model                    |
| Input  | --bnd_file          | \<bnd_file>          | File    | Name of the model's BND file         |
| Input  | --cfg_file          | \<cfg_file>          | File    | Name of the model's CFG file         |
| Input  | --parallel          | \<parallel>          | Integer | Internal parallelism                 |
| Input  | --max_time          | \<max_time>          | Integer | PhysiBoSS simulation maximum time    |
| Output | --out_file          | \<out_file>          | File    | Main output of the PhysiBoSS run     |
| Output | --err_file          | \<err_file>          | File    | Error output of the PhysiBoSS run    |
| Output | --results_dir       | \<results_dir>       | Folder  | Results directory                    |
| Output | --working_directory | \<working_directory> | Folder  | Working directory (temporary files)  |


#### physiboss_model

The command line is:

```bash
PhysiBoSS_BB -d \
    --tmpdir PhysiBoSS_wd \
    physiboss_model \
    --sample <sample> \
    --repetition <repetition> \
    --prefix <prefix> \
    --model_dir <model_dir> \
    --out_file <out_file> \
    --err_file <err_file> \
    --results_file <results_file> \
    --parallel <parallel> \
    --max_time <max_time>
```

Where the parameters are:

|        | Flag                | Parameter            | Type    | Description                          |
|--------|---------------------|----------------------|---------|--------------------------------------|
| Input  | --sample            | \<sample>            | String  | Patient's identifier                 |
| Input  | --repetition        | \<repetition>        | Integer | Number of repetition to be performed |
| Input  | --prefix            | \<prefix>            | String  | Name of the model                    |
| Input  | --model_dir         | \<model_dir>         | Folder  | Model directory                      |
| Output | --out_file          | \<out_file>          | File    | Main output of the PhysiBoSS run     |
| Output | --err_file          | \<err_file>          | File    | Error output of the PhysiBoSS run    |
| Output | --results_dir       | \<results_dir>       | Folder  | Results directory                    |
| Input  | --parallel          | \<parallel>          | Integer | Internal parallelism                 |
| Input  | --max_time          | \<max_time>          | Integer | PhysiBoSS simulation maximum time    |


#### analyse_replicates

The command line is:

```bash
PhysiBoSS_BB -d \
    --tmpdir PhysiBoSS_wd \
    analyse_replicates \
    --replicates <replicates> \
    --replicates_folder <replicates_folder> \
    --prefix <prefix> \
    --out_file <out_file> \
    --err_file <err_file> \
    --results_dir <results_dir> \
    --parallel <parallel>
```

Where the parameters are:

|        | Flag                | Parameter            | Type    | Description                          |
|--------|---------------------|----------------------|---------|--------------------------------------|
| Input  | --replicates        | \<replicates>        | Integer | Number of replicates                 |
| Input  | --replicates_folder | \<replicates_folder> | Folder  | Replicates folder                    |
| Input  | --prefix            | \<prefix>            | String  | Name of the model                    |
| Output | --out_file          | \<out_file>          | File    | Main output of the PhysiBoSS run     |
| Output | --err_file          | \<err_file>          | File    | Error output of the PhysiBoSS run    |
| Output | --results_dir       | \<results_dir>       | Folder  | Results directory                    |
| Input  | --parallel          | \<parallel>          | Integer | Internal parallelism                 |


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
