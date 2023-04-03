import os

from permedcoe import constraint
from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_IN
from permedcoe import FILE_OUT
from permedcoe import TMPDIR

# Import container definition
from export_solver_hdf5_BB.definitions import CONTAINER
from export_solver_hdf5_BB.definitions import ASSETS_PATH
from export_solver_hdf5_BB.definitions import COMPUTING_UNITS

# Globals
EXPORT_SOLVER_HDF5_BINARY = os.path.join(ASSETS_PATH, "export_solver_hdf5.sh")


@constraint(computing_units=COMPUTING_UNITS)
@container(engine="SINGULARITY", image=CONTAINER)
@binary(binary=EXPORT_SOLVER_HDF5_BINARY)
@task(sif=FILE_IN, measurements=FILE_IN, inputs=FILE_IN, output_file=FILE_OUT)
def export(tmpdir=TMPDIR,
           sif=None,
           measurements=None,
           inputs=None,
           output_file=None,
           verbose_flag='-v', verbose=None):
    """
    Runs export solver to hdf5

    The Definition is equal to:
        <tmpdir>
        Rscript --vanilla /opt/export.R <sif>
                                        <measurements>
                                        <inputs>
                                        <output_file>
                                        <verbose_flag> <verbose>
    By default:
        <tmpdir>
        Rscript --vanilla /opt/export.R <sif>
                                        <measurements>
                                        <inputs>
                                        <output_file>
                                        -v <verbose>
    """
    # Empty function since it represents a binary execution:
    pass


def invoke(arguments, config):
    """ Common interface.

    export_bb -i sif.csv measurements.csv inputs.csv TRUE -o file.h5

    Args:
        arguments (args): Building Block parsed arguments.
        config (dict): Configuration dictionary (not used).
    Returns:
        None
    """
    # Process parameters
    sif = arguments.sif
    measurements = arguments.measurements
    inputs = arguments.inputs
    verbose = arguments.verbose
    output_file = arguments.output_file
    tmpdir = arguments.tmpdir
    # Building block invocation
    export(tmpdir=tmpdir,
           sif=sif,
           measurements=measurements,
           inputs=inputs,
           output_file=output_file,
           verbose=verbose)
