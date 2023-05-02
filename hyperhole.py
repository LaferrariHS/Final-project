import networkx as nx
import numpy as np
from copy import deepcopy

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

g = nx.Graph()
g.add_edges_from(hyperantihole1)

def is_hyperhole(g:nx):
     # O(n+m)
    if (not nx.is_connected(g)): 
        return 0 
    # O(n+m)
    if (nx.is_chordal(g)):
        return 0
    g1=deepcopy(g)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    degree=dict(g.degree)
    X_now=[]
    sorted_v_bydegree=dict(sorted(degree.items(), key=lambda item: item[1]))
    v=max(degree,key=degree.get)
    v_NR = set(g.neighbors(v))
    v_NR.add(v)
    for key in sorted_v_bydegree:
        key_NR = set(g.neighbors(key))
        key_NR.add(key)
        if(key_NR.issubset(v_NR)):
            X_now.append(key)
    popi = 0
    while(popi < len(X_now)-1):
        now_NR = set(g.neighbors(X_now[popi]))
        now_NR.add(X_now[popi])
        next_NR = set(g.neighbors(X_now[popi+1]))
        next_NR.add(X_now[popi+1])
        if(not now_NR.issubset(next_NR)):
            X_now.pop(popi)
        popi = popi+1
    first_list = X_now
    first_v =  X_now[-1]
    NR_xi = set(g.neighbors(X_now[-1]))
    NR_xi.add(X_now[-1])
    Xlast_Xnext=NR_xi.difference(X_now)
    Xnext_unsorted=list((set(g.neighbors(list(Xlast_Xnext)[0])).intersection(Xlast_Xnext)))
    Xnext_unsorted.insert(0, list(Xlast_Xnext)[0])
    Xnext = [x for x in sorted_v_bydegree if x in Xnext_unsorted]
    Xlast_unsorted = Xlast_Xnext.difference(Xnext)
    Xlast = [x for x in sorted_v_bydegree if x in Xlast_unsorted]
    XlastandXnext = Xlast+Xnext
    for i in X_now:
        for j in XlastandXnext:
            if not g.has_edge(i, j):
                return False
    count = 1
    for i in X_now:
        g1.remove_node(i)
    Xlast = X_now
    X_now = Xnext
    while len(g1.nodes()) != 0 or X_now[-1] != first_v:
        NR_xi = set(g.neighbors(X_now[-1]))
        NR_xi.add(X_now[-1])
        Xnext_unsorted=list(NR_xi.difference(X_now + Xlast))
        Xnext = [x for x in sorted_v_bydegree if x in Xnext_unsorted]
        XlastandXnext = Xlast+Xnext
        for i in X_now:
            for j in XlastandXnext:
                if not g.has_edge(i, j):
                    return False
        count = count + 1
        for i in X_now:
            if i not in g1.nodes():
                return False
            g1.remove_node(i)
        Xlast = X_now
        X_now = Xnext
        
    if count > 3 and X_now[-1] == first_v and X_now == first_list:
        return True
    return False
