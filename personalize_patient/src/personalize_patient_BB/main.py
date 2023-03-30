import os

from permedcoe import constraint
from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_IN
from permedcoe import FILE_OUT
from permedcoe import DIRECTORY_OUT
from permedcoe import TMPDIR

# Import single container and assets definitions
from personalize_patient_BB.definitions import CONTAINER
from personalize_patient_BB.definitions import ASSETS_PATH
from personalize_patient_BB.definitions import COMPUTING_UNITS

# Globals
PERSONALIZE_PATIENT_BINARY = os.path.join(ASSETS_PATH, "personalize_patient.sh")
PERSONALIZE_CELLLINE_BINARY = os.path.join(ASSETS_PATH, "personalize_cellline.sh")


# @constraint(computing_units=COMPUTING_UNITS)
@container(engine="SINGULARITY", image=CONTAINER)
@binary(binary=PERSONALIZE_PATIENT_BINARY)
@task(norm_data=FILE_IN, cells=FILE_IN, model_output_dir=DIRECTORY_OUT, personalized_result=FILE_OUT, ko=FILE_IN)
def personalize_patient(tmpdir=TMPDIR,
                        norm_data_flag="-e", norm_data=None,
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
       <tmpdir> \
       -e <norm_data> \
       -c <cells> \
       -m <model_prefix> -t <t> \
       -o <model_output_dir> -p <personalization_result> \
       -k <ko>
    Sample:
       ./personalize_patient.sh \
       $(pwd)/personalize_patient_wd/ \
       -e $outdir/$sample/norm_data.tsv \
       -c $outdir/$sample/cells_metadata.tsv \
       -m $model_prefix -t Epithelial_cells \
       -o $outdir/$sample/models -p $outdir/$sample/personalized_by_cell_type.tsv \
       -k $ko_file
    """
    # Empty function since it represents a binary execution:
    pass


@container(engine="SINGULARITY", image=CONTAINER)
@binary(binary=PERSONALIZE_CELLLINE_BINARY)
@task(expression_data=FILE_IN, cnv_data=FILE_IN, mutation_data=FILE_IN, model_bnd=FILE_IN, model_cfg=FILE_IN, model_output_dir=DIRECTORY_OUT)
def personalize_patient_cellline(tmpdir=TMPDIR,
                                 expression_data_flag="-e", expression_data=None,
                                 cnv_data_flag="-c", cnv_data=None,
                                 mutation_data_flag="-m", mutation_data=None,
                                 model_bnd_flag="-x", model_bnd=None,
                                 model_cfg_flag="-y", model_cfg=None,
                                 t_flag="-t", t="Epithelial_cells",
                                 model_output_flag="-o", model_output_dir=None,
                                 # personalized_result_flag="-p", personalized_result=None
                                 ):
    """
    Performs the personalize patient.

    The Definition is equal to:
       ./personalize_patient.sh \
       <tmpdir> \
       -e <expression> \
       -c <cells> \
       -m <model_prefix> -t <t> \
       -o <model_output_dir> \
        # -p <personalization_result> \
    Sample:
       ./personalize_patient.sh \
       $(pwd)/personalize_patient_wd/ \
       -e $outdir/$sample/norm_data.tsv \
       -c $outdir/$sample/cells_metadata.tsv \
       -m $model_prefix -t Epithelial_cells \
       -o $outdir/$sample/models \
       # -p $outdir/$sample/personalized_by_cell_type.tsv \
    """
    # Empty function since it represents a binary execution:
    pass


def invoke(arguments, config):
    """ Common interface.

    Args:
        arguments (args): Building Block parsed arguments.
        config (dict): Configuration dictionary (not used).
    Returns:
        None
    """
    if arguments.mode == "uc2":
        # Process parameters
        expression = arguments.expression
        cnv = arguments.cnv
        mutation = arguments.mutation
        cell_type = arguments.cell_type
        model_bnd = arguments.model_bnd
        model_cfg = arguments.model_cfg
        model_output_dir = os.path.abspath(arguments.model_output_dir)
        tmpdir = arguments.tmpdir
        # Building block invocation
        personalize_patient_cellline(tmpdir=tmpdir,
                                     expression_data=expression,
                                     cnv_data=cnv,
                                     mutation_data=mutation,
                                     model_bnd=model_bnd,
                                     model_cfg=model_cfg,
                                     t=cell_type,
                                     model_output_dir=model_output_dir)
    else:
        # Process parameters
        norm_data = arguments.norm_data
        cells = arguments.cells
        model_prefix = arguments.model_prefix
        t = arguments.t
        ko = arguments.ko
        model_output_dir = os.path.abspath(arguments.model_output_dir)
        personalized_result = arguments.personalized_result
        tmpdir = arguments.tmpdir
        # Building block invocation
        personalize_patient(tmpdir=tmpdir,
                            norm_data=norm_data,
                            cells=cells,
                            model_prefix=model_prefix,
                            t=t,
                            model_output_dir=model_output_dir,
                            personalized_result=personalized_result,
                            ko=ko)
