from collections import defaultdict
from functools import lru_cache
from typing import List


class Solution:
    def canFinish(self, N: int, pre: List[List[int]]) -> bool:
        g = defaultdict(set)
        visiting = set()

        @lru_cache(None)
        def dfs(node):
            if node in visiting:
                return False

            visiting.add(node)
            ok = all(dfs(neig) for neig in g[node])
            visiting.remove(node)

            return ok

        for course, prereq in pre:
            g[prereq].add(course)

        return all(dfs(course) for course in range(N))
