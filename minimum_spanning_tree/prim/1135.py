from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Edge:

    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

    def __lt__(self, other):
        return self.w < other.w


class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        cost = 0
        visited = {1}
        h = []
        g = defaultdict(set)

        for u, v, w in connections:
            if u == 1:
                heappush(h, Edge(u, v, w))

            g[u].add((v, w))
            g[v].add((u, w))

        while len(visited) < N and h:
            e = heappop(h)
            u, v, w = e.u, e.v, e.w

            if v in visited:
                continue

            visited.add(v)
            cost += w

            for nv, nw in g[v]:
                heappush(h, Edge(v, nv, nw))

        return cost if len(visited) == N else -1
