from collections import defaultdict
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.g = defaultdict(set)

        for u, v in edges:
            self.g[u].add(v)
            self.g[v].add(u)

        self.visited = set()
        res = 0

        for i in range(n):
            if i not in self.visited:
                self.dfs(i)
                res += 1

        return res

    def dfs(self, node):
        if node in self.visited:
            return

        self.visited.add(node)

        for ng in self.g[node]:
            self.dfs(ng)
