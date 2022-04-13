import omnipath as op
from pypath.utils import mapping
import igraph
import itertools
import os


def generate_dict(gene_list, graph):
    gene_dict = {}
    for gene in gene_list:
        name1= list(mapping.map_name(gene, 'genesymbol', 'uniprot'))[0]
        name2 = list(mapping.map_name(name1, 'uniprot', 'genesymbol'))[0]
        if len(name1) != 0:
            try:
                graph.vs.find(name=name1)
                gene_dict[name2] = name1
            except:
                try:
                    name2 = list(mapping.map_name(gene, 'uniprot', 'genesymbol'))[0]
                    name1 = list(mapping.map_name(name2, 'genesymbol', 'uniprot'))[0]
                    graph.vs.find(name=name1)
                    gene_dict[name2] = name1
                except:
                    print(name1, " not present in the databases")
        else:
            print("Can't find genesymbol: ", name1, " try to look on genecards for other names")

    return gene_dict


# sometimes the function above is not working, here is an alternative using directly the omnipath database:

def get_code_from_annotations(gene_list):
    HPA_compare = op.requests.Annotations.get(
        proteins=gene_list,
        resources='HPA_tissue'
    )
    genes_code = HPA_compare.groupby(['uniprot', 'genesymbol']).size().reset_index()
    dict_gene_code = {}
    for i in range(len(genes_code.index)):
        # print(genes_code.at[i, 'uniprot'], genes_code.at[i, 'genesymbol'])
        dict_gene_code[genes_code.at[i, 'genesymbol']] = genes_code.at[i, 'uniprot']

    return dict_gene_code

def load_network_from_pickle(pw_legacy, pickle):
    path_to_pickle = os.path.isfile(pickle)
    if path_to_pickle == False:
        print("Path error: No pickle file found")
        return
    pw_legacy.init_network(pickle_file=pickle)
    return pw_legacy.graph

#the function below returns an average between the possible interections
#taken from the different databases
def get_consensus_edges(direction, gene_dict):
    a = direction.consensus_edges()
    code1 = a[0][0]
    code2 = a[0][1]
    for symbol, code in gene_dict.items():
        #print(code, code1)
        if code==code1:
            a[0][0] = symbol
    for symbol, code in gene_dict.items():
        if code==code2:
            a[0][1] = symbol
    return a

#it is possible to visualize the dataframe containing all the informations about each edge:

def show_edge_dataframe(graph, gene_dict):
    df = graph.get_edge_dataframe()
    df_vert = graph.get_vertex_dataframe()
    for gene in gene_dict.keys():
        df_vert = df_vert.replace(gene_dict[gene], gene)
    df['source'].replace(df_vert['name'], inplace=True)
    df['target'].replace(df_vert['name'], inplace=True)
    df_vert.set_index('name', inplace=True)  # Optional
    return df

#the following function is similar to complete_dict, but I am adding the interactions JUST for the node that are NOT already connected
def complete_connection(graph, gene_dict, depth, pw_legacy):
    list_genes = list(gene_dict.keys())
    for node in graph.vs:
        if node.degree() == 0: #select the node with degree == 0
            for node2 in graph.vs:
                if node2 == node: #loop again for all the other nodes but exclude the node already selected
                    continue
                else:
                    node_1 = pw_legacy.vs.find(label=node['label'])
                    node_2 = pw_legacy.vs.find(label=node2['label'])
                    for paths in pw_legacy.find_all_paths(node_1.index, node_2.index, mode='ALL',
                                                              maxlen=depth):  # do not use graph index, for each graph the indexes are different
                        #print(paths)
                        for i in range(1, len(paths) - 1):
                            if str(pw_legacy.vs[paths[i]]['name'])[:7] == "COMPLEX":
                                break
                            elif pw_legacy.vs[paths[i]]['label'] in list_genes:
                                break
                            else:
                                #print(pw_legacy.vs[paths[i]]['label'], end=' ')
                                list_genes.append(pw_legacy.vs[paths[i]]['label'])
                                #new_dict[pw_legacy.vs[paths[i]]['label']] = \
                                #list(mapping.map_name(pw_legacy.vs[paths[i]]['label'], 'genesymbol', 'uniprot'))[0]

    new_dict = generate_dict(list_genes, pw_legacy)                    #print('\n')
    return new_dict

