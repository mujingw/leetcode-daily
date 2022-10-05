from collections import defaultdict
from typing import List


class UF:

    def __init__(self):
        self.parent = defaultdict(int)
        self.rank = defaultdict(int)
        self.count = 0

    def add(self, x):
        if x in self.parent:
            return

        self.parent[x] = x
        self.rank[x] = 1
        self.count += 1

    def size(self):
        return self.count

    def union(self, u, v):
        ru, rv = self.find(u), self.find(v)

        if ru == rv:
            return

        if self.rank[ru] < self.rank[rv]:
            self.parent[ru] = rv
        elif self.rank[rv] < self.rank[ru]:
            self.parent[rv] = ru
        else:
            self.parent[rv] = ru
            self.rank[ru] += 1

        self.count -= 1

    def find(self, x):
        if x == self.parent[x]:
            return x

        self.parent[x] = self.find(self.parent[x])

        return self.parent[x]


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        N = len(stones)
        uf = UF()

        for i in range(N):
            uf.add(i)

            for j in range(i + 1, N):
                uf.add(j)
                x1, y1 = stones[i]
                x2, y2 = stones[j]

                if x1 == x2 or y1 == y2:
                    uf.union(i, j)

        return N - uf.size()
