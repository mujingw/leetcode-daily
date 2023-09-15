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
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        self.N = n
        all_edges = [Edge(u, v, w) for u, v, w in edges]
        C = self.build_mst(all_edges[:], 0, UF(), 0)
        critical, pseudo = [], []

        for i, e in enumerate(all_edges):
            curr_edges = all_edges[:i] + all_edges[i + 1:]
            cost = self.build_mst(curr_edges[:], 0, UF(), 0)

            if cost != C:
                critical.append(i)
            else:
                uf = UF()
                uf.add(e.u)
                uf.add(e.v)
                uf.union(e.u, e.v)
                new_cost = self.build_mst(curr_edges[:], e.w, uf, 1)

                if new_cost == C:
                    pseudo.append(i)

        return [critical, pseudo]

    def build_mst(self, edges, init_cost, init_uf, init_edge_count):
        heapify(edges)
        cost = init_cost
        uf = init_uf
        edge_count = init_edge_count

        while edge_count < self.N - 1 and edges:
            e = heappop(edges)
            u, v, w = e.u, e.v, e.w
            uf.add(u)
            uf.add(v)

            if uf.find(u) == uf.find(v):
                continue

            cost += w
            uf.union(u, v)
            edge_count += 1

        return cost
