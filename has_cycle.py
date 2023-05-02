def cycle_DFS(graph, v, visited, parent):
    visited[v] = True
    for i in range(len(graph)):
        if graph[v][i] == 1:
            if visited[i] == False:
                if cycle_DFS(graph, i, visited, v) == True:
                    return True
            elif parent != i:
                return True
    return False

def has_cycle(graph):
    visited = [False] * len(graph)
    for i in range(len(graph)):
        if visited[i] == False:
            if cycle_DFS(graph, i, visited, -1) == True:
                return True
    return False

if __name__ == "__main__":
    graph = [
        [0, 1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    if has_cycle(graph):
        print("Yes")
    else:
        print("No")
        