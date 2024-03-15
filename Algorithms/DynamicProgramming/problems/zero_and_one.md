https://leetcode.com/problems/ones-and-zeroes/?envType=list&envId=55ac4kuc

# bottom up
```python
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:            
        dp = [[0] * (n+1) for _ in range(m+1)]
        counter=[[s.count("0"), s.count("1")] for s in strs]
        
        for zeroes, ones in counter:
            for i in range(m, zeroes-1, -1):
                for j in range(n, ones-1, -1):                   
                    dp[i][j] = max(dp[i][j], 1+dp[i-zeroes][j-ones])
        
        return dp[-1][-1]
```

use reverse order loop (of m,n) to prevent use duplicated str in strs.

## top down
```python

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counter=[[s.count("0"), s.count("1")] for s in strs]
        
        @cache
        def dp(i,j,idx):
            if i<0 or j<0:
                return -math.inf
            
            if idx==len(strs):
                return 0
            
            return max(dp(i,j,idx+1), 1 + dp(i-counter[idx][0], j-counter[idx][1], idx+1))
        return dp(m,n,0)
```

## backtrack with memo:
```python
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        res = [0]
        memo = set()
        def dfs(st, zeros, ones, cnt):
            if (zeros, ones, cnt) not in memo:
                res[0] = max(res[0], cnt)
                if zeros or ones:
                    for s in st:
                        if st[s] and cntr[s]["0"] <= zeros and cntr[s]["1"] <= ones:
                            st[s] -= 1
                            dfs(st, zeros - cntr[s]["0"], ones - cntr[s]["1"], cnt + 1)
                            st[s] += 1
                memo.add((zeros, ones, cnt))
                
        cntr = {s:Counter(s) for s in strs}
        dfs(Counter(strs), m, n, 0)
        return res[0]
```