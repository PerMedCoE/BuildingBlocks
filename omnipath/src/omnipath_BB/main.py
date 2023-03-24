import os

from permedcoe import constraint
from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_OUT
from permedcoe import TMPDIR

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
def omnipath(tmpdir=TMPDIR,
             output_file=None):
    """
    Runs Omnipath

    The Definition is equal to:
        <tmpdir>
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
    tmpdir = arguments.tmpdir
    # Building block invocation
    omnipath(tmpdir=tmpdir,
             output_file=output_file)
