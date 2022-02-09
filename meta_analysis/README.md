# HPC/Exascale Centre of Excellence in Personalised Medicine

## Meta Analysis Building Block

This package provides the meta_analysis **Building Blocks (BB)**.

## Table of Contents

- [HPC/Exascale Centre of Excellence in Personalised Medicine](#hpcexascale-centre-of-excellence-in-personalised-medicine)
  - [Meta Analysis Pilot Building Block](#meta-analysis-building-block)
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

TO BE COMPLETED

## User instructions

### Requirements

- Python >= 3.6
- [Singularity](https://singularity.lbl.gov/docs-installation)

In addtion to the dependencies, it is necessary to download the singularity
image and the building block asset.
They must be available and exported in the following environment variables:

```bash
export PERMEDCOE_IMAGES="/path/to/images/"
export PERMEDCOE_ASSETS="/path/to/assets/"
```

### Installation

There are two ways to install this package (from Pypi and manually):

- From Pypi:

  This package is **NOT YET** publicly available in Pypi:

  ```bash
  pip install meta_analysis_BB
  ```

  or more specifically:

  ```bash
  python3 -m pip install meta_analysis_BB
  ```

- From source code:

  This package provides an automatic installation script:

  ```bash
  ./install.sh
  ```

  This script creates a file `installation_files.txt` to keep track of the
  installed files.
  It is used with the `uninstall.sh` script to clean up the system.

### Usage

The `meta_analysis_BB` package provides a clear interface that allows it to be
used with multiple workflow managers (e.g. PyCOMPSs, NextFlow and Snakemake).

It imported from python and invoked directly from a **PyCOMPSs** application,
or through the binaries from other workflow managers (e.g. Snakemake and
NextFlow).

The binary is:

  ```bash
  meta_analysis -d {TO BE COMPLETED}
  ```

### Uninstall

Uninstall can be done as usual `pip` packages:

```bash
pip uninstall meta_analysis_BB
```

or more specifically:

```bash
./uninstall.sh
./clean.sh
```

## License

[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)

## Contact

<https://permedcoe.eu/contact/>
