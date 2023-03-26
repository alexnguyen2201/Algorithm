from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 'low' and 'high' represent the range of values of the target
        def check(curr):
            count = sum(num <= curr for num in nums)

            return count > curr

        left = 1
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left


nums = [1, 3, 4, 2, 2]
s = Solution()
s.findDuplicate(nums)
