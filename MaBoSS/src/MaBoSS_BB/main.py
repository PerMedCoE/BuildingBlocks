import os

from permedcoe import Arguments
from permedcoe import constraint
from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import DIRECTORY_IN
from permedcoe import FILE_IN
from permedcoe import FILE_OUT

# Import single container and assets definitions
from MaBoSS_BB.definitions import MABOSS_ASSETS_PATH
from MaBoSS_BB.definitions import MABOSS_CONTAINER
from MaBoSS_BB.definitions import MABOSS_SENSITIVITY_CONTAINER
from MaBoSS_BB.definitions import COMPUTING_UNITS

# Globals
MABOSS_BINARY = os.path.join(MABOSS_ASSETS_PATH, "MaBoSS_analysis.sh")
MABOSS_SENSITIVIY_ANALYSIS_BINARY = os.path.join(
    MABOSS_ASSETS_PATH, "MaBoSS_sensitivity_analysis.sh"
)


@constraint(computing_units=COMPUTING_UNITS)
@container(engine="SINGULARITY", image=MABOSS_CONTAINER)
@binary(binary=MABOSS_BINARY)
@task(data_folder=DIRECTORY_IN, ko_file=FILE_OUT)
def MaBoSS_analysis(
    model="epithelial_cell_2", data_folder=None, ko_file=None, parallel=COMPUTING_UNITS
):
    """
    Performs the MaBoSS analysis.
    Produces the ko file, containing the set of selected gene candidates.

    The Definition is equal to:
        ./MaBoSS_analysis.sh <model> <data_folder> <ko_file> <computing_units>
    """
    # Empty function since it represents a binary execution:
    pass


@constraint(computing_units=COMPUTING_UNITS)
@container(engine="SINGULARITY", image=MABOSS_SENSITIVITY_CONTAINER)
@binary(binary=MABOSS_SENSITIVIY_ANALYSIS_BINARY)
@task(
    model_folder=DIRECTORY_IN,
    genes_druggable=FILE_IN,
    genes_target=FILE_IN,
    result_file=FILE_OUT,
)
def MaBoSS_sensitivity_analysis(
    model_folder=None, genes_druggable=None, genes_target=None, result_file=None
):
    """
    Performs the MaBoSS analysis.
    Produces the ko file, containing the set of selected gene candidates.

    The Definition is equal to:
        ./MaBoSS_sensitivity_analysis.sh <model_folder> <genes_druggable> <genes_target> <result_file>
    """
    # Empty function since it represents a binary execution:
    pass


def invoke(arguments, config):
    """Common interface.

    Args:
        arguments (args): Building Block parsed arguments.
        config (dict): Configuration dictionary (not used).
    Returns:
        None
    """
    if arguments.mode == "sensitivity":
        # Process parameters
        model_folder = arguments.model_folder
        genes_druggable = arguments.genes_druggable
        genes_target = arguments.genes_target
        result_file = arguments.result_file
        # Building block invocation
        MaBoSS_sensitivity_analysis(
            model_folder=model_folder,
            genes_druggable=genes_druggable,
            genes_target=genes_target,
            result_file=result_file,
        )
    else:
        # Process parameters
        model = arguments.model
        data_folder = arguments.data_folder
        parallel = arguments.parallel
        ko_file = arguments.ko_file
        # Building block invocation
        MaBoSS_analysis(
            model=model,
            data_folder=data_folder,
            ko_file=ko_file,
            parallel=parallel
        )


def arguments_info():
    """Arguments definition.

    Builds the arguments definition.

    Returns:
        Supported arguments.
    """
    arguments = Arguments()
    arguments.add_input(name="model",
                        type=str,
                        description="Model",
                        check=str)
    arguments.add_input(name="data_folder",
                        type=str,
                        description="Data folder",
                        check="folder")
    arguments.add_input(name="parallel",
                        type=int,
                        description="Internal parallelism",
                        check=None)
    arguments.add_output(name="ko_file",
                         type=str,
                         description="KO file")
    sensitivity = "sensitivity"
    arguments.add_input(name="model_folder",
                        type=str,
                        description="Model folder",
                        check="folder",
                        mode=sensitivity)
    arguments.add_input(name="genes_druggable",
                        type=str,
                        description="Genes druggable (csv)",
                        check="file",
                        mode=sensitivity)
    arguments.add_input(name="genes_target",
                        type=str,
                        description="Genes target (csv)",
                        check="file",
                        mode=sensitivity)
    arguments.add_output(name="result_file",
                         type=str,
                         description="Sensitivity result file (json)",
                         mode=sensitivity)
    return arguments
