import os

from permedcoe import constraint
from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_IN
from permedcoe import DIRECTORY_OUT
from permedcoe import TMPDIR

# Import single container and assets definitions"
from cll_run_boolean_model_BB.definitions import ASSETS_PATH
from cll_run_boolean_model_BB.definitions import CLL_RUN_BOOLEAN_MODEL_CONTAINER
from cll_run_boolean_model_BB.definitions import COMPUTING_UNITS


# Globals
CLL_RUN_BOOLEAN_MODEL_BINARY = os.path.join(ASSETS_PATH, "run.sh")
# Override COMPUTING_UNITS
COMPUTING_UNITS = 48


@constraint(computing_units=COMPUTING_UNITS)
@container(engine="SINGULARITY", image=CLL_RUN_BOOLEAN_MODEL_CONTAINER)
@binary(binary=CLL_RUN_BOOLEAN_MODEL_BINARY)
@task(sif=FILE_IN, bnd=FILE_IN, cfg=FILE_IN, outdir=DIRECTORY_OUT)
def cll_run_boolean_model(
    tmpdir=TMPDIR,
    sif_flag="-s",
    sif=None,
    bnd_flag="-b",
    bnd=None,
    cfg_flag="-c",
    cfg=None,
    id_flag="-i",
    id=None,
    outdir_flag="-o",
    outdir=None,
):
    """
    Run personalised boolean models

    The Definition is equal to:
        assets/run.sh
                  tmpdir \
                  -s  sif \
                  -b  bnd \
                  -c  cfg \
                  -i  id \
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
    cll_run_boolean_model(
        tmpdir=arguments.tmpdir,
        sif=arguments.sif,
        bnd=arguments.bnd,
        cfg=arguments.cfg,
        id=arguments.id,
        outdir=arguments.outdir,
    )
