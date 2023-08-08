import argparse, os, maboss, pandas

print("Mutant analysis with MaBoSS")

parser = argparse.ArgumentParser(description="Process input parameters.")
parser.add_argument("projectname", type=str,
                    help="Input list of genes (.csv)")

parser.add_argument("data_folder", type=str,
                    help="File with list of druggable nodes")

parser.add_argument("ko_file", type=str,
                    help="File with list of nodes to quantify")

parser.add_argument("parallel", type=int,
                    help="RNASeq data for personalization")

args = parser.parse_args()
args.data_folder = os.path.realpath(args.data_folder)
args.ko_file = os.path.realpath(args.ko_file)

inputs = []
with open(os.path.join(args.data_folder, "inputs.txt"), "r") as inputs_file:
    inputs = [input.strip() for input in inputs_file.readlines()]

outputs = []
with open(os.path.join(args.data_folder, "outputs.txt"), "r") as outputs_file:
    outputs = [output.strip() for output in outputs_file.readlines()]

model_bnd_path = os.path.join(args.data_folder, "%s.bnd" % args.projectname)
model_cfg_path = os.path.join(args.data_folder, "%s.cfg" % args.projectname)

model = maboss.load(model_bnd_path, model_cfg_path)

intermediary_nodes = set(list(model.network.keys())).difference(set(inputs)).difference(set(outputs))

res_simple = {}

nodes_quantify = ["Apoptosis_type_I", "Apoptosis_type_II"]

model.update_parameters(thread_count=args.parallel)

model.network.set_output(nodes_quantify)

# Analyzing for all possible inputs
for node in model.network.keys():
    model.network.set_istate(node, [0.5, 0.5])
    
list_single_mutants = [(node, "OFF") for node in intermediary_nodes]


for i, single_mutant in enumerate(list_single_mutants):
    t_model = model.copy()
    t_model.mutate(*single_mutant)
    t_res = t_model.run(cmaboss=True)
    t_probtraj = t_res.get_last_nodes_probtraj()

    t_values = { node : t_probtraj[node].values[0] for node in nodes_quantify}

    res_simple.update({(single_mutant[0]): t_values})

df = pandas.DataFrame.from_dict(res_simple,"index")

ko_nodes = []
for node_quantify in nodes_quantify:
    ko_nodes += list(df[df[node_quantify] ==df[node_quantify].min()].index)

with open(args.ko_file, "w") as t_file:
    t_file.write("\n".join(set(ko_nodes)))
