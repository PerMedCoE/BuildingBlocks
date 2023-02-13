import os

from permedcoe import constraint
from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_IN
from permedcoe import FILE_OUT
from permedcoe import DIRECTORY_IN
from permedcoe import DIRECTORY_OUT

# Import single container and assets definitions
from PhysiBoSS_BB.definitions import PHYSIBOSS_ASSETS_PATH
from PhysiBoSS_BB.definitions import PHYSIBOSS_CONTAINER
from PhysiBoSS_BB.definitions import COMPUTING_UNITS

# Globals# Globals
PHYSIBOSS_BINARY = os.path.join(PHYSIBOSS_ASSETS_PATH, "PhysiBoSS.sh")
PHYSIBOSS_MODEL_BINARY = os.path.join(PHYSIBOSS_ASSETS_PATH, "PhysiBoSS_model.sh")


@constraint(computing_units=COMPUTING_UNITS)
@container(engine="SINGULARITY", image=PHYSIBOSS_CONTAINER)
@binary(binary=PHYSIBOSS_MODEL_BINARY)
@task(
    model_dir=DIRECTORY_IN,
    out_file=FILE_OUT,
    err_file=FILE_OUT,
    results_dir=DIRECTORY_OUT,
)
def physiboss_model(
    sample="C141",
    repetition=1,
    prefix="epithelial_cell_2_personalized",
    model_dir=None,
    out_file=None,
    err_file=None,
    results_dir=None,
    parallel=COMPUTING_UNITS,
    max_time=8640,
    working_directory="None"
):
    """
    Performs the PhysiCell + MaBoSS analysis.

    The Definition is equal to:
        ./physiboss_model.sh <sample> <repetition> <prefix> <model_dir> \
                             <file_name> <out_file> <err_file> <results_dir> \
                             <computing_units> <max_time> <working_directory>
    """
    # Empty function since it represents a binary execution:
    pass


@constraint(computing_units=COMPUTING_UNITS)
@container(engine="SINGULARITY", image=PHYSIBOSS_CONTAINER)
@binary(binary=PHYSIBOSS_BINARY)
@task(
    bnd_file=FILE_IN,
    cfg_file=FILE_IN,
    out_file=FILE_OUT,
    err_file=FILE_OUT,
    results_dir=DIRECTORY_OUT,
)
def physiboss(
    sample="C141",
    repetition=1,
    prefix="epithelial_cell_2_personalized",
    bnd_file=None,
    cfg_file=None,
    out_file=None,
    err_file=None,
    results_dir=None,
    parallel=COMPUTING_UNITS,
    max_time=8640,
    working_directory="None"
):
    """
    Performs the PhysiCell + MaBoSS analysis.

    The Definition is equal to:
        ./physiboss.sh <sample> <repetition> <prefix> <bnd_file> \
                       <cfg_file> <out_file> <err_file> <results_dir> \
                       <computing_units> <max_time> <working_directory>
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
    # Process parameters
    sample = arguments.sample
    repetition = arguments.repetition
    prefix = arguments.prefix
    bnd_file = arguments.bnd_file
    cfg_file = arguments.cfg_file
    parallel = arguments.parallel
    max_time = arguments.max_time
    out_file = arguments.out_file
    err_file = arguments.err_file
    results_dir = arguments.results_dir
    working_directory = arguments.working_directory
    # Building block invocation
    physiboss(
        sample=sample,
        repetition=repetition,
        prefix=prefix,
        bnd_file=bnd_file,
        cfg_file=cfg_file,
        out_file=out_file,
        err_file=err_file,
        results_dir=results_dir,
        parallel=parallel,
        max_time=max_time,
        working_directory=working_directory
    )
