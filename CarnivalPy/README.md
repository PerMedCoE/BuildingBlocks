# CarnivalPy Building Block

This package provides the CARNIVALPy **Building Block (BB)**.

## Table of Contents

- [CarnivalPy Building Block](#carnivalpy-building-block)
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

The `CARNIVALPy` building block is a refactored vanilla CARNIVAL R version for Python with support for many commercial and non-commercial open source MILP solvers. This extends the capabilities of the old CARNIVAL software to support also open-source solvers such as GLPK or CBC, and better integration with the building block ecosystem.

## User instructions

### Requirements

- Python >= 3.6
- [Singularity](https://singularity.lbl.gov/docs-installation)
- `permedcoe` base package: `python3 -m pip install permedcoe`

In addition to the dependencies, it is necessary to generate the associated
singularity image ([`carnivalpy.singularity`](../Resources/images/carnivalpy.singularity)),
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

The `CarnivalPy_BB` package provides a clear interface that allows
it to be used with multiple workflow managers (e.g. PyCOMPSs, NextFlow and
Snakemake).

It can be imported from python and invoked directly from a **PyCOMPSs**
application, or through the command line for other workflow managers
(e.g. Snakemake and NextFlow).

The command line is:

```bash
CarnivalPy_BB -d \
    -i <path> <penalty> <solver> <tol> <maxtime> \
    -o <export>
```

Where the parameters are:

|        | Parameter   | Type      | Description                                                                                   |
|--------|-------------|-----------|-----------------------------------------------------------------------------------------------|
| Input  | \<path>     | String    | Path containing a `sif.csv` file, a `measurements.csv` file, and `perturbations.csv` file.    |
| Input  | \<penalty>  | Float     | Penalty value for sparsity (penalty for the number of nodes in the final result). E.g 0.0001. |
| Input  | \<solver>   | String    | Name of the solver to be used: gurobi, cplex, cbc, gurobi_mip, glpk. Any solver supported by Python-MIP and [PICOS](https://picos-api.gitlab.io/picos/introduction.html) can be passed. |
| Input  | \<tol>      | Float     | MIP Gap tolerance.                                                                            |
| Input  | \<maxtime>  | Int       | Max time in seconds.                                                                          |
| Output | \<export>   | String    | Path to the file to be exported with the solution                                             |

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
