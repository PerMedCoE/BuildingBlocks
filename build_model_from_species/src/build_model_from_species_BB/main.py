import os

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


def invoke(input, output, config):
    """ Common interface.

    Args:
        input (str): Input file path.
        output (str): Output directory path.
        config (dict): Configuration dictionary.
    Returns:
        None
    """
    build_model_from_key = "build_model_from"
    if build_model_from_key in config.keys():
        if config[build_model_from_key] == "genes":
            print("List genes")
            input_file = input[0]
            output_bnd_file = output[0]
            output_cfg_file = output[1]
            build_model_from_species(input_file=input_file,
                                     output_bnd_file=output_bnd_file,
                                     output_cfg_file=output_cfg_file)
        elif config[build_model_from_key] == "sif":
            print("SIF file")
            input_file = input[0]
            output_bnd_file = output[0]
            output_cfg_file = output[1]
            build_model_from_sif(input_file=input_file,
                                 output_bnd_file=output_bnd_file,
                                 output_cfg_file=output_cfg_file)
        else:
            raise Exception("Unsupported %s value in config file. Supported: genes | sif" % build_model_from_key)
    else:
        raise Exception("Could not find %s in config file." % build_model_from_key)
