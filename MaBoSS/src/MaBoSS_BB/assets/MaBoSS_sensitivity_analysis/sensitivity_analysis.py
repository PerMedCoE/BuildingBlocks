import sys, argparse, os, json

import maboss

print("Mutant analysis with MaBoSS")

parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument("path_models", type=str,
                    help="Input list of genes (.csv)")


parser.add_argument("list_druggable", type=str,
                    help="File with list of druggable nodes")

parser.add_argument("nodes_quantify", type=str,
                    help="File with list of nodes to quantify")

parser.add_argument("results_file", type=str,
                    help="RNASeq data for personalization")

parser.add_argument("--mode", type=str, default="double", required=False,
                    help="RNASeq data for personalization")


args = parser.parse_args()
args.path_models = os.path.realpath(args.path_models)
args.list_druggable = os.path.realpath(args.list_druggable)
args.nodes_quantify = os.path.realpath(args.nodes_quantify)
args.results_file = os.path.realpath(args.results_file)

print("Model path : %s" % args.path_models)

model_bnd_path = os.path.join(args.path_models, "model.bnd")
model_cfg_path = os.path.join(args.path_models, "model.cfg")

model = maboss.load(model_bnd_path, model_cfg_path)


list_nodes = ["KRT20", "MAPKAPK2", "CRK", "NOTCH3"]

with open(args.list_druggable, 'r') as f_druggable:
    list_nodes = [name.strip() for name in f_druggable.readlines()]

nodes_quantify = ["CDK1", "CASP3"]
with open(args.nodes_quantify, 'r') as f_nodes:
    nodes_quantify = [name.strip() for name in f_nodes.readlines()]

res_simple = {}

model.network.set_output(nodes_quantify)

if args.mode == "single":
    list_single_mutants = [(node, "ON") for node in list_nodes]
    list_single_mutants += [(node, "OFF") for node in list_nodes]


    for i, single_mutant in enumerate(list_single_mutants):
        t_model = model.copy()
        t_model.mutate(*single_mutant)
        t_res = t_model.run(cmaboss=True)
        t_probtraj = t_res.get_last_nodes_probtraj()

        t_values = { node : t_probtraj[node].values[0] for node in nodes_quantify}


        res_simple.update({(single_mutant[0] + ("++" if single_mutant[1] == "ON" else "--")): t_values})

        print("Simulation %d/%d done" % (i, len(list_single_mutants)))


elif args.mode == "double":

    list_single_mutants = [(node, "ON") for node in list_nodes]
    list_single_mutants += [(node, "OFF") for node in list_nodes]

    list_double_mutants = [(a, b) for idx, a in enumerate(list_single_mutants) for b in list_single_mutants[idx + 1:] if a[0] != b[0]]

    for i, double_mutant in enumerate(list_double_mutants):
        t_model = model.copy()
        t_model.mutate(*(double_mutant[0]))
        t_model.mutate(*(double_mutant[1]))
        t_res = t_model.run(cmaboss=True)
        t_probtraj = t_res.get_last_nodes_probtraj()

        t_values = { node : t_probtraj[node].values[0] for node in nodes_quantify}

        print(double_mutant)
        id = double_mutant[0][0] + ("++" if double_mutant[0][1] == "ON" else "--")
        id += "," + double_mutant[1][0] + ("++" if double_mutant[1][1] == "ON" else "--")

        res_simple.update({id:t_values})

        print("Simulation %d/%d done" % (i, len(list_double_mutants)))


print(res_simple)
with open(args.results_file, "w") as t_file:
    t_file.write(json.dumps(res_simple))
