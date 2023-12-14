import os

from permedcoe import constraint
from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_IN
from permedcoe import DIRECTORY_IN
from permedcoe import DIRECTORY_OUT
from permedcoe import TMPDIR

# Import single container and assets definitions
from cll_combine_models_BB.definitions import ASSETS_PATH
from cll_combine_models_BB.definitions import CLL_COMBINE_MODELS_CONTAINER
from cll_combine_models_BB.definitions import COMPUTING_UNITS

# Globals
CLL_COMBINE_MODELS_BINARY = os.path.join(ASSETS_PATH, "run.sh")
# Override COMPUTING_UNITS
COMPUTING_UNITS = 48


@constraint(computing_units=COMPUTING_UNITS)
@container(engine="SINGULARITY", image=CLL_COMBINE_MODELS_CONTAINER)
@binary(binary=CLL_COMBINE_MODELS_BINARY)
@task(runs=DIRECTORY_IN, metadata=FILE_IN, outdir=DIRECTORY_OUT)
def cll_combine_models(
    tmpdir=TMPDIR,
    runs_flag="-r",
    runs=None,
    metadata_flag="-m",
    metadata=None,
    group_flag="-g",
    group=None,
    outdir_flag="-o",
    outdir=None,
):
    """
    Combine boolean models analysis from different patients

    The Definition is equal to:
        assets/run.sh
                  tmpdir \
                  -r  runs \
                  -m  metadata \
                  -g  group \
                  -o  outdir
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
    cll_combine_models(
        tmpdir=arguments.tmpdir,
        runs=arguments.runs,
        metadata=arguments.metadata,
        group=arguments.group,
        outdir=arguments.outdir,
    )
