# COBREXA FVA Building Block

This package provides the COBREXA Flux Variability Analysis (FVA) **Building Block (BB)**. Use this BB to analyze the viable feasibility and optimality ranges of your metabolic models.

## Table of Contents

- [COBREXA Building Block](#cobrexa-building-block)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [User instructions](#user-instructions)
    - [Requirements](#requirements)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Uninstall](#uninstall)
  - [Contact](#contact)

## Description

COBREXA is a toolkit for working with large constraint-based metabolic models, and running very large numbers of analysis tasks on these models in parallel. Its main purpose is to make the methods of Constraint-based Reconstruction and Analysis (COBRA) scale to problem sizes that require the use of huge computer clusters and HPC environments, which allows them to be realistically applied to pre-exascale-sized models.

This building block runs Flux Variability Analysis (FVA) on a given model. The analysis computes a feasible range of fluxes that may go through each reaction in the model while the model is in near-optimal state (in particular, constrained to the minimum of 99% of the flux through the objective function). This gives a relatively good overview of what the model is capable of, in particular allowing to enumerate the under-definedness and redundancy present in the main model pathways.

## User instructions

### Requirements

- Python >= 3.6
- [Singularity](https://singularity.lbl.gov/docs-installation)
- `permedcoe` base package: `python3 -m pip install permedcoe`

In addition to the dependencies, it is necessary to download the `cobrexa.jl_latest.sif` singularity image.
It can be downloaded with:

```
singularity pull oras://ghcr.io/lcsb-biocore/apptainer/cobrexa.jl:latest
```

or running the [`cobrexa.jl_latest.sif`](../Resources/images/cobrexa.jl_latest.sh) script,
located in the **Resources** folder of this repository.

It **MUST be available and exported respectively in the following environment variable**
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

The `COBREXA` package provides a clear interface that allows
it to be used with multiple workflow managers (e.g. PyCOMPSs, NextFlow and
Snakemake).

It can be imported from python and invoked directly from a **PyCOMPSs**
application, or through the command line for other workflow managers
(e.g. Snakemake and NextFlow).

The command line is:

```bash
COBREXA_FVA -d \
    --verbose <verbose> \
    --input_sbml <input_sbml> \
    --output_txt <output_txt>
```

Where the parameters are:

|        | Flag          | Parameter      | Type      | Description                                           |
|--------|---------------|----------------|-----------|-------------------------------------------------------|
| Input  | --verbose     | \<verbose>     | Boolean   | Enable or disable debug mode (true | false)           |
| Input  | --input_sbml  | \<input_sbml>  | File      | Input SBML file (internally XML-formatted)            |
| Output | --output_txt  | \<output_txt>  | File      | Output text file                                      |


### Uninstall

Uninstall can be achieved by executing the following scripts:

```bash
./uninstall.sh
./clean.sh
```

## Contact

<https://permedcoe.eu/contact/>

This software has been developed for the [PerMedCoE project](https://permedcoe.eu/), funded by the European Commission (EU H2020 [951773](https://cordis.europa.eu/project/id/951773)).

![](https://permedcoe.eu/wp-content/uploads/2020/11/logo_1.png "PerMedCoE")
