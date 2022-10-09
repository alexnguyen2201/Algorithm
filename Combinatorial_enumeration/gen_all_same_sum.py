for n in range(1, 10):
    curr_list = []
    res = []

    def dfs(start):
        if sum(curr_list) == n:
            res.append(curr_list[:])
        for end in range(start, n):
            curr_list.append(end + 1 - start)
            dfs(end + 1)
            curr_list.pop()

    dfs(0)

    print(len(res))
