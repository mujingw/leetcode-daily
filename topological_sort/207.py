from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, N: int, pre: List[List[int]]) -> bool:
        self.visited, self.visiting = set(), set()
        self.g = self.build_graph(pre)

        return all(self.dfs(course) for course in range(N))

    def build_graph(self, pre):
        g = defaultdict(set)

        for course, prereq in pre:
            g[prereq].add(course)

        return g

    def dfs(self, node):
        if node in self.visited:
            return True

        if node in self.visiting:
            return False

        self.visiting.add(node)
        ok = all(self.dfs(ng) for ng in self.g[node])
        self.visiting.remove(node)
        self.visited.add(node)

        return ok
