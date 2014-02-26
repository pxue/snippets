def iterative_dfs(graph, start):

    q = [start]
    path = []
    while q:
        node = q.pop(0)
        if node not in path:
            path = path+[node]
            q.append(graph[node])

    return path

