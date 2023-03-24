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
EXPORT_SOLVER_HDF5_ASSETS=$(python3 -c "import export_solver_hdf5_BB; import os; print(os.path.dirname(export_solver_hdf5_BB.__file__))")

export_solver_hdf5_BB -d \
    --mount_point ${EXPORT_SOLVER_HDF5_ASSETS}/assets:${EXPORT_SOLVER_HDF5_ASSETS}/assets,<working_directory>:<working_directory> \
    --sif <sif> \
    --measurements <measurements> \
    --inputs <inputs> \
    --verbose <verbose> \
    --output_file <output_file> \
    --working_directory <working_directory>
```

Where the parameters are:

|        | Flag                | Parameter            | Type   | Description                                       |
|--------|---------------------|----------------------|--------|---------------------------------------------------|
| Input  | --sif               | \<sif>               | File   | The sif csv file containing the signaling network |
| Input  | --measurements      | \<measurements>      | String | The measurements csv with the TFs and weights     |
| Input  | --inputs            | \<inputs>            | File   | The csv file with the input protein targets       |
| Input  | --verbose           | \<verbose>           | String | Verbose output (TRUE/FALSE)                       |
| Output | --output_file       | \<output_file>       | File   | The final HDF5 file.                              |
| Output | --working_directory | \<working_directory> | Folder | Working directory (temporary files)               |


An example with toy data from here https://github.com/saezlab/permedcoe/tree/master/containers/toolset/scripts/examples/export would be:

```bash
export_solver_hdf5_BB \
    --sif sif.csv \
    --measurements measurements.csv \
    --inputs inputs.csv \
    --verbose TRUE \
    --output_file file.h5
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

This software has been developed for the [PerMedCoE project](https://permedcoe.eu/), funded by the European Commission (EU H2020 [951773](https://cordis.europa.eu/project/id/951773)).

![](https://permedcoe.eu/wp-content/uploads/2020/11/logo_1.png "PerMedCoE")
