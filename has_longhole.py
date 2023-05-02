import networkx as nx
G = nx.Graph()
hashole1 = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 0), (3, 5), (5, 6), (6, 4),(6, 7),(4, 2)]#have
cycle1 = [(0,1),(0,2),(1,2),(1,3),(2,4),(5,3),(4,5)]#have
hashole2 = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5,0)] # have
hashole3 = [(0, 1), (2, 1), (2, 3),(3,0)] #dont have long hole
hashole4 = [(0, 1), (1, 2), (2, 3), (3, 4),(4, 5),(5,6),(6,0)] # hava
hashole5 = [(0, 1), (1, 2), (2, 3), (3, 4),(4, 5),(5,0),(2,5)] #not
hashole6 =[(0, 1), (1, 2), (2, 3), (3, 4),(4, 5),(5,0),(2,5),(2,6),(6,7),(7,8),(8,5)] # have
G.add_edges_from(hashole3)

not_in_hole = {}
in_path = {}
    
    
def has_longhole(G:nx):
    # Initialize not_in_hole and in_path
    for v in G.nodes():
        in_path[v]=0
        for edge in G.edges():
            not_in_hole[edge,v]=0
            not_in_hole[(edge[1],edge[0]),v]=0
            
    # Main loop
    for u in G.nodes():
        in_path[u] = 1
        for v,w in G.edges():
            if (u,v) in G.edges() or (v,u) in G.edges():
                if u not in (v,w) and not_in_hole[(u,v),w] == 0:
                    if (((u,v) in G.edges() or (v,u) in G.edges()) and ((u,w) not in G.edges() and (w,u) not in G.edges())):
                        in_path[v] = 1
                        if process(G, u, v, w):
                            return True
                        in_path[v] = 0                     
        in_path[u] = 0
    return False


def process(G, a, b, c):
    in_path[c] = 1
    for d in G.neighbors(c):
        if  ((d,a) not in G.edges() and (a,d) not in G.edges()) and ((d,b) not in G.edges() and (b,d) not in G.edges()):
            if in_path[d] == 1 :
                return True
            if not_in_hole[(b,c),d] == 0:
                if process(G, b, c, d):
                    return True
   
    in_path[c] = 0
    not_in_hole[(a,b),c] = 1
    not_in_hole[(b,c),a] = 1
    return False

print(has_longhole(G))