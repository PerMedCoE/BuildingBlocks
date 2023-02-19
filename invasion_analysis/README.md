# Invasion Analysis Building Block

This package provides the Invasion Analysis **Building Block (BB)**.

## Table of Contents

- [Invasion Analysis Building Block](#invasion-analysis-building-block)
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

This building block extracts quantifications about type of invasion from a physiboss result.

## User instructions

### Requirements

- Python >= 3.6
- [Singularity](https://singularity.lbl.gov/docs-installation)
- `permedcoe` base package: `python3 -m pip install permedcoe`

In addtion to the dependencies, it is necessary to generate the associated
singularity image ([`InvasionAnalysis.singularity`](../Resources/images/InvasionAnalysis.singularity)),
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

The `invasion_analysis` package provides a clear interface that allows
it to be used with multiple workflow managers (e.g. PyCOMPSs, NextFlow and
Snakemake).

It can be imported from python and invoked directly from a **PyCOMPSs**
application, or through the command line for other workflow managers
(e.g. Snakemake and NextFlow).

The command line is:

```bash
INVASION_ANALYSIS_ASSETS=$(python3 -c "import invasion_analysis_BB; import os; print(os.path.dirname(invasion_analysis_BB.__file__))")

invasion_analysis_BB -d \
    --mount_point ${PERSONALIZE_PATIENT_ASSETS}/assets:${PERSONALIZE_PATIENT_ASSETS}/assets \
    --physiboss_result_path <physiboss_result_path> \
    --output_data <output_data> 
```

Where the parameters are:

|        | Flag                     | Parameter          | Type    | Description                              |
|--------|--------------------------|--------------------|---------|------------------------------------------|
| Input  | --physiboss_result_path  | \<input_file>      | File    | Path of the PhysiBoSS result to analyse  |
| Output | --output_data            | \<output_data> | File    | Path of the CSV file to generate         |

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
