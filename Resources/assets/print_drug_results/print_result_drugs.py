import sys, argparse, os, json, numpy, pandas, seaborn
import matplotlib.pyplot as plt

print("Final result analysis")

parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument("result_folder", type=str,
                    help="Input list of genes (.csv)")

parser.add_argument("report_folder", type=str,
                    help="File with list of druggable nodes")

args = parser.parse_args()
args.result_folder = os.path.realpath(args.result_folder)
args.report_folder = os.path.realpath(args.report_folder)

print("Results folder : " + args.result_folder)
print("Report folder : " + args.report_folder)

cell_lines = os.listdir(args.result_folder)

mutants = set()
targets = set()
for cell_line in cell_lines:
    result_path = os.path.join(args.result_folder, cell_line, "sensitivity.json")
    with open(result_path, 'r') as result_file:
        result = json.load(result_file)

    mutants = mutants.union(set(list(result.keys())))
    targets = targets.union(set(list(list(result.values())[0].keys())))

print("mutants: " + str(mutants))
print("targets: " + str(targets))

dfs = {}
for target in targets:
    dfs.update({
        target: pandas.DataFrame(
            numpy.zeros((len(list(mutants)), len(list(cell_lines)))),
            list(mutants), list(cell_lines)
        )
    })

print("dfs: " + str(dfs))
print(dfs.keys())

for cell_line in cell_lines:
    result_path = os.path.join(args.result_folder, cell_line, "sensitivity.json")
    with open(result_path, 'r') as result_file:
        result = json.load(result_file)

    for mutant, mutant_val in result.items():
        for gene, gene_val in mutant_val.items():
            dfs[gene].loc[mutant, cell_line] = gene_val

# Create report folder if not exists
if not os.path.exists(args.report_folder):
    os.makedirs(args.report_folder, exist_ok=True)

for target, df in dfs.items():
    plt.figure(figsize=(10,5),dpi=100)
    ax = plt.axes()
    seaborn.heatmap(df, ax = ax, annot=True)

    ax.set_title(target)
    plt.subplots_adjust(left=0.3)
    plt.savefig(os.path.join(args.report_folder, (target + ".png")))
    
    df.to_csv(os.path.join(args.report_folder, (target + ".csv")))

