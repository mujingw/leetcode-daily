from collections import defaultdict
from heapq import heappush, heappop
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        h = []
        heappush(h, (0, k))
        seen = defaultdict(lambda: float('inf'))
        seen[k] = 0
        g = self.build_graph(times)

        while h:
            cost, curr = heappop(h)

            for nx, weight in g[curr]:
                if cost + weight < seen[nx]:
                    seen[nx] = cost + weight
                    heappush(h, (cost + weight, nx))

        return max(seen.values()) if len(seen) == n else -1

    def build_graph(self, times):
        g = defaultdict(set)

        for u, v, w in times:
            g[u].add((v, w))

        return g
