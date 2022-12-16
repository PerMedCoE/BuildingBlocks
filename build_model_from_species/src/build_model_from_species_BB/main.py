import os

from permedcoe import Arguments
from permedcoe import constraint
from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_IN
from permedcoe import FILE_OUT

# Import single container and assets definitions
from build_model_from_species_BB.definitions import BUILD_MODEL_FROM_SPECIES_CONTAINER
from build_model_from_species_BB.definitions import BUILD_MODEL_FROM_SPECIES_ASSETS_PATH
from build_model_from_species_BB.definitions import COMPUTING_UNITS

# Globals
BUILD_MODEL_FROM_SPECIES_BINARY = os.path.join(BUILD_MODEL_FROM_SPECIES_ASSETS_PATH, "FromSpeciesToMaBoSSModel.sh")


@container(engine="SINGULARITY", image=BUILD_MODEL_FROM_SPECIES_CONTAINER)
@binary(binary=BUILD_MODEL_FROM_SPECIES_BINARY)
@task(output_bnd_file=FILE_OUT, output_cfg_file=FILE_OUT, input_file=FILE_IN)
def build_model_from_species(output_bnd_file=None,
                             output_cfg_file=None,
                             input_file_flag="--list-genes",input_file=None
                             ):
    # The Definition is equal to:
    #    BUILD_MODEL_FROM_SPECIES_BINARY <output_bnd_file> <output_cfg_file> --list-genes <input_file>
    # Empty function since it represents a binary execution:
    pass


@container(engine="SINGULARITY", image=BUILD_MODEL_FROM_SPECIES_CONTAINER)
@binary(binary=BUILD_MODEL_FROM_SPECIES_BINARY)
@task(output_bnd_file=FILE_OUT, output_cfg_file=FILE_OUT, input_file=FILE_IN)
def build_model_from_sif(output_bnd_file=None,
                         output_cfg_file=None,
                         input_file_flag="--sif-file", input_file=None
                         ):
    # The Definition is equal to:
    #    BUILD_MODEL_FROM_SPECIES_BINARY <output_bnd_file> <output_cfg_file> --sif-file <input_file>
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
    if arguments.build_model_from == "genes":
        print("List genes")
        input_file = arguments.input_file
        output_bnd_file = arguments.output_bnd_file
        output_cfg_file = arguments.output_cfg_file
        build_model_from_species(input_file=input_file,
                                 output_bnd_file=output_bnd_file,
                                 output_cfg_file=output_cfg_file)
    elif arguments.build_model_from == "sif":
        print("SIF file")
        input_file = arguments.input_file
        output_bnd_file = arguments.output_bnd_file
        output_cfg_file = arguments.output_cfg_file
        build_model_from_sif(input_file=input_file,
                             output_bnd_file=output_bnd_file,
                             output_cfg_file=output_cfg_file)
    else:
        raise Exception("Unsupported %s build model from key. Supported: genes | sif" % arguments.mode)


def arguments_info():
    """Arguments definition.

    Builds the arguments definition.

    Returns:
        Supported arguments.
    """
    arguments = Arguments()
    arguments.add_input(name="build_model_from",
                        type=str,
                        description="Build model from key (genes | sif)",
                        check=str)
    arguments.add_input(name="input_file",
                        type=str,
                        description="List of genes as a CSV file",
                        check="file")
    arguments.add_output(name="output_bnd_file",
                         type=str,
                         description="BND file of the generated MaBoSS model")
    arguments.add_output(name="output_cfg_file",
                         type=str,
                         description="CFG file of the generated MaBoSS model")
    return arguments
