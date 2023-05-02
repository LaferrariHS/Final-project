from copy import deepcopy
from MCS import MCS,cliqueCutsets
from anticompent import get_anticompent
import networkx as nx
import numpy as np




connections1=[('a', 'c'),('a','d'),('b','e'),('b','d'),('c','e')]
g = nx.Graph()
g.add_edges_from(connections1)

def is_Bu(g):
    largest_component_size,anticompents = get_anticompent(g)
    if largest_component_size <= 2:#Condition 2: All the nontrivial anti-components of G are K2_ isomorphic
        return True
    if len(anticompents) == 1:
        if len(anticompents[0].nodes()) >= 5 and all(anticompents[0].degree(d) == 2 for d in anticompents[0].nodes()):
          return True
    return False

