import pandas as pd
import numpy as np
import sys
import os
import utils

if len(sys.argv) < 2:
    print("Please specify name for the output folder")
    sys.exit(1)

if len(sys.argv) < 3:
    print("Please specify name for the output")
    sys.exit(1)

print("USING: ", sys.argv[1])

physi_output = sys.argv[1]
file_csv = sys.argv[2]

singles = []
doubles = []
for replicate in os.listdir(physi_output):
    
    if os.path.isdir(os.path.join(physi_output, replicate)):
    
        list_of_file = []

        for file in os.listdir(os.path.join(physi_output, replicate)):
            if file.startswith("final_net"):
                list_of_file.append(file)

        list_of_file.sort()
        list_of_file.remove(list_of_file[0])

        single = []
        double = []


        for file in list_of_file:
            path = os.path.join(physi_output, replicate,file)
            net_df = pd.read_csv(path)
            utils.split_col(net_df)

            I = utils.create_graph(net_df, ' neighID')
            comp_x = utils.count_component(I)[0]
            comp_y = utils.count_component(I)[1]

            single.append(comp_x)
            double.append(comp_y)

        singles.append(single)
        doubles.append(double)

avg_singles = []
avg_doubles = []
for i, _ in enumerate(singles[0]):
    avg_singles.append(sum([single[i] for single in singles])/len(singles))
    avg_doubles.append(sum([double[i] for double in doubles])/len(doubles))


data = {'single': avg_singles, 'cluster': avg_doubles}

df = pd.DataFrame(data)

df.to_csv(file_csv, index=True, header=True)

print("GENERATED: ", file_csv)
