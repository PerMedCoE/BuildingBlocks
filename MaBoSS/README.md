# High-throughput mutant analysis Building Block

This package provides the MaBoSS **Building Block (BB)**.

## Table of Contents

- [High-throughput mutant analysis Building Block](#high-throughput-mutant-analysis-building-block)
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

This building block uses MaBoSS to screen all the possible knock outs of a given Boolean model.
More information in MaBoSS can be found in the work [Stoll, G. et al. (2017) MaBoSS 2.0: an environment for stochastic Boolean modeling. Bioinformatics, 33, 2226–2228.](https://academic.oup.com/bioinformatics/article-lookup/doi/10.1093/bioinformatics/btx123) and in the dedicated [GitHub repository](https://github.com/maboss-bkmc/MaBoSS-env-2.0).

## User instructions

### Requirements

- Python >= 3.6
- [Singularity](https://singularity.lbl.gov/docs-installation)
- `permedcoe` base package: `python3 -m pip install permedcoe`

In addtion to the dependencies, it is necessary to generate the associated
singularity images ([`MaBoSS.singularity`](../Resources/images/MaBoSS.singularity) and
[MaBoSS_sensitivity.singularity](../Resources/images/MaBoSS_sensitivity.singularity)),
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

The `MaBoSS` package provides a clear interface that allows
it to be used with multiple workflow managers (e.g. PyCOMPSs, NextFlow and
Snakemake).

It can be imported from python and invoked directly from a **PyCOMPSs**
application, or through the command line for other workflow managers
(e.g. Snakemake and NextFlow).

The command line is:

```bash
MABOSS_ASSETS=$(python3 -c "import MaBoSS_BB; import os; print(os.path.dirname(MaBoSS_BB.__file__))")

MaBoSS_BB -d \
    -i <prefix> <data_folder> <parallel> \
    -o <ko_file> \
    --mount_point ${MABOSS_ASSETS}/assets:${MABOSS_ASSETS}/assets
```

Where the parameters are:

|        | Parameter          | Type      | Description                                             |
|--------|--------------------|-----------|---------------------------------------------------------|
| Input  | \<prefix>          | String    | Name of the model                                       |
| Input  | \<data_folder>     | Directory | Folder where the model files are located                |
| Input  | \<parallel>        | Int       | Internal parallelism                                    |
| Output | \<ko_file>         | File      | Name of the output file with the knock-out candidates   |

Alternatively, it can be used to perform sensitivity analysis:

The command line is:

```bash
MABOSS_ASSETS=$(python3 -c "import MaBoSS_BB; import os; print(os.path.dirname(MaBoSS_BB.__file__))")

MaBoSS_BB -d \
    -i <model_folder> <genes_druggable> <genes_target> \
    -o <result_file> \
    -c <config_file> \
    --mount_point ${MABOSS_ASSETS}/assets:${MABOSS_ASSETS}/assets
```

Where the parameters are:

|        | Parameter          | Type      | Description                                             |
|--------|--------------------|-----------|---------------------------------------------------------|
| Input  | \<model_folder>    | Directory | Folder that contains the model                          |
| Input  | \<genes_druggable> | String    | Druggable genes                                         |
| Input  | \<genes_target>    | String    | Target genes                                            |
| Output | \<result_file>     | File      | Result file path                                        |
| Config | \<config_file>     | File      | Config file (yaml format containing "uc2" key)          |

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
