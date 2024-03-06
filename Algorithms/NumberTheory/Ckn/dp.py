def cnk(n, k):
    M = 1000000007
    f = [[0 for x in range(n-k + 1)] for _ in range(k + 1)]

    for i in range(k + 1):
        for j in range(n-k + 1):
            if j == 0 or i == 0:
                f[i][j] = 1
                continue

            f[i][j] = (f[i][j-1] % M + f[i-1][j] % M) % M

    return f[n-k][k]


print(cnk(4, 2))


def cnk(n, k):
    f = [[0] * (n-k + 1) for _ in range(k + 1)]

    for i in range(k + 1):
        for j in range(n-k + 1):
            if j == 0 or i == 0:
                f[i][j] = 1
                continue

            f[i][j] = f[i][j-1] + f[i-1][j]

    return f[n-k][k]


print(cnk(4, 2))