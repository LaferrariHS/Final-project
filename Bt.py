import networkx as nx
import numpy as np
from copy import deepcopy
from ring import is_ring
from hyperantihole import is_7hyperantihole
connec=[('a','b'),('a','e'),('b','c'),('c','d'),('d','e'),('a1','a'),('a1','e'),('a1','b'),('b1','b'),('b1','a'),
('b1','c'),('b1','c1'),('c1','c'),('c1','b'),('c1','d')]
connections=[('a','b'),('a','c'),('a','e'),('b','d'),('b','e'),('c','e'),('c','d'),('d','e')]
connections2=[('a', 'c'),
                   ('a', 'd'),('a','f'), ('b', 'c'),('b', 'g'),('c','h'),('c','f'),('c', 'd'),  ('d', 'e')
                   ,('d','i'),('d','f'),('e','j'),('g','h'),('h','k'),('k','i'),('i','j')]
connections1=[('a', 'b'),('a','d'),('b','c'),('c','d'),('a', 'c'),('b', 'd')]
ring1 = [(1,2),(1,5),(1,6),(1,7),(2,6),(2,3),(2,9),(3,4),(3,8),(3,9),(4,5),(4,7),(4,8),(4,9),(5,6),(5,7),(5,8),(6,7)]
ring2 = [(1,2),(1,5),(1,6),(1,7),(2,6),(2,3),(2,9),(3,4),(3,8),(3,9),(4,5),(4,7),(4,8),(4,9),(5,6),(5,7),(5,8),(6,7),(10,5),(10,4),(10,8)]
hyperhole1 = [(1,2),(1,5),(1,6),(1,7),(2,6),(2,3),(2,9),(3,4),(3,8),(3,9),(4,5),(4,7),(4,8),(4,9),(5,6),(5,7),(5,8),(6,7),(7,8),(8,9)]
hyperantihole1 = [(1,6),(1,3),(1,9),(1,4),(1,8),(6,3),(6,9),(6,8),(6,4),(2,4),(2,8),(2,5),(2,7),(3,9),(3,5),(3,7),(9,5),(9,7),(4,8),(5,7)]

g = nx.Graph()
g.add_edges_from(hyperantihole1)

def is_Bt(g:nx):
    if len(g.edges()) == len(g.nodes()) * (len(g.nodes()) - 1) // 2:
        return True
    if is_7hyperantihole(g):
        return True
    if is_ring(g) != 0:
        return True
    return False