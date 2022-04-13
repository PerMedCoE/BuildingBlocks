# ML Jax Drug Prediction Building Block

This package provides the ML Jax Drug Prediction **Building Block (BB)**.

## Table of Contents

- [ML Jax Drug Prediction Building Block](#ml-jax-drug-prediction-building-block)
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

In addition to the dependencies, it is necessary to generate the associated
singularity image ([`tf-jax.singularity`](../Resources/images/tf-jax.singularity)),
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

The `ml_jax_drug_prediction_BB` package provides a clear interface that allows
it to be used with multiple workflow managers (e.g. PyCOMPSs, NextFlow and
Snakemake).

It can be imported from python and invoked directly from a **PyCOMPSs**
application, or through the command line for other workflow managers
(e.g. Snakemake and NextFlow).

The command line is:

```bash
ml_jax_drug_prediction_BB -d \
    -i <input_file> <drug_features> <cell_features> <epochs> <adam_lr> <reg> <latent_size> <test_drugs> <test_cells>
    -o <output_file>
```

Where the parameters are:

|        | Parameter          | Type      | Description                                             |
|--------|--------------------|-----------|---------------------------------------------------------|
| Input  | \<input_file>      | String    | [TO BE COMPLETED]                                       |
| Input  | \<drug_features>   | String    | [TO BE COMPLETED]                                       |
| Input  | \<cell_features>   | String    | [TO BE COMPLETED]                                       |
| Input  | \<epochs>          | String    | [TO BE COMPLETED]                                       |
| Input  | \<adam_lr>         | String    | [TO BE COMPLETED]                                       |
| Input  | \<reg>             | String    | [TO BE COMPLETED]                                       |
| Input  | \<latent_size>     | String    | [TO BE COMPLETED]                                       |
| Input  | \<test_drugs>      | String    | [TO BE COMPLETED]                                       |
| Input  | \<test_cells>      | String    | [TO BE COMPLETED]                                       |
| Output | \<output_file>     | String    | [TO BE COMPLETED]                                       |

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
