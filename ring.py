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
connections2=[(1, 2),(1,3),(1,4),(2,3),(2, 4),(3, 4)]
ring1 = [(1,2),(1,5),(1,6),(1,7),(2,6),(2,3),(2,9),(3,4),(3,8),(3,9),(4,5),(4,7),(4,8),(4,9),(5,6),(5,7),(5,8),(6,7)]# yes 5
ring4 = [(1,2),(1,5),(1,6),(1,7),(2,6),(2,3),(2,9),(3,4),(3,8),(3,9),(4,5),(4,7),(4,8),(4,9),(5,6),(5,7),(5,8),(6,7),(1,10),(4,10),(5,10),(8,10)]#no
ring2 = [(1,2),(1,5),(1,6),(1,7),(2,6),(2,3),(2,7),(2,8),(3,8),(3,9),(3,7),(4,5),(4,3),(4,8),(4,9),(5,9),(5,6),(6,7),(7,8),(8,9)]# yes5
ring3 = [(1,2),(1,3),(2,4),(3,4)]# yes4
hyperantihole1 = [(1,6),(1,3),(1,9),(1,4),(1,8),(6,3),(6,9),(6,8),(6,4),(2,4),(2,8),(2,5),(2,7),(3,9),(3,5),(3,7),(9,5),(9,7),(4,8),(5,7)]# yes
hyperantihole2 = [(1,4),(1,3),(1,5),(1,6),(2,4),(2,5),(2,6),(2,7),(3,5),(3,6),(3,7),(4,6),(4,7),(5,7),(8,1),(8,3),(8,4),(8,5),(8,6)]# no


g = nx.Graph()
g.add_edges_from(hyperantihole1)

def is_ring(g:nx):  
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
    # Get the vertex with the greatest degree
    v=max(degree, key=degree.get)
    v_NR = set(g.neighbors(v))
    v_NR.add(v)
    # O(n1^2)
    for key in sorted_v_bydegree:
        key_NR = set(g.neighbors(key))
        key_NR.add(key)
        if(key_NR.issubset(v_NR)):
            X_now.append(key)
    popi = 0
    # O(n1^2)
    while(popi < len(X_now)-1):
        now_NR = set(g.neighbors(X_now[popi]))
        now_NR.add(X_now[popi])
        next_NR = set(g.neighbors(X_now[popi+1]))
        next_NR.add(X_now[popi+1])
        if(not now_NR.issubset(next_NR)):
           return 0
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
    if len(Xnext) == 0 or len(Xlast) == 0:
        return 0
    for i in X_now:
        if i not in g.neighbors(Xlast[-1]) or i not in g.neighbors(Xnext[-1]):
            return 0
    count = 1
    for i in X_now:
        g1.remove_node(i)
    Xlast = X_now
    X_now = Xnext
    # O(n^2)
    while len(g1.nodes()) != 0 and X_now != first_list:
        popi = 0
        while(popi < len(X_now)-1):
            now_NR = set(g.neighbors(X_now[popi]))
            now_NR.add(X_now[popi])
            next_NR = set(g.neighbors(X_now[popi+1]))
            next_NR.add(X_now[popi+1])
            if(not now_NR.issubset(next_NR)):
                return 0
            popi = popi+1
        NR_xi = set(g.neighbors(X_now[-1]))
        NR_xi.add(X_now[-1])
        Xnext_unsorted=list(NR_xi.difference(X_now + Xlast))
        if len(Xnext_unsorted) == 0:
            return 0
        Xnext = [x for x in sorted_v_bydegree if x in Xnext_unsorted]
        for i in X_now:
            if i not in g.neighbors(Xlast[-1]) or i not in g.neighbors(Xnext[-1]):
                return 0
        count = count + 1
        for i in X_now:
            if i not in g1.nodes():
                return 0
            g1.remove_node(i)
            sorted_v_bydegree.pop(i)
        Xlast = X_now
        X_now = Xnext
        
    if count > 3 and X_now == first_list and len(g1.nodes()) == 0:
        return count
    return 0
print(is_ring(g))