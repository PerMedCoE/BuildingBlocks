import os

from permedcoe import constraint
from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_IN

# Import container definition
from CellNOpt_BB.definitions import CONTAINER
from CellNOpt_BB.definitions import COMPUTING_UNITS


@constraint(computing_units=COMPUTING_UNITS)
@container(engine="SINGULARITY", image=CONTAINER)
@binary(binary="/opt/cellnopt/build/example1")
@task(input_file=FILE_IN)
def cellnopt(input_file=None):
    """
    Runs CellNOpt

    The Definition is equal to:
        /opt/cellnopt/build/example1 <input_file>
    """
    # Empty function since it represents a binary execution:
    pass


def invoke(arguments, config):
    """ Common interface.

    # TODO: add options to export in a given folder

    Args:
        arguments (args): Building Block parsed arguments.
        config (dict): Configuration dictionary (not used).
    Returns:
        None
    """
    # Process parameters
    input_file = arguments.input_file
    # Generate config file
    cellnopt(input_file=input_file)
