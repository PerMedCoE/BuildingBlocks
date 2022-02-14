import os

from permedcoe import constraint
from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import DIRECTORY_IN
from permedcoe import FILE_OUT

# Import single container and assets definitions
from maboss_BB.definitions import MABOSS_CONTAINER
from maboss_BB.definitions import MABOSS_ASSETS
from maboss_BB.definitions import COMPUTING_UNITS

# Globals
MABOSS_BINARY = os.path.join(MABOSS_ASSETS, "MaBoSS_analysis.sh")


@constraint(computing_units=COMPUTING_UNITS)
@container(engine="SINGULARITY", image=MABOSS_CONTAINER)
@binary(binary=MABOSS_BINARY)
@task(data_folder=DIRECTORY_IN, ko_file=FILE_OUT)
def MaBoSS_analysis(model="epithelial_cell_2",
                    data_folder=None,
                    ko_file=None,
                    parallel=COMPUTING_UNITS):
    """
    Performs the MaBoSS analysis.
    Produces the ko file, containing the set of selected gene candidates.

    The Definition is equal to:
        ./MaBoSS_analysis.sh <model> <data_folder> <ko_file> <computing_units>
    """
    # Empty function since it represents a binary execution:
    pass


def invoke(input, output, config):
    """ Common interface.

    Args:
        input (list): List containing the model and data folder.
        output (list): list containing the output directory path.
        config (dict): Configuration dictionary (not used).
    Returns:
        None
    """
    # Process parameters
    model = input[0]
    data_folder = input[1]
    parallel = input[2]
    ko_file = output[0]
    # Building block invokation
    MaBoSS_analysis(model=model,
                    data_folder=data_folder,
                    ko_file=ko_file,
                    parallel=parallel)
