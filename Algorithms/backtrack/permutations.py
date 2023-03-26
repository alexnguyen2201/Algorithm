def sol(A, B):
    arr = list('a' * A + 'b' * B)
    n = len(arr)
    res, path = set(), []

    def dfs(step):
        if step == n:
            res.add(tuple(arr))
            return

        for i in range(step, n):
            arr[i], arr[step] = arr[step], arr[i]
            dfs(i + 1)
            arr[i], arr[step] = arr[step], arr[i]

    dfs(0)
    res = [''.join(item) for item in res]
    return res


print("3, 5: ", sol(3, 5))
