import timeit
from collections import OrderedDict

d = {k: k for k in range(100000)}

d2 = OrderedDict(d)

i = 0
j = 0


def f1():
    global i
    del d[i]
    i += 1


def f2():
    global j
    del d2[j]
    j += 1


print(timeit.timeit(f1, number=100000))
print(timeit.timeit(f2, number=100000))
