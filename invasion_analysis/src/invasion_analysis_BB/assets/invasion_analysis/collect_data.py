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
print(physi_output)
print(file_csv)
singles = []
clusters = []
ratios = []
cells_in_cluster = []

for replicate in os.listdir(physi_output):
    
    if os.path.isdir(os.path.join(physi_output, replicate)):
    
        list_of_file = []

        for file in os.listdir(os.path.join(physi_output, replicate)):
            if file.startswith("final_net"):
                list_of_file.append(file)

        list_of_file.sort()
        list_of_file.remove(list_of_file[0])

        single = []
        cluster = []
        ratio = []
        cell_in_cluster = []

        for file in list_of_file:
            path = os.path.join(physi_output, replicate,file)
            net_df = pd.read_csv(path)
            utils.split_col(net_df)

            I = utils.create_graph(net_df, ' neighID')
            comp_x = utils.count_component(I)[0]
            comp_y = utils.count_component(I)[1]
            comp_z = utils.count_cell_in_cluster(I)[0]
            comp_w = utils.count_cell_in_cluster(I)[1]
            single.append(comp_x)
            cluster.append(comp_y)
            ratio.append(comp_z)
            cell_in_cluster.append(comp_w)
            
        singles.append(single)
        clusters.append(cluster)
        ratios.append(ratio)
        cells_in_cluster.append(cell_in_cluster)

avg_singles = []
avg_clusters = []
avg_ratios = []
avg_cells_in_cluster = []
std_singles = []
std_clusters = []
std_ratios = []
std_cells_in_cluster = []
for i, _ in enumerate(singles[0]):
    avg_singles.append(np.mean([single[i] for single in singles if i < len(single)]))
    avg_clusters.append(np.mean([cluster[i] for cluster in clusters if i < len(cluster)]))
    avg_ratios.append(np.mean([ratio[i] for ratio in ratios if i < len(ratio)]))
    avg_cells_in_cluster.append(np.mean([cell_in_cluster[i] for cell_in_cluster in cells_in_cluster if i < len(cell_in_cluster)]))
    std_singles.append(np.std([single[i] for single in singles if i < len(single)]))
    std_clusters.append(np.std([cluster[i] for cluster in clusters if i < len(cluster)]))
    std_ratios.append(np.std([ratio[i] for ratio in ratios  if i < len(ratio)]))
    std_cells_in_cluster.append(np.std([cell_in_cluster[i] for cell_in_cluster in cells_in_cluster if i < len(cell_in_cluster)]))


data = {
    'single': avg_singles, 'cluster': avg_clusters, 'ratio': avg_ratios, 'cells_in_cluster': avg_cells_in_cluster, 
    'error_single': std_singles, 'error_cluster': std_clusters, 'error_ratio': std_ratios, 'error_cells_in_cluster': std_cells_in_cluster }

df = pd.DataFrame(data)

df.to_csv(file_csv, index=True, header=True)

print("GENERATED: ", file_csv)
