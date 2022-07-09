from typing import List
from functools import cache


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)

        @cache
        def jump(i):
            if i == n-1:
                return nums[i]

            return max(
                nums[i] + jump(j) for j in range(i+1, min(n-1, i+k) + 1)
            )

        return jump(0)
