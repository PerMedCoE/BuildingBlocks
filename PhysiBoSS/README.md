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
    - [Uninstall](#uninstall)
  - [Contact](#contact)

## Description

In this building block we perform a multiscale simulation of a population of cells using PhysiBoSS.
The tool uses the different Boolean models personalized by the "Personalize patient" building block and with the mutants selected by the "High-throughput mutant analysis" building block.
More information on this tool can be found in the work ["Ponce-de-Leon,M. et al. (2022) PhysiBoSS 2.0: a sustainable integration of stochastic Boolean and agent-based modelling frameworks. bioRxiv, 2022.01.06.468363."](https://www.biorxiv.org/content/10.1101/2022.01.06.468363v1) and its code can be found in [its GitHub repository](https://github.com/PhysiBoSS/PhysiBoSS).

## User instructions

### Requirements

- Python >= 3.6
- [Singularity](https://singularity.lbl.gov/docs-installation)
- `permedcoe` base package: `python3 -m pip install permedcoe`

In addtion to the dependencies, it is necessary to generate the associated
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

The command line is:

```bash
PHYSIBOSS_ASSETS=$(python3 -c "import PhysiBoSS_BB; import os; print(os.path.dirname(PhysiBoSS_BB.__file__))")

PhysiBoSS_BB -d \
      -i <sample> <repetition> <prefix> <bnd_file> <cfg_file> \
      -o  <out_file> <err_file> \
      --mount_points ${PHYSIBOSS_ASSETS}/assets/:${PHYSIBOSS_ASSETS}/assets/
```

Where the parameters are:

|        | Parameter      | Type      | Description                           |
|--------|----------------|-----------|---------------------------------------|
| Input  | \<sample>      | String    | Patient's identifier                  |
| Input  | \<repetition>  | Int       | Number of repetition to be performed  |
| Input  | \<prefix>      | String    | Name of the model                     |
| Input  | \<bnd_file>    | File      | Name of the model's BND file          |
| Input  | \<cfg_file>    | File      | Name of the model's CFG file          |
| Input  | \<parallel>    | Int       | Internal parallelism                  |
| Output | \<out_file>    | File      | Main output of the PhysiBoSS run      |
| Output | \<err_file>    | File      | Error output of the PhysiBoSS run     |
| Output | \<results_dir> | Directory | Results directory                     |

### Uninstall

Uninstall can be achieved by executing the following scripts:

```bash
./uninstall.sh
./clean.sh
```

## Contact

<https://permedcoe.eu/contact/>
