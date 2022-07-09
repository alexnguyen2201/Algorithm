from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        def calculate(nums: List[int], index: int, is_up: bool) -> int:
            max_count = 0
            for i in range(index+1, len(nums)):
                if((is_up and nums[i] > nums[index]) or
                   (not is_up and nums[i] < nums[index])):
                    max_count = max(
                        max_count, 1 + calculate(nums, i, not is_up)
                    )
            return max_count

        if len(nums) < 2:
            return len(nums)
        return 1 + max(calculate(nums, 0, True), calculate(nums, 0, False))
