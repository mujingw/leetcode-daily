from collections import deque, defaultdict
from typing import List


class Solution:
    def canFinish(self, N: int, prereqs: List[List[int]]) -> bool:
        g = self.build_graph(prereqs)
        in_degrees = self.get_indegrees(prereqs, N)
        q = deque([x for x in range(N) if in_degrees[x] == 0])
        count = 0

        while q:
            curr = q.popleft()
            count += 1

            for neig in g[curr]:
                in_degrees[neig] -= 1

                if in_degrees[neig] == 0:
                    q.append(neig)

        return count == N

    def get_indegrees(self, prereqs, N):
        in_degrees = [0] * N

        for course, prereq in prereqs:
            in_degrees[course] += 1

        return in_degrees

    def build_graph(self, pre):
        g = defaultdict(set)

        for course, prereq in pre:
            g[prereq].add(course)

        return g
