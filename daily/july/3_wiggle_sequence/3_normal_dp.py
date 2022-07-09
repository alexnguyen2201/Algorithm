from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        up = [0] * len(nums)
        down = up.copy()

        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    up[i] = max(up[i], down[j] + 1)
                elif nums[i] < nums[j]:
                    down[i] = max(down[i], up[j] + 1)

        return 1 + max(down[-1], up[-1])
