# Personalize Patient Building Block

This package provides the Personalize Patient **Building Block (BB)**.

## Table of Contents

- [Personalize Patient Building Block](#personalize-patient-building-block)
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

This building block tailors a given MaBoSS Boolean model to a given RNAseq dataset of interest.
This RNAseq dataset can come from the "Single cell processing" buildig block  needs to be normalised as described in ["Béal, J. et al. (2019) Personalization of logical models with multi-omics data allows clinical stratification of patients. Front. Physiol., 9, 1965."](https://www.frontiersin.org/articles/10.3389/fphys.2018.01965/full?field=&journalName=Frontiers_in_Physiology&id=369984) and in the [PROFILE's GitHub repository](https://github.com/sysbio-curie/PROFILE).

Future uses of this building block may include other data sources such as mutations, Copy Number Alterations and proteomics counts.

## User instructions

### Requirements

- Python >= 3.6
- [Singularity](https://singularity.lbl.gov/docs-installation)
- `permedcoe` base package: `python3 -m pip install permedcoe`

In addtion to the dependencies, it is necessary to generate the associated
singularity image ([`PhysiCell-COVID19.singularity`](../Resources/images/PhysiCell-COVID19.singularity))
and the building block asset folder ([`personalize_patient`](../Resources/assets/personalize_patient)),
located in the **Resources** folder of this repository.

They **MUST be available and exported in the following environment variables**
before its usage:

```bash
export PERMEDCOE_IMAGES="/path/to/images/"
export PERMEDCOE_ASSETS="/path/to/assets/"
```

### Installation

This package provides an automatic installation script:

```bash
./install.sh
```

This script creates a file `installation_files.txt` to keep track of the
installed files.
It is used with the `uninstall.sh` script to uninstall the Building Block
from the system.

### Usage

The `personalize_patient` package provides a clear interface that allows
it to be used with multiple workflow managers (e.g. PyCOMPSs, NextFlow and
Snakemake).

It can be imported from python and invoked directly from a **PyCOMPSs**
application, or through the command line for other workflow managers
(e.g. Snakemake and NextFlow).

The command line is:

```bash
personalize_patient_BB -d \
      -i <normalized_data_file> <cells_metadata> <data_folder> <model_prefix> <prefix> <ko_file> \
      -o <result_folder> \
      --mount_points ${COVID19_BB_ASSETS}/personalize_patient/:${COVID19_BB_ASSETS}/personalize_patient/,<data_folder>:<data_folder>
```

Where the parameters are:

|        | Parameter               | File      | Description                                             |
|--------|-------------------------|-----------|---------------------------------------------------------|
| Input  | \<normalized_data_file> | File      | tsv of the normalized RNAseq data |
| Input  | \<cells_metadata>       | File      | tsv of the different patients to be analysed with their clinical information|
| Input  | \<data_folder>          | Directory | folder where the source data is located |
| Input  | \<model_prefix>         | String    | prefix that describes the model |
| Input  | \<prefix>               | String    | prefix that describe the patient |
| Input  | \<ko_file>              | File      | file result of the "High-throughput mutant analysis" (aka MaBoSS) building block |
| Output | \<result_folder>        | Directory | folder where the results will be located |

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
