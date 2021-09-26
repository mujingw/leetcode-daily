from functools import lru_cache
from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        @lru_cache(None)
        def dfs(root):
            if root in visited:
                return False

            visited.add(root)

            if root in terminals:
                return True

            return all(dfs(neig) for neig in graph[root])

        N = len(graph)
        terminals = set([i for i in range(N) if not graph[i]])
        visited = set()

        return [i for i in range(N) if dfs(i)]
