import sys, os
import maboss
import pandas as pd
import argparse
import shutil

DEFAULT_WORK_DIR = "/tmp"


parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument("bnd_file", type=str,
                    help="Output model bnd file")

parser.add_argument("cfg_file", type=str,
                    help="Output model cfg file")
                    
parser.add_argument("--list-genes", type=str,
                    help="Input as list of gene")
                    
parser.add_argument("--sif-file", type=str,
                    help="Input as a sif network file")

args = parser.parse_args()
args.bnd_file = os.path.realpath(args.bnd_file)
args.cfg_file = os.path.realpath(args.cfg_file)

if args.list_genes is not None:
    bnd_file = args.bnd_file
    cfg_file = args.cfg_file
    list_genes_file = os.path.realpath(args.list_genes)

    workdir=os.path.dirname(bnd_file)
    print("Workdir : " + workdir)
    os.makedirs(workdir, exist_ok=True)
    
    os.chdir(workdir)
    
    if os.path.exists(os.path.join(workdir, "cache")):
        shutil.rmtree(os.path.join(workdir, "cache"))
    
    shutil.copytree(
        "/opt/FromSpeciesToMaBoSSModel/cache", os.path.join(workdir, "cache")
    )
    
    from pypath.share import settings

    settings.setup(basedir=workdir) 
    settings.setup(cachedir=os.path.join(workdir, "cache"))
    settings.setup(log_verbosity=0)
    
    from pypath.legacy import main as legacy
    pw_legacy = legacy.PyPath()
    
    import pypath_functions as pf

    # source = ["signor"]
    pickle_file = "/opt/FromSpeciesToMaBoSSModel/network.pickle"
    graph = pf.load_network_from_pickle(pw_legacy, pickle_file)

    # Import a list of genes from a file
    genes = pd.read_csv(list_genes_file)
    gene_list = []
    for gene in genes.values:
        gene_list.append(str(gene[0]))


    # gene_dict = pf.generate_dict(gene_list, pw_legacy)

    # We start by associating the uniprot IDs from a gene list

    sources = gene_list
    uniprot_dict = pf.generate_dict(sources,pw_legacy)
    # The subgraph is built

    subg1 = graph.induced_subgraph([pw_legacy.vs.find(name = uniprot_dict[e]) for e in uniprot_dict.keys()])

    # According to the depth f search (distance between two nodes), we can search in the databases all the possible paths of length==depth 
    # and add all the nodes found in the graph (this can take some time depending on the depth)

    connected_dict = pf.complete_connection(subg1, uniprot_dict, 2, pw_legacy)
    subg2 = graph.induced_subgraph([pw_legacy.vs.find(name = connected_dict[e]) for e in connected_dict.keys()])


    pf.write_bnet(subg2, connected_dict, name=os.path.join(workdir, "model.bnet"))

    model = maboss.loadBNet(os.path.join(workdir, "model.bnet"))
    for node in model.network:
        model.network[node].set_rate("$u_" + str(node), "$d_" + str(node))
        model.update_parameters(**{"$u_" + str(node): 1.0, "$d_" + str(node): 1.0})

    with open(bnd_file, "w") as bnd_file:
        model.print_bnd(bnd_file)
        
    with open(cfg_file, "w") as cfg_file:
        model.print_cfg(cfg_file)
        
    shutil.rmtree(os.path.join(workdir, "cache"))
    shutil.rmtree(os.path.join(workdir, "pypath_log"))

elif args.sif_file is not None:
    
#     elif sif_file is not None:
    bnd_file = args.bnd_file
    cfg_file = args.cfg_file
    sif_file = os.path.realpath(args.sif_file)
    workdir=os.path.dirname(bnd_file)
    print("Workdir : " + workdir)

    from functions import write_bnet_from_sif
    write_bnet_from_sif(sif_file,name=os.path.join(workdir, "model.bnet"))

    model = maboss.loadBNet(os.path.join(workdir, "model.bnet"))
    for node in model.network:
        model.network[node].set_rate("$u_" + str(node), "$d_" + str(node))
        model.update_parameters(**{"$u_" + str(node): 1.0, "$d_" + str(node): 1.0})
        
    with open(bnd_file, "w") as bnd_file:
        model.print_bnd(bnd_file)
        
    with open(cfg_file, "w") as cfg_file:
        model.print_cfg(cfg_file)
        
    