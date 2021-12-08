from collections import deque, defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        q = deque([(k, 0)])
        seen = defaultdict(lambda: float('inf'))
        seen[k] = 0
        g = self.build_graph(times)

        while q:
            curr, cost = q.popleft()

            for nx, weight in g[curr]:
                if cost + weight < seen[nx]:
                    seen[nx] = cost + weight
                    q.append((nx, cost + weight))

        return max(seen.values()) if len(seen) == n else -1

    def build_graph(self, times):
        g = defaultdict(set)

        for u, v, w in times:
            g[u].add((v, w))

        return g
