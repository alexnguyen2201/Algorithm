class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 1

        remain_arr = [nums[i] - nums[i-1] for i in range(1, len(nums)) if
                      nums[i] != nums[i-1]]

        if len(remain_arr) <= 1:
            return 1 + len(remain_arr)

        f = [0] * len(remain_arr)

        for i in range(len(remain_arr)-1):
            if remain_arr[i] * remain_arr[i+1] >= 0:
                f[i+1] = f[i] + 1
            else:
                f[i+1] = f[i]

        return 1 + len(remain_arr) - f[-1]
