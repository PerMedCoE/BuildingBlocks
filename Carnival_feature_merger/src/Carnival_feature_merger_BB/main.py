import os

from permedcoe import constraint
from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_OUT
from permedcoe import DIRECTORY_IN

# Import container definition
from Carnival_feature_merger_BB.definitions import CARNIVAL_FEATURE_MERGER_ASSETS_PATH
from Carnival_feature_merger_BB.definitions import CARNIVAL_FEATURE_MERGER_CONTAINER
from Carnival_feature_merger_BB.definitions import COMPUTING_UNITS

# Globals
CARNIVAL_FEATURE_MERGER_BINARY = os.path.join(CARNIVAL_FEATURE_MERGER_ASSETS_PATH, "carnival_feature_merger.sh")


@constraint(computing_units=COMPUTING_UNITS)
@container(engine="SINGULARITY", image=CARNIVAL_FEATURE_MERGER_CONTAINER)
@binary(binary=CARNIVAL_FEATURE_MERGER_BINARY)
@task(input_dir=DIRECTORY_IN, output_file=FILE_OUT)
def feature_merger(input_dir=None, output_file=None,
                   feature_file_flag='--feature_file', feature_file=None,
                   merge_csv_file_flag='--merge_csv_file', merge_csv_file=None,
                   merge_csv_index_flag='--merge_csv_index', merge_csv_index=None,
                   merge_csv_prefix_flag='--merge_csv_prefix', merge_csv_prefix=None):
    """
    Runs CarnivalPy

    The Definition is equal to:
        /opt/miniconda/bin/python /opt/feature_merge.py <input_dir> <output_file>
                                                        <feature_file_flag> <feature_file>
                                                        <merge_csv_file_flag> <merge_csv_file>
                                                        <merge_csv_index_flag> <merge_csv_index>
                                                        <merge_csv_prefix_flag> <merge_csv_prefix>
    By default:
        /opt/miniconda/bin/python /opt/feature_merge.py <input_dir> <output_file>
                                                        --feature_file <feature_file>
                                                        --merge_csv_file <merge_csv_file>
                                                        --merge_csv_index <merge_csv_index>
                                                        --merge_csv_prefix <merge_csv_prefix>
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
    input_dir = arguments.input_dir
    feature_file = arguments.feature_file
    merge_csv_file = arguments.merge_csv_file
    merge_csv_index = arguments.merge_csv_index
    merge_csv_prefix = arguments.merge_csv_prefix
    output_file = arguments.output_file
    # Building block invocation
    feature_merger(input_dir=input_dir,
                   output_file=output_file,
                   feature_file=feature_file,
                   merge_csv_file=merge_csv_file,
                   merge_csv_index=merge_csv_index,
                   merge_csv_prefix=merge_csv_prefix)
