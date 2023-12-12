

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
from cll_tf_activities.definitions import ASSETS_PATH  # binary could be in this folder
from cll_tf_activities.definitions import CONTAINER
from cll_tf_activities.definitions import COMPUTING_UNITS

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
CLL_TF_ACTIVITIES_BINARY = os.path.join(ASSETS_PATH, "run.sh")


# @constraint(computing_units=COMPUTING_UNITS)
@container(engine="SINGULARITY", image=CONTAINER)
@binary(binary=CLL_TF_ACTIVITIES_BINARY)
@task(norm_exp=FILE_IN, metadata=FILE_IN, dea=FILE_IN, collectri_database=FILE_IN, progeny_database=FILE_IN, outdir=DIRECTORY_OUT, activities=FILE_OUT)
def cll_tf_activities(
                  norm_exp_flag='-n', norm_exp=None, 
                  metadata_flag='-m', metadata=None, 
                  dea_flag='-d', dea=None, 
                  group_flag='-g', group=None, 
                  treatment_flag='-t', treatment=None, 
                  control_flag='-c', control=None, 
                  collectri_database_flag='-b', collectri_database=None, 
                  progeny_database_flag='-p', progeny_database=None, 
                  outdir_flag='-o', outdir=None, 
                  activities_flag='-a', activities=None):
    """
    Inference of transcription factor analysis from differential expression analysis

    The Definition is equal to:
        assets/run.sh 
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
                  norm_exp=arguments.norm_exp, 
                  metadata=arguments.metadata, 
                  dea=arguments.dea, 
                  group=arguments.group, 
                  treatment=arguments.treatment, 
                  control=arguments.control, 
                  collectri_database=arguments.collectri_database, 
                  progeny_database=arguments.progeny_database, 
                  outdir=arguments.outdir, 
                  activities=arguments.activities)


