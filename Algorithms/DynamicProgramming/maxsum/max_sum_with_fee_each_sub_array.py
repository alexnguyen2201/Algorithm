class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) == 1:
            return 0
        if len(prices) == 2:
            return max(0, prices[1]-prices[0] - fee)
        y = [prices[i] - prices[i-1] for i in range(1, len(prices))]
        f = [[0 for i in range(2)] for _ in range(len(prices))]

        f[0][0] = 0
        f[0][1] = y[0] - fee
        f[1][0] = max(f[0][0], f[0][1])
        f[1][1] = max(f[0][1] + y[1], f[0][0] + y[1] - fee)

        for i in range(2, len(y)):
            f[i][0] = max(f[i-1][0], f[i-1][1])
            f[i][1] = max(f[i-1][1] + y[i], f[i-1][0] + y[i] - fee)

        return max(f[len(y)-1][0], f[len(y)-1][1])
