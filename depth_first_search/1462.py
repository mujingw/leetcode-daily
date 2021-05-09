from collections import defaultdict
from functools import lru_cache
from typing import List


class Solution:
    def checkIfPrerequisite(self, n: int, prereqs: List[List[int]], queries: List[List[int]]) -> List[bool]:
        @lru_cache(None)
        def dfs(src, dest):
            if src == dest:
                return True

            return any(dfs(neig, dest) for neig in g[src])

        g = defaultdict(set)
        res = []

        for course, pre in prereqs:
            g[course].add(pre)

        for u, v in queries:
            res.append(dfs(u, v))

        return res
