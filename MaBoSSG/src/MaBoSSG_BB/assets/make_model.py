import sys, argparse, os, json

import maboss

print("Mutant analysis with MaBoSSG")

parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument("path_models", type=str,
                    help="Input list of genes (.csv)")


parser.add_argument("list_druggable", type=str,
                    help="File with list of druggable nodes")


parser.add_argument("nodes_quantify", type=str,
                    help="File with list of nodes to quantify")

args = parser.parse_args()
args.path_models = os.path.realpath(args.path_models)
args.list_druggable = os.path.realpath(args.list_druggable)
args.nodes_quantify = os.path.realpath(args.nodes_quantify)

print("Model path : %s" % args.path_models)

model_bnd_path = os.path.join(args.path_models, "model.bnd")
model_cfg_path = os.path.join(args.path_models, "model.cfg")

model = maboss.load(model_bnd_path, model_cfg_path)

nodes_quantify = []
with open(args.nodes_quantify, 'r') as f_nodes:
    nodes_quantify = [name.strip() for name in f_nodes.readlines()]

model.network.set_output(nodes_quantify)

list_nodes = []
with open(args.list_druggable, 'r') as f_druggable:
    list_nodes = [name.strip() for name in f_druggable.readlines()]

for node in list_nodes:
    model.mutate(node, 'WT')
    
with open(os.path.join(args.path_models, "mutable_model.bnd"), "w") as mutable_bnd:
    model.print_bnd(out=mutable_bnd)
    
with open(os.path.join(args.path_models, "mutable_model.cfg"), "w") as mutable_cfg:
    model.print_cfg(out=mutable_cfg)

