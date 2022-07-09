from typing import List


def rob(nums: List[int]) -> int:
    n = len(nums)
    f = [[0 for x in range(2)] for y in range(n)]
    print(f)
    f[0][0] = 0
    f[0][1] = nums[0]

    for i in range(1, n):
        f[i][0] = max(f[i-1][0], f[i-1][1])
        f[i][1] = f[i-1][0] + nums[i]

    return max(f[n-1][0], f[n-1][1])


print(rob([2, 1, 1, 2]))
