import os

from permedcoe import constraint
from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_IN
from permedcoe import FILE_OUT
from permedcoe import DIRECTORY_IN
from permedcoe import DIRECTORY_OUT
from permedcoe import TMPDIR

# Import single container and assets definitions
from PhysiBoSS_BB.definitions import ASSETS_PATH
from PhysiBoSS_BB.definitions import CONTAINER_ENGINE
from PhysiBoSS_BB.definitions import CONTAINER
from PhysiBoSS_BB.definitions import CONTAINER_OPTIONS
from PhysiBoSS_BB.definitions import COMPUTING_UNITS

# Globals# Globals
PHYSIBOSS_BINARY = os.path.join(ASSETS_PATH, "PhysiBoSS.sh")
PHYSIBOSS_MODEL_BINARY = os.path.join(ASSETS_PATH, "PhysiBoSS_model.sh")
PHYSIBOSS_ANALYSE_REPLICATES_BINARY = os.path.join(ASSETS_PATH, "PhysiBoSS_analyse_replicates.sh")

@constraint(computing_units=COMPUTING_UNITS)
@container(engine=CONTAINER_ENGINE, image=CONTAINER, options=CONTAINER_OPTIONS)
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
    parallel=8,
    max_time=8640,
    tmpdir=TMPDIR
):
    """
    Performs the PhysiCell + MaBoSS analysis.

    The Definition is equal to:
        ./physiboss_model.sh <sample> <repetition> <prefix> <model_dir> \
                             <file_name> <out_file> <err_file> <results_dir> \
                             <computing_units> <max_time> <tmpdir>
    """
    # Empty function since it represents a binary execution:
    pass



@constraint(computing_units=COMPUTING_UNITS)
@container(engine="SINGULARITY", image=CONTAINER)
@binary(binary=PHYSIBOSS_ANALYSE_REPLICATES_BINARY)
@task(
    replicates_folder=DIRECTORY_IN,
    out_file=FILE_OUT,
    err_file=FILE_OUT,
    results_dir=DIRECTORY_OUT,
)
def physiboss_analyse_replicates(
    replicates=1,
    replicates_folder=DIRECTORY_IN,
    prefix="prefix",
    out_file=None,
    err_file=None,
    results_dir=None,
    parallel=8,
    tmpdir=TMPDIR
):
    """
    Performs the PhysiCell + MaBoSS analysis.

    The Definition is equal to:
        ./physiboss_analyse_replicates.sh <replicates> <replicates_folder> <prefix> \
                                          <out_file> <err_file> <results_dir> <parallel> <tmpdir>
    """
    # Empty function since it represents a binary execution:
    pass



@constraint(computing_units=COMPUTING_UNITS)
@container(engine=CONTAINER_ENGINE, image=CONTAINER, options=CONTAINER_OPTIONS)
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
    tmpdir=TMPDIR
):
    """
    Performs the PhysiCell + MaBoSS analysis.

    The Definition is equal to:
        ./physiboss.sh <sample> <repetition> <prefix> <bnd_file> \
                       <cfg_file> <out_file> <err_file> <results_dir> \
                       <computing_units> <max_time> <tmpdir>
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
    if arguments.mode == "analyse_replicates":
        # Process parameters
        replicates = arguments.replicates
        replicates_folder = arguments.replicates_folder
        prefix = arguments.prefix
        out_file = arguments.out_file
        err_file = arguments.err_file
        results_dir = arguments.results_dir
        parallel = arguments.parallel
        tmpdir = arguments.tmpdir
        # Building block invocation
        physiboss_analyse_replicates(
            replicates=replicates,
            replicates_folder=replicates_folder,
            prefix=prefix,
            out_file=out_file,
            err_file=err_file,
            results_dir=results_dir,
            parallel=parallel,
            tmpdir=tmpdir
        )
    elif arguments.mode == "physiboss_model":
        # Process parameters
        sample = arguments.sample
        repetition = arguments.repetition
        prefix = arguments.prefix
        model_dir = arguments.model_dir
        out_file = arguments.out_file
        err_file = arguments.err_file
        results_dir = arguments.results_dir
        parallel = arguments.parallel
        max_time = arguments.max_time
        tmpdir = arguments.tmpdir
        # Building block invocation
        physiboss_model(
            sample=sample,
            repetition=repetition,
            prefix=prefix,
            model_dir=model_dir,
            out_file=out_file,
            err_file=err_file,
            results_dir=results_dir,
            parallel=parallel,
            max_time=max_time,
            tmpdir=tmpdir
        )
    else:
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
        tmpdir = arguments.tmpdir
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
            tmpdir=tmpdir
        )
