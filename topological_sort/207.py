from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(temp, perm, g, curr):
            if temp[curr]:
                return False

            if perm[curr]:
                return True

            temp[curr] = True

            for neig in g[curr]:
                if not dfs(temp, perm, g, neig):
                    return False

            temp[curr] = False
            perm[curr] = True

            return True

        g = defaultdict(set)

        for course, prereq in prerequisites:
            g[prereq].add(course)

        temp = [False] * numCourses
        perm = [False] * numCourses

        for pre in list(g.keys()):
            if not dfs(temp, perm, g, pre):
                return False

        return True
