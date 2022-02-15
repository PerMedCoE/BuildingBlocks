
def write_bnet_from_sif(sif_file, name="logic_formula.bnet"):
    node_list = []
    interaction_list = []
    with open(sif_file, "r") as f:
        lines = f.readlines()
    for line in lines:
        sent = line.split()
        interaction_list.append(sent)
        node_list.append(sent[0])
        node_list.append(sent[2])

    node_list = list(dict.fromkeys(node_list))
    #print(node_list)

    with open(name, "w") as f:
        for node in node_list:
            formula_ON = []
            formula_OFF = []
            for interaction in interaction_list:
                #print(interaction)
                if interaction[2] == node:
                    if interaction[1] == "inhibit":
                        formula_OFF.append(interaction[0])
                    if interaction[1] == "activate":
                        formula_ON.append(interaction[0])
            formula = formula_ON + formula_OFF

            f.write(node + ",")
            offset = 16 - len(node)  # nice offset so the visualization is understandable
            f.write(" " * offset)
            if not formula:
                f.write(" ( ")
                f.write(node)
                f.write(" ) ")
                f.write("\n")
            if formula_ON:
                f.write(" ( ")
                f.write(" | ".join(formula_ON))  # writing the first parenthesis with all the positive interactions
                f.write(" ) ")
                if not formula_OFF:
                    f.write("\n")
            if formula_ON != [] and formula_OFF != []:
                f.write(" & ")
                f.write(" !( ")
                f.write(" | ".join(formula_OFF))  # writing the first parenthesis with all the positive interactions
                f.write(" ) ")
                f.write("\n")
            if formula_ON == [] and formula_OFF != []:
                f.write(" !( ")
                f.write(" | ".join(formula_OFF))  # writing the first parenthesis with all the positive interactions
                f.write(" ) ")
                f.write("\n")
     # good to go
    return