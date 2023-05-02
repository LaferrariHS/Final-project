from copy import deepcopy
from MCS import MCS,cliqueCutsets
import networkx as nx
import numpy as np
from Bu import is_Bu

connections=[('a','b'),('a','c'),('a','e'),('b','d'),('b','e'),('c','e'),('c','d'),('d','e')]

connections1=[('a', 'b'),('a','d'),('b','c'),('c','d'),('a', 'c'),('b', 'd')]
connec=[('a','b'),('a','d'),('a','e'),('b','d'),('b','c'),('b','g'),('c','h'),('d','e'),('d','f'),
('d','g'),('e','f'),('f','g'),('h','g')]
connec1 = [(1,2),(1,3),(2,3),(2,4),(3,4),(3,5),(4,5)]
connec2 = [(1,2),(1,3),(2,3),(2,4),(2,6),(3,4),(4,5),(5,6),(5,7),(6,7)]
connections2=[('a', 'c'),
                   ('a', 'd'),('a','f'), ('b', 'c'),('b', 'g'),('c','h'),('c','f'),('c', 'd'),  ('d', 'e')
                   ,('d','i'),('d','f'),('e','j'),('g','h'),('h','k'),('k','i'),('i','j')] ## gu example
g = nx.Graph()
g.add_edges_from(connec2)

def gu_recognize(g):
    order,fillin_graph, clique_gen=MCS(g)## get fill-in graph with perfect elimination ordering.
    leaves=cliqueCutsets(g,fillin_graph,clique_gen,order) ## get leaves from the decompostion of the tree
    for i in leaves:
        if is_Bu(i) != True:
            return False
    return True

print(gu_recognize(g))