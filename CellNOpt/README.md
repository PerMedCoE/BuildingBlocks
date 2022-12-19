# CellNOpt Building Block

This package provides the CellNOpt **Building Block (BB)**.

## Table of Contents

- [CellNOpt Building Block](#cellnopt-building-block)
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

This is the refactored CellNopt in C++ with the ACO solver with OpenMP/MPI support. A description of what CellNopt is and how to use it is available here https://saezlab.github.io/CellNOptR/.

## User instructions

### Requirements

- Python >= 3.6
- [Singularity](https://singularity.lbl.gov/docs-installation)
- `permedcoe` base package: `python3 -m pip install permedcoe`

In addition to the dependencies, it is necessary to generate the associated
singularity image ([`signaling-solvers.singularity`](../Resources/images/signaling-solvers.singularity)),
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

The `CellNOpt_BB` package provides a clear interface that allows
it to be used with multiple workflow managers (e.g. PyCOMPSs, NextFlow and
Snakemake).

It can be imported from python and invoked directly from a **PyCOMPSs**
application, or through the command line for other workflow managers
(e.g. Snakemake and NextFlow).

The command line is:

```bash
CellNOpt_BB -d \
    -i <input_file>
```

Where the parameters are:

|        | Parameter          | Type      | Description                                             |
|--------|--------------------|-----------|---------------------------------------------------------|
| Input  | \<input_file>      | String    | HDF5 input data required by CellNopt.                   |


An input toy example is available here: https://github.com/saezlab/permedcoe/blob/master/containers/parallel-solvers/examples/cellnopt_toy_example.h5

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
