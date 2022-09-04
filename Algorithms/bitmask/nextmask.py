def next_popcount(n):

    c = (n & -n)
    r = n + c
    return (((r ^ n) >> 2) // c) | r


first = (1 << 3) - 1

for i in range(10):

    print(bin(first))
    first = next_popcount(first)
