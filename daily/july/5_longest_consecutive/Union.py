from typing import List


class UF:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.count = n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, p, q):
        p = self.find(p)
        q = self.find(q)
        if p == q:
            return
        if self.size[p] > self.size[q]:
            self.parent[q] = p
            self.size[p] += self.size[q]
        else:
            self.parent[p] = q
            self.size[q] += self.size[p]
        self.count -= 1

    def largest_group_size(self):
        largest_size = 0
        for i, x in enumerate(self.parent):
            if i != x:
                continue
            largest_size = max(largest_size, self.size[x])
        return largest_size


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num2index = {}
        uf = UF(len(nums))
        for i, num in enumerate(nums):
            if num in num2index:
                continue
            num2index[num] = i
            prev_ = num2index.get(num - 1)
            if prev_ is not None:
                uf.union(i, prev_)
            next_ = num2index.get(num + 1)
            if next_ is not None:
                uf.union(i, next_)
        return uf.largest_group_size()
