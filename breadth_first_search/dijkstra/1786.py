from collections import defaultdict, deque
from functools import lru_cache
from typing import List


class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        def build_graph(edges):
            g = defaultdict(set)

            for u, v, w in edges:
                g[u].add((v, w))
                g[v].add((u, w))

            return g

        def bfs(g, src):
            q = deque([(src, 0)])
            seen = {src: 0}

            while q:
                curr, dist = q.popleft()

                for v, w in g[curr]:
                    if v not in seen or dist + w < seen[v]:
                        seen[v] = dist + w
                        q.append((v, dist + w))

            return seen

        @lru_cache(None)
        def dfs(u):
            if u == 1:
                return 1

            res = 0

            for v, w in g[u]:
                if dist_lookup[u] < dist_lookup[v]:
                    res += dfs(v)

            return res

        MOD = 10 ** 9 + 7
        g = build_graph(edges)
        dist_lookup = bfs(g, n)

        return dfs(n) % MOD
