nums = [4, 5, 2, 1]
queries = [3, 10, 21]
nums.sort()
print(nums)


def cnt(nums, query):

    curr = 0
    count = 0
    for i in nums:
        curr += i
        count += 1
        if curr > query:
            return count - 1

    return count


for i in queries:
    return cnt(nums, i)
