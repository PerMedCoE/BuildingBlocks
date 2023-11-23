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

# Import single container and assets definitions
from cll_prepare_data.definitions import ASSETS_PATH  # binary could be in this folder
from cll_prepare_data.definitions import CONTAINER
from cll_prepare_data.definitions import COMPUTING_UNITS


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
# CLL_PREPARE_DATA_BINARY = "cd /home/permed; Rscript /home/permed/prepare_data.R" #os.path.join(ASSETS_PATH, "cll_prepare_data.sh")
CLL_PREPARE_DATA_BINARY = os.path.join(ASSETS_PATH, "run.sh")


# @constraint(computing_units=COMPUTING_UNITS)
@container(engine="SINGULARITY", image=CONTAINER)
@binary(binary=CLL_PREPARE_DATA_BINARY)
@task(exp_file=FILE_IN,
      metadata=FILE_IN,
      xref=FILE_IN,
      outdir=DIRECTORY_IN)
def cll_prepare_data(
                  #tmpdir=TMPDIR,
                  exp_file_flag='-e', exp_file=None,
                  metadata_flag='-m', metadata=None,                  
                  xref_flag='-x', xref=None, 
                  group_flag='-g', group=None,
                  treatment_flag='-t', treatment=None,
                  control_flag='-c', control=None,
                  batch_flag='-b', batch="T",
                  outdir_flag='-o', outdir=None):
    """
    Prepare RNA-Seq data for downstream analysis.

    The Definition is equal to:
        assets/run.sh <tmpdir> \
                           -e <exp_file> \
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
    # Process parameters
    exp_file = arguments.exp_file
    metadata = arguments.metadata
    xref = arguments.xref
    group = arguments.group
    treatment = arguments.treatment
    control = arguments.control
    batch = arguments.batch
    outdir = arguments.outdir
    tmpdir = arguments.tmpdir
    
    # Building block invocation
    cll_prepare_data(exp_file=exp_file,
                  metadata=metadata,
                  xref=xref,
                  group=group,
                  treatment=treatment,
                  control=control,
                  batch=batch,
                  outdir=outdir)
