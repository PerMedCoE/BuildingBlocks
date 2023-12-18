import os

from permedcoe import constraint
from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_IN
from permedcoe import FILE_OUT
from permedcoe import DIRECTORY_OUT
from permedcoe import TMPDIR

# Import single container and assets definitions"
from cll_network_inference_BB.definitions import ASSETS_PATH
from cll_network_inference_BB.definitions import CLL_NETWORK_INFERENCE_CONTAINER
from cll_network_inference_BB.definitions import COMPUTING_UNITS

# Globals
CLL_NETWORK_INFERENCE_BINARY = os.path.join(ASSETS_PATH, "run.sh")
# Override COMPUTING_UNITS
COMPUTING_UNITS = 48


@constraint(computing_units=COMPUTING_UNITS)
@container(engine="SINGULARITY", image=CLL_NETWORK_INFERENCE_CONTAINER)
@binary(binary=CLL_NETWORK_INFERENCE_BINARY)
@task(activities=FILE_IN, omnipath_database=FILE_IN, outdir=DIRECTORY_OUT, sif=FILE_OUT)
def cll_network_inference(
    tmpdir=TMPDIR,
    cplex_bin_flag="-c",
    cplex_bin=None,
    activities_flag="-a",
    activities=None,
    omnipath_database_flag="-z",
    omnipath_database=None,
    outdir_flag="-o",
    outdir=None,
    sif_flag="-s",
    sif=None,
):
    """
    Inference of contextualize signaling network from TF activities

    The Definition is equal to:
        assets/run.sh
                  tmpdir \
                  -c  cplex_bin \
                  -a  activities \
                  -z  omnipath_database \
                  -o  outdir \
                  -s  sif
    """
    # Empty function since it represents a binary execution:
    pass


def invoke(arguments, config):
    """Common interface.

    Args:
        arguments (args): Building Block parsed arguments.
        config (dict): Configuration dictionary (not used).
    Returns:
        None
    """
    # Building block invocation
    cll_network_inference(
        tmpdir=arguments.tmpdir,
        cplex_bin=arguments.cplex_bin,
        activities=arguments.activities,
        omnipath_database=arguments.omnipath_database,
        outdir=arguments.outdir,
        sif=arguments.sif,
    )
