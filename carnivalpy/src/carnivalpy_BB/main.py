import os

from permedcoe import constraint
from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import DIRECTORY_INOUT

# Import container definition
from carnivalpy_BB.definitions import CARNIVALPY_CONTAINER
from carnivalpy_BB.definitions import COMPUTING_UNITS


@constraint(computing_units=COMPUTING_UNITS)
@container(engine="SINGULARITY", image=CARNIVALPY_CONTAINER)
@binary(binary="/opt/conda/bin/python /opt/carnival/carnivalpy/carnival.py")
@task(path=DIRECTORY_INOUT)
def carnivalpy(path=None,
               penalty_flag='--penalty', penalty=None,
               solver_flag='--solver', solver=None):
    """
    Runs CarnivalPy

    The Definition is equal to:
        /opt/conda/bin/python /opt/carnival/carnivalpy/carnival.py <path>
                                                                   <col_genes_flag> <penalty>
                                                                   <solver_flag> <solver>
    By default:
        /opt/conda/bin/python /opt/carnival/carnivalpy/carnival.py <path>
                                                                   --penalty <penalty>
                                                                   --solver <solver>
    """
    # Empty function since it represents a binary execution:
    pass


def invoke(input, output, config):
    """ Common interface.

    Example of training:

        carnivalpy -i example/ 0.0001 cbc -o .

    Args:
        input (list): List containing the model and data folder.
        output (list): list containing the output directory path.
        config (dict): Configuration dictionary (not used).
    Returns:
        None
    """
    # Process parameters
    path = input[0]
    penalty = input[1]
    solver = input[2]
    # Building block invokation
    carnivalpy(path=path,
               penalty=penalty,
               solver=solver)
