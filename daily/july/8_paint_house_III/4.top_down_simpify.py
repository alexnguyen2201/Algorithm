from functools import cache
from math import inf


class Solution:

    def minCost(self, houses, cost, m, n, target):
        @cache
        def dp(i, nc, c):
            if i == len(houses):
                return 0 if nc == target else inf

            if nc > target:
                return inf

            if houses[i] != 0:
                return dp(i + 1, nc + int(houses[i] != c), houses[i])

            return min(
                cost[i][j-1] + dp(i+1, nc + int(j != c), j)
                for j in range(1, n+1)
            )

        answer = dp(0, 0, 0)
        return (answer, -1)[answer == inf]


houses = [0, 0, 2, 3]
cost = [[5, 4, 1], [1, 2, 1], [4, 4, 2], [5, 2, 5]]
m = 4
n = 3
target = 4
s = Solution()
print(s.minCost(houses, cost, m, n, target))
