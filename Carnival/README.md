# Carnival Building Block

This package provides the CARNIVAL **Building Block (BB)**.

## Table of Contents

- [Carnival Building Block](#carnival-building-block)
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

The CARNIVAL building block contains the refactored CARNIVAL C++ with the new Ant Colony Optimisation (ACO) in C++ with support for OpenMP and MPI. The hdf5 file required as an input can be generated with the `Export Solver HDF5` building block. For a general overview of what CARNIVAL does, see the [CARNIVAL website](https://saezlab.github.io/CARNIVAL/). This building block uses the new developed ACO algorithm to find solutions without the need of using ILP solvers.

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

The `Carnival_BB` package provides a clear interface that allows
it to be used with multiple workflow managers (e.g. PyCOMPSs, NextFlow and
Snakemake).

It can be imported from python and invoked directly from a **PyCOMPSs**
application, or through the command line for other workflow managers
(e.g. Snakemake and NextFlow).

The command line is:

```bash
Carnival_BB -d \
    -i <input_file>
```

Where the parameters are:

|        | Flag         | Parameter      | Type   | Description                                                                                                                                |
|--------|--------------|----------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Input  | --input_file | \<input_file>  | String | HDF5 data with the SIF network, measurements and perturbations. This file can be produced from csv files using the `export_solver_hdf5_bb` |


Example usage:

```bash
Carnival_BB --input_file file.h5
```

[Here](https://github.com/saezlab/permedcoe/blob/master/containers/parallel-solvers/examples/carnival_toy_example.h5) is an example of already converted CSV data into h5 that can be used to try CARNIVAL. This example was exported with the `export_solver_hdf5_bb` building block from [this example](https://github.com/saezlab/permedcoe/tree/master/containers/toolset/scripts/examples/export).


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
