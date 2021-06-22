from collections import defaultdict
from typing import List


class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = defaultdict(set)

        for u, v in edges:
            g[u].add(v)

        def dfs(curr, g, visited, visiting):
            if not g[curr]:
                return curr == destination

            visiting.add(curr)

            for neig in g[curr]:
                if neig in visiting:
                    return False

                if neig not in visited:
                    if not dfs(neig, g, visited, visiting):
                        return False

            visiting.remove(curr)
            visited.add(curr)

            return True

        return dfs(source, g, set(), set())
