nums = [3, 2, 1, 0, 4]


def can_jump_from_pos(pos, nums, memo):
    print(pos, nums, memo)
    if(memo[pos] != 0):
        if memo[pos] == 1:
            return True
        else:
            return False

    furthest_jump = max(pos + nums[pos], len(nums) - 1)
    print(pos, nums[pos], len(nums) - 1)
    for nexpos in range(pos + 1, furthest_jump + 1):
        if (can_jump_from_pos(nexpos, nums, memo)):
            memo[pos] = 1
            return True

    memo[pos] = -1
    return False


memo = [0 for i in range(len(nums))]
memo[len(nums) - 1] = 1
print(can_jump_from_pos(0, nums, memo))
