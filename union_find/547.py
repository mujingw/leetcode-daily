from typing import List


class UF:
    def __init__(self, size):
        self.rank = [0] * size
        self.parent = [i for i in range(size)]

    def union(self, u, v):
        if u != v:
            ru, rv = self.find(u), self.find(v)

            if self.rank[ru] < self.rank[rv]:
                self.parent[rv] = ru
            elif self.rank[rv] < self.rank[ru]:
                self.parent[ru] = rv
            else:
                self.parent[rv] = ru
                self.rank[ru] += 1

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        uf = UF(N)

        for i in range(N):
            for j in range(N):
                if isConnected[i][j] == 1:
                    uf.union(i, j)

        parents = set()

        for i in range(N):
            p = uf.find(i)

            if p not in parents:
                parents.add(p)

        return len(parents)
