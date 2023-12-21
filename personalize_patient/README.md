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
This RNAseq dataset can come from the `Single-cell Processing` building block and needs to be normalised as described in [Béal et al. (2019)](https://www.frontiersin.org/articles/10.3389/fphys.2018.01965/full?field=&journalName=Frontiers_in_Physiology&id=369984) and in the [PROFILE GitHub repository](https://github.com/sysbio-curie/PROFILE). The `Single-cell Processing` building block performs this normalisation step.

Another option of this building block is to personalise a given MaBoSS model using cell line information such as mutations, copy number alterations and expression counts.

## User instructions

### Requirements

- Python >= 3.6
- [Singularity](https://singularity.lbl.gov/docs-installation)
- `permedcoe` base package: `python3 -m pip install permedcoe`

In addition to the dependencies, it is necessary to generate the associated
singularity image ([`PhysiCell-COVID19.singularity`](../Resources/images/PhysiCell-COVID19.singularity)),
located in the **Resources** folder of this repository.

They **MUST be available and exported in the following environment variable**
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

The `personalize_patient` package provides a clear interface that allows
it to be used with multiple workflow managers (e.g. PyCOMPSs, NextFlow and
Snakemake).

It can be imported from python and invoked directly from a **PyCOMPSs**
application, or through the command line for other workflow managers
(e.g. Snakemake and NextFlow).

The command line is:

```bash
personalize_patient_BB -d \
    --tmpdir <working_directory> \
    default \
    --norm_data <norm_data> \
    --cells <cells> \
    --model_prefix <model_prefix> \
    --t <t> \
    --ko_file <ko_file> \
    --model_ouput_dir <model_ouput_dir> \
    --personalized_result <personalized_result>
```

Where the parameters are:

|        | Flag                  | Parameter              | File   | Description                                                                      |
|--------|-----------------------|------------------------|--------|----------------------------------------------------------------------------------|
|        | --tmpdir              | \<working_directory>   | Folder | Working directory (temporary files)                                              |
| Input  | --norm_data           | \<norm_data>           | File   | tsv of the normalized RNAseq data                                                |
| Input  | --cells               | \<cells>               | File   | tsv of the different patients to be analyzed with their clinical information     |
| Input  | --model_prefix        | \<model_prefix>        | String | Prefix that describes the model                                                  |
| Input  | --t                   | \<t>                   | String | Specific cell type of interest                                                   |
| Input  | --ko_file             | \<ko_file>             | File   | File result of the "High-throughput mutant analysis" (aka MaBoSS) building block |
| Output | --model_output_dir    | \<model_output_dir>    | Folder | Folder where the results will be located                                         |
| Output | --personalized_result | \<personalized_result> | File   | Personalisation summary file                                                     |

Alternatively, it can be used to perform patient personalize cellline:

The command line is:

```bash
personalize_patient_BB -d \
    --tmpdir <working_directory> \
    uc2 \
    --expression <expression> \
    --cnv <cnv> \
    --mutation <mutation> \
    --cell_type <cell_type> \
    --model_bnd <model_bnd> \
    --model_cfg <model_cfg> \
    --model_output_dir <model_ouput_dir>
```

Where the parameters are:

|        | Flag                | Parameter            | File   | Description                                            |
|--------|---------------------|----------------------|--------|--------------------------------------------------------|
|        | --tmpdir            | \<working_directory> | Folder | Working directory (temporary files)                    |
| Input  | --expression        | \<expression>        | File   | Expression data file                                   |
| Input  | --cnv               | \<cnv>               | File   | Copy number variation file                             |
| Input  | --mutation          | \<mutation>          | File   | Mutation file                                          |
| Input  | --cell_type         | \<cell_type>         | String | Identifier of the cell line to use for personalization |
| Input  | --model_bnd         | \<model_bnd>         | File   | BND file of the MaBoSS model to personalize            |
| Input  | --model_cfg         | \<model_cfg>         | File   | CFG file of the MaBoSS model to personalize            |
| Output | --model_output_dir  | \<model_output_dir>  | Folder | Folder where the results will be located               |


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
