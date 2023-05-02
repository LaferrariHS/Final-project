import networkx as nx
import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt
from collections import deque
import itertools

g = nx.Graph()
w54=[(9,1),(9,2),(1,3),(2,3),(2,4),(3,4),(3,5),(4,5),(4,6),(5,6),(6,8),(5,7),(7,8),(2,5)]
g.add_edges_from(w54)

def MCS(g:nx):
    g1=deepcopy(g)
    n=len(g.nodes())
    order=[0]*n
    w={}
    s=-1  
    clique_generators=[]
    fill_edges=[]
    for key in g1.nodes():
        w[key]=0
    for i in range(n,0,-1):
        #filtered = filter(lambda value: value != 0, order)
        filt_Dict = { key:value for (key,value) in w.items() if key not in order}
        v=max(filt_Dict,key=filt_Dict.get)## picked unnumbered max weight vertex
        if w[v]<=s:
          clique_generators.append(v)
        s=w[v]
        reached={}
        for key in g1.nodes():
            if key==v:
                reached[key]=True
            else:
                reached[key]=False
        reach=[None]*n
        adj = []
        adj=list(g1.neighbors(v))
        for key in adj:
            if not reached[key]:
                reached[key]=True
            if(reach[w[key]]==None):
                reach[w[key]]=deque([])
            reach[w[key]].append(key)
        for j in range(n):
            while reach[j] !=None and len(reach[j])>0:
                u=reach[j][0]
                reach[j].popleft()
                for z in list(g1.neighbors(u)):
                    if not reached[z]:
                        reached[z]=True
                        if w[z]>j:
                            adj.append(z)
                            if(reach[w[z]]==None):
                               reach[w[z]]=deque([])  
                            reach[w[z]].append(z)
                        else :
                            reach[j].append(z)                        
        for u in adj:
            w[u]=w[u]+1
            fill_edges.append((v,u))
        order[i-1]=v
        g1.remove_node(v)
    new_graph = nx.Graph()
    new_graph.add_edges_from(fill_edges)
    return order,new_graph,clique_generators

def is_clique(g:nx,separator):
    temp=separator.copy()
    for i in separator:
        ng=g.neighbors(i)
        temp.remove(i)
        if not set(temp).issubset(ng):
            return False
        if len(temp)==1:
            break
    return True
    
def get_connections(g:nx,nodes):
        conn=[]
        temp=nodes.copy()
        for node in nodes:
            temp.remove(node)
            for t in temp:
                if g.has_edge(node,t):
                    conn.append((node,t))
        return conn

def cliqueCutsets(g:nx,fillin_graph:nx,clique_gen,order):
    g1=deepcopy(g)
    h1=deepcopy(fillin_graph)
    leafs=[]
    for x in order:
        if x in clique_gen:
            separator= list(h1.neighbors(x))
            if is_clique(g,separator):
                g1_copy=deepcopy(g1)
                for v in separator:
                    g1_copy.remove_node(v)
                c= list(set(g1_copy.neighbors(x)))# 
                g1_copy.remove_node(x)
                for u in c:
                    nlist=g1_copy.neighbors(u)
                    c=c+list(nlist)
                    g1_copy.remove_node(u)
                c=c+[x]   ### connected component containg x
                del g1_copy
                conn = get_connections(g1,c+separator)# getting edges for the leafs
                leaf_graph = nx.Graph()
                leaf_graph.add_edges_from(conn)
                leafs.append(leaf_graph)
                for v in c:
                     g1.remove_node(v)
        h1.remove_node(x)
    leafs.append(g1)
    return leafs

order,fillin_graph, clique_gen=MCS(g)## get fill-in graph with perfect elimination ordering.
print(fillin_graph.edges())
leaves=cliqueCutsets(g,fillin_graph,clique_gen,order)