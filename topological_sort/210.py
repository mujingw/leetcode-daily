from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, N: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(res, curr, g, visited, visiting):
            if curr in visiting:
                return False

            if curr in visited:
                return True

            visiting.add(curr)

            for neig in g[curr]:
                if not dfs(res, neig, g, visited, visiting):
                    return False

            visiting.remove(curr)
            visited.add(curr)
            res.append(curr)

            return True

        g = defaultdict(set)
        res = []

        for course, pre in prerequisites:
            g[pre].add(course)

        visited, visiting = set(), set()

        for course in list(g.keys()):
            if not dfs(res, course, g, visited, visiting):
                return []

        s = set(res)

        for i in range(N):
            if i not in s:
                res.append(i)

        return res[::-1]
