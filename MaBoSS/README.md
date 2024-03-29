# High-throughput Mutant Analysis Building Block

This package provides the High-throughput Mutant Analysis **Building Block (BB)**.

## Table of Contents

- [High-throughput Mutant Analysis Building Block](#high-throughput-mutant-analysis-building-block)
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

This building block uses MaBoSS to screen all the possible knockouts of a given Boolean model. It produces a candidate gene list formatted as a text file (single gene per row). More information on MaBoSS can be found in [Stoll G. et al. (2017)](https://academic.oup.com/bioinformatics/article-lookup/doi/10.1093/bioinformatics/btx123) and in the [MaBoSS GitHub repository](https://github.com/maboss-bkmc/MaBoSS-env-2.0).

## User instructions

### Requirements

- Python >= 3.6
- [Singularity](https://singularity.lbl.gov/docs-installation)
- `permedcoe` base package: `python3 -m pip install permedcoe`

In addition to the dependencies, it is necessary to generate the associated
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
MaBoSS_BB -d \
    --tmpdir <working_directory> \
    default \
    --model <model> \
    --data_folder <data_folder> \
    --parallel <parallel> \
    --ko_file <ko_file>
```

Where the parameters are:

|        | Flag                | Parameter            | Type   | Description                                           |
|--------|---------------------|----------------------|--------|-------------------------------------------------------|
|        | --tmpdir            | \<working_directory> | Folder | Working directory (temporary files)                   |
| Input  | --model             | \<model>             | String | Name of the model                                     |
| Input  | --data_folder       | \<data_folder>       | Folder | Folder where the model files are located              |
| Input  | --parallel          | \<parallel>          | Int    | Internal parallelism                                  |
| Output | --ko_file           | \<ko_file>           | File   | Name of the output file with the knock-out candidates |

Alternatively, it can be used to perform sensitivity analysis:

The command line is:

```bash
MaBoSS_BB -d \
    --tmpdir <working_directory> \
    sensitivity \
    --model_folder <model_folder> \
    --genes_druggable <genes_druggable> \
    --genes_target <genes_target> \
    --result_file <result_file>
```

Where the parameters are:

|        | Flag                | Parameter            | Type   | Description                         |
|--------|---------------------|----------------------|--------|-------------------------------------|
|        | --tmpdir            | \<working_directory> | Folder | Working directory (temporary files) |
| Input  | --model_folder      | \<model_folder>      | Folder | Folder that contains the model      |
| Input  | --genes_druggable   | \<genes_druggable>   | String | Druggable genes                     |
| Input  | --genes_target      | \<genes_target>      | String | Target genes                        |
| Output | --result_file       | \<result_file>       | File   | Result file path                    |

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
