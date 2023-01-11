from permedcoe import constraint
from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_IN

# Import container definition
from Carnival_BB.definitions import CARNIVAL_CONTAINER
from Carnival_BB.definitions import COMPUTING_UNITS


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
    # Building block invocation
    carnival(input_file=input_file)
