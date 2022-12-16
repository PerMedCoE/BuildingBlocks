import os

from permedcoe import Arguments
from permedcoe import constraint
from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_IN
from permedcoe import FILE_OUT

# Import container definition
from ml_jax_drug_prediction_BB.definitions import ML_JAX_DRUG_PREDICTION_ASSETS_PATH
from ml_jax_drug_prediction_BB.definitions import ML_JAX_DRUG_PREDICTION_CONTAINER
from ml_jax_drug_prediction_BB.definitions import COMPUTING_UNITS

# Globals
ML_JAX_DRUG_PREDICTION_BINARY = os.path.join(ML_JAX_DRUG_PREDICTION_ASSETS_PATH,
                                             "ml_jax_drug_prediction.sh")


@constraint(computing_units=COMPUTING_UNITS)
@container(engine="SINGULARITY", image=ML_JAX_DRUG_PREDICTION_CONTAINER)
@binary(binary=ML_JAX_DRUG_PREDICTION_BINARY)
@task(input_file=FILE_IN, output_file=FILE_OUT, cell_features=FILE_IN)
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


def invoke(arguments, config):
    """ Common interface.

    Process parameters
    Example of training:
        ml -i ic50.csv drug.csv cell.csv 200 0.1 0.001 10 0.1 0.1 -o model.npz
        ml -i .x .x .x 200 0.1 0.001 10 0.1 0.1 -o model.npz

    Args:
        arguments (args): Building Block parsed arguments.
        config (dict): Configuration dictionary (not used).
    Returns:
        None
    """
    # Process parameters
    input_file = arguments.input_file
    drug_features = arguments.drug_features
    cell_features = arguments.cell_features
    epochs = arguments.epochs
    adam_lr = arguments.adam_lr
    reg = arguments.reg
    latent_size = arguments.latent_size
    test_drugs = arguments.test_drugs
    test_cells = arguments.test_cells
    output_file = arguments.output_file
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


def arguments_info():
    """Arguments definition.

    Builds the arguments definition.

    Returns:
        Supported arguments.
    """
    arguments = Arguments()
    arguments.add_input(name="input_file",
                        type=str,
                        description="CSV with the matrix to predict (e.g IC50 drug/cell responses) \
                                     for training (see this example). If the file is a .npz file, \
                                     then the model is imported and this is run in inference mode for \
                                     predictions. If .x is provided, the example file is used for \
                                     training a mode",
                        check="file")
    arguments.add_input(name="drug_features",
                        type=str,
                        description="CSV with row features (e.g. drug targets). \
                                     If .x is provided, the example file is used.",
                        check="file")
    arguments.add_input(name="cell_features",
                        type=str,
                        description="CSV with col features (e.g. cell features). \
                                     If .x is provided, the example file is used.",
                        check="file")
    arguments.add_input(name="epochs",
                        type=int,
                        description="Number of epochs for training using the ADAM optimizer (e.g. 200)",
                        check=int)
    arguments.add_input(name="adam_lr",
                        type=float,
                        description="Learning rate for the ADAM solver. E.g. 0.1. Recommended <= 0.1. \
                                     Lower values slow down the convergence.",
                        check=float)
    arguments.add_input(name="reg",
                        type=float,
                        description="L2 regularization weight (e.g. 0.001)",
                        check=float)
    arguments.add_input(name="latent_size",
                        type=int,
                        description="Number of dimensions for the latent matrices to be estimated \
                                     from the data. As a rule of thumb, this should be at most the \
                                     minimum number of features for cells or drugs used. Larger \
                                     values might create overfitted models.",
                        check=int)
    arguments.add_input(name="test_drugs",
                        type=str,
                        description="If row features are provided, this is the proportion of samples \
                                     removed from training for validation (e.g. 0.2)",
                        check=str)
    arguments.add_input(name="test_cells",
                        type=str,
                        description="If col features are provided, this is the proportion of samples \
                                     removed from training for validation (e.g. 0.2)",
                        check=str)
    arguments.add_output(name="output_file",
                         type=str,
                         description="npz file with the trained model if in \
                                      training mode, or csv file with \
                                      prediction results")
    return arguments
