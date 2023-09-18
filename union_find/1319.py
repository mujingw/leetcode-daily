from typing import List


class UF:

    def __init__(self):
        self.parent = {}
        self.rank = {}

    def add(self, x):
        if x in self.parent:
            return

        self.parent[x] = x
        self.rank[x] = 1

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

    def find(self, x):
        if self.parent[x] == x:
            return x

        self.parent[x] = self.find(self.parent[x])

        return self.parent[x]


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        k = len(connections)

        if k < n - 1:
            return -1

        uf = UF()

        for x in range(n):
            uf.add(x)

        for u, v in connections:
            uf.union(u, v)

        groups = set(uf.find(x) for x in range(n))

        return len(groups) - 1
