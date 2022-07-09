class Solution:

    def longestConsecutive(self, nums):
        num_set = set(nums)
        best = 0

        for num in num_set:
            if num - 1 not in num_set:
                next_num = num + 1

                while next_num in num_set:
                    next_num += 1

                best = max(best, next_num - num)

        return best
