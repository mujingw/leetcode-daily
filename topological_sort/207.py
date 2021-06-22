from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, N: int, pre: List[List[int]]) -> bool:
        def dfs(node, visited, visiting):
            if node in visiting:
                return False

            if node in visited:
                return True

            visiting.add(node)

            for neig in g[node]:
                if not dfs(neig, visited, visiting):
                    return False

            visiting.remove(node)
            visited.add(node)

            return True

        g = defaultdict(set)

        for course, prereq in pre:
            g[prereq].add(course)

        return all(dfs(course, set(), set()) for course in range(N))
