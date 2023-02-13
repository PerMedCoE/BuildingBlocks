import os

from permedcoe import constraint
from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import DIRECTORY_IN
from permedcoe import FILE_OUT

# Import container definition
from CarnivalPy_BB.definitions import CARNIVALPY_ASSETS_PATH
from CarnivalPy_BB.definitions import CARNIVALPY_CONTAINER
from CarnivalPy_BB.definitions import COMPUTING_UNITS

# Globals
CARNIVALPY_BINARY = os.path.join(CARNIVALPY_ASSETS_PATH, "carnivalpy.sh")


@constraint(computing_units=COMPUTING_UNITS)
@container(engine="SINGULARITY", image=CARNIVALPY_CONTAINER)
@binary(binary=CARNIVALPY_BINARY)
@task(path=DIRECTORY_IN, export=FILE_OUT)
def carnivalpy(working_directory="None",
               path=None,
               penalty_flag='--penalty', penalty=None,
               solver_flag='--solver', solver=None,
               tol_flag='--tol', tol=0.01,
               maxtime_flag='--maxtime', maxtime=600,
               export_flag='--export', export=None):
    """
    Runs CarnivalPy

    The Definition is equal to:
        <working_directory>
        /opt/conda/bin/python /opt/carnival/carnivalpy/carnival.py <path>
                                                                   <col_genes_flag> <penalty>
                                                                   <solver_flag> <solver>
                                                                   <tol_flag> <tol>
                                                                   <maxtime_flag> <maxtime>
                                                                   <export_flag> <export>
    By default:
        <working_directory>
        /opt/conda/bin/python /opt/carnival/carnivalpy/carnival.py <path>
                                                                   --penalty <penalty>
                                                                   --solver <solver>
                                                                   --tol <tol>
                                                                   --maxtime <maxtime>
                                                                   --export <export>
    """
    # Empty function since it represents a binary execution:
    pass


def invoke(arguments, config):
    """ Common interface.

    Args:
        arguments (args): Building Block parsed arguments.
        config (dict): Configuration dictionary (not used).
    Returns:
        None
    """
    # Process parameters
    path = arguments.path
    penalty = arguments.penalty
    solver = arguments.solver
    tol = arguments.tol
    maxtime = arguments.maxtime
    export = arguments.export
    working_directory = arguments.working_directory
    # Building block invocation
    carnivalpy(working_directory=working_directory,
               path=path,
               penalty=penalty,
               solver=solver,
               tol=tol,
               maxtime=maxtime,
               export=export)
