import os, sys, argparse, csv
import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as shc
import seaborn as sns

parser = argparse.ArgumentParser(description='Process input')
parser.add_argument('-m', '--meta_file', type=str, default=None, help='Choose which results to analyse')
parser.add_argument('-o', '--out_dir', type=str, default=None, help='Inform how many replicated where done')
parser.add_argument('-p', '--model_prefix', type=str, default=None, help='Number of cores to use for analysing results')
parser.add_argument('-k', '--ko_file', type=str, default=None, help="Default dir format for PhysiCell replicates")
parser.add_argument('-r', '--repetitions', type=int, default=1, help="Number of replicates")
parser.add_argument('-v', '--verbose', type=bool, default=False, help="Verbosity")
parser.add_argument('-z', '--result', type=str, default=None, help="result directory")

args = parser.parse_args()

patients = []
with open(args.meta_file, 'r') as metadata_fd:
    reader = csv.DictReader(metadata_fd, delimiter="\t")
    for line in reader:
        patients.append(line["id"])

genes = [""]
with open(args.ko_file, 'r') as kofile_fd:
    for line in kofile_fd.readlines():
        genes.append("_%s_ko_" % line.strip())
        
a = sio.loadmat(os.path.join(args.out_dir, patients[0], "physiboss_replicates_analysis", "%s_personalized_%sresults" % (args.model_prefix, genes[0]), "timeReplicate.mat"))
max_timesteps = a['timedata'].shape[2]

start_timestep = max_timesteps-10
max_timestep = max_timesteps

epi_results = np.zeros((len(genes)*len(patients), max_timestep-start_timestep))
mac_results = np.zeros((len(genes)*len(patients), max_timestep-start_timestep))
cd8_results = np.zeros((len(genes)*len(patients), max_timestep-start_timestep))
epi_traces = np.zeros((len(genes)*len(patients)*args.repetitions, max_timestep-start_timestep))
cd8_traces = np.zeros((len(genes)*len(patients)*args.repetitions, max_timestep-start_timestep))

for i_patient, patient in enumerate(patients):
    patient_path = os.path.join(args.out_dir, patient)
    patient_data_path = os.path.join(patient_path, "physiboss_replicates_analysis")
    
    for i_gene, gene in enumerate(genes):
        gene_path = os.path.join(patient_data_path, "%s_personalized_%sresults" % (args.model_prefix, gene))
        
        a = sio.loadmat(os.path.join(gene_path, 'timeReplicate.mat'))
        cells = a['timedata']
        b = sio.loadmat(os.path.join(gene_path, 'timeTraces.mat'))
        cellsb = b['tracedata']
        epi_results[i_patient*len(genes)+i_gene, :] = cells[0, 16, start_timestep:max_timestep]
        mac_results[i_patient*len(genes)+i_gene, :] = np.sum(cells[0, 1:5, start_timestep:max_timestep], axis=0)
        cd8_results[i_patient*len(genes)+i_gene, :] = cells[0, 0, start_timestep:max_timestep]
        ind_start = i_patient*len(genes)*args.repetitions + i_gene*args.repetitions
        epi_traces[ind_start:ind_start+args.repetitions, :] = cellsb[:,start_timestep:max_timestep,16]
        cd8_traces[ind_start:ind_start+args.repetitions, :] = cellsb[:,start_timestep:max_timestep,0]
        
        t = np.linspace(0, 12, max_timesteps)
        
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(t,  np.transpose(cellsb[:,:,16]), color = 'C0', linewidth=1, alpha=0.35)  
        fig.savefig(os.path.join(args.result, 'epithelials_traces_%s%s.png' % (patient, gene)), dpi=600, pad_inches=0.1, bbox_inches='tight')  # dpi=600,
        plt.close()
        
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(t,  np.transpose(cellsb[:,:,0]), color = 'C0', linewidth=1, alpha=0.35)  
        fig.savefig(os.path.join(args.result, 'cd8_traces_%s%s.png' % (patient, gene)), dpi=600, pad_inches=0.1, bbox_inches='tight')  # dpi=600,
        plt.close()
        
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(t, cells[0, 16, :])
        fig.savefig(os.path.join(args.result, 'epithelials_%s%s.png' % (patient, gene)), dpi=600, pad_inches=0.1, bbox_inches='tight')  # dpi=600,
        plt.close()
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(t, np.sum(cells[0, 1:5, :], axis=0))
        fig.savefig(os.path.join(args.result, 'macrophages_%s%s.png' % (patient, gene)), dpi=600, pad_inches=0.1, bbox_inches='tight')  # dpi=600,
        plt.close()
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(t, cells[0, 0, :])
        fig.savefig(os.path.join(args.result, 'cd8s_%s%s.png' % (patient, gene)), dpi=600, pad_inches=0.1, bbox_inches='tight')  # dpi=600,
        plt.close()
        
columns = ["epi_%d" % index for index in range(max_timestep-start_timestep)]
columns += ["mac_%d" % index for index in range(max_timestep-start_timestep)]
columns += ["cd8_%d" % index for index in range(max_timestep-start_timestep)]
rows = ["%s%s" % (patient, gene[:-1]) for patient in patients for gene in genes]

results = np.concatenate([epi_results, mac_results, cd8_results], axis=1)
df = pd.DataFrame(results, index=rows, columns=columns)

columns_traces = ["epi_%d" % index for index in range(max_timestep-start_timestep)]
columns_traces += ["cd8_%d" % index for index in range(max_timestep-start_timestep)]
rows_traces = ["%s%s_%s" % (patient, gene[:-1], i_rep) for patient in patients for gene in genes for i_rep in range(args.repetitions)]
results_traces = np.concatenate([epi_traces, cd8_traces], axis=1)
df_traces = pd.DataFrame(results_traces, index=rows_traces, columns=columns_traces)

results_patients = np.zeros((len(patients), (max_timestep-start_timestep)*3))
for i, patient in enumerate(patients):
    results_patients[i, :] = np.mean(results[i*len(patients):i*len(patients)+2, :], axis=0)

df_patients = pd.DataFrame(results_patients, index=patients, columns=columns)

results_genes = np.zeros((len(genes), (max_timestep-start_timestep)*3))
for i, gene in enumerate(genes):
    indices = [j*len(patients)+i for j, _ in enumerate(patients)]
    results_genes[i, :] = np.mean(results[indices, :], axis=0)

df_genes = pd.DataFrame(results_genes, index=genes, columns=columns)



cmap="vlag"
# cmap="mako"
## Figures - Per patient
fig, ax = plt.subplots(figsize=(10, 7))
selected_data = df_patients
clusters = shc.linkage(selected_data, 
            method='ward', 
            metric="euclidean")
shc.dendrogram(Z=clusters, labels=patients, ax=ax)
ax.tick_params(axis='x', which='major', labelsize=5)
plt.savefig(os.path.join(args.result, "dendogram_patients.png"), dpi=600, pad_inches=0.1, bbox_inches='tight')


fig, ax = plt.subplots(figsize=(10, 7))
sns_plot = sns.clustermap(selected_data, cmap=cmap, col_cluster=False)
fig_sns = sns_plot._figure
fig_sns.savefig(os.path.join(args.result, "clustermap_patients.png"), dpi=600, pad_inches=0.1, bbox_inches='tight')


## Figures - Per genes
fig, ax = plt.subplots(figsize=(10, 7))
selected_data = df_genes
clusters = shc.linkage(selected_data, 
            method='ward', 
            metric="euclidean")
shc.dendrogram(Z=clusters, labels=genes, ax=ax)
ax.tick_params(axis='x', which='major', labelsize=5)
plt.savefig(os.path.join(args.result, "dendogram_genes.png"), dpi=600, pad_inches=0.1, bbox_inches='tight')


fig, ax = plt.subplots(figsize=(10, 7))
sns_plot = sns.clustermap(selected_data, cmap=cmap, col_cluster=False)
fig_sns = sns_plot._figure
fig_sns.savefig(os.path.join(args.result, "clustermap_genes.png"), dpi=600, pad_inches=0.1, bbox_inches='tight')


## Figures - Per patient & Condition
fig, ax = plt.subplots(figsize=(10, 7))
selected_data = df
clusters = shc.linkage(selected_data, 
            method='ward', 
            metric="euclidean")
shc.dendrogram(Z=clusters, labels=rows, ax=ax)
ax.tick_params(axis='x', which='major', labelsize=5)
plt.savefig(os.path.join(args.result, "dendogram.png"), dpi=600, pad_inches=0.1, bbox_inches='tight')

fig, ax = plt.subplots(figsize=(10, 7))
sns_plot = sns.clustermap(selected_data, cmap=cmap, col_cluster=False)
fig_sns = sns_plot._figure
fig_sns.savefig(os.path.join(args.result, "clustermap.png"), dpi=600, pad_inches=0.1, bbox_inches='tight')


## Figures - Per patient & Condition & Replicate
fig, ax = plt.subplots(figsize=(10, 7))
selected_data = df_traces
clusters = shc.linkage(selected_data, 
            method='ward', 
            metric="euclidean")
shc.dendrogram(Z=clusters, labels=rows_traces, ax=ax)
ax.tick_params(axis='x', which='major', labelsize=5)
plt.savefig(os.path.join(args.result, "dendogram_traces.png"), dpi=600, pad_inches=0.1, bbox_inches='tight')


fig, ax = plt.subplots(figsize=(10, 7))
sns_plot = sns.clustermap(selected_data, cmap=cmap, col_cluster=False)
fig_sns = sns_plot._figure
fig_sns.savefig(os.path.join(args.result, "clustermap_traces.png"), dpi=600, pad_inches=0.1, bbox_inches='tight')
