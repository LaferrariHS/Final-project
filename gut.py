import networkx as nx
import numpy as np
from ring import is_ring
from MCS import MCS,cliqueCutsets
from typing import List
from has_K23 import has_K23
from has_C6_ import has_C6_
from has_W54 import has_W54
from has_longhole import has_longhole
from anticompent import get_anticompent

g = nx.Graph()
w54=[('a','b'),('a','e'),('b','c'),('b','f'),('c','d'),('c','f'),('d','e'),('d','f'),('e','f')]
g1 = [('a','b'),('a','c'),('a','d'),('a','e'),('b','c'),('b','e'),('c','d'),('d','e'),('g','f')]
w=[(1,2),(1,3),(2,3),(2,4),(3,4),(3,5),(4,5),(4,6),(5,6),(6,7),(5,7)]
g.add_edges_from(w)

def max_stable(G:nx):
    stable_set = set()
    sorted_nodes = sorted(G.nodes(), key=lambda x: G.degree(x), reverse=True)
    while sorted_nodes:
        # Pick the node with the smallest degree
        node = sorted_nodes[-1]
        # Remove the node and its neighbours from the graph
        neighbors = set(G.neighbors(node)) | set([node])
        for i in neighbors:
            sorted_nodes.remove(i)
        # Add this node to the stable set
        stable_set.add(node)
    return len(stable_set)

def is_gut(g:nx):
    if(has_K23(g) or  has_C6_(g) or has_W54(g)):
        return False
    order,fillin_graph, clique_gen=MCS(g)
    leafs=cliqueCutsets(g,fillin_graph,clique_gen,order)
    for leaf in leafs:
        len_anti,antis = get_anticompent(leaf)
        for anti in antis:
            if max_stable(anti)> 2 and (not(is_ring(anti) > 4) and has_longhole(anti)):
                return False
    return True

print(is_gut(g))