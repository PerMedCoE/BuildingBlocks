# Export Solver HDF5 Building Block

This package provides the Export Solver HDF5 **Building Block (BB)**.

## Table of Contents

- [Export Solver HDF5 Building Block](#export-solver-hdf5-building-block)
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

Exports input data required by [the vanilla version of CARNIVAL](https://saezlab.github.io/CARNIVAL/) (sif file, measurements and perturbations) into a HDF5 file required by the optimised version of CARNIVAL with the parallel ACO C++ solver.

## User instructions

### Requirements

- Python >= 3.6
- [Singularity](https://singularity.lbl.gov/docs-installation)
- `permedcoe` base package: `python3 -m pip install permedcoe`

In addition to the dependencies, it is necessary to generate the associated
singularity image ([`toolset.singularity`](../Resources/images/toolset.singularity)),
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

The `export_solver_hdf5_BB` package provides a clear interface that allows
it to be used with multiple workflow managers (e.g. PyCOMPSs, NextFlow and
Snakemake).

It can be imported from python and invoked directly from a **PyCOMPSs**
application, or through the command line for other workflow managers
(e.g. Snakemake and NextFlow).

The command line is:

```bash
export_solver_hdf5_BB -d \
    -i <sif> <measurements> <inputs> <verbose>
    -o <output_file>
```

Where the parameters are:

|        | Parameter          | Type      | Description                                             |
|--------|--------------------|-----------|---------------------------------------------------------|
| Input  | \<sif>             | String    | The sif csv file containing the signaling network       |
| Input  | \<measurements>    | String    | The measurements csv with the TFs and weights           |
| Input  | \<inputs>          | String    | The csv file with the input protein targets             |
| Input  | \<verbose>         | String    | Verbose output (True/False)                             |
| Output | \<output_file>     | String    | The final HDF5 file.                                    |


An example with toy data from here https://github.com/saezlab/permedcoe/tree/master/containers/toolset/scripts/examples/export would be:

```bash
export_solver_hdf5_BB -i sif.csv measurements.csv inputs.csv TRUE -o file.h5
```

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
