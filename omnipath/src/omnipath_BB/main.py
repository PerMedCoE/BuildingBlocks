import os

from permedcoe import Arguments
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


def invoke(arguments, config):
    """ Common interface.

    Args:
        arguments (args): Building Block parsed arguments.
        config (dict): Configuration dictionary (not used).
    Returns:
        None
    """
    # Process parameters
    verbose = arguments.verbose
    output_file = arguments.output_file
    # Building block invocation
    omnipath(output_file=output_file)


def arguments_info():
    """Arguments definition.

    Builds the arguments definition.

    Returns:
        Supported arguments.
    """
    arguments = Arguments()
    arguments.add_input(name="verbose",
                        type=bool,
                        description="If verbose or not (True | False)",
                        check=bool)
    arguments.add_output(name="output_file",
                         type=str,
                         description="File with the exported PKN data")
    return arguments
