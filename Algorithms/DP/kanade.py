import math


def kadane(gen):
    # Maximum non-empty subarray sum
    ans = cur = -math.inf
    for x in A:
        cur = x + max(cur, 0)
        ans = max(ans, cur)
    print(ans)
    return ans


A2 = [3, -5]

print(kadane(A2))
