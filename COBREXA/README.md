# COBREXA Building Block

This package provides the COBREXA **Building Block (BB)**.

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

[TODO: ADD DESCRIPTION]

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
COBREXA_BB -d \
    --verbose <verbose> \
    --input_xml <input_xml> \
    --output_txt <output_txt>
```

Where the parameters are:

|        | Flag          | Parameter      | Type      | Description                                           |
|--------|---------------|----------------|-----------|-------------------------------------------------------|
| Input  | --verbose     | \<verbose>     | Boolean   | Enable or disable debug mode (true | false)           |
| Input  | --input_xml   | \<input_xml>   | File      | Input xml file                                        |
| Output | --output_txt  | \<output_txt>  | File      | Output txt file                                       |


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
