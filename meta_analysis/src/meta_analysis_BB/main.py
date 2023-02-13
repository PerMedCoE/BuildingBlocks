import os

from permedcoe import constraint
from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_IN
from permedcoe import DIRECTORY_IN
from permedcoe import DIRECTORY_OUT

# Import single container and assets definitions
from meta_analysis_BB.definitions import META_ANALYSIS_ASSETS_PATH
from meta_analysis_BB.definitions import META_ANALYSIS_CONTAINER
from meta_analysis_BB.definitions import COMPUTING_UNITS

# Globals
META_ANALYSIS_BINARY = os.path.join(META_ANALYSIS_ASSETS_PATH,
                                    "meta_analysis.sh")


# @constraint(computing_units=COMPUTING_UNITS)
@container(engine="SINGULARITY", image=META_ANALYSIS_CONTAINER)
@binary(binary=META_ANALYSIS_BINARY)
@task(meta_file=FILE_IN,
      out_dir=DIRECTORY_IN,
      ko_file=FILE_IN,
      results=DIRECTORY_OUT)
def meta_analysis(working_directory="None",
                  meta_file_flag='-m', meta_file=None,
                  out_dir_flag='-o', out_dir=None,
                  model_prefix_flag='-p', model_prefix=None,
                  ko_file_flag='-k', ko_file=None,
                  reps_flag='-r', reps=None,
                  verbose_flag='-v', verbose="T",
                  results_flag='-z', results=None):
    """
    Performs the Single Cell processing.

    The Definition is equal to:
        ./meta_analysis.sh <working_directory> \
                           -m <meta_file> \
                           -o <out_dir> \
                           -p <model_prefix> \
                           -k <ko_file> \
                           -r <repetitions> \
                           -v <verbose>
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
    meta_file = arguments.meta_file
    out_dir = arguments.out_dir
    model_prefix = arguments.model_prefix
    ko_file = arguments.ko_file
    reps = arguments.reps
    verbose = arguments.verbose
    results = arguments.results
    working_directory = arguments.working_directory
    # Building block invocation
    meta_analysis(meta_file=meta_file,
                  out_dir=out_dir,
                  model_prefix=model_prefix,
                  ko_file=ko_file,
                  reps=reps,
                  verbose=verbose,
                  results=results,
                  working_directory=working_directory)
