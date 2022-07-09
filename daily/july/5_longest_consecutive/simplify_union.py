from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums, prev = set(nums), dict()

        def find(n):
            if n in prev and prev[n] != n-1:
                return prev[n]
            if n-1 in nums:
                prev[n] = find(n-1)
                return prev[n]
            else:
                return n-1

        best = 0
        for i in nums:

            best = max(best, i - find(i))
            print("i: {}, prev: {}".format(i, prev))

        return best


nums = [100, 4, 200, 1, 3, 2]
s = Solution()
s.longestConsecutive(nums)
