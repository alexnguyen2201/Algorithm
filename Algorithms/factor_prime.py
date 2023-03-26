import math


def primeFactors(n):
    if n < 0:
        n = n*(-1)
    prime_set = set()
    while n % 2 == 0:
        prime_set.add(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            prime_set.add(i)
            n = n // i

    if n > 2:
        prime_set.add(int(n))

    return prime_set


def union_prime_set(lst):
    prime_set = set()
    for num in lst:
        prime_set = prime_set.union(primeFactors(num))
    return prime_set


def sum_for_list(lst):
    prime_set = union_prime_set(lst)

    res = []
    for i in prime_set:
        total = 0
        for j in lst:
            if j % i == 0:
                total += j
        res.append([i, total])
    res = list(res)
    res.sort()
    return res


n = [15, 21, 24, 30, 45]
x = sum_for_list(n)
print(x)
