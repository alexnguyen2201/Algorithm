from collections import Counter


def find_abs_num_pair_less_than_k(nums, k) -> int:
    nums.sort()
    n = len(nums)
    count, i, j = 0, 0, 0
    while i < n or j < n:
        while j < n and nums[j] - nums[i] <= k:  # move fast pointer
            j += 1
        count += j - i - 1  # count pairs
        i += 1  # move slow pointer
    return count


def find_abs_num_pair_less_than_k_version_2(nums, k) -> int:
    nums.sort()
    count = slow = 0
    c = Counter(nums)
    for fast, val in enumerate(nums):
        while val - nums[slow] > k:
            slow += 1
        count += (fast - slow + 1) // 2
    return count


arr = [1, 2, 2, 2, 3, 3, 4]
K = 1
print(find_abs_num_pair_less_than_k(nums=arr, k=K))
print(find_abs_num_pair_less_than_k_version_2(nums=arr, k=K))

# Tại sao đều sử dụng 2-pointers nhưng check2 nhanh hơn check1??
