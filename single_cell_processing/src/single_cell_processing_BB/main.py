import os

from permedcoe import constraint
from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_IN
from permedcoe import FILE_OUT
from permedcoe import DIRECTORY_OUT

# Import single container and assets definitions
from single_cell_processing_BB.definitions import SINGLE_CELL_ASSETS_PATH
from single_cell_processing_BB.definitions import SINGLE_CELL_PROCESSING_CONTAINER
from single_cell_processing_BB.definitions import COMPUTING_UNITS

# Globals
SINGLE_CELL_PROCESSING_BINARY = os.path.join(
    SINGLE_CELL_ASSETS_PATH, "single_cell_processing_individual.sh"
)


@constraint(computing_units=COMPUTING_UNITS)
@container(engine="SINGULARITY", image=SINGLE_CELL_PROCESSING_CONTAINER)
@binary(binary=SINGLE_CELL_PROCESSING_BINARY)
@task(
    p_file=FILE_IN,
    norm_data=FILE_OUT,
    raw_data=FILE_OUT,
    scaled_data=FILE_OUT,
    cells_metadata=FILE_OUT,
    outdir=DIRECTORY_OUT,
)
def single_cell_processing(
    working_directory="None",
    id_flag="-i",
    p_id="C141",
    group_flag="-g",
    p_group="C",
    file_flag="-f",
    p_file=None,
    norm_data_flag="-n",
    norm_data=None,
    raw_data_flag="-r",
    raw_data=None,
    scaled_data_flag="-c",
    scaled_data=None,
    cells_metadata_flag="-m",
    cells_metadata=None,
    outdir_flag="-o",
    outdir=None,
    parallelize_flag="-p",
    parallelize=COMPUTING_UNITS
):
    """
    Performs the Single Cell processing.

    The Definition is equal to:
        ./single_cell_processing.sh <working_directory> \
                                    -i <id> -g <group> -f <file> \
                                    -nd <norm_data> \
                                    -rd <raw_data> \
                                    -sd <scaled_data> \
                                    -cm <cells_metadata> \
                                    -o <outdir> \
                                    -p <computing_units>
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
    p_id = arguments.p_id
    p_group = arguments.p_group
    p_file = arguments.p_file
    parallelize = arguments.parallelize
    norm_data = arguments.norm_data
    raw_data = arguments.raw_data
    scaled_data = arguments.scaled_data
    cells_metadata = arguments.cells_metadata
    outdir = arguments.outdir
    working_directory = arguments.working_directory
    # Building block invocation
    single_cell_processing(
        p_id=p_id,
        p_group=p_group,
        p_file=p_file,
        norm_data=norm_data,
        raw_data=raw_data,
        scaled_data=scaled_data,
        cells_metadata=cells_metadata,
        outdir=outdir,
        parallelize=parallelize,
        working_directory=working_directory,
    )
