from bisect import bisect
from typing import List


class Solution:
    def nextPermutation(self, arr: List[int]) -> None:
        arr = list(arr)
        n = len(arr)
        i = n - 1
        j = n - 1

        while i > 0 and arr[i] <= arr[i - 1]:
            i -= 1
        if i == 0:
            arr.reverse()
            return

        k = i - 1
        while arr[k] >= arr[j]:
            j -= 1
        arr[k], arr[j] = arr[j], arr[k]

        l = k + 1
        r = n - 1
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

        return ''.join(arr)


s = Solution()
print(s.nextPermutation('aebc'))


# Pythonic:

def gen_next(num: List[int]):
    num = [int(n) for n in num]
    i = len(num) - 2
    while num[i] >= num[i + 1]:
        i -= 1
    after = list(sorted(num[i:]))
    t = bisect(after, num[i])
    num[i:] = [after.pop(t)] + after


def gen_next2(num):
    num = list(num)
    i = len(num) - 2
    while num[i] >= num[i + 1]:
        i -= 1
    after = list(sorted(num[i:]))
    t = bisect(after, num[i])
    num[i:] = [after.pop(t)] + after

    return ''.join(num)


print(gen_next2('aeabca'))
