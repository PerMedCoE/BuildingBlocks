import networkx as nx

# import xml.etree.ElementTree as ET


def split_col(net_df):
    for col in net_df.columns:
        if col != "ID":
            i = 0
            for list_id in net_df[col]:
                if type(list_id) == str:
                    id_list = [x for x in list_id.split("/")]
                    id_list.pop(-1)
                    id_list = [int(x) for x in id_list]
                    net_df.at[i, col] = id_list
                    # print(id_list)
                    i = i + 1
                else:
                    a = None
                    net_df.at[i, col] = a
                    i = i + 1
                    continue
    return


def create_graph(net_df, column_name):
    G = nx.Graph()

    for node in net_df["ID"]:
        G.add_node(node)
    G.number_of_nodes()

    i = 0
    for node1 in net_df["ID"]:
        # print(net_df[' neighID'][node1])
        if net_df[column_name][i] != None:
            for node2 in net_df[column_name][i]:
                # print(node1, node2)
                G.add_edge(node1, node2)
            i = i + 1
        else:
            i = i + 1
            continue
    return G


def largest_component(G):
    S = [G.subgraph(c).copy() for c in nx.connected_components(G)]
    largest_component = max(S, key=len)
    return largest_component


# def create_color_dict(G, larg_comp):
#     color_list_degree = []
#     color_list_nodes_class = []
#     for node in G.nodes:
#         if node in larg_comp:
#             color_list_degree.append(6)
#             color_list_nodes_class.append(6)
#         else:
#             color_list_degree.append(G.degree[node])
#             if G.degree[node] != 0:
#                 color_list_nodes_class.append(4)
#             else:
#                 color_list_nodes_class.append(0)
#     color_dict = dict(zip(G.nodes, color_list_nodes_class))
#     return color_dict


# def color_svg(file_name, file_name2, color_dict):
#     tree = ET.parse(file_name)
#     root = tree.getroot()
#     g = root.find("{http://www.w3.org/2000/svg}g//{http://www.w3.org/2000/svg}g[2]")
#     for cell in g:
#         code = cell.get('id')
#         ID = code.lstrip('cell')
#         # print(int(ID))
#         if color_dict[int(ID)] == 6:
#             cell[0].set('fill', 'rgb(255,0,0)')
#             cell[1].set('fill', 'rgb(125,0,0)')
#         if color_dict[int(ID)] == 4:
#             cell[0].set('fill', 'rgb(255,204,204)')
#             cell[1].set('fill', 'rgb(125,102,102)')
#         if color_dict[int(ID)] == 0:
#             cell[0].set('fill', 'rgb(0,0,255)')
#             cell[1].set('fill', 'rgb(0,0,125)')
#         # print(code, node.get('fill'))
#     tree.write(file_name2)
#     return


def count_component(G):
    S = [G.subgraph(c).copy() for c in nx.connected_components(G)]
    largest_component = max(S, key=len)
    S.remove(largest_component)
    single = 0
    cluster = 0
    for net in S:
        if len(net.nodes()) == 1:
            single = single + 1
        else:
            cluster = cluster + 1
    return [single, cluster]


def count_cell_in_cluster(G):
    S = [G.subgraph(c).copy() for c in nx.connected_components(G)]
    largest_component = max(S, key=len)
    S.remove(largest_component)
    size = 0
    single = 0
    for net in S:
        if len(net.nodes()) == 1:
            single = single + 1
        else:
            size = size + len(net.nodes())
    if size == 0 and single == 0:
        ratio_single_cluster = 0
    else:
        ratio_single_cluster = (size / (size + single)) * 100

    return [ratio_single_cluster, size]
