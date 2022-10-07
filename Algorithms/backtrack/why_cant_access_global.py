n = 2
k = 6
target = 7

M = 1000000007


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        M = 1000000007
        res = 0

        def backtrack(cnt, target):
            global res
            if cnt > n:
                return

            if target == 0:
                res += 1

            for i in range(1, k + 1):
                backtrack(cnt + 1, target - i)

        backtrack(0, target)
        print(res)


s = Solution()
s.numRollsToTarget(n, k, target)
