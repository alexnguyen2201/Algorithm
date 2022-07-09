class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        f = [0] * (n+1)
        f0 = 0
        f1 = 1
        for i in range(1, n):
            f[i+1] = f1 + f0
            f0 = f1
            f1 = f[i+1]
            print(i+1, f[i+1])

        return f[n]


n = 4
s = Solution()
print(s.fib(n))
