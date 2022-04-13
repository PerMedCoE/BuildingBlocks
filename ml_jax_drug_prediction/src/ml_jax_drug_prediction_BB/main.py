import os

from permedcoe import constraint
from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_IN
from permedcoe import FILE_OUT

# Import container definition
from ml_jax_drug_prediction_BB.definitions import ML_JAX_DRUG_PREDICTION_CONTAINER
from ml_jax_drug_prediction_BB.definitions import COMPUTING_UNITS


@constraint(computing_units=COMPUTING_UNITS)
@container(engine="SINGULARITY", image=ML_JAX_DRUG_PREDICTION_CONTAINER)
@binary(binary="/opt/conda/bin/python /opt/ml.py")
@task(input_file=FILE_IN, output_file=FILE_OUT)
def ml(input_file=None, output_file=None,
       drug_features_flag='--drug_features', drug_features=None,
       cell_features_flag='--cell_features', cell_features=None,
       epochs_flag='--epochs', epochs=None,
       adam_lr_flag='--adam_lr', adam_lr=None,
       reg_flag='--reg', reg=None,
       latent_size_flag='--latent_size', latent_size=None,
       test_drugs_flag='--test_drugs', test_drugs=None,
       test_cells_flag='--test_cells', test_cells=None):
    """
    Runs ML Jax Drug Prediction

    The Definition is equal to:
        /opt/conda/bin/python /opt/ml.py <input_file> <output_file>
                                         <drug_features_flag> <drug_features>
                                         <cell_features_flag> <cell_features>
                                         <epochs_flag> <epochs>
                                         <adam_lr_flag> <adam_lr>
                                         <reg_flag> <reg>
                                         <latent_size_flag> <latent_size>
                                         <test_drugs_flag> <test_drugs>
                                         <test_cells_flag> <test_cells>
    By default:
        /opt/conda/bin/python /opt/ml.py <input_file> <output_file>
                                         --drug_features <drug_features>
                                         --cell_features <cell_features>
                                         --epochs <epochs>
                                         --adam_lr <adam_lr>
                                         --reg <reg>
                                         --latent_size <latent_size>
                                         --test_drugs <test_drugs>
                                         --test_cells <test_cells>
    """
    # Empty function since it represents a binary execution:
    pass


def invoke(input, output, config):
    """ Common interface.

    Process parameters
    Example of training:
        ml -i ic50.csv drug.csv cell.csv 200 0.1 0.001 10 0.1 0.1 -o model.npz
        ml -i .x .x .x 200 0.1 0.001 10 0.1 0.1 -o model.npz

    Args:
        input (list): List containing the model and data folder.
        output (list): list containing the output directory path.
        config (dict): Configuration dictionary (not used).
    Returns:
        None
    """
    # Process parameters
    input_file = input[0]
    drug_features = input[1]
    cell_features = input[2]
    epochs = input[3]
    adam_lr = input[4]
    reg = input[5]
    latent_size = input[6]
    test_drugs = input[7]
    test_cells = input[8]
    output_file = output[0]
    # Building block invocation
    ml(input_file=input_file,
       output_file=output_file,
       drug_features=drug_features,
       cell_features=cell_features,
       epochs=epochs,
       adam_lr=adam_lr,
       reg=reg,
       latent_size=latent_size,
       test_drugs=test_drugs,
       test_cells=test_cells)
