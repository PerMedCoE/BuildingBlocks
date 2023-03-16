# PhysiBoSS Invasion Building Block

This package provides the PhysiBoSS Invasion **Building Block (BB)**.

## Table of Contents

- [PhysiBoSS Invasion Building Block](#physiboss-building-block)
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

This building block is used to perform a multiscale simulation of a population of cancer cells undergoing invasion using PhysiBoSS.More information on this tool can be found in [Ponce-de-Leon et al. (2022)](https://www.biorxiv.org/content/10.1101/2022.01.06.468363v1) and the [PhysiBoSS GitHub repository](https://github.com/PhysiBoSS/PhysiBoSS).

## User instructions

### Requirements

- Python >= 3.6
- [Singularity](https://singularity.lbl.gov/docs-installation)
- `permedcoe` base package: `python3 -m pip install permedcoe`

In addtion to the dependencies, it is necessary to generate the associated
singularity image ([`PhysiCell-Invasion.singularity`](../Resources/images/PhysiCell-Invasion.singularity)),
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

The `PhysiBoSS_Invasion` package provides a clear interface that allows
it to be used with multiple workflow managers (e.g. PyCOMPSs, NextFlow and
Snakemake).

It can be imported from python and invoked directly from a **PyCOMPSs**
application, or through the command line for other workflow managers
(e.g. Snakemake and NextFlow).

The command line is:

```bash
PHYSIBOSS_INVASION_ASSETS=$(python3 -c "import PhysiBoSS_BB; import os; print(os.path.dirname(PhysiBoSS_BB.__file__))")

PhysiBoSS_Invasion_BB -d \
      --mount_points ${PHYSIBOSS_INVASION_ASSETS}/assets/:${PHYSIBOSS_INVASION_ASSETS}/assets/ \
      --repetition <repetition> \
      --out_file <out_file> \
      --err_file <err_file>
```

Where the parameters are:

|        | Flag          | Parameter      | Type    | Description                          |
|--------|---------------|----------------|---------|--------------------------------------|
| Input  | --repetition  | \<repetition>  | Integer | Number of repetition to be performed |
| Input  | --parallel    | \<parallel>    | Integer | Internal parallelism                 |
| Input  | --max_time    | \<max_time>    | Integer | PhysiBoSS simulation maximum time    |
| Output | --out_file    | \<out_file>    | File    | Main output of the PhysiBoSS run     |
| Output | --err_file    | \<err_file>    | File    | Error output of the PhysiBoSS run    |
| Output | --results_dir | \<results_dir> | Folder  | Results directory                    |

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
