graph1 = {1: [], 2: [1], 3: [1]}
graph2 = {1: [2], 2: [3], 3: [1]}


def toposort(graph):
    visited = [False for _ in range(len(graph)+1)]
    result = []

    def DFS(node):
        if visited[node]:
            return
        visited[node] = True
        for adj in graph[node]:
            DFS(adj)
        result.append(node)

    for i in graph:
        DFS(i)

    return result


print(toposort(graph1)[::-1])
print(toposort(graph2)[::-1])
