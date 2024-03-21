"""
Cho một dãy số arr, một số target
Chọn các số trong dãy số có tổng bé hoặc bằng target và tổng đó gần target nhất
Return tổng đó

Given an array arr, a number target
Select numbers in the array whose sum is less than or equal to target and is closest to the target
Return that sum
"""

nums = [1, 2, 7]
target = 5


def closest_sum(nums, target):
    dp = [0] * (target + 1)
    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] = max(dp[i], dp[i - num] + num)

    return dp[target]


print(closest_sum(nums, target))
