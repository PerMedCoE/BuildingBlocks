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
@task(physiboss_result_path=DIRECTORY_IN, output_data=FILE_OUT)
def invasion_analysis(tmpdir=TMPDIR,
                      physiboss_result_path=None,
                      output_data=None
                      ):
    # The Definition is equal to:
    #    INVASION_ANALYSIS_BINARY <output_bnd_file> <output_cfg_file> --list-genes <input_file>
    # Empty function since it represents a binary execution:
    pass

@container(engine="SINGULARITY", image=CONTAINER)
@binary(binary=INVASION_PLOTTING_BINARY)
@task(simulations_path=DIRECTORY_IN, parameter_sets=FILE_IN, plot_directory=DIRECTORY_OUT)
def invasion_generate_plots(tmpdir=TMPDIR,
                            simulations_path=None,
                            parameter_sets=None,
                            plot_directory=None
                            ):
    # The Definition is equal to:
    #    INVASION_PLOTTING_BINARY <simulations_path> <parameter_sets> <plot_directory>
    # Empty function since it represents a binary execution:
    pass



def invoke(arguments, config):
    """ Common interface.

    Args:
        arguments (args): Building Block parsed arguments.
        config (dict): Configuration dictionary.
    Returns:
        None
    """

    if arguments.mode == "generate_plots":
        tmpdir = arguments.tmpdir
        simulations_path = arguments.simulations_path
        parameter_sets = arguments.parameter_sets
        plot_directory = arguments.plot_directory
        invasion_generate_plots(tmpdir=tmpdir,
                                simulations_path=simulations_path,
                                parameter_sets=parameter_sets,
                                plot_directory=plot_directory)
    else:
        tmpdir = arguments.tmpdir
        physiboss_result_path = arguments.physiboss_result_path
        output_data = arguments.output_data
        invasion_analysis(tmpdir=tmpdir,
                          physiboss_result_path=physiboss_result_path,
                          output_data=output_data)
