from heapq import heappop, heapify
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
            self.parent[ru] = rv
            self.rank[rv] += 1

    def find(self, x):
        if self.parent[x] == x:
            return x

        self.parent[x] = self.find(self.parent[x])

        return self.parent[x]


class Edge:

    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

    def __lt__(self, other):
        return self.w < other.w


class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        h = [Edge(u, v, w) for u, v, w in connections]
        heapify(h)
        edge_count, cost = 0, 0
        uf = UF()

        while edge_count < N - 1 and h:
            e = heappop(h)
            u, v, w = e.u, e.v, e.w
            uf.add(u)
            uf.add(v)

            if uf.find(u) == uf.find(v):
                continue

            edge_count += 1
            uf.union(u, v)
            cost += w

        return cost if edge_count == N - 1 else -1
