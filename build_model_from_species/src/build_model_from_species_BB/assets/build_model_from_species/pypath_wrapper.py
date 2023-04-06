from pypath.core.network import Network
from itertools import combinations
from igraph import *
from pypath.utils import mapping
from pypath.resources import network as netres
from pypath import omnipath
import matplotlib.pyplot as plt
import sys

class Wrap_net(Network):

    def __init__(self, pickle_file=None):
        super().__init__()
        self.__graph = None
        if pickle_file != None:
            self.load_from_pickle(pickle_file)

    def extract_subnet(self, list_of_nodes, max_len, resources=None, complete_connections=False):

        """extract a subnetwork of the same type of this object, given a list of nodes and a max length
        user should check in the end to actually have a full connected network with no disconnected component
        :argument
        list_of_nodes : a list of starting nodes for your network
        max_len : in case two nodes a and b are not connected, this function will automatically search for possible connections with max length == max_len
        resources=None : a list of database like SIGNOR, SPIKE, ADHESOME etc...
        """
        new_net = Wrap_net()

        verified_genes = []
        for node in list_of_nodes:
            try:
                uniprot = list(mapping.map_name(node, 'genesymbol', 'uniprot'))
                genesymbol = list(mapping.map_name(uniprot[0], 'uniprot', 'genesymbol'))
                new_net.add_node(self.entity(genesymbol[0]))
                verified_genes.append(genesymbol[0])
            except:
                print("Couldn't process the gene %s" % node, file=sys.stderr) 
         
        #to add a check if the node is in the database/node has a good name/ uniprot correspondance
        @staticmethod
        def check_interaction(pth):
            if pth is None:
                return False
            elif pth.is_directed and pth.is_inhibition():
                return True
            elif pth.is_directed and pth.is_stimulation():
                return True
            else:
                return False

        @staticmethod
        def list_of_paths(nodes, i, res):
            list_of_edges = []
            for node1, node2 in combinations(nodes, 2):
                counter = 0
                while counter <= i:
                    a = self.find_paths(node1, node2, maxlen=counter, minlen=0, loops=False, mode='ALL', resources=res)
                    if not a:
                        counter += 1
                    else:
                        list_of_edges += a
                        break
            return list_of_edges

        @staticmethod
        def check_connected(net):
            for x in net.nodes_by_label:
                if not net.get_neighbours(x):
                    return False
            return True

        @staticmethod
        def complete_connection(net, res):
            list_of_edges = []
            for y in net.nodes_by_label:
                if not net.get_neighbours(y):
                    direct_connections = []
                    neighs = self.get_neighbours(y)
                    for neigh in neighs:
                        interaction_with_neigh = self.interaction(y, neigh)
                        if check_interaction(interaction_with_neigh):
                            direct_connections.append(neigh)
                    if not direct_connections:
                        print("The disconnected node has no directed connections with its neighbours, it is impossible to complete the connections")
                        print(y)
                        return
                    for x in (x for x in net.nodes_by_label if x != y):
                        flag = True
                        i = 0
                        while flag:
                            a = self.find_paths(y, x, maxlen=i, loops=False, mode='ALL', resources=res)
                            if not a:
                                i += 1
                            else:
                                list_of_edges += a
                                flag = False
                else:
                    continue
            # iterate for each node of the network and try to complete the connection, connecting all the disconnected component
            # according to the database selected as resource, this can return or not a fully connected network
            return list_of_edges

        @staticmethod
        def add_edges(b, net):
            for c in b:
                i = 0
                edge_list = []
                while i < len(c) - 1:
                    edge = self.interaction(c[i], c[i + 1])
                    if check_interaction(edge):
                        edge_list.append(edge)
                        i = i + 1
                    else:
                        break
                for ed in edge_list:
                    net.add_interaction(ed)
            return
        
        paths = list_of_paths(verified_genes, max_len, resources)
        add_edges(paths, new_net)

        if complete_connections and not check_connected(new_net):
            new_edges = complete_connection(new_net, resources)
            if new_edges:
                add_edges(new_edges, new_net)

        return new_net

    def get_neighbours(self, node):
        list_of_neigh = []
        for i in self.get_interactions():
            if node == i[0].label:
                list_of_neigh.append(i[1].label)
            if node == i[1].label:
                list_of_neigh.append(i[0].label)
        return list(set(list_of_neigh))

    def generate_graph(self):
        #to do: generate a graph so I can access information like vertex degree etc...
        self.__graph = Graph(directed=True)

        for node in self.nodes.values():
            self.__graph.add_vertices(node.label)

        for interaction in self.interactions.values():
            for edge in interaction.which_signs():
                self.__graph.add_edge(edge[0][0].label, edge[0][1].label, sign=edge[1])


    def print_graph(self):

        positive_directed_edges = self.__graph.es.select(sign='positive')
        negative_directed_edges = self.__graph.es.select(sign='negative')
        positive_directed_edges['color'] = 'green'
        negative_directed_edges['color'] = 'red'

        graph =  plot(self.__graph,
             layout=self.__graph.layout_auto(), vertex_label=self.__graph.vs['name'], edge_width=0.3,
             vertex_color='white', vertex_frame_width=0,
             vertex_label_color='black', inline=True, margin=20, vertex_frame_color="black")

        return graph

    def write_bnet(self, file_name="logic_formula.bnet"):

        if self.interactions == {}:
            print("there are no interaction in this network, so makes no sense to print a bnet file!")
            return
        with open(file_name, "w") as f:
            f.write("# model in BoolNet format\n")
            f.write("# the header targets, factors is mandatory to be importable in the R package BoolNet\n")
            f.write("\n")
            f.write(
                "targets, factors\n")  # this is the standard label that I found in the biolqm github, is it ok? lo scopriremo solo vivendo
            for node in list(self.nodes_by_label.keys()):
                formula_on = []
                formula_off = []
                for element in self.interactions.values():
                    interactions = element.which_signs()
                    for interaction in interactions:  # iterate over the possible interactions
                        if interaction:  # I don't know why, but some interactions are empty... so I am using this to skip the empty interactions
                            if interaction[0][1].label == node:  # that's tricky one... when you write a bnet file (gene, formula) the gene is not the source, but the target! so I have to iterate between the targets
                                # print(element.consensus_edges()[0][1].label, "  ", node ) # used to check
                                if interaction[1] == "positive":  # checking if the interaction is positive
                                    source = interaction[0][0].label  # if it is, store the source of the positive interaction
                                    formula_on.append(source)  # append the gene into the list
                                elif interaction[1] == "negative":  # checking if the interaction is negative
                                    source = interaction[0][0].label  # storing
                                    formula_off.append(source)  # append it to the formula with "!"
                                else:
                                    print("there is an undirected interaction that was dismissed: ",
                                          interaction[0][0].label,
                                          " and ",
                                          interaction[0][1].label)  # this should never happen, ma non si sa mai...
                formula = formula_on + formula_off
                commons = list(set(formula_on).intersection(set(formula_off)))
                # print(shared)
                for common in commons:
                    print("Two possible opposite interactions found for: ", common, " and ", node)
                    formula_off.remove(common) #here I should insert something to create an ensamble of model
                f.write(node.replace("-", "_") + ",")
                offset = 16 - len(node)  # nice offset so the visualization is understandable
                f.write(" " * offset)
                if not formula:
                    f.write(" ( ")
                    f.write(node.replace("-", "_"))
                    f.write(" ) ")
                    f.write("\n")
                if formula_on:
                    f.write(" ( ")
                    f.write(" | ".join(list(set(formula_on))).replace("-", "_"))  # writing the first parenthesis with all the positive interactions
                    f.write(" ) ")
                    if not formula_off:
                        f.write("\n")
                if formula_on != [] and formula_off != []:
                    f.write(" & ")
                    f.write(" !( ")
                    f.write(" | ".join(list(set(formula_off))).replace("-", "_"))  # writing the first parenthesis with all the positive and negative interactions
                    f.write(" ) ")
                    f.write("\n")
                if formula_on == [] and formula_off != []:
                    f.write(" !( ")
                    f.write(" | ".join(list(set(formula_off))).replace("-", "_"))  # writing the first parenthesis with all the negative interactions
                    f.write(" ) ")
                    f.write("\n")
        f.close  # good to go
        return

