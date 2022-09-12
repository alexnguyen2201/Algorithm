import heapq
from collections import defaultdict
d = defaultdict(list)
intervals = [[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]

intervals.sort()

pq = []
for interval in intervals:

    heapq.heappush(pq, interval[1])

    if interval[0] > pq[0]:
        heapq.heappop(pq)

print(pq)
