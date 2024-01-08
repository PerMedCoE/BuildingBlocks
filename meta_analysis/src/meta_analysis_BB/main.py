import os

from permedcoe import constraint
from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_IN
from permedcoe import DIRECTORY_IN
from permedcoe import DIRECTORY_OUT
from permedcoe import TMPDIR

# Import single container and assets definitions
from meta_analysis_BB.definitions import ASSETS_PATH
from meta_analysis_BB.definitions import CONTAINER_ENGINE
from meta_analysis_BB.definitions import CONTAINER
from meta_analysis_BB.definitions import CONTAINER_OPTIONS
from meta_analysis_BB.definitions import COMPUTING_UNITS

# Globals
META_ANALYSIS_BINARY = os.path.join(ASSETS_PATH, "meta_analysis.sh")


# @constraint(computing_units=COMPUTING_UNITS)
@container(engine=CONTAINER_ENGINE, image=CONTAINER, options=CONTAINER_OPTIONS)
@binary(binary=META_ANALYSIS_BINARY)
@task(meta_file=FILE_IN,
      out_dir=DIRECTORY_IN,
      ko_file=FILE_IN,
      results=DIRECTORY_OUT)
def meta_analysis(tmpdir=TMPDIR,
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
        ./meta_analysis.sh <tmpdir> \
                           -m <meta_file> \
                           -o <out_dir> \
                           -p <model_prefix> \
                           -k <ko_file> \
                           -r <repetitions> \
                           -v <verbose> \
                           -z <results>
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
    tmpdir = arguments.tmpdir
    # Building block invocation
    meta_analysis(meta_file=meta_file,
                  out_dir=out_dir,
                  model_prefix=model_prefix,
                  ko_file=ko_file,
                  reps=reps,
                  verbose=verbose,
                  results=results,
                  tmpdir=tmpdir)
