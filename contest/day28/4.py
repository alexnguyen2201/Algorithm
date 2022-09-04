# 3
# [[1, 2], [2, 3], [3, 1], [2, 3]]
# [[2, 1]]

k = 3


rowConditions = [[1, 2], [2, 3], [3, 1]]
colConditions = [[2, 1]]
d_row = dict()
d_col = dict()

for i in range(1, k+1):
    d_row[i] = set()

for item in rowConditions:
    d_row[item[0]].add(item[1])

for i in d_row:
    d_row[i] = list(d_row[i])


for i in range(1, k+1):
    d_col[i] = set()

for item in colConditions:
    d_col[item[0]].add(item[1])

for i in d_row:
    d_col[i] = list(d_col[i])

print(d_row)
print(d_col)


def toposort(graph):
    visited = [False for _ in graph] + [False]
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


res_row = toposort(d_row)[::-1]
res_col = toposort(d_col)[::-1]
print(res_row)
print(res_col)
maxtrix = [[0 for i in range(k)] for j in range(k)]
print(maxtrix)

for i in range(1, k+1):
    i_row_index = res_row.index(i)
    i_col_index = res_col.index(i)
    maxtrix[i_row_index][i_col_index] = i

print(maxtrix)
