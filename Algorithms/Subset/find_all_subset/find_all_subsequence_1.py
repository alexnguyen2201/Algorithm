nums = [1, 2, 2, 3]

n = len(nums)
output = [[]]

for num in nums:
    output += [curr + [num] for curr in output]

print(output)
