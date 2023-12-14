import os

from permedcoe import constraint
from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_IN
from permedcoe import DIRECTORY_OUT
from permedcoe import TMPDIR

# Import single container and assets definitions
from cll_prepare_data_BB.definitions import ASSETS_PATH
from cll_prepare_data_BB.definitions import CLL_PREPARE_DATA_CONTAINER
from cll_prepare_data_BB.definitions import COMPUTING_UNITS

# Globals
CLL_PREPARE_DATA_BINARY = os.path.join(ASSETS_PATH, "run.sh")


@constraint(computing_units=COMPUTING_UNITS)
@container(engine="SINGULARITY", image=CLL_PREPARE_DATA_CONTAINER)
@binary(binary=CLL_PREPARE_DATA_BINARY)
@task(exp=FILE_IN, metadata=FILE_IN, xref=FILE_IN, outdir=DIRECTORY_OUT)
def cll_prepare_data(
    tmpdir=TMPDIR,
    exp_flag="-e",
    exp=None,
    metadata_flag="-m",
    metadata=None,
    xref_flag="-x",
    xref=None,
    group_flag="-g",
    group=None,
    treatment_flag="-t",
    treatment=None,
    control_flag="-c",
    control=None,
    batch_flag="-b",
    batch="T",
    outdir_flag="-o",
    outdir=None,
):
    """
    Prepare RNA-Seq data for downstream analysis.

    The Definition is equal to:
        assets/run.sh \
                tmpdir \
                -e <exp> \
                -m <metadata> \
                -x <xref> \
                -g <group> \
                -t <treatment> \
                -c <control> \
                -b <batch> \
                -o <outdir>
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
    cll_prepare_data(
        tmpdir=arguments.tmpdir,
        exp=arguments.exp,
        metadata=arguments.metadata,
        xref=arguments.xref,
        group=arguments.group,
        treatment=arguments.treatment,
        control=arguments.control,
        batch=arguments.batch,
        outdir=arguments.outdir,
    )
