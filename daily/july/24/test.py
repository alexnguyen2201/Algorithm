from bisect import bisect_right


def BinarySearch(a, x):
    i = bisect_right(a, x)
    if i:
        return (i-1)
    else:
        return -1


a = [1, 4, 5, 11, 15]
x = 5
res = BinarySearch(a, x)
print(res)
