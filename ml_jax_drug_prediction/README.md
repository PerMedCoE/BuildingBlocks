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

The `ML JAX Drug Prediction` building block implements a matrix factorisation approach to predict IC50 response values of cells with different drugs, with or without side features using JAX. This is a wrapper for [a script hosted on the Saez Lab GitHub repository](https://github.com/saezlab/permedcoe/blob/master/containers/ml-jax/ml.py). This can be used to predict e.g drug responses on cell lines from partial observations of drug/cell responses.

There are two ways of using the building block: for training and for inference (prediction).

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

|        | Parameter          | Type      | Description                                                                                                   |
|--------|--------------------|-----------|---------------------------------------------------------------------------------------------------------------|
| Input  | \<input_file>      | String    | CSV with the matrix to predict (e.g IC50 drug/cell responses) for training (see [this example](https://raw.githubusercontent.com/saezlab/Macau_project_1/master/DATA/IC50)). If the file is a .npz file, then the model is imported and this is run in inference mode for predictions. If `.x` is provided, the example file is used for training a model. |
| Input  | \<drug_features>   | String    | CSV with row features (e.g drug targets). See [this example](https://raw.githubusercontent.com/saezlab/Macau_project_1/master/DATA/target). If `.x` is provided, the example file is used. |
| Input  | \<cell_features>   | String    | CSV with col features (e.g cell features). See [this example](https://raw.githubusercontent.com/saezlab/Macau_project_1/master/DATA/progeny11). If `.x` is provided, the example file is used. |
| Input  | \<epochs>          | Integer    | Number of epochs for training using the ADAM optimizer. E.g 200                                               |
| Input  | \<adam_lr>         | Float    | Learning rate for the ADAM solver. E.g 0.1. Recommended <= 0.1. Lower values slow down the convergence.         |
| Input  | \<reg>             | Float    |  L2 regularization weight. E.g 0.001. |
| Input  | \<latent_size>     | Integer    | Number of dimensions for the latent matrices to be estimated from the data. As a rule of thumb, this should be at most the minimum number of features for cells or drugs used. Larger values might create overfitted models. |
| Input  | \<test_drugs>      | Float    | If row features are provided, this is the proportion of samples removed from training for validation. E.g 0.2.  |
| Input  | \<test_cells>      | String    | If col features are provided, this is the proportion of samples removed from training for validation. E.g 0.2. |
| Output | \<output_file>     | String    | npz file with the trained model if in training mode, or csv file with prediction results.                      |


Training example (using example data files) that builds a trained `model.npz`:

```bash
ml_jax_drug_prediction_BB -i .x .x .x 200 0.1 0.001 10 0.1 0.1 -o model.npz
```

Example of prediction using a trained `model.npz` file (drug_features.csv and cell_features.csv contains new data in the same format as the files used for training, but from new drugs/cells to make predictions):

```bash
ml_jax_drug_prediction_BB -i .x drug_features.csv cell_features.csv 0 0 0 0 0 0 -o predictions.csv
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
