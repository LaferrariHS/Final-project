from copy import deepcopy
from MCS import MCS,cliqueCutsets
import networkx as nx
import numpy as np
from Bt import is_Bt

connections=[('a','b'),('a','c'),('a','e'),('b','d'),('b','e'),('c','e'),('c','d')]

connections1=[('a', 'b'),('a','d'),('b','c'),('c','d'),('a', 'c'),('b', 'd')]
connec=[('a','b'),('a','d'),('a','e'),('b','d'),('b','c'),('b','g'),('c','h'),('d','e'),('d','f'),
('d','g'),('e','f'),('f','g'),('h','g')]

connections3=[('a', 'c'),
                   ('a', 'd'),('a','f'), ('b', 'c'),('b', 'g'),('c','h'),('c','f'),('c', 'd'),  ('d', 'e')
                   ,('d','i'),('d','f'),('e','j'),('g','h'),('h','k'),('k','i'),('i','j')] ## gu example
connec=[('a','b'),('a','e'),('b','c'),('c','d'),('d','e'),('a1','a'),('a1','e'),('a1','b'),('b1','b'),('b1','a'),
('b1','c'),('b1','c1'),('c1','c'),('c1','b'),('c1','d')]

connections2=[('a', 'c'),
                   ('a', 'd'),('a','f'), ('b', 'c'),('b', 'g'),('c','h'),('c','f'),('c', 'd'),  ('d', 'e')
                   ,('d','i'),('d','f'),('e','j'),('g','h'),('h','k'),('k','i'),('i','j')]
connections1=[('a', 'b'),('a','d'),('b','c'),('c','d'),('a', 'c'),('b', 'd')]
ring1 = [(1,2),(1,5),(1,6),(1,7),(2,6),(2,3),(2,9),(3,4),(3,8),(3,9),(4,5),(4,7),(4,8),(4,9),(5,6),(5,7),(5,8),(6,7)]
ring2 = [(1,2),(1,5),(1,6),(1,7),(2,6),(2,3),(2,9),(3,4),(3,8),(3,9),(4,5),(4,7),(4,8),(4,9),(5,6),(5,7),(5,8),(6,7),(10,5),(10,4),(10,8)]
hyperhole1 = [(1,2),(1,5),(1,6),(1,7),(2,6),(2,3),(2,9),(3,4),(3,8),(3,9),(4,5),(4,7),(4,8),(4,9),(5,6),(5,7),(5,8),(6,7),(7,8),(8,9)]
hyperantihole1 = [(1,6),(1,3),(1,9),(1,4),(1,8),(6,3),(6,9),(6,8),(6,4),(2,4),(2,8),(2,5),(2,7),(3,9),(3,5),(3,7),(9,5),(9,7),(4,8),(5,7)]
hyperantihole2 = [(1,4),(1,3),(1,5),(1,6),(2,4),(2,5),(2,6),(2,7),(3,5),(3,6),(3,7),(4,6),(4,7),(5,7),(8,1),(8,3),(8,4),(8,5),(8,6)]
nothyperantihole2 = [(1,4),(1,3),(1,5),(1,6),(2,4),(2,5),(2,6),(2,7),(3,5),(3,6),(3,7),(4,6),(4,7),(5,7),(8,1),(8,3),(8,4),(8,5)]

g = nx.Graph()
g.add_edges_from(nothyperantihole2)

def gt_recognize(g):
    order,fillin_graph, clique_gen=MCS(g)## get fill-in graph with perfect elimination ordering.
    leaves=cliqueCutsets(g,fillin_graph,clique_gen,order) ## get leaves from the decompostion of the tree
    for i in leaves:
        if is_Bt(i) != True:
            return False
    return True

print(gt_recognize(g))