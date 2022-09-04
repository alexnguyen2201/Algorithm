graph1 = [[1], [], [1]]


def toposort(graph):
    res, found = [], [0] * len(graph)
    stack = list(range(len(graph)))
    print(stack)
    while stack:
        node = stack.pop()
        print(node)
        if node < 0:
            res.append(~node)
        elif not found[node]:
            print(node)
            found[node] = 1
            stack.append(~node)
            print(stack)
            stack += graph[node]

            print(stack)

    # cycle check
    for node in res:
        if any(found[nei] for nei in graph[node]):
            return None
        found[node] = 0

    return res[::-1]


print(toposort(graph1))
