import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from copy import deepcopy
from MCS import MCS,cliqueCutsets
import itertools

g = nx.Graph()
k23=[('a','e'),('a','c'),('a','d'),('b','c'),('b','d'),('b','e'),('e','f')]
g.add_edges_from(k23)

def has_K23(g:nx):
    if len(g.nodes()) < 5:
        return False
    # C(n,5),so time complexity of n^5
    for sub_nodes in itertools.combinations(g.nodes(),5):
        subg = g.subgraph(sub_nodes)
        degree_three = []
        degree_two = []
        for i in sub_nodes:
            if subg.degree(i) == 3:
                degree_three.append(i)
            if subg.degree(i) == 2:
                degree_two.append(i)
        if len(degree_two) == 3 and len(degree_three) ==2:
            out_loop = False
            count = 0
            for i in degree_three:
                for j in degree_two:
                    if subg.has_edge(i, j):
                        count=count+1
                    else:
                        out_loop = True
                        break
                if out_loop == True:
                    break
            if count == 6:
                return True
    return False