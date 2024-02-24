"""
Sử dụng luôn grid để đánh dấu, vậy ta không cần sử dụng thêm một set là seen
=> giảm bộ nhớ
Nhưng phải chuyển phần tìm thấy goal vào vòng lặp luôn trước khi đánh dấu vì
đã dùng grid để đánh dấu thì sẽ không còn grid[x][y] == goal
"""

from collections import deque
from typing import List, Tuple


def bfs(grid, start) -> List[Tuple[int, int]]:
    """
    grid: 2D array, example: ["..........", "..*#...##."]
    start: Tuple(int, int), example: (1,2)
    return value: List[Tuple(int, int)], example: [(4, 4), (5, 4), (6, 4)]
    """
    queue = deque([[start]])
    # queue is a deque: List[List[Tuple[int, int]]]
    while queue:
        rows = len(grid)
        cols = len(grid[0])

        path = queue.popleft()
        x, y = path[-1]

        for x_next, y_next in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if (
                0 <= x_next < rows and 0 <= y_next < cols
                and grid[x_next][y_next] in (clear, goal)
            ):
                if grid[x_next][y_next] == goal:
                    return path + [(x_next, y_next)]
                queue.append(path + [(x_next, y_next)])
                grid[x_next][y_next] = 0


wall, clear, goal = "#", ".", "*"


grid = ["..........",
        "..*#...##.",
        "..##...#*.",
        ".....###..",
        "......*..."]

grid = [list(row) for row in grid]

path = bfs(grid, (2, 5))

print(path)
