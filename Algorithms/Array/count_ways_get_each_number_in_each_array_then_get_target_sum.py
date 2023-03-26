from collections import Counter, defaultdict
from typing import List


def sum_count(lsts: List[List[int]]) -> Counter:
    res = Counter({0: 1})
    for lst in lsts:
        temp = Counter()
        for a in lst:
            for total in res:
                temp[total + a] += res[total]
        res = temp
    return res


lsts = [
    [1, 2, 3],
    [6, 5, 4],
    [7, 4, 1],
    [12, 12, 12],
    [19, 19, 19]
]

res = sum_count(lsts)
print(res)
# Counter({45: 27, 44: 27, 43: 27, 42: 27, 41: 27, 40: 27, 39: 27, 46: 18, 38: 18, 47: 9, 37: 9})

# there are 9 ways to create sum = 37 by the way get each element in each array.