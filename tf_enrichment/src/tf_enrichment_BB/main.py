import os

from permedcoe import Arguments
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


def arguments_info():
    """Arguments definition.

    Builds the arguments definition.

    Returns:
        Supported arguments.
    """
    arguments = Arguments()
    arguments.add_input(name="input_file",
                        type=str,
                        description="Input gene expression data. Genes should be normalized across samples",
                        check="file")
    arguments.add_input(name="tsv",
                        type=bool,
                        description="Import data as TSV instead of CSV (True | False)",
                        check=bool)
    arguments.add_input(name="weight_col",
                        type=str,
                        description="Name of the column containing differential expression values \
                                     (e.g t-statistic from DESeq2) between a control/treatment \
                                     condition for example, or just log-fold change.",
                        check=str)
    arguments.add_input(name="id_col",
                        type=str,
                        description="Name of the column for gene ids",
                        check=str)
    arguments.add_input(name="minsize",
                        type=int,
                        description="Minimum size for regulons (e.g. 10)",
                        check=int)
    arguments.add_input(name="source",
                        type=str,
                        description="Column with the TFs (e.g. tf)",
                        check=str)
    arguments.add_input(name="confidence",
                        type=str,
                        description="Level of confidence to be used for regulons. E.g.: A,B,C. (see https://saezlab.github.io/dorothea/ for documentation)",
                        check=str)
    arguments.add_input(name="verbose",
                        type=str,
                        description="Verbose output (True | False).",
                        check=str)
    arguments.add_input(name="pval_threshold",
                        type=float,
                        description="Filter out TFs with adj. p-val above the provided value",
                        check=float)
    arguments.add_input(name="export_carnival",
                        type=str,
                        description="Export a table with the results with two columns (id, value) only (for CARNIVAL)(TRUE/FALSE)",
                        check=str)
    arguments.add_output(name="output_file",
                         type=str,
                         description="Result csv file with estimated TF activities")
    return arguments
