from typing import List


def rob_simple(self, nums: List[int]) -> int:
    t1 = 0
    t2 = 0
    for current in nums:
        temp = t1
        t1 = max(current + t2, t1)
        t2 = temp

    return t1
