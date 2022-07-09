from typing import List, Tuple


def bfs(grid, start) -> List[Tuple[int, int]]:
    """
    grid: 2D array, example: ["..........", "..*#...##."]
    start: Tuple(int, int), example: (1,2)
    return value: List[Tuple(int, int)], example: [(4, 4), (5, 4), (6, 4)]
    """
    queue = [[start]]
    # queue is a deque: List[List[Tuple[int, int]]]
    seen = set([start])
    # using set: "in" operator has O(1) complexity compare to list O(n)
    while queue:

        path = queue.pop(0)
        x, y = path[-1]
        if grid[x][y] == goal:
            return path
        for x_next, y_next in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if (
                0 <= x_next < height and 0 <= y_next < width
                and grid[x_next][y_next] != wall
                and (x_next, y_next) not in seen
            ):
                queue.append(path + [(x_next, y_next)])
                seen.add((x_next, y_next))


wall, clear, goal = "#", ".", "*"
width, height = 10, 5
grid = ["..........",
        "..*#...##.",
        "..##...#*.",
        ".....###..",
        "......*..."]
path = bfs(grid, (2, 5))

print(path)
