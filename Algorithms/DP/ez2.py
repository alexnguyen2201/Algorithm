def minCostClimbingStairs(cost) -> int:
    n = len(cost)
    f = [[0]*2]*n
    f[0][1] = 8
    print(f[2][1])
    print(f)


print(minCostClimbingStairs([10, 15, 20]))
