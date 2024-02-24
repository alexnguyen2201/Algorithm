# https://docs.python.org/3/library/bisect.html

from bisect import bisect, bisect_right, bisect_left

arr = [60, 70, 80, 90]
scores = [60, 61, 99]

for score in scores:
    idx = bisect(arr, score)
    idx_r = bisect_right(arr, score)
    idx_l = bisect_left(arr, score)

    print(idx, end=' ')
    print(idx_r, end=' ')
    print(idx_l)
