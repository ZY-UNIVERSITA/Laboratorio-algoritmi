import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import random
import networkx as nx
from collections import deque

# Some constants
L_VISITED = 'visited'
L_VISIT_ORDER = 'visit_order'
L_ROOT = 'root'
L_COLOR = 'color'
L_PARENT = 'parent'
L_DIST = 'distance'

def char_range(start='a', end='z'):
    return map(chr,list(range(ord(start),ord(end)+1)))

def plot_basic_graph(G, pos = None, layout = nx.random_layout, seed = None):
    # Define positions for nodes
    if pos is None:
        pos = layout(G, seed = seed)
    # Create matplotlib figure
    fig, ax = plt.subplots(1, 1, figsize=(8,5))
    # Draw nodes and edges
    node_colors = [node[1]['color'] for node in G.nodes(data=True)]
    nx.draw(G, pos, ax = ax, with_labels=True, node_color=node_colors, edgecolors='#000', 
            linewidths=1, font_size=16, font_weight='bold', node_size=600)
    # Draw labels nearby nodes
    for n in G.nodes:
        x, y = pos[n]
        ax.text(x-0.2, y-0.1, f"{G.nodes[n]['label']}",ha='right', va='bottom', color='#00f', fontsize=14)
    # Draw edge labels
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    # Show figure
    fig.set_facecolor("#ededed")
    plt.show()

# TODO: implement this
def bfv(g, root, f):
    queue = deque()

    if f(root):
        return root

    for node in g[root]:
        queue.append(node)

    g.nodes[root][L_VISITED] = True

    while len(queue) > 0:
        firstNode = queue.popleft()
        g.nodes[firstNode][L_VISITED] = True

        for node in g[firstNode]:
            if node not in queue and g.nodes[node][L_VISITED] == False:
                queue.append(node)

        if f(firstNode):
            return firstNode


# TODO: implement this
def dfv(g, root, f):
    g.nodes[root][L_VISITED] = True

    if f(root):
        return root

    for node in g.nodes:
        if g.nodes[node][L_VISITED] == False:
            dfv(g, node, f)


# TODO: implement this
# The function should annotate the nodes with their parent and distance from source
def dijkstra(g, src):
    # initialization
    for n in g.nodes:
        g.nodes[n][L_VISITED] = False
        g.nodes[n][L_DIST] = float("inf")
        g.nodes[n][L_PARENT] = ''

    queue = deque()
    queue.append(src)
    
    g.nodes[src][L_VISITED] = True
    g.nodes[src][L_DIST] = 0

    while len(queue) > 0:    
        minimumNode = ""
        previousNode = queue.popleft()

        for node in g[previousNode]:
            if g.nodes[node][L_VISITED] == False:

                new_distance = g[previousNode][node]["weight"] + g.nodes[previousNode][L_DIST]

                if new_distance < g.nodes[node][L_DIST]:
                    g.nodes[node][L_DIST] = new_distance
                    g.nodes[node][L_PARENT] = previousNode


                if minimumNode == "":
                    minimumNode = node
                elif g.nodes[node][L_DIST] < g.nodes[minimumNode][L_DIST]:
                        minimumNode = node
                

        if minimumNode != "":
            queue.append(minimumNode)
            g.nodes[minimumNode][L_VISITED] = True

    # for node in g.nodes:
    #     print(f"{node}: {g.nodes[node]}")


def shortest_path(g, src, dest):
    queue = deque()
    queue.append(dest)

    queuePrint = deque()

    while len(queue) > 0:
        node = queue.popleft()
        queuePrint.appendleft(node)
        nextNode = g.nodes[node][L_PARENT]

        if (nextNode != src):
            queue.append(nextNode)

    queuePrint.appendleft(src)
    queue = []

    for i in range(len(queuePrint)):
        node = queuePrint.popleft()
        queue.append(node)

    return queue


if __name__ == "__main__":
    g = nx.Graph()
    default_node_attributes = {'visited': False, 'parent': None, 'distance': float("inf"), 'label': '', 'color': '#ededed'}
    g.add_nodes_from(char_range('A','F'), **default_node_attributes)
    g.add_weighted_edges_from([('A','B',1), ('A','F',3), ('B','C',3), ('B','E',5), ('B','F',1), 
                            ('C','D',2), ('D','E',1), ('D','F',6), ('E','F',2)], )
    pos = { 'A': (0,0.5), 'B': (1,1), 'C': (2,1), 'D':(3,0.5), 'E':(2,0), 'F':(1,0) }

    print("*** BFV")
    bfv(g, 'A', print) # expected print order: ABFCED
    print("\n*** DFV")
    dfv(g, 'A', print) # expected print order: ABCDEF
    print("\n*** Dijkstra")
    dijkstra(g, 'A') # should annotate the nodes in the graph
    print(['A', 'B', 'F', 'E', 'D'] == shortest_path(g, 'A', 'D')) # should be True

    plot_basic_graph(g, pos)