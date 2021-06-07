from typing import List


class UF:
    def __init__(self, size):
        self.rank = [0] * size
        self.parent = [i for i in range(size)]

    def union(self, u, v):
        ru, rv = self.find(u), self.find(v)

        if ru < rv:
            self.parent[ru] = rv
        elif rv < ru:
            self.parent[rv] = ru
        else:
            self.parent[rv] = ru
            self.rank[ru] += 1

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        N = len(graph)
        uf = UF(N)

        for u in range(N):
            for v in graph[u]:
                if uf.find(v) == uf.find(u):
                    return False

                uf.union(v, graph[u][0])

        return True
