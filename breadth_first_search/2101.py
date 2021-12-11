from collections import defaultdict, deque
from itertools import product
from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        g = self.build_graph(bombs)

        return max(self.bfs(g, x) for x in range(len(bombs)))

    def build_graph(self, bombs):
        N = len(bombs)
        g = defaultdict(set)

        for i, j in product(range(N), range(N)):
            if i == j:
                continue

            if self.reachable(bombs, i, j):
                g[i].add(j)

        return g

    def reachable(self, bombs, i, j):
        x1, y1, r1 = bombs[i]
        x2, y2, r2 = bombs[j]

        return (x2 - x1) ** 2 + (y2 - y1) ** 2 <= r1 ** 2

    def bfs(self, g, start):
        q = deque([start])
        seen = {start}
        count = 0

        while q:
            curr = q.popleft()
            count += 1

            for ng in g[curr]:
                if ng not in seen:
                    seen.add(ng)
                    q.append(ng)

        return count
