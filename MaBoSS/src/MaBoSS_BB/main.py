import os

from permedcoe import constraint
from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import DIRECTORY_IN
from permedcoe import FILE_IN
from permedcoe import FILE_OUT
from permedcoe import TMPDIR

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
    model="epithelial_cell_2", data_folder=None, ko_file=None, parallel=COMPUTING_UNITS, tmpdir=TMPDIR
):
    """
    Performs the MaBoSS analysis.
    Produces the ko file, containing the set of selected gene candidates.

    The Definition is equal to:
        ./MaBoSS_analysis.sh <model> <data_folder> <ko_file> <computing_units> <tmpdir>
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
    tmpdir=TMPDIR, model_folder=None, genes_druggable=None, genes_target=None, result_file=None
):
    """
    Performs the MaBoSS analysis.
    Produces the ko file, containing the set of selected gene candidates.

    The Definition is equal to:
        ./MaBoSS_sensitivity_analysis.sh <tmpdir> <model_folder> <genes_druggable> <genes_target> <result_file>
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
        tmpdir = arguments.tmpdir
        # Building block invocation
        MaBoSS_sensitivity_analysis(
            model_folder=model_folder,
            genes_druggable=genes_druggable,
            genes_target=genes_target,
            result_file=result_file,
            tmpdir=tmpdir
        )
    else:
        # Process parameters
        model = arguments.model
        data_folder = arguments.data_folder
        ko_file = arguments.ko_file
        parallel = arguments.parallel
        tmpdir = arguments.tmpdir
        # Building block invocation
        MaBoSS_analysis(
            model=model,
            data_folder=data_folder,
            ko_file=ko_file,
            parallel=parallel,
            tmpdir=tmpdir
        )
