import os

from permedcoe import constraint
from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_OUT

# Import container definition
from omnipath_BB.definitions import OMNIPATH_ASSETS_PATH
from omnipath_BB.definitions import OMNIPATH_CONTAINER
from omnipath_BB.definitions import COMPUTING_UNITS

# Globals
OMNIPATH_BINARY = os.path.join(OMNIPATH_ASSETS_PATH, "omnipath.sh")


@constraint(computing_units=COMPUTING_UNITS)
@container(engine="SINGULARITY", image=OMNIPATH_CONTAINER)
@binary(binary=OMNIPATH_BINARY)
@task(output_file=FILE_OUT)
def omnipath(output_file=None):
    """
    Runs Omnipath

    The Definition is equal to:
        Rscript --vanilla /opt/omnipath.R <output_file>
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
    debug = input[0]
    output_file = output[0]
    # Building block invocation
    omnipath(output_file=output_file)
