import networkx as nx
import numpy as np
from copy import deepcopy
from collections import defaultdict

connec=[('a','b'),('a','e'),('b','c'),('c','d'),('d','e'),('a1','a'),('a1','e'),('a1','b'),('b1','b'),('b1','a'),
('b1','c'),('b1','c1'),('c1','c'),('c1','b'),('c1','d')]
connections=[('a','b'),('a','c'),('a','e'),('b','d'),('b','e'),('c','e'),('c','d'),('d','e')]
connections2=[('a', 'c'),
                   ('a', 'd'),('a','f'), ('b', 'c'),('b', 'g'),('c','h'),('c','f'),('c', 'd'),  ('d', 'e')
                   ,('d','i'),('d','f'),('e','j'),('g','h'),('h','k'),('k','i'),('i','j')]
connections1=[('a', 'b'),('a','d'),('b','c'),('c','d'),('a', 'c'),('b', 'd')]
ring1 = [(1,2),(1,5),(1,6),(1,7),(2,6),(2,3),(2,9),(3,4),(3,8),(3,9),(4,5),(4,7),(4,8),(4,9),(5,6),(5,7),(5,8),(6,7)]
ring2 = [(1,2),(1,5),(1,4),(1,6),(1,7),(2,6),(2,3),(2,9),(3,4),(3,8),(3,9),(4,5),(4,7),(4,8),(4,9),(5,6),(5,7),(5,8),(6,7)]
hyperhole1 = [(1,2),(1,5),(1,6),(1,7),(2,6),(2,3),(2,9),(3,4),(3,8),(3,9),(4,5),(4,7),(4,8),(4,9),(5,6),(5,7),(5,8),(6,7),(7,8),(8,9)]
hyperantihole1 = [(1,6),(1,3),(1,9),(1,4),(1,8),(6,3),(6,9),(6,8),(6,4),(2,4),(2,8),(2,5),(2,7),(3,9),(3,5),(3,7),(9,5),(9,7),(4,8),(5,7)]
hyperantihole2 = [(1,4),(1,3),(1,5),(1,6),(2,4),(2,5),(2,6),(2,7),(3,5),(3,6),(3,7),(4,6),(4,7),(5,7),(8,1),(8,3),(8,4),(8,5),(8,6)]

g = nx.Graph()
g.add_edges_from(hyperantihole2)


# Find all cliques and return the set of one of the vertices of each clique
def get_clique_node(g:nx):
    if len(g.nodes()) < 7:
        return False
    grouped_nodes = defaultdict(list)
    # Find all clique, O(n)
    for node in g.nodes():
        neighbors = set(g.neighbors(node))
        neighbors.add(node)  # # Add self
        grouped_nodes[frozenset(neighbors)].append(node)
    result = []
    if (len(grouped_nodes) != 7):
        return False
    # Derive the first point of each clique and form the set, O(ni)
    for group in grouped_nodes.values():
        if group:
            result.append(group[0])
    return set(result)

def is_7hyperantihole(g:nx):
    # O(n)
    new_graph_node =  get_clique_node(g)
    if new_graph_node != False:
        new_graph = g.subgraph(new_graph_node)
        new_graph_complement = nx.complement(new_graph)
        if not nx.is_connected(new_graph_complement):
            return False
        if (nx.is_chordal(new_graph_complement)):
            return False
        for i in new_graph_complement.nodes():
            if new_graph_complement.degree(i) !=2:
                return False
    else:
        return False
    return True

print(is_7hyperantihole(g))