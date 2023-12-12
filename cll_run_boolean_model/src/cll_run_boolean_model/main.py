

import os

# Decorator imports
from permedcoe import constraint       # To define constraints needs (e.g. number of cores)
from permedcoe import container        # To define container related needs
from permedcoe import binary           # To define binary to execute related needs
from permedcoe import mpi              # To define an mpi binary to execute related needs (can not be used with @binary)
from permedcoe import task             # To define task related needs
# @task supported types
from permedcoe import FILE_IN          # To define file type and direction
from permedcoe import FILE_OUT         # To define file type and direction
from permedcoe import FILE_INOUT       # To define file type and direction
from permedcoe import DIRECTORY_IN     # To define directory type and direction
from permedcoe import DIRECTORY_OUT    # To define directory type and direction
from permedcoe import DIRECTORY_INOUT  # To define directory type and direction
# Other permedcoe available functionalities
from permedcoe import Arguments        # Arguments definition
from permedcoe import get_environment  # Get variables from invocation (tmpdir, processes, gpus, memory)
from permedcoe import TMPDIR           # Default tmpdir key

# Import single container and assets definitions"
from cll_run_boolean_model.definitions import ASSETS_PATH  # binary could be in this folder
from cll_run_boolean_model.definitions import CONTAINER
from cll_run_boolean_model.definitions import COMPUTING_UNITS

def function_name(*args, **kwargs):
    """Extended python interface:
    To be used only with PyCOMPSs - Enables to define a workflow within the building block.
    Tasks are not forced to be binaries: PyCOMPSs supports tasks that are pure python code.

    # PyCOMPSs help: https://pycompss.readthedocs.io/en/latest/Sections/02_App_Development/02_Python.html

    Requirement: all tasks should be executed in a container (with the same container definition)
                 to ensure that they all have the same requirements.
    """
    print("Building Block entry point to be used with PyCOMPSs")
    # TODO: (optional) Pure python code calling to PyCOMPSs tasks (that can be defined in this file or in another).


# Globals
CLL_RUN_BOOLEAN_MODEL_BINARY = os.path.join(ASSETS_PATH, "run.sh")


# @constraint(computing_units=COMPUTING_UNITS)
@container(engine="SINGULARITY", image=CONTAINER)
@binary(binary=CLL_RUN_BOOLEAN_MODEL_BINARY)
@task(sif=FILE_IN, bnd=FILE_IN, cfg=FILE_IN, outdir=DIRECTORY_OUT)
def cll_run_boolean_model(
                  sif_flag='-s', sif=None, 
                  bnd_flag='-b', bnd=None, 
                  cfg_flag='-c', cfg=None, 
                  id_flag='-i', id=None, 
                  outdir_flag='-o', outdir=None):
    """
    Run personalised boolean models

    The Definition is equal to:
        assets/run.sh 
                  -s  sif \ 
                  -b  bnd \ 
                  -c  cfg \ 
                  -i  id \ 
                  -o  outdir
    """
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
                  sif=arguments.sif, 
                  bnd=arguments.bnd, 
                  cfg=arguments.cfg, 
                  id=arguments.id, 
                  outdir=arguments.outdir)


