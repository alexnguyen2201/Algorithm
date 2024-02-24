from collections import defaultdict, deque
from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        # build Graph

        d = defaultdict(list)

        for x, y in dislikes:
            d[x].append(y)
            d[y].append(x)

        print(d)
        color = [-1 for _ in range(n + 1)]
        print(color)

        def bfs(start):
            queue = deque([])
            queue.append(start)
            color[start] = 0
            while queue:
                node = queue.pop()
                print(node)
                for nei in d[node]:
                    if color[nei] != -1:
                        if color[nei] == color[node]:
                            return False
                    else:
                        color[nei] = 1 - color[node]
                        queue.append(nei)
            return True

        # for start in dislikes
        for start in range(1, n + 1):
            if color[start] == -1:
                if not bfs(start):
                    return False
        return True


solution = Solution()
n = 4
dislikes = [[1, 2], [1, 3], [2, 4]]
print(solution.possibleBipartition(n, dislikes))
