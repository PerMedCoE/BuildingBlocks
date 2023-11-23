import os

from permedcoe import constraint
from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_IN
from permedcoe import FILE_OUT
from permedcoe import DIRECTORY_OUT
from permedcoe import TMPDIR

# Import single container and assets definitions
from PhysiBoSS_invasion_BB.definitions import CONTAINER
from PhysiBoSS_invasion_BB.definitions import ASSETS_PATH
from PhysiBoSS_invasion_BB.definitions import COMPUTING_UNITS

# Globals
PHYSIBOSS_INVASION_BINARY = os.path.join(ASSETS_PATH, "PhysiBoSS_invasion.sh")


@constraint(computing_units=COMPUTING_UNITS)
@container(engine="SINGULARITY", image=CONTAINER)
@binary(binary=PHYSIBOSS_INVASION_BINARY)
@task(
    parameter_set=FILE_IN,
    out_file=FILE_OUT,
    err_file=FILE_OUT,
    results_dir=DIRECTORY_OUT,
    final_net_dir=DIRECTORY_OUT,
)
def physiboss_invasion(
    parameter_set=None,
    repetition=1,
    out_file=None,
    err_file=None,
    results_dir=None,
    parallel=8,
    max_time=8640,
    final_net_dir=None,
    tmpdir=TMPDIR,
):
    """
    Performs the PhysiCell + MaBoSS analysis.

    The Definition is equal to:
        ./PhysiBoSS_invasion.sh \
            <parameter_set> \
            <repetition> \
            <out_file> \
            <err_file> \
            <results_dir> \
            <computing_units> \
            <max_time> \
            <final_net_dir> \
            <tmpdir>
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
    parameter_set = arguments.parameter_set
    repetition = arguments.repetition
    parallel = arguments.parallel
    max_time = arguments.max_time
    out_file = arguments.out_file
    err_file = arguments.err_file
    results_dir = arguments.results_dir
    final_net_dir = arguments.final_net_dir
    tmpdir = arguments.tmpdir
    # Building block invocation
    physiboss_invasion(
        parameter_set=parameter_set,
        repetition=repetition,
        out_file=out_file,
        err_file=err_file,
        results_dir=results_dir,
        parallel=parallel,
        max_time=max_time,
        final_net_dir=final_net_dir,
        tmpdir=tmpdir,
    )