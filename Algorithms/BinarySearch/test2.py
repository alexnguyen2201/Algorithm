from bisect import bisect, bisect_left, bisect_right

nums = [-1, 0, 3, 5, 9, 12]
target = 9
index1 = bisect(nums, target)
index2 = bisect_left(nums, target)
index3 = bisect_right(nums, target)

print(index1)
print(index2)
print(index3)
