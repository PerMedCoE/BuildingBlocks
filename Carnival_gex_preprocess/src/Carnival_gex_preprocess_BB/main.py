import os

from permedcoe import Arguments
from permedcoe import constraint
from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_IN
from permedcoe import FILE_OUT

# Import container definition
from Carnival_gex_preprocess_BB.definitions import CARNIVAL_GEX_PREPROCESS_ASSETS_PATH
from Carnival_gex_preprocess_BB.definitions import CARNIVAL_GEX_PREPROCESS_CONTAINER
from Carnival_gex_preprocess_BB.definitions import COMPUTING_UNITS

# Globals
CARNIVAL_GEX_PREPROCESS_BINARY = os.path.join(CARNIVAL_GEX_PREPROCESS_ASSETS_PATH,
                                              "carnival_gex_preprocess.sh")


@constraint(computing_units=COMPUTING_UNITS)
@container(engine="SINGULARITY", image=CARNIVAL_GEX_PREPROCESS_CONTAINER)
@binary(binary=CARNIVAL_GEX_PREPROCESS_BINARY)
@task(input_file=FILE_IN, output_file=FILE_OUT)
def preprocess(input_file=None, output_file=None,
               col_genes_flag='-c', col_genes=None,
               scale_flag='-s', scale=None,
               exclude_cols_flag='-e', exclude_cols=None,
               tsv_flag='-t', tsv=None,
               remove_flag='-r', remove=None,
               verbose_flag='-v', verbose=None):
    """
    Runs Carnival Gex Preprocess

    The Definition is equal to:
        Rscript --vanilla /opt/preprocess.R <input_file> <output_file>
                                            <col_genes_flag> <col_genes>
                                            <scale_flag> <scale>
                                            <exclude_cols_flag> <exclude_cols>
                                            <tsv_flag> <tsv>
                                            <remove_flag> <remove>
                                            <verbose_flag> <verbose>
    By default:
        Rscript --vanilla /opt/preprocess.R <input_file> <output_file>
                                            -c <col_genes>
                                            -s <scale>
                                            -e <exclude_cols>
                                            -t <tsv>
                                            -r <remove>
                                            -v <verbose>
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
    col_genes = arguments.col_genes
    scale = arguments.scale
    exclude_cols = arguments.exclude_cols
    tsv = arguments.tsv
    remove = arguments.remove
    verbose = arguments.verbose
    output_file = arguments.output_file
    # Building block invocation
    preprocess(input_file=input_file,
               output_file=output_file,
               col_genes=col_genes,
               scale=scale,
               exclude_cols=exclude_cols,
               tsv=tsv,
               remove=remove,
               verbose=verbose)


def arguments_info():
    """Arguments definition.

    Builds the arguments definition.

    Returns:
        Supported arguments.
    """
    arguments = Arguments()
    arguments.add_input(name="input_file",
                        type=str,
                        description="csv with the GDSC gene expression data",
                        check="file")
    arguments.add_input(name="col_genes",
                        type=str,
                        description="Name of the column containing the gene symbols (e.g. GENE_SYMBOLS)",
                        check=str)
    arguments.add_input(name="scale",
                        type=str,
                        description="Normalize genes across samples (True | False)",
                        check=str)
    arguments.add_input(name="exclude_cols",
                        type=str,
                        description="Exclude columns containing the given string (e.g. GENE_title)",
                        check=str)
    arguments.add_input(name="tsv",
                        type=str,
                        description="Import as TSV instead of CSV (True | False)",
                        check=str)
    arguments.add_input(name="remove",
                        type=str,
                        description="Remove the given substring from columns (e.g. .DATA)",
                        check=str)
    arguments.add_input(name="verbose",
                        type=str,
                        description="Verbose output (True | False)",
                        check=str)
    arguments.add_output(name="output_file",
                         type=str,
                         description="Processed csv file")
    return arguments
