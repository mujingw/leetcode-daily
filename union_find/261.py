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
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not len(edges) == n - 1:
            return False

        uf = UF(n)

        for u, v in edges:
            ru, rv = uf.find(u), uf.find(v)

            if ru != rv:
                uf.union(u, v)
            else:
                return False

        return True
