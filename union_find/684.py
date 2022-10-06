from collections import defaultdict
from typing import List


class UF:
    def __init__(self):
        self.parent = defaultdict(int)
        self.rank = defaultdict(int)

    def add(self, x):
        if x in self.parent:
            return

        self.parent[x] = x
        self.rank[x] = 1

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
        if self.parent[x] == x:
            return x

        self.parent[x] = self.find(self.parent[x])

        return self.parent[x]


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UF()

        for u, v in edges:
            uf.add(u)
            uf.add(v)
            root_u, root_v = uf.find(u), uf.find(v)

            if root_u != root_v:
                uf.union(u, v)
            else:
                return [u, v]
