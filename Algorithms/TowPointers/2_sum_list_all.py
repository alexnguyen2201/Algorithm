from typing import List


def twoSum(nums: List[int], target: int) -> List[List[int]]:
    res = []
    lo, hi = 0, len(nums) - 1

    while (lo < hi):
        curr_sum = nums[lo] + nums[hi]
        if curr_sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
            lo += 1
        elif curr_sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
            hi -= 1
        else:
            res.append([nums[lo], nums[hi]])
            lo += 1
            hi -= 1

    return res
