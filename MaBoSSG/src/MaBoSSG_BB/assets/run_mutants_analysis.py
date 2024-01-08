import sys, argparse, os, json, subprocess

import maboss

print("Mutant analysis with MaBoSSG")

parser = argparse.ArgumentParser(description="Process some integers.")
# parser.add_argument("path_models", type=str,
#                     help="Input list of genes (.csv)")

parser.add_argument("list_druggable", type=str,
                    help="File with list of druggable nodes")

parser.add_argument("nodes_quantify", type=str,
                    help="File with list of nodes to quantify")

parser.add_argument("json_file", type=str,
                    help="JSON file for settings of MaBoSSG")

parser.add_argument("results_file", type=str,
                    help="Path of the results file")

parser.add_argument("--mode", type=str, default="double", required=False,
                    help="Should we run single or double mutants")

args = parser.parse_args()
# args.path_models = os.path.realpath(args.path_models)
args.list_druggable = os.path.realpath(args.list_druggable)
args.nodes_quantify = os.path.realpath(args.nodes_quantify)
args.json_file = os.path.realpath(args.json_file)
args.results_file = os.path.realpath(args.results_file)


def run_mabossg(settings):
    
    with open(os.path.join(os.path.dirname(args.json_file), "settings_run.json"), "w") as json_modified:
        json.dump(settings, json_modified)
        
    res_run = subprocess.Popen("./build/MaBoSSG -o res %s" % os.path.join(os.path.dirname(args.json_file), "settings_run.json"), stdout=subprocess.PIPE, shell=True)
    out, err = res_run.communicate()
    if err is not None:
        print(err, file=sys.stderr)
    
    if res_run.returncode != 0:
        exit(res_run.returncode)
        
    return maboss.results.StoredResult(".")


nodes_quantify = []
with open(args.nodes_quantify, 'r') as f_nodes:
    nodes_quantify = [name.strip() for name in f_nodes.readlines()]

list_nodes = []
with open(args.list_druggable, 'r') as f_nodes:
    list_nodes = [name.strip() for name in f_nodes.readlines()]


list_single_mutants = [(node, "ON") for node in list_nodes]
list_single_mutants += [(node, "OFF") for node in list_nodes]
list_double_mutants = [(a, b) for idx, a in enumerate(list_single_mutants) for b in list_single_mutants[idx + 1:] if a[0] != b[0]]

res_simple = {}
for double_mutant in list_double_mutants:
    settings = {}
    with open(args.json_file, 'r') as json_file:
        settings = json.load(json_file)
    
    for mutant in double_mutant:
        if mutant[1] == "ON":
            settings["variables"]["High_%s" % mutant[0]] = 1
        elif mutant[1] == "OFF":
            settings["variables"]["Low_%s" % mutant[0]] = 1
    
    settings["variables"]["nb_mutable"] = 2
            
    res = run_mabossg(settings)    
    
    t_probtraj = res.get_last_nodes_probtraj()
    t_values = { node : (t_probtraj[node].values[0] if node in t_probtraj.columns else 0.0)for node in nodes_quantify}

    id = double_mutant[0][0] + ("++" if double_mutant[0][1] == "ON" else "--")
    id += "," + double_mutant[1][0] + ("++" if double_mutant[1][1] == "ON" else "--")

    res_simple.update({id:t_values})
    
with open(args.results_file, "w") as t_file:
    t_file.write(json.dumps(res_simple))