def get_complete_dict(graph, gene_dict, depth, pw_legacy):
    complete_dict = gene_dict.copy()
    for node1, node2 in itertools.combinations(graph.vs, 2):
        #print(graph.are_connected(gene_dict[node1['label']], gene_dict[node2['label']]))
        #path = graph.get_all_shortest_paths(gene_dict[node1['label']], gene_dict[node2['label']])
        dist = graph.shortest_paths(gene_dict[node1['label']], gene_dict[node2['label']], mode='all')
        #print(path)
        if dist[0][0] > depth: # if node disconnected, the distance is inf which should be > depth
            node_1 = pw_legacy.vs.find(label=node1['label'])
            node_2 = pw_legacy.vs.find(label=node2['label'])
            for paths in pw_legacy.find_all_paths(node_1.index, node_2.index, mode='ALL', maxlen=depth): #do not use graph index, for each graph the indexes are different
                #print(paths)
                for i in range(1, len(paths)-1):
                    if str(pw_legacy.vs[paths[i]]['name'])[:7] == "COMPLEX":
                        break
                    if pw_legacy.vs[paths[i]]['label'] in complete_dict.keys():
                        break
                    else:
                        print(pw_legacy.vs[paths[i]]['label'], end=' ')
                        complete_dict[pw_legacy.vs[paths[i]]['label']] = list(mapping.map_name(pw_legacy.vs[paths[i]]['label'], 'genesymbol', 'uniprot'))[0]
                    
                #print('\n')  
    return complete_dict

def filter_by_node_degree(graph, degree, pw_legacy):
    filtered_dict = {}
    label_tmp = [node if d > degree else '\n' for node, d in zip(graph.vs['label'], graph.degree())]
    labels = [label for label in label_tmp if label != '\n']
    for node in labels:
        filtered_dict[node] = list(mapping.map_name(node, 'genesymbol', 'uniprot'))[0]
    subg = pw_legacy.graph.induced_subgraph([pw_legacy.vs.find(name = filtered_dict[e]) for e in filtered_dict.keys()])
    graph_obj = igraph.plot(subg, target='network_degree_filtered.pdf',
                layout=subg.layout_auto(),
                vertex_size=subg.degree(), edge_width=0.3, edge_color='purple',
                vertex_color='#97BE73', vertex_frame_width=0,
                vertex_label_size=7,
                vertex_label_color='red', inline=True, margin=20)
    return graph_obj

#if I want to know which are the neighbors of a particular node in the subgraph that I just built:

def search_neigh_interactions(gene, gene_dict, graph):
    for neigh in graph.neighbors(gene_dict[gene]):
        eid = graph.get_eid(gene_dict[gene], neigh)
        print(gene, ' -- ', graph.vs[neigh]['label'])
        print(graph.es[eid]['dirs'])
        print(graph.es[eid]['references'])

#with this function, you can select two node of one of your graph, and check which are the shortest paths
#that link the two node, and then plot them

def write_bnet(graph, gene_dict, name="logic_formula.bnet"):
    # database = ['SIGNOR', "Adhesome"]  # ==> insert name of the database
    edge_df = show_edge_dataframe(graph, gene_dict)
    # df_signor = edge_df[pd.DataFrame(edge_df.sources.tolist()).isin(database).any(1).values] # I have filtered the dictionary to have directed interaction from signor
    node_list = []
    for element in edge_df["attrs"]:
        if element.consensus_edges() != []:
            node_list.append(element.consensus_edges()[0][
                                 0].label)  # I am storing into a list the labels (genesymbol) of the genes in "sources", I will use it later
            node_list.append(element.consensus_edges()[0][
                                 1].label)  # I am storing into a list the labels (genesymbol) of the genes in "target", I will use it later
    node_list = list(dict.fromkeys(
        node_list))  # now I have collected in a list all the genes that I have found with directed interactions and without duplicates
    # print(node_list)
    with open(name, "w") as f:
        # f.write("# model in BoolNet format\n")
        # f.write("# the header targets, factors is mandatory to be importable in the R package BoolNet\n")
        # f.write("\n")
        # f.write(
        #     "targets, factors\n")  # this is the standard label that I found in the biolqm github, is it ok? lo scopriremo solo vivendo
        for node in node_list:
            formula_ON = []
            formula_OFF = []
            for element in edge_df["attrs"]:
                interactions = element.consensus_edges()
                for interaction in interactions:  # iterate over the possible interactions
                    if interaction:  # I don't know why, but some interactions are empty... so I am using this to skip the empty interactions
                        if interaction[
                            1].label == node:  # that's tricky one... when you write a bnet file (gene, formula) the gene is not the source, but the target! so I have to iterate between the targets
                            # print(element.consensus_edges()[0][1].label, "  ", node ) # used to check
                            if interaction[2] == "directed" and interaction[
                                3] == "positive":  # checking if the interaction is positive
                                source = interaction[0].label  # if it is, store the source of the positive interaction
                                formula_ON.append(source)  # append the gene into the list
                            elif interaction[2] == "directed" and interaction[
                                3] == "negative":  # checking if the interaction is negative
                                source = interaction[0].label  # storing
                                formula_OFF.append(source)  # append it to the formula with "!"
                            else:
                                print("there is an undirected interaction that was dismissed: ", interaction[0].label,
                                      " and ", interaction[1].label)  # this should never happen, ma non si sa mai...
            formula = formula_ON + formula_OFF
            commons = list(set(formula_ON).intersection(set(formula_OFF)))
            # print(shared)
            for common in commons:
                print("Two possible opposite interactions found for: ", common, " and ", node)
                formula_OFF.remove(common)
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
    f.close  # good to go
    return

