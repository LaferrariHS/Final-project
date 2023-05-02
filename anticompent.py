import networkx as nx
import numpy as np
import itertools

g = nx.Graph()
connt = [(1,2),(2,3),(2,4),(4,5),(4,6),(5,7),(4,8),(9,10),(10,11)]
connections=[('a','b'),('a','c'),('a','e'),('b','d'),('b','e'),('c','e'),('c','d'),('d','e')]
connections2=[('a', 'c'),
                   ('a', 'd'),('a','f'), ('b', 'c'),('b', 'g'),('c','h'),('c','f'),('c', 'd'),  ('d', 'e')
                   ,('d','i'),('d','f'),('e','j'),('g','h'),('h','k'),('k','i'),('i','j')]
connections1=[('a', 'b'),(1,2),(2,3),(4,5),(5,6),(6,4)]
connections3=[(1,2),(2,3),(3,4),(4,1)]
g.add_edges_from(connt)


H = nx.complement(g)

A=np.array(nx.adjacency_matrix(g).todense())

def connected_components(g:nx):
    visited = set()
    components = []

    for node in g.nodes():
        if node not in visited:
            component = set()
            stack = [node]

            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    component.add(node)
                    for neighbor in g.neighbors(node):
                        stack.append(neighbor)
            components.append(component)
    return components

#Since you need to find the largest, search in reverse order
def get_anticompent(g:nx):
    complement_g = nx.complement(g)
    components = connected_components(complement_g)
    largest_component_size = 0
    largest_subgraphs = []
    
    # Find the set of nodes with the largest connected component
    largest_component_size = max(len(component) for component in components)
    # Generate all max-connected induced subgraphs
    for component in components:
        if len(component) == largest_component_size:
            largest_subgraph = g.subgraph(component)
            largest_subgraphs.append(largest_subgraph)
    return largest_component_size,largest_subgraphs

