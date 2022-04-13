import os

from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_IN
from permedcoe import FILE_OUT
from permedcoe import DIRECTORY_IN
from permedcoe import DIRECTORY_OUT

# Import single container and assets definitions
from print_drug_results_BB.definitions import PRINT_DRUG_RESULTS_CONTAINER
from print_drug_results_BB.definitions import PRINT_DRUG_RESULTS_ASSETS_PATH
from print_drug_results_BB.definitions import COMPUTING_UNITS

try:
    from pycompss.api.parameter import COLLECTION_IN
except ImportError:
    COLLECTION_IN = None

# Globals
PRINT_DRUG_RESULTS_BINARY = os.path.join(PRINT_DRUG_RESULTS_ASSETS_PATH,
                                         "print_result_drugs.sh")

############################################
###### Parallelized code for PyCOMPSs ######
############################################

def print_drug_results_parallelized(cell_lines, result_files, report_folder):
    """
    Python code that processes the drug results and implements an inner
    PyCOMPSs worflow.
    """
    print("Cell lines: " + str(cell_lines))
    results = []
    mutants = []
    targets = []
    for result_path in result_files:
        result = read_result_file(result_path)
        results.append(result)  # avoid reading twice
        mutant, target = get_mutant_target(result)
        mutants.append(mutant)
        targets.append(target)
    merged_mutants = merge_reduce(merge_mutants, mutants)
    merged_targets = merge_reduce(merge_targets, targets)

    dfs = create_dfs(merged_mutants, merged_targets, cell_lines, results)

    print_results(dfs, report_folder)


def merge_reduce(f, data):
    """ Apply function cumulatively to the items of data,
    from left to right in binary tree structure, so as to
    reduce the data to a single value.

    :param f: function to apply to reduce data
    :param data: List of items to be reduced
    :return: result of reduce the data to a single value
    """
    from collections import deque
    q = deque(range(len(data)))
    while len(q):
        x = q.popleft()
        if len(q):
            y = q.popleft()
            data[x] = f(data[x], data[y])
            q.append(x)
        else:
            return data[x]

@container(engine="SINGULARITY", image=PRINT_DRUG_RESULTS_CONTAINER)
@task(returns=1)
def merge_mutants(mutant_a, mutant_b):
    return mutant_a.union(mutant_b)

@container(engine="SINGULARITY", image=PRINT_DRUG_RESULTS_CONTAINER)
@task(returns=1)
def merge_targets(target_a, target_b):
    return target_a.union(target_b)

@container(engine="SINGULARITY", image=PRINT_DRUG_RESULTS_CONTAINER)
@task(result_path=FILE_IN, returns=1)
def read_result_file(result_path):
    import json
    with open(result_path, 'r') as result_file:
        result = json.load(result_file)
    return result

@container(engine="SINGULARITY", image=PRINT_DRUG_RESULTS_CONTAINER)
@task(returns=2)
def get_mutant_target(result):
    mutant = set(list(result.keys()))
    target = set(list(list(result.values())[0].keys()))
    return mutant, target

@container(engine="SINGULARITY", image=PRINT_DRUG_RESULTS_CONTAINER)
@task(returns=1, results=COLLECTION_IN)
def create_dfs(mutants, targets, cell_lines, results):
    import numpy, pandas
    dfs = {}
    for target in targets:
        dfs.update({
            target: pandas.DataFrame(
                numpy.zeros((len(list(mutants)),
                             len(list(cell_lines)))),
                list(mutants),
                list(cell_lines)
            )
        })
    position = 0
    for result in results:
        for mutant, mutant_val in result.items():
            for gene, gene_val in mutant_val.items():
                dfs[gene].loc[mutant, cell_lines[position]] = gene_val
        position += 1
    return dfs

@container(engine="SINGULARITY", image=PRINT_DRUG_RESULTS_CONTAINER)
@task(report_folder=DIRECTORY_OUT)
def print_results(dfs, report_folder):
    import seaborn
    import matplotlib.pyplot as plt

    # Create report folder if not exists
    if not os.path.exists(report_folder):
        os.makedirs(report_folder, exist_ok=True)

    for target, df in dfs.items():
        plt.figure(figsize=(10,5),dpi=100)
        ax = plt.axes()
        seaborn.heatmap(df, ax = ax, annot=True)

        ax.set_title(target)
        plt.subplots_adjust(left=0.3)
        plt.savefig(os.path.join(report_folder, (target + ".png")))

        df.to_csv(os.path.join(report_folder, (target + ".csv")))


#######################################
###### Using directly the binary ######
#######################################

@container(engine="SINGULARITY", image=PRINT_DRUG_RESULTS_CONTAINER)
@binary(binary=PRINT_DRUG_RESULTS_BINARY)
@task(drug_results_folder=DIRECTORY_IN, reports_folder=DIRECTORY_OUT)
def print_drug_results(drug_results_folder=None, reports_folder=None):
    """

    """
    # Empty function since it represents a binary execution:
    #    PRINT_DRUG_RESULTS_BINARY <drug_results_folder> <reports_folder>
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
    results_folder = input[0]
    reports_folder = output[0]
    # Building block invocation
    print_drug_results(
        drug_results_folder=results_folder,
        reports_folder=reports_folder
    )
