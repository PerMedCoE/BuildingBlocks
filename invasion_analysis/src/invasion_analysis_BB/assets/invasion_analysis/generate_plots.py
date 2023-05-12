# import utils
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import seaborn as sb
import sys

if len(sys.argv) < 2:
    print("Please specify name for the output")
    sys.exit(1)

print(sys.argv)
simulations_path = sys.argv[1]
parameters_file = sys.argv[2]
plots_directory = sys.argv[3]

print("Generating plots....")
print("- simulations path : %s" % simulations_path)
print("- parameters set : %s" % parameters_file)
print("- plots directory : %s" % plots_directory)




parameters_sets = []
with open(parameters_file, 'r') as psets:
    for line in psets.readlines():
        # print(line)
        raw_pset = line.split(",")
        # print(raw_pset)
        for value in raw_pset[1:]:
            parameters_sets.append((raw_pset[0].strip(), float(value.strip())))
    
parameters_data = {}

for i_set, parameter_set in enumerate(parameters_sets):
    
    parameter, value = parameter_set
    data_file = os.path.join(simulations_path, "parameter_%d" % i_set, "invasion_analysis", "data.csv")
    df = pd.read_csv(data_file)
    values = df.iloc[-1]
    if parameter not in parameters_data.keys():
        parameters_data[parameter] = {value: values}
    else:
        parameters_data[parameter].update({value: values})
    
for parameter in parameters_data.keys():
    df = pd.DataFrame(parameters_data[parameter])
    
        
    fig, ax = plt.subplots(1, figsize=(5,3), dpi=500)

    fields = ['single', 'cells_in_cluster']#, 'ratio']
    for field in fields:
        # ax.errorbar(df.columns, df.loc[field, :], df.loc['error_%s' % field],fmt='.', label=field)
        ax.errorbar(df.columns, df.loc[field, :], df.loc['error_%s' % field], alpha=.75, fmt=':', capsize=3, capthick=1)
        data = {
            'x': df.columns,
            'y1': [y - e for y, e in zip(df.loc[field, :], df.loc['error_%s' % field])],
            'y2': [y + e for y, e in zip(df.loc[field, :], df.loc['error_%s' % field])]}
        plt.fill_between(**data, alpha=.25)

    fig.legend(["Single cells", "Cells in clusters"])
    fig.savefig(os.path.join(plots_directory, "%s.png" % parameter))
    
    fig, ax = plt.subplots(1, figsize=(5,3), dpi=500)

    field = "ratio"
    ax.errorbar(df.columns, df.loc[field, :], df.loc['error_%s' % field], alpha=.75, fmt=':', capsize=3, capthick=1)
    data = {
        'x': df.columns,
        'y1': [y - e for y, e in zip(df.loc[field, :], df.loc['error_%s' % field])],
        'y2': [y + e for y, e in zip(df.loc[field, :], df.loc['error_%s' % field])]}
    plt.fill_between(**data, alpha=.25)

    fig.legend(["Single cells", "Cells in clusters"])
    fig.savefig(os.path.join(plots_directory, "%s_ratio.png" % parameter))
print("Done")