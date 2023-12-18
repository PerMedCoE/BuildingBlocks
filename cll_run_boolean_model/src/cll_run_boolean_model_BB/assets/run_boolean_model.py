#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 14:26:27 2023

@author: jose
"""
# import os
# os.chdir("/media/jose/secondary/projects/permedcoe/pmc_uc1_cll_clean/05_run_models/")

import maboss
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import optparse
import argparse
import os

if __name__ == '__main__':

    ## Read input parameters
    parser = argparse.ArgumentParser(prog='MaBoSS on CLL data')
    parser.add_argument('-s', '--sif', action='store', default=None, required=True)
    parser.add_argument('-b', '--bnd', action='store', default=None, required=True)
    parser.add_argument('-c', '--cfg', action='store', default=None, required=True)
    parser.add_argument('-i', '--id', action='store', default=None, required=False)
    parser.add_argument('-o', '--outdir', action='store', default=None, required=True)
    args = parser.parse_args()

    # For debugging
    # args = {}
    # args['sif'] = "results/boolean_models/inferred_network.sif"
    # args['bnd'] = "results/boolean_models/inferred_network.sif.bnd"
    # args['cfg'] = "results/boolean_models/group_profiles/inferred_network__MUT.sif.cfg"
    # args['id'] = "MUT"
    # args['outdir'] = "results/boolean_models/group_runs"
    # class Obj(object):
    #     def __init__(self, initial_data):
    #         for key in initial_data:
    #             setattr(self, key, initial_data[key])
    # args = Obj(args)

    if args.id is None:
        print("Sample ID not provided, inferring from cfg file")
        args.id = os.path.basename(args.cfg).replace("inferred_network__","").replace(".sif.cfg", "")

    # Load bnd and config
    master_simulation = maboss.load(args.bnd, args.cfg)

    # Define end nodes
    sif = pd.read_table(args.sif, delimiter="\t", header=None)
    sif.columns = ["source", "interaction", "target"]
    end_nodes = [x for x in sif.target.unique() if x not in sif.source.unique()]
    maboss.set_output(master_simulation, end_nodes)

    # Initialize parameters
    master_simulation.update_parameters(time_tick=0.1, max_time=10)

    # Running simulation
    # TO-FIX
    # when cmaboss==True then prefix is always "res"
    workdir = args.outdir
    master_results = master_simulation.run(workdir=workdir, overwrite=True, prefix="", cmaboss=False, only_final_state=False)

    # Save results
    master_results.get_last_nodes_probtraj().to_csv(workdir + "/last_node_probs.csv", index=False)

    master_results.get_nodes_probtraj().to_csv(workdir + "/node_probs.csv", index=True)

    # master_results.get_states_probtraj().to_csv(workdir + "/probtraj.csv", index=False)

    master_results.plot_trajectory(legend=True)
    plt.savefig(workdir + "/trajectories.png", bbox_inches="tight")

    master_results.plot_piechart(legend=True, embed_labels=False)
    plt.savefig(workdir + "/pie.png", bbox_inches="tight")

    master_results.plot_node_trajectory(legend=True, error=True)
    plt.savefig(workdir + "/node_trajectories.png", bbox_inches="tight")

    master_results.plot_entropy_trajectory()
    plt.savefig(workdir + "/entropy_trajectory.png", bbox_inches="tight")
