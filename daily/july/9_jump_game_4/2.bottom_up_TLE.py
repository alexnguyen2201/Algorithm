from typing import List
from math import inf


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            max_res = -inf

            for j in range(max(0, i-k), i):
                max_res = max(max_res, dp[j])

            dp[i] = max_res + nums[i]

        return dp[len(nums)-1]
