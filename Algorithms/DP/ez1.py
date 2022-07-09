def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2

    f1 = 1
    fn_1 = 2
    fn = 2
    for i in range(3, n + 1):
        fn = fn_1 + f1
        f1 = fn_1
        fn_1 = fn

    return fn


print(climbStairs(4))
