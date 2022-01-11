from collections import deque, defaultdict
from typing import List


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        indegree, g = defaultdict(int), defaultdict(set)
        courses_taken, semesters = 0, 0

        for prev, curr in relations:
            g[prev].add(curr)
            indegree[curr] += 1

        q = deque([node for node in range(1, n + 1) if indegree[node] == 0])

        while q:
            size = len(q)

            for _ in range(size):
                curr = q.popleft()
                courses_taken += 1

                for neig in g[curr]:
                    indegree[neig] -= 1

                    if indegree[neig] == 0:
                        q.append(neig)

            semesters += 1

        return semesters if courses_taken == n else -1
