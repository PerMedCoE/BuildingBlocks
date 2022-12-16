import os

from permedcoe import Arguments
from permedcoe import constraint
from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_IN
from permedcoe import FILE_OUT

# Import container definition
from export_solver_hdf5_BB.definitions import EXPORT_SOLVER_HDF5_ASSETS_PATH
from export_solver_hdf5_BB.definitions import EXPORT_SOLVER_HDF5_CONTAINER
from export_solver_hdf5_BB.definitions import COMPUTING_UNITS

# Globals
EXPORT_SOLVER_HDF5_BINARY = os.path.join(EXPORT_SOLVER_HDF5_ASSETS_PATH,
                                         "export_solver_hdf5.sh")


@constraint(computing_units=COMPUTING_UNITS)
@container(engine="SINGULARITY", image=EXPORT_SOLVER_HDF5_CONTAINER)
@binary(binary=EXPORT_SOLVER_HDF5_BINARY)
@task(sif=FILE_IN, measurements=FILE_IN, inputs=FILE_IN, output_file=FILE_OUT)
def export(sif=None,
           measurements=None,
           inputs=None,
           output_file=None,
           verbose_flag='-v', verbose=None):
    """
    Runs export solver to hdf5

    The Definition is equal to:
        Rscript --vanilla /opt/export.R <sif>
                                        <measurements>
                                        <inputs>
                                        <output_file>
                                        <verbose_flag> <verbose>
    By default:
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
    # Building block invocation
    export(sif=sif,
           measurements=measurements,
           inputs=inputs,
           output_file=output_file,
           verbose=verbose)


def arguments_info():
    """Arguments definition.

    Builds the arguments definition.

    Returns:
        Supported arguments.
    """
    arguments = Arguments()
    arguments.add_input(name="sif",
                        type=str,
                        description="The sif csv file containing the signaling network",
                        check="file")
    arguments.add_input(name="measurements",
                        type=str,
                        description="The measurements csv with the TFs and weights",
                        check=str)
    arguments.add_input(name="inputs",
                        type=str,
                        description="The csv file with the input protein targets",
                        check="file")
    arguments.add_input(name="verbose",
                        type=str,
                        description="Verbose output (True | False)",
                        check=str)
    arguments.add_output(name="output_file",
                         type=str,
                         description="The final HDF5 file")
    return arguments
