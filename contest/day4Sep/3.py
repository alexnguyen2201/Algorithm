nums = [84139415, 693324769, 614626365, 497710833, 615598711, 264, 65552, 50331652, 1, 1048576, 16384, 544,
        270532608, 151813349, 221976871, 678178917, 845710321, 751376227, 331656525, 739558112, 267703680]

# dp = [1 for _ in range(len(nums))]

# for i in range(1, len(dp)):
#     flag = 0

#     for j in range(i-1, i - dp[i-1] - 1, -1):
#         if nums[j] & nums[i] != 0:
#             dp[i] = 1
#             flag = 1
#             break

#     if flag == 0:
#         dp[i] = dp[i-1] + 1
#     else:
#         dp[i] = 1

# for i in range(len(dp)):
#     print(i, dp[i])

# print(max(dp))


def longestNiceSubarray(self, nums: List[int]) -> int:
    lo, mask, ans = -1, 0, 1
    for hi, n in enumerate(nums):
        while (mask & n):
            lo += 1
            mask ^= nums[lo]
        mask |= n
        ans = max(ans, hi - lo)
    return ans
