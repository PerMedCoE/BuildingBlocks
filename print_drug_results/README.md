# Print Drug Results analysis Building Block

This package provides the print_drug_results **Building Block (BB)**.

## Table of Contents

- [Print Drug Results analysis Building Block](#print-drug-results-analysis-building-block)
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

[TO BE COMPLETED]

## User instructions

### Requirements

- Python >= 3.6
- [Singularity](https://singularity.lbl.gov/docs-installation)
- `permedcoe` base package: `python3 -m pip install permedcoe`

In addtion to the dependencies, it is necessary to generate the associated
singularity images ([`print_drug_results.singularity`](../Resources/images/print_drug_results.singularity),
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

The `print_drug_results` package provides a clear interface that allows
it to be used with multiple workflow managers (e.g. PyCOMPSs, NextFlow and
Snakemake).

It can be imported from python and invoked directly from a **PyCOMPSs**
application, or through the command line for other workflow managers
(e.g. Snakemake and NextFlow).

The command line is:

```bash
PRINT_DRUG_RESULTS_ASSETS=$(python3 -c "import print_drug_results_BB; import os; print(os.path.dirname(print_drug_results_BB.__file__))")

print_drug_results_BB -d \
    --mount_point ${PRINT_DRUG_RESULTS_ASSETS}/assets:${PRINT_DRUG_RESULTS_ASSETS}/assets \
    --results_folder <results_folder> \
    --reports_folder <reports_folder>
```

Where the parameters are:

|        | Flag             | Parameter         | Type | Description    |
|--------|------------------|-------------------|------|----------------|
| Input  | --results_folder | \<input_file>     | File | Results folder |
| Output | --reports_folder | \<reports_folder> | File | Reports folder |

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
