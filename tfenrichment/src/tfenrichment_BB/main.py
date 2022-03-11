import os

from permedcoe import constraint
from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_IN
from permedcoe import FILE_OUT

# Import container definition
from tfenrichment_BB.definitions import TFENRICHMENT_CONTAINER
from tfenrichment_BB.definitions import COMPUTING_UNITS


@constraint(computing_units=COMPUTING_UNITS)
@container(engine="SINGULARITY", image=TFENRICHMENT_CONTAINER)
@binary(binary="Rscript --vanilla /opt/tf_enrichment.R")
@task(input_file=FILE_IN, output_file=FILE_OUT)
def tf_enrichment(input_file=None, output_file=None,
                  weight_col_flag='-w', weight_col=None,
                  source_flag='-s', source=None,
                  id_col_flag='-i', id_col=None,
                  tsv_flag='-t', tsv=None,
                  minsize_flag='-m', minsize=None,
                  confidence_flag='-c', confidence=None,
                  verbose_flag='-v', verbose=None):
    """
    Runs TF Enrichment

    The Definition is equal to:
        Rscript --vanilla /opt/tf_enrichment.R <input_file> <output_file>
                                               <weight_col_flag> <weight_col>
                                               <source_flag> <source>
                                               <id_col_flag> <id_col>
                                               <tsv_flag> <tsv>
                                               <minsize_flag> <minsize>
                                               <confidence_flag> <confidence>
                                               <verbose_flag> <verbose>
    By default:
        Rscript --vanilla /opt/tf_enrichment.R <input_file> <output_file>
                                               -w <weight_col>
                                               -s <source>
                                               -i <id_col>
                                               -t <tsv>
                                               -m <minsize>
                                               -c <confidence>
                                               -v <verbose>
    """
    # Empty function since it represents a binary execution:
    pass


def invoke(input, output, config):
    """ Common interface.

    Example:
        tfenrichment -i gex.csv DATA.906826 GENE_SYMBOLS tf FALSE 10 'A,B,C' TRUE -o 906826_tf.csv

    Args:
        input (list): List containing the model and data folder.
        output (list): list containing the output directory path.
        config (dict): Configuration dictionary (not used).
    Returns:
        None
    """
    # Process parameters
    input_file = input[0]
    weight_col = input[1]
    source = input[2]
    id_col = input[3]
    tsv = input[4]
    minsize = input[5]
    confidence = input[6]
    verbose = input[7]
    output_file = output[0]
    # Building block invokation
    tf_enrichment(input_file=input_file,
                  output_file=output_file,
                  weight_col=weight_col,
                  source=source,
                  id_col=id_col,
                  tsv=tsv,
                  minsize=minsize,
                  confidence=confidence,
                  verbose=verbose)
