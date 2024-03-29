import os

from permedcoe import constraint
from permedcoe import container
from permedcoe import binary
from permedcoe import julia
from permedcoe import task
from permedcoe import FILE_IN
from permedcoe import FILE_OUT

# Import single container and assets definitions
from COBREXA_FVA.definitions import CONTAINER
from COBREXA_FVA.definitions import ASSETS_PATH
from COBREXA_FVA.definitions import COMPUTING_UNITS

# Globals
COBREXA_BINARY = os.path.join(ASSETS_PATH, "fva.jl")


@constraint(computing_units=COMPUTING_UNITS)
@container(engine="SINGULARITY", image=CONTAINER)
@julia(script=COBREXA_BINARY, project="/project")
@task(input_file_xml=FILE_IN, output_file_txt=FILE_OUT)
def COBREXA_analysis(
    debug_flag="-d",
    input_file_xml=None,
    output_file_txt=None
):
    """
    Performs the COBREXA analysis.
    Produces the output txt file.

    The Definition is equal to:
        julia --project=/project <cobrexa_binary> <debug_flag> <input_sbml> <output_txt>
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
    input_file_xml = arguments.input_sbml
    output_file_txt = arguments.output_txt
    verbose = arguments.verbose == "true"
    if verbose:
        debug_flag = "-d"
    else:
        debug_flag = ""
    # Building block invocation
    COBREXA_analysis(
        debug_flag=debug_flag,
        input_file_xml=input_file_xml,
        output_file_txt=output_file_txt
    )
