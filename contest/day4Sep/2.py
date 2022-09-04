# class Solution:
#     def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
#         if (k + endPos - startPos) % 2 != 0:
#             return 0

#         positive = (k + endPos - startPos) // 2
#         negative = k - positive

#         M = 1000000007
#         f = [[0 for x in range(negative + 1)] for _ in range(positive + 1)]

#         for i in range(positive + 1):
#             for j in range(negative + 1):
#                 if j == 0 or i == 0:
#                     f[i][j] = 1
#                 if i == 1 and j == 1:
#                     f[i][j] = 2
#                 else:
#                     f[i][j] = (f[i][j-1] % M + f[i-1][j] % M) % M

#         print(f[positive][negative])
from functools import lru_cache


class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        M = 1000000007

        if (k + endPos - startPos) % 2 != 0:
            return 0

        positive = (k + endPos - startPos) // 2
        negative = k - positive
        if negative < 0:
            return 0

        @lru_cache
        def cal(pos, neg):
            if neg == 0 or pos == 0:
                return 1

            return (cal(pos, neg - 1) % M + cal(pos - 1, neg) % M) % M

        print(positive, negative)
        return cal(positive, negative)


s = Solution()
s.numberOfWays(1, 10, 3)
