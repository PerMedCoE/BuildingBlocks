# Carnival Feature Merger Building Block

This package provides the Carnival Feature Merger **Building Block (BB)**.

## Table of Contents

- [Carnival Feature Merger Building Block](#carnival-feature-merger-building-block)
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

This building block is used in Use Case 2 (`Drug Synergies Screening`) to merge the features extracted by CARNIVAL for each cell line with the original cell line features, in order to produce a final csv file that can be used for prediction with the `ML Jax Drug Prediction` building block. 

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

The `Carnival_feature_merger_BB` package provides a clear interface that allows
it to be used with multiple workflow managers (e.g. PyCOMPSs, NextFlow and
Snakemake).

It can be imported from python and invoked directly from a **PyCOMPSs**
application, or through the command line for other workflow managers
(e.g. Snakemake and NextFlow).

The command line is:

```bash
Carnival_feature_merger_BB -d \
    -i <input_dir> <feature_file> <merge_csv_file> <merge_csv_index> <merge_csv_prefix> \
    -o <output_file>
```

Where the parameters are:

|        | Parameter           | Type      | Description                                                                                             |
|--------|---------------------|-----------|---------------------------------------------------------------------------------------------------------|
| Input  | \<input_dir>        | String    | Path containing the folders with the samples. Name of the folders are used for the name of the samples  |
| Input  | \<feature_file>     | String    | File containing a list of features. If provided, only those features are retrieved from solutions.      |
| Input  | \<merge_csv_file>   | String    | If provided, join the merged features into the given file.                                              |
| Input  | \<merge_csv_index>  | String    | Column ID used as the index for the data (default: `sample`)                                            |
| Input  | \<merge_csv_prefix> | String    | Prefix for the merged features                                                                          |
| Output | \<output_file>      | String    | Output file with the features, where rows are samples and columns features                              |

An example of how to use this connected with the rest of the building blocks is available at https://github.com/saezlab/permedcoe/blob/master/containers/workflow_bb.sh

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
