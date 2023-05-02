import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from copy import deepcopy
from MCS import MCS,cliqueCutsets
import itertools

g = nx.Graph()
C6=[('a','b'),('b','c'),('c','d'),('d','e'),('e','f'),('f','a')]
_C6=[('a','d'),('a','e'),('a','f'),('b','e'),('b','f'),('c','b'),('c','f'),('c','d')]
g.add_edges_from(C6)
c6_ = nx.complement(g)

def cycle_DFS(g, v, visited, parent):
    visited[v] = True
    for neighbor in g.neighbors(v):
        if not visited[neighbor]:
            if cycle_DFS(g, neighbor, visited, v):
                return True
        elif neighbor != parent:
            return True
    return False

def has_C6_(g:nx):
    if len(g.nodes()) < 6:
        return False
    # C(n,6),so time complexity of n^6
    for sub_nodes in itertools.combinations(g.nodes(),6):
        subg = g.subgraph(sub_nodes)
        # O(n+m)
        complement_subg = nx.complement(subg)
        judge = 0
        # O(n+m)
        if nx.is_connected(complement_subg) != 1:
            continue
        # O(n^2)
        for i in sub_nodes:
            if complement_subg.degree(i) !=2:
                judge = 1
                break
        if judge == 0:
            return True
    return False    
