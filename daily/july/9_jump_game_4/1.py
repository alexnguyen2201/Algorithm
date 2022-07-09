from collections import deque

nums = [1, 3, 5, 7, 4, 5, 9, 5]
k = 4
min_range = []
queue = deque([])

print(queue)

for i in range(len(nums)):
    while queue and nums[queue[-1]] >= nums[i]:
        queue.pop()

    queue.append(i)

    if queue[0] + k <= i:
        queue.popleft()

    if i >= k-1:
        min_range.append(nums[queue[0]])

    print(queue, min_range)
