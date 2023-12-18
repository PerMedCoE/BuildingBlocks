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
from cll_tf_activities_BB.definitions import ASSETS_PATH
from cll_tf_activities_BB.definitions import CLL_TF_ACTIVITIES_CONTAINER
from cll_tf_activities_BB.definitions import COMPUTING_UNITS

# Globals
CLL_TF_ACTIVITIES_BINARY = os.path.join(ASSETS_PATH, "run.sh")
# Override COMPUTING_UNITS
COMPUTING_UNITS = 48


@constraint(computing_units=COMPUTING_UNITS)
@container(engine="SINGULARITY", image=CLL_TF_ACTIVITIES_CONTAINER)
@binary(binary=CLL_TF_ACTIVITIES_BINARY)
@task(
    norm_exp=FILE_IN,
    metadata=FILE_IN,
    dea=FILE_IN,
    collectri_database=FILE_IN,
    progeny_database=FILE_IN,
    outdir=DIRECTORY_OUT,
    activities=FILE_OUT,
)
def cll_tf_activities(
    tmpdir=TMPDIR,
    norm_exp_flag="-n",
    norm_exp=None,
    metadata_flag="-m",
    metadata=None,
    dea_flag="-d",
    dea=None,
    group_flag="-g",
    group=None,
    treatment_flag="-t",
    treatment=None,
    control_flag="-c",
    control=None,
    collectri_database_flag="-b",
    collectri_database=None,
    progeny_database_flag="-p",
    progeny_database=None,
    outdir_flag="-o",
    outdir=None,
    activities_flag="-a",
    activities=None,
):
    """
    Inference of transcription factor analysis from differential expression analysis

    The Definition is equal to:
        assets/run.sh
                  tmpdir \
                  -n  norm_exp \
                  -m  metadata \
                  -d  dea \
                  -g  group \
                  -t  treatment \
                  -c  control \
                  -b  collectri_database \
                  -p  progeny_database \
                  -o  outdir \
                  -a  activities
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
    cll_tf_activities(
        tmpdir=arguments.tmpdir,
        norm_exp=arguments.norm_exp,
        metadata=arguments.metadata,
        dea=arguments.dea,
        group=arguments.group,
        treatment=arguments.treatment,
        control=arguments.control,
        collectri_database=arguments.collectri_database,
        progeny_database=arguments.progeny_database,
        outdir=arguments.outdir,
        activities=arguments.activities,
    )
