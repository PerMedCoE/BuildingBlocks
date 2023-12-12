

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
from cll_network_inference.definitions import ASSETS_PATH  # binary could be in this folder
from cll_network_inference.definitions import CONTAINER
from cll_network_inference.definitions import COMPUTING_UNITS

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
CLL_NETWORK_INFERENCE_BINARY = os.path.join(ASSETS_PATH, "run.sh")


# @constraint(computing_units=COMPUTING_UNITS)
@container(engine="SINGULARITY", image=CONTAINER)
@binary(binary=CLL_NETWORK_INFERENCE_BINARY)
@task(activities=FILE_IN, omnipath_database=FILE_IN, outdir=DIRECTORY_OUT, sif=FILE_OUT)
def cll_network_inference(
                  cplex_bin_flag='-c', cplex_bin=None, 
                  activities_flag='-a', activities=None, 
                  omnipath_database_flag='-z', omnipath_database=None, 
                  outdir_flag='-o', outdir=None, 
                  sif_flag='-s', sif=None):
    """
    Inference of contextualize signaling network from TF activities

    The Definition is equal to:
        assets/run.sh 
                  -c  cplex_bin \ 
                  -a  activities \ 
                  -z  omnipath_database \ 
                  -o  outdir \ 
                  -s  sif
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
    cll_network_inference(
                  cplex_bin=arguments.cplex_bin, 
                  activities=arguments.activities, 
                  omnipath_database=arguments.omnipath_database, 
                  outdir=arguments.outdir, 
                  sif=arguments.sif)


