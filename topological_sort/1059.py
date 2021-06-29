from collections import defaultdict
from typing import List


class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = defaultdict(set)

        for u, v in edges:
            g[u].add(v)

        def dfs(curr, g, visiting, visited):
            if not g[curr]:
                return curr == destination

            if curr in visiting:
                return False

            visiting.add(curr)
            ok = all(dfs(neig, g, visiting, visited) for neig in g[curr])
            visiting.remove(curr)

            return ok

        return dfs(source, g, set(), set())
