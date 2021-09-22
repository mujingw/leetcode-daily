from itertools import product
from typing import List


class UF:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.count = 0

    def add(self, x):
        if x in self.parent or x in self.rank:
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
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]


class Solution:
    def findCircleNum(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        uf = UF()

        for r, c in product(range(R), range(C)):
            if grid[r][c] == 1:
                uf.add(r)
                uf.add(c)
                uf.union(r, c)

        return uf.size()
