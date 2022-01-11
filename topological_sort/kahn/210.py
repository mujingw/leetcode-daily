from collections import deque, defaultdict
from typing import List


class Solution:
    def findOrder(self, n: int, prereqs: List[List[int]]) -> List[int]:
        g = self.build_graph(prereqs)
        in_degrees = self.get_indegrees(prereqs)
        q = deque([x for x in range(n) if in_degrees[x] == 0])
        res = []
        courses_taken = 0

        while q:
            for _ in range(len(q)):
                curr = q.popleft()

                for neig in g[curr]:
                    in_degrees[neig] -= 1

                    if in_degrees[neig] == 0:
                        q.append(neig)

                courses_taken += 1
                res.append(curr)

        return res if courses_taken == n else []

    def build_graph(self, prereqs):
        g = defaultdict(set)

        for course, prereq in prereqs:
            g[prereq].add(course)

        return g

    def get_indegrees(self, prereqs):
        in_degrees = defaultdict(int)

        for course, prereq in prereqs:
            in_degrees[course] += 1

        return in_degrees
