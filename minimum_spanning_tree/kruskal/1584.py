from heapq import heappush, heappop
from typing import List


class UF:

    def __init__(self):
        self.parent = {}

    def add(self, x):
        if x in self.parent:
            return

        self.parent[x] = x

    def union(self, u, v):
        root_u, root_v = self.find(u), self.find(v)

        if root_u == root_v:
            return

        self.parent[root_u] = root_v

    def find(self, x):
        if self.parent[x] == x:
            return x

        return self.find(self.parent[x])


class Edge:

    def __init__(self, u, v):
        self.u = u
        self.v = v
        self.weight = abs(u.x - v.x) + abs(u.y - v.y)

    def __lt__(self, other):
        return self.weight < other.weight


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return other.x == self.x and other.y == self.y

    def __hash__(self):
        return hash((self.x, self.y))


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        h = []
        uf = UF()
        edge_count = 0
        res = 0
        self._push_edges(h, points)

        while edge_count < len(points) - 1:
            edge = heappop(h)
            u, v = edge.u, edge.v
            uf.add(u)
            uf.add(v)
            ru, rv = uf.find(u), uf.find(v)

            if ru == rv:
                continue

            edge_count += 1
            uf.union(u, v)
            res += edge.weight

        return res

    def _push_edges(self, h, points):
        N = len(points)

        for i in range(N):
            u = Point(points[i][0], points[i][1])

            for j in range(i + 1, N):
                v = Point(points[j][0], points[j][1])
                heappush(h, Edge(u, v))
