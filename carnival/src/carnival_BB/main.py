import os

from permedcoe import constraint
from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_IN

# Import container definition
from carnival_BB.definitions import CARNIVAL_CONTAINER
from carnival_BB.definitions import COMPUTING_UNITS


@constraint(computing_units=COMPUTING_UNITS)
@container(engine="SINGULARITY", image=CARNIVAL_CONTAINER)
@binary(binary="/opt/carnival/build/aco")
@task(input_file=FILE_IN)
def carnival(input_file=None):
    """
    Runs Carnival

    The Definition is equal to:
        ./opt/carnival/build/aco <input_file>
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
    input_file = input[0]
    # Building block invokation
    carnival(input_file=input_file)
