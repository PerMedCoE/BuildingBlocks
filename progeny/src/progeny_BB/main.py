import os

from permedcoe import Arguments
from permedcoe import constraint
from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_IN
from permedcoe import FILE_OUT

# Import container definition
from progeny_BB.definitions import PROGENY_ASSETS_PATH
from progeny_BB.definitions import PROGENY_CONTAINER
from progeny_BB.definitions import COMPUTING_UNITS

# Globals
PROGENY_BINARY = os.path.join(PROGENY_ASSETS_PATH, "progeny.sh")


@constraint(computing_units=COMPUTING_UNITS)
@container(engine="SINGULARITY", image=PROGENY_CONTAINER)
@binary(binary=PROGENY_BINARY)
@task(input_file=FILE_IN, output_file=FILE_OUT)
def progeny(input_file=None, output_file=None,
            organism_flag='-o', organism=None,
            ntop_flag='-i', ntop=None,
            col_genes_flag='-c', col_genes=None,
            scale_flag='-s', scale=None,
            exclude_cols_flag='-e', exclude_cols=None,
            tsv_flag='-t', tsv=None,
            perms_flag='-p', perms=None,
            zscore_flag='-z', zscore=None,
            verbose_flag='-v', verbose=None):
    """
    Runs Carnival Gex Preprocess

    The Definition is equal to:
        Rscript --vanilla /opt/progeny.R <input_file> <output_file>
                                         <organism_flag> <organism>
                                         <ntop_flag> <ntop>
                                         <col_genes_flag> <col_genes>
                                         <scale_flag> <scale>
                                         <exclude_cols_flag> <exclude_cols>
                                         <tsv_flag> <tsv>
                                         <perms_flag> <perms>
                                         <zscore_flag> <zscore>
                                         <verbose_flag> <verbose>
    By default:
        Rscript --vanilla /opt/progeny.R <input_file> <output_file>
                                         -o <organism>
                                         -i <ntop>
                                         -c <col_genes>
                                         -s <scale>
                                         -e <exclude_cols>
                                         -t <tsv>
                                         -p <perms>
                                         -z <zscore>
                                         -v <verbose>
    """
    # Empty function since it represents a binary execution:
    pass


def invoke(arguments, config):
    """ Common interface.

    Example:
        progeny -i gex.csv Human 60 GENE_SYMBOLS TRUE GENE_title FALSE 3000 TRUE TRUE -o progeny11.csv

    Args:
        arguments (args): Building Block parsed arguments.
        config (dict): Configuration dictionary (not used).
    Returns:
        None
    """
    # Process parameters
    input_file = arguments.input_file
    organism = arguments.organism
    ntop = arguments.ntop
    col_genes = arguments.col_genes
    scale = arguments.scale
    exclude_cols = arguments.exclude_cols
    tsv = arguments.tsv
    perms = arguments.perms
    zscore = arguments.zscore
    verbose = arguments.verbose
    output_file = arguments.output_file
    # Building block invocation
    progeny(input_file=input_file,
            output_file=output_file,
            organism=organism,
            ntop=ntop,
            col_genes=col_genes,
            scale=scale,
            exclude_cols=exclude_cols,
            tsv=tsv,
            perms=perms,
            zscore=zscore,
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
                        description="CSV with gene expression data, where rows are genes and columns are samples",
                        check="file")
    arguments.add_input(name="organism",
                        type=str,
                        description="Human\/Mouse",
                        check=str)
    arguments.add_input(name="ntop",
                        type=int,
                        description="Number of top genes used to estimate pathway activities",
                        check=int)
    arguments.add_input(name="col_genes",
                        type=str,
                        description="Name of the column containing gene IDs",
                        check=str)
    arguments.add_input(name="scale",
                        type=bool,
                        description="Scale data (True | False)",
                        check=bool)
    arguments.add_input(name="exclude_cols",
                        type=str,
                        description="Columns containing this string will be removed",
                        check=str)
    arguments.add_input(name="tsv",
                        type=str,
                        description="Import input data as TSV",
                        check=str)
    arguments.add_input(name="perms",
                        type=int,
                        description="Number of permutations to estimate the null distribution. \
                                     For default usage of PROGENy, just pass 1 to skip this step",
                        check=int)
    arguments.add_input(name="zscore",
                        type=bool,
                        description="If True, the z-scores will be returned for the pathway \
                                     activity estimations. Else, the function returns a normalized \
                                     z-score value between -1 and 1",
                        check=bool)
    arguments.add_input(name="verbose",
                        type=str,
                        description="Verbose output (True | False)",
                        check=str)
    arguments.add_output(name="output_file",
                         type=str,
                         description="File with the results containing pathway activities")
    return arguments
