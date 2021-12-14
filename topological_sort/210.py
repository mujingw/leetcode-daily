from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, N: int, pre: List[List[int]]) -> List[int]:
        self.visited, self.visiting = set(), set()
        self.g = self.build_graph(pre)
        self.res = deque([])

        for course in range(N):
            if not self.dfs(course):
                return []

        return list(self.res)

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

        self.res.appendleft(node)

        return ok
