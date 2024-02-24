# flake8: noqa
# https://stackoverflow.com/questions/55316735/shortest-path-in-a-grid-using-bfs

def find_path_bfs(s, e, grid):
    queue = [(s, [])]  # start point, empty path

    while len(queue) > 0:
        node, path = queue.pop(0)
        path.append(node)
        mark_visited(node, v)

        if node == e:
            return path

        adj_nodes = get_neighbors(node, grid)
        for item in adj_nodes:
            if not is_visited(item, v):
                queue.append((item, path[:]))

    return None  # no path found
