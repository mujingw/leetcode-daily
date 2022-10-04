from collections import deque, defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = self.build_graph(times)
        q = deque([(k, 0)])
        seen = defaultdict(lambda: float('inf'))
        seen[k] = 0

        while q:
            curr, dist = q.popleft()

            for neig, weight in g[curr]:
                if seen[neig] > dist + weight:
                    seen[neig] = dist + weight
                    q.append((neig, dist + weight))

        return max(seen.values()) if len(seen) == n else -1

    def build_graph(self, times):
        g = defaultdict(list)

        for u, v, w in times:
            g[u].append((v, w))

        return g
