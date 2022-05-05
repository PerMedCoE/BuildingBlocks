import os

from permedcoe import constraint
from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_IN
from permedcoe import FILE_OUT

# Import container definition
from tf_enrichment_BB.definitions import TF_ENRICHMENT_ASSETS_PATH
from tf_enrichment_BB.definitions import TF_ENRICHMENT_CONTAINER
from tf_enrichment_BB.definitions import COMPUTING_UNITS

# Globals
TF_ENRICHMENT_BINARY = os.path.join(TF_ENRICHMENT_ASSETS_PATH,
                                    "tf_enrichment.sh")


@constraint(computing_units=COMPUTING_UNITS)
@container(engine="SINGULARITY", image=TF_ENRICHMENT_CONTAINER)
@binary(binary=TF_ENRICHMENT_BINARY)
@task(input_file=FILE_IN, output_file=FILE_OUT)
def tf_enrichment(input_file=None, output_file=None,
                  tsv_flag='-t', tsv=None,
                  weight_col_flag='-w', weight_col=None,
                  id_col_flag='-i', id_col=None,
                  minsize_flag='-m', minsize=None,
                  source_flag='-s', source=None,
                  confidence_flag='-c', confidence=None,
                  verbose_flag='-v', verbose=None,
                  pval_threshold_flag='-p', pval_threshold=None,
                  export_carnival_flag='-e', export_carnival=None):
    """
    Runs TF Enrichment

    The Definition is equal to:
        Rscript --vanilla /opt/tf_enrichment.R <input_file> <output_file>
                                               <tsv_flag> <tsv>
                                               <weight_col_flag> <weight_col>
                                               <id_col_flag> <id_col>
                                               <minsize_flag> <minsize>
                                               <source_flag> <source>
                                               <confidence_flag> <confidence>
                                               <verbose_flag> <verbose>
                                               <pval_threshold_flag> <pval_threshold>
                                               <export_carnival_flag> <export_carnival>
    By default:
        Rscript --vanilla /opt/tf_enrichment.R <input_file> <output_file>
                                               -t <tsv>
                                               -w <weight_col>
                                               -i <id_col>
                                               -m <minsize>
                                               -s <source>
                                               -c <confidence>
                                               -v <verbose>
                                               -p <pval_threshold>
                                               -e <export_carnival>
    """
    # Empty function since it represents a binary execution:
    pass


def invoke(input, output, config):
    """ Common interface.

    Args:
        input (list): List containing the model and data folder.
        output (list): list containing the output directory path.
        config (dict): Configuration dictionary (not used).
    Returns:
        None
    """
    # Process parameters
    input_file = input[0]
    tsv = input[1]
    weight_col = input[2]
    id_col = input[3]
    minsize = input[4]
    source = input[5]
    confidence = input[6]
    verbose = input[7]
    pval_threshold = input[8]
    export_carnival = input[9]
    output_file = output[0]
    # Building block invocation
    tf_enrichment(input_file=input_file,
                  output_file=output_file,
                  tsv=tsv,
                  weight_col=weight_col,
                  id_col=id_col,
                  minsize=minsize,
                  source=source,
                  confidence=confidence,
                  verbose=verbose,
                  pval_threshold=pval_threshold,
                  export_carnival=export_carnival)
