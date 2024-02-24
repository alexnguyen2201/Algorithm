from lctest import *

"""
[Medium] 581. Shortest Unsorted Continuous Subarray
https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
Created: 2022-05-03 14:25 (Tuesday)
Done   : 20 mins
Attempt: n | failed with case [1,3,2,2,2]
---------------------NOTE---------------------
Time: O(n)
Space: O(n)

Institution:
Keep a monotonic stack and not append if new number is less than the last number.
"""


# noinspection PyMethodMayBeStatic
@testcase(
    log(5, [2, 6, 4, 8, 10, 9, 15]),
    (0, [1, 2, 3, 4]),
    (5, [1, 2, 3, 4, 0]),
    log(4, [1, 3, 2, 2, 2]),
    (4, [1, 5, 2, 3, 2]),
    (0, [1, 2, 2, 2, 3]),
    (None, [6, 5, 4, 3, 2, 1])
)
class Solution:
    @solution
    def findUnsortedSubarray(self, nums):
        stack = [(-float('inf'), -1)]
        first = float('inf')
        last = -1
        for i, n in enumerate(nums):
            if n < stack[-1][0]:
                ma, ma_index = stack[-1]
                last = i
                while n < stack[-1][0]:
                    _, index = stack.pop()
                    if first > index:
                        first = index
                stack.append((ma, ma_index))
            else:
                stack.append((n, i))
        return last - first + 1 if first < last else 0

