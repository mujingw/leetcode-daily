from collections import defaultdict
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        self.g = defaultdict(set)

        for u, v in edges:
            self.g[u].add(v)
            self.g[v].add(u)

        self.visited = set()
        self.dfs(0)

        return len(self.visited) == n

    def dfs(self, v):
        if v in self.visited:
            return

        self.visited.add(v)

        for x in self.g[v]:
            self.dfs(x)
