import os

from permedcoe import constraint
from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_IN
from permedcoe import FILE_OUT
from permedcoe import DIRECTORY_OUT

# Import single container and assets definitions
from personalize_patient_BB.definitions import PERSONALIZE_PATIENT_CONTAINER
from personalize_patient_BB.definitions import PERSONALIZE_PATIENT_ASSETS
from personalize_patient_BB.definitions import COMPUTING_UNITS

# Globals
PERSONALIZE_PATIENT_BINARY = os.path.join(PERSONALIZE_PATIENT_ASSETS,
                                          "personalize_patient.sh")


# @constraint(computing_units=COMPUTING_UNITS)
@container(engine="SINGULARITY", image=PERSONALIZE_PATIENT_CONTAINER)
@binary(binary=PERSONALIZE_PATIENT_BINARY)
@task(norm_data=FILE_IN, cells=FILE_IN, model_output_dir=DIRECTORY_OUT, personalized_result=FILE_OUT, ko=FILE_IN)
def personalize_patient(norm_data_flag="-e", norm_data=None,
                        cells_flag="-c", cells=None,
                        model_prefix_flag="-m", model_prefix="prefix",
                        t_flag="-t", t="Epithelial_cells",
                        model_output_flag="-o", model_output_dir=None,
                        personalized_result_flag="-p", personalized_result=None,
                        ko_flag="-k", ko=None,
                        ):
    """
    Performs the personalize patient.

    The Definition is equal to:
       ./personalize_patient.sh \
       -e <norm_data> \
       -c <cells> \
       -m <model_prefix> -t <t> \
       -o <model_output_dir> -p <personalization_result> \
       -k <ko>
    Sample:
       ./personalize_patient.sh \
       -e $outdir/$sample/norm_data.tsv \
       -c $outdir/$sample/cells_metadata.tsv \
       -m $model_prefix -t Epithelial_cells \
       -o $outdir/$sample/models -p $outdir/$sample/personalized_by_cell_type.tsv \
       -k $ko_file
    """
    # Empty function since it represents a binary execution:
    pass


def invoke(input, output, config):
    """ Common interface.

    Args:
        input (list): List containing the normalized data file path, cells
                      metadata, model prefix, tag and ko file.
        output (list): list containing the output directory path.
        config (dict): Configuration dictionary (not used).
    Returns:
        None
    """
    # Process parameters
    norm_data = input[0]
    cells = input[1]
    model_prefix = input[2]
    t = input[3]
    ko = input[4]
    model_output_dir = output[0]
    personalized_result = output[1]
    # Building block invocation
    personalize_patient(norm_data=norm_data,
                        cells=cells,
                        model_prefix=model_prefix,
                        t=t,
                        model_output_dir=model_output_dir,
                        personalized_result=personalized_result,
                        ko=ko)
