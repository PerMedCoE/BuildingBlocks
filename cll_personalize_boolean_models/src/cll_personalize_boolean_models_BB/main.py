import os

from permedcoe import constraint
from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_IN
from permedcoe import DIRECTORY_OUT
from permedcoe import TMPDIR

# Import single container and assets definitions"
from cll_personalize_boolean_models_BB.definitions import ASSETS_PATH
from cll_personalize_boolean_models_BB.definitions import (
    CLL_PERSONALIZE_BOOLEAN_MODELS_CONTAINER,
)
from cll_personalize_boolean_models_BB.definitions import COMPUTING_UNITS

# Globals
CLL_PERSONALIZE_BOOLEAN_MODELS_BINARY = os.path.join(ASSETS_PATH, "run.sh")
# Override COMPUTING_UNITS
COMPUTING_UNITS = 48


@constraint(computing_units=COMPUTING_UNITS)
@container(engine="SINGULARITY", image=CLL_PERSONALIZE_BOOLEAN_MODELS_CONTAINER)
@binary(binary=CLL_PERSONALIZE_BOOLEAN_MODELS_BINARY)
@task(sif=FILE_IN, norm_exp=FILE_IN, metadata=FILE_IN, outdir=DIRECTORY_OUT)
def cll_personalize_boolean_models(
    tmpdir=TMPDIR,
    sif_flag="-s",
    sif=None,
    norm_exp_flag="-n",
    norm_exp=None,
    metadata_flag="-m",
    metadata=None,
    group_flag="-g",
    group=None,
    outdir_flag="-o",
    outdir=None,
):
    """
    Personalize boolean models

    The Definition is equal to:
        assets/run.sh
                  tmpdir \
                  -s  sif \
                  -n  norm_exp \
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
    cll_personalize_boolean_models(
        tmpdir=arguments.tmpdir,
        sif=arguments.sif,
        norm_exp=arguments.norm_exp,
        metadata=arguments.metadata,
        group=arguments.group,
        outdir=arguments.outdir,
    )
