https://leetcode.com/problems/coin-change/description/?envType=list&envId=55ac4kuc

# topdown:
```python
class Solution:
    def coinChange(self, coins, amount):
        def help(amount):
            if amount == 0:
                return 0
        
            if dp[amount] != -1:
                return dp[amount]
        
            mini = float("inf")
        
            for coin in coins:
                if amount >= coin:
                    ans = help(amount - coin)
                    if ans != float("int"):
                        mini = min(1 + ans, mini)
        
            dp[amount] = mini
            return mini
        
        dp = [-1] * (amount + 1)
        
        ans = help(amount)
        
        return -1 if ans == float('inf') else ans
```


# bottom up:
```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount

        for i in range(amount + 1):
            for coin in coins:
                if i > coin:
                    dp[i] = min(dp[i], dp[i - coin])
        
        return dp[amount] if dp[amount] != float('inf') else -1
```

# optima using special |=, >>
```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        coins = [c for c in coins if c <= amount]
        if not coins: return -1
        if len(coins) < 2:
            ret = amount // coins[0]
            return -1 if amount - ret * coins[0] else ret

        if amount & 1 and not any(c & 1 for c in coins):
            return -1

        seen = 1 << amount
        for step in range(1, amount):
            cur = seen
            for coin in coins:
                cur |= seen >> coin
            if cur & 1:
                return step
            if cur == seen:
                return -1
            seen = cur
```
