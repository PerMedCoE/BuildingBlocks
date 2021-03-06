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
    input_dir = input[0]
    feature_file = input[1]
    merge_csv_file = input[2]
    merge_csv_index = input[3]
    merge_csv_prefix = input[4]
    output_file = output[0]
    # Building block invocation
    feature_merger(input_dir=input_dir,
                   output_file=output_file,
                   feature_file=feature_file,
                   merge_csv_file=merge_csv_file,
                   merge_csv_index=merge_csv_index,
                   merge_csv_prefix=merge_csv_prefix)
