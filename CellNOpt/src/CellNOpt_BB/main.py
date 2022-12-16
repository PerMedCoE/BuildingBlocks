import os

from permedcoe import Arguments
from permedcoe import constraint
from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_IN

# Import container definition
from CellNOpt_BB.definitions import CELLNOPT_CONTAINER
from CellNOpt_BB.definitions import COMPUTING_UNITS


@constraint(computing_units=COMPUTING_UNITS)
@container(engine="SINGULARITY", image=CELLNOPT_CONTAINER)
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


def arguments_info():
    """Arguments definition.

    Builds the arguments definition.

    Returns:
        Supported arguments.
    """
    arguments = Arguments()
    arguments.add_input(name="input_file",
                        type=str,
                        description="HDF5 input data required by CellNopt",
                        check="file")
    return arguments
