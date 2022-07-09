class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        if len(prices) == 2:
            return max(0, prices[1]-prices[0])

        y = [prices[i] - prices[i-1] for i in range(1, len(prices))]

        dp = [[0 for i in range(2)] for _ in range(len(y))]

        dp[0][0] = 0
        dp[0][1] = y[0]
        dp[1][0] = max(0, y[0])
        dp[1][1] = max(y[1], y[0] + y[1])

        for i in range(2, len(y)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            dp[i][1] = max(y[i] + dp[i-1][1], dp[i-2][0] + y[i])

        return max(dp[len(y)-1][0], dp[len(y)-1][1])
