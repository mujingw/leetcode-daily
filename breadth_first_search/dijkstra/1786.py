from collections import defaultdict
from functools import lru_cache
from heapq import heappop, heappush
from typing import List


class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        self.g = self.build_graph(edges)
        self.dists = self.dijk(n)

        return self.dfs(n)

    @lru_cache(None)
    def dfs(self, u):
        if u == 1:
            return 1

        MOD = 10 ** 9 + 7
        res = 0

        for neig, w in self.g[u]:
            if self.dists[neig] > self.dists[u]:
                res += self.dfs(neig) % MOD

        return res % MOD

    def build_graph(self, edges):
        g = defaultdict(set)

        for u, v, w in edges:
            g[u].add((v, w))
            g[v].add((u, w))

        return g

    def dijk(self, start):
        h = [(0, start)]
        seen = defaultdict(lambda: float('inf'))
        seen[start] = 0

        while h:
            dist, curr = heappop(h)

            for neig, w in self.g[curr]:
                if seen[neig] > dist + w:
                    seen[neig] = dist + w
                    heappush(h, (dist + w, neig))

        return seen
