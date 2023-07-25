import os

from permedcoe import constraint
from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import DIRECTORY_IN
from permedcoe import FILE_IN
from permedcoe import FILE_OUT
from permedcoe import TMPDIR
from permedcoe.base import set_debug

# Import single container and assets definitions
from MaBoSSG_BB.definitions import MABOSSG_CONTAINER
from MaBoSSG_BB.definitions import ASSETS_PATH
from MaBoSSG_BB.definitions import COMPUTING_UNITS

set_debug(True)
# Globals
MABOSSG_SENSITIVIY_ANALYSIS_BINARY = os.path.join(ASSETS_PATH, "MaBoSSG_sensitivity_analysis.sh")


@constraint(computing_units=COMPUTING_UNITS)
@container(engine="SINGULARITY", image=MABOSSG_CONTAINER)
@binary(binary=MABOSSG_SENSITIVIY_ANALYSIS_BINARY)
@task(
    model_folder=DIRECTORY_IN,
    genes_druggable=FILE_IN,
    genes_target=FILE_IN,
    result_file=FILE_OUT,
)
def MaBoSSG_sensitivity_analysis(
    tmpdir=TMPDIR, model_folder=None, genes_druggable=None, genes_target=None, result_file=None
):
    """
    Performs the MaBoSSG analysis.
    Produces the ko file, containing the set of selected gene candidates.

    The Definition is equal to:
        ./MaBoSSG_sensitivity_analysis.sh <tmpdir> <model_folder> <genes_druggable> <genes_target> <result_file>
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
    # Process parameters
    model_folder = arguments.model_folder
    genes_druggable = arguments.genes_druggable
    genes_target = arguments.genes_target
    result_file = arguments.result_file
    tmpdir = arguments.tmpdir
    # Building block invocation
    MaBoSSG_sensitivity_analysis(
        model_folder=model_folder,
        genes_druggable=genes_druggable,
        genes_target=genes_target,
        result_file=result_file,
        tmpdir=tmpdir
    )
