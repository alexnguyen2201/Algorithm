from calendar import c
from collections import Counter
from heapq import nlargest

nums = [1, 1, 1, 2, 2, 3]
k = 2
count = Counter(nums)
print(count.keys())
print(count.get)
print(nlargest(k, count.keys(), count.get))
