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

parser.add_argument("--list-genes", "-list-genes", type=str,
                    help="Input as list of gene")

parser.add_argument("--sif-file", "-sif-file", type=str,
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

    if os.path.exists(os.path.join(workdir, "pickles")):
        shutil.rmtree(os.path.join(workdir, "pickles"))

    shutil.copytree(
        "/opt/FromSpeciesToMaBoSSModel/pickles", os.path.join(workdir, "pickles")
    )

    from pypath.share import settings

    settings.setup(basedir=workdir) 
    settings.setup(cachedir=os.path.join(workdir, "cache"))
    settings.setup(pickle_dir=os.path.join(workdir, "pickles"))
    settings.setup(log_verbosity=0)

    from pypath import omnipath
    from pypath_wrapper import Wrap_net
    m = omnipath.db.pickle_path('network')
    w = Wrap_net(m)
    
    # Import a list of genes from a file
    genes = pd.read_csv(list_genes_file)
    gene_list = []
    for gene in genes.values:
        gene_list.append(str(gene[0]))

    distance = 2
    net = w.extract_subnet(gene_list, distance, complete_connections=True)
    
    net.write_bnet(file_name=os.path.join(workdir, "model.bnet"))
    
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
