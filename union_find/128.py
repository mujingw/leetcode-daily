from collections import defaultdict
from typing import List


class UF:
    def __init__(self, size):
        self.rank = [0] * size
        self.parent = [i for i in range(size)]

    def union(self, u, v):
        ru, rv = self.find(u), self.find(v)

        if self.rank[ru] < self.rank[rv]:
            self.parent[ru] = rv
        elif self.rank[rv] < self.rank[ru]:
            self.parent[rv] = ru
        else:
            self.parent[rv] = ru
            self.rank[ru] += 1

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        lookup = {val: idx for idx, val in enumerate(nums)}
        N = len(nums)
        uf = UF(N)

        for num in nums:
            if num - 1 in lookup:
                uf.union(lookup[num], lookup[num - 1])

            if num + 1 in lookup:
                uf.union(lookup[num], lookup[num + 1])

        parents = defaultdict(int)

        for i in range(N):
            parents[uf.find(i)] += 1

        return max(parents.values())
