import os

from permedcoe import constraint
from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_IN
from permedcoe import FILE_OUT

# Import container definition
from omnipath_BB.definitions import OMNIPATH_CONTAINER
from omnipath_BB.definitions import COMPUTING_UNITS


@constraint(computing_units=COMPUTING_UNITS)
@container(engine="SINGULARITY", image=OMNIPATH_CONTAINER)
@binary(binary="Rscript --vanilla /opt/omnipath.R")
@task(input_file=FILE_IN, output_file=FILE_OUT)
def omnipath(input_file=None, output_file=None):
    """
    Runs Omnipath

    The Definition is equal to:
        Rscript --vanilla /opt/omnipath.R <input_file> <output_file>
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
    output_file = output[0]
    # Building block invocation
    omnipath(input_file=input_file,
             output_file=output_file)
