import os

from permedcoe import constraint
from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_IN
from permedcoe import FILE_OUT
from permedcoe import TMPDIR

# Import container definition
from tf_enrichment_BB.definitions import CONTAINER
from tf_enrichment_BB.definitions import ASSETS_PATH
from tf_enrichment_BB.definitions import COMPUTING_UNITS

# Globals
TF_ENRICHMENT_BINARY = os.path.join(ASSETS_PATH, "tf_enrichment.sh")


@constraint(computing_units=COMPUTING_UNITS)
@container(engine="SINGULARITY", image=CONTAINER)
@binary(binary=TF_ENRICHMENT_BINARY)
@task(input_file=FILE_IN, output_file=FILE_OUT)
def tf_enrichment(tmpdir=TMPDIR,
                  input_file=None, output_file=None,
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
        <tmpdir>
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
        <tmpdir>
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


def invoke(arguments, config):
    """ Common interface.

    Args:
        arguments (args): Building Block parsed arguments.
        config (dict): Configuration dictionary (not used).
    Returns:
        None
    """
    # Process parameters
    input_file = arguments.input_file
    tsv = arguments.tsv
    weight_col = arguments.weight_col
    id_col = arguments.id_col
    minsize = arguments.minsize
    source = arguments.source
    confidence = arguments.confidence
    verbose = arguments.verbose
    pval_threshold = arguments.pval_threshold
    export_carnival = arguments.export_carnival
    output_file = arguments.output_file
    tmpdir = arguments.tmpdir
    # Building block invocation
    tf_enrichment(tmpdir=tmpdir,
                  input_file=input_file,
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
