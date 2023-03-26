def primes_method5(n):
    out = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p] and sieve[p] % 2 == 1:
            out.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return out


print(primes_method5(1000))
print(len(primes_method5(1000)))
