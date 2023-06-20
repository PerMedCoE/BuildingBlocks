import os

from permedcoe import Arguments
from permedcoe import constraint
from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_IN
from permedcoe import FILE_OUT
from permedcoe import DIRECTORY_IN
from permedcoe import DIRECTORY_OUT
from permedcoe import TMPDIR

# Import single container and assets definitions
from invasion_analysis_BB.definitions import CONTAINER
from invasion_analysis_BB.definitions import ASSETS_PATH
from invasion_analysis_BB.definitions import COMPUTING_UNITS

# Globals
INVASION_ANALYSIS_BINARY = os.path.join(ASSETS_PATH, "InvasionAnalysis.sh")
INVASION_PLOTTING_BINARY = os.path.join(ASSETS_PATH, "InvasionPlotting.sh")


@container(engine="SINGULARITY", image=CONTAINER)
@binary(binary=INVASION_ANALYSIS_BINARY)
@task(output_data=FILE_OUT, varargs_type=DIRECTORY_IN)
def invasion_analysis(tmpdir=TMPDIR, output_data=None, *args):
    # The Definition is equal to:
    #    INVASION_ANALYSIS_BINARY <tmpdir> <output_data> *<physiboss_final_net_result_path>
    # Empty function since it represents a binary execution:
    pass


@container(engine="SINGULARITY", image=CONTAINER)
@binary(binary=INVASION_PLOTTING_BINARY)
@task(parameter_sets=FILE_IN, plot_directory=DIRECTORY_OUT, varargs_type=FILE_IN)
def invasion_generate_plots(
    tmpdir=TMPDIR, parameter_sets=None, plot_directory=None, *args
):
    # The Definition is equal to:
    #    INVASION_PLOTTING_BINARY <tmpdir> <analysis_paths> <parameter_sets> <plot_directory>
    # Empty function since it represents a binary execution:
    pass


def invoke(arguments, config):
    """Common interface.

    Args:
        arguments (args): Building Block parsed arguments.
        config (dict): Configuration dictionary.
    Returns:
        None
    """

    if arguments.mode == "generate_plots":
        tmpdir = arguments.tmpdir
        parameter_sets = arguments.parameter_sets
        plot_directory = arguments.plot_directory
        analysis_paths = list(arguments.analysis_paths.split(" "))
        invasion_generate_plots(tmpdir, parameter_sets, plot_directory, *analysis_paths)
    else:
        tmpdir = arguments.tmpdir
        output_data = arguments.output_data
        physiboss_final_net_result_path = list(
            arguments.physiboss_final_net_result_path.split(" ")
        )
        invasion_analysis(tmpdir, output_data, *physiboss_final_net_result_path)
