import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from copy import deepcopy
from MCS import MCS,cliqueCutsets
import itertools

g = nx.Graph()
w54=[('a','b'),('a','e'),('b','c'),('b','f'),('c','d'),('c','f'),('d','e'),('d','f'),('e','f')]
g1 = [('a','b'),('a','c'),('a','d'),('a','f'),('b','c'),('b','e'),('c','d'),('d','e'),('e','f')]
test = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('e', 'f'), ('f', 'a')]
g.add_edges_from(w54)

def has_W54(g:nx):
    # C(n,6),so time complexity of n^6
    if len(g.nodes()) < 6:
        return False
    for sub_nodes in itertools.combinations(g.nodes(),6):
        subg = g.subgraph(sub_nodes)
        degree_4 = []
        degree_3 = []
        degree_2 = []
        for i in sub_nodes:
            if subg.degree(i) == 4:
                degree_4.append(i)
            elif subg.degree(i) == 3:
                degree_3.append(i)
            elif subg.degree(i) == 2:
                degree_2.append(i)
            else:
                break
        if len(degree_4) == 1 and len(degree_3) == 4 and len(degree_2) == 1:
            judge1 = 0
            subg1 = subg.copy()
            subg1.remove_node(degree_4[0])
            if nx.is_connected(subg1) != 1:
                continue
            for i in subg1.nodes():
                if subg1.degree(i) !=2:
                    judge1 = 1
                    break
            if  judge1 == 0:
                return True
    return False
            
