from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(res, curr, g, temp, perm):
            if temp[curr]:
                return False

            if perm[curr]:
                return True

            temp[curr] = True

            for neig in g[curr]:
                if not dfs(res, neig, g, temp, perm):
                    return False

            temp[curr] = False
            perm[curr] = True
            res.append(curr)

            return True

        g = defaultdict(set)

        for course, pre in prerequisites:
            g[pre].add(course)

        temp = [False] * numCourses
        perm = [False] * numCourses
        res = []

        for course in list(g.keys()):
            if not dfs(res, course, g, temp, perm):
                return []

        s = set(res)

        for i in range(numCourses):
            if i not in s:
                res.append(i)

        return res[::-1]
