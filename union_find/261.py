from typing import List


class UF:
    def __init__(self, size):
        self.rank = {i: 1 for i in range(size)}
        self.parent = {i: i for i in range(size)}

    def union(self, u, v):
        ru, rv = self.find(u), self.find(v)

        if ru == rv:
            return False

        if self.rank[ru] < self.rank[rv]:
            self.parent[ru] = rv
        elif self.rank[rv] < self.rank[ru]:
            self.parent[rv] = ru
        else:
            self.parent[rv] = ru
            self.rank[ru] += 1

        return True

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])

        return self.parent[p]


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        uf = UF(n)

        return all(uf.union(u, v) for u, v in edges)
