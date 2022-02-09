import os

from permedcoe import constraint
from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_IN
from permedcoe import FILE_OUT
from permedcoe import DIRECTORY_IN
from permedcoe import DIRECTORY_OUT

# Import single container and assets definitions
from physiboss.definitions import PHYSIBOSS_CONTAINER
from physiboss.definitions import PHYSIBOSS_ASSETS
from physiboss.definitions import COMPUTING_UNITS

# Globals# Globals
PHYSIBOSS_BINARY = os.path.join(PHYSIBOSS_ASSETS, "PhysiBoSS.sh")
PHYSIBOSS_MODEL_BINARY = os.path.join(PHYSIBOSS_ASSETS, "PhysiBoSS_model.sh")


@constraint(computing_units=COMPUTING_UNITS)
@container(engine="SINGULARITY", image=PHYSIBOSS_CONTAINER)
@binary(binary=PHYSIBOSS_MODEL_BINARY)
@task(model_dir=DIRECTORY_IN, out_file=FILE_OUT, err_file=FILE_OUT, results_dir=DIRECTORY_OUT)
def physiboss_model(sample="C141",
                    repetition=1,
                    prefix="epithelial_cell_2_personalized",
                    model_dir=None,
                    out_file=None,
                    err_file=None,
                    results_dir=None,
                    parallel=COMPUTING_UNITS):
    """
    Performs the PhysiCell + MaBoSS analysis.

    The Definition is equal to:
        ./physiboss_model.sh <sample> <repetition> <prefix> <model_dir> \
                             <file_name> <out_file> <err_file> <results_dir> \
                             <computing_units>
    """
    # Empty function since it represents a binary execution:
    pass


@constraint(computing_units=COMPUTING_UNITS)
@container(engine="SINGULARITY", image=PHYSIBOSS_CONTAINER)
@binary(binary=PHYSIBOSS_BINARY)
@task(bnd_file=FILE_IN, cfg_file=FILE_IN, out_file=FILE_OUT, err_file=FILE_OUT, results_dir=DIRECTORY_OUT)
def physiboss(sample="C141",
              repetition=1,
              prefix="epithelial_cell_2_personalized",
              bnd_file=None,
              cfg_file=None,
              out_file=None,
              err_file=None,
              results_dir=None,
              parallel=COMPUTING_UNITS):
    """
    Performs the PhysiCell + MaBoSS analysis.

    The Definition is equal to:
        ./physiboss.sh <sample> <repetition> <prefix> <bnd_file> \
                       <cfg_file> <out_file> <err_file> <results_dir> \
                       <computing_units>
    """
    # Empty function since it represents a binary execution:
    pass



def invoke(input, output, config):
    """ Common interface.

    Args:
        input (list): List containing the sample label, number of repetitions,
                      prefix name, bnd file path and cfg file path.
        output (list): list containing the output and error files.
        config (dict): Configuration dictionary (not used).
    Returns:
        None
    """
    # Process parameters
    sample = input[0]
    repetition = input[1]
    prefix = input[2]
    bnd_file = input[3]
    cfg_file = input[4]
    parallel = input[5]
    out_file = output[0]
    err_file = output[1]
    results_dir = output[2]
    # Building block invocation
    physiboss(sample=sample,
              repetition=repetition,
              prefix=prefix,
              bnd_file=bnd_file,
              cfg_file=cfg_file,
              out_file=out_file,
              err_file=err_file,
              results_dir=results_dir,
              parallel=parallel)
