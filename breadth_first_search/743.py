from collections import defaultdict
from heapq import heappush, heappop
from typing import List


class Solution:

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        h = []
        heappush(h, (0, k))
        seen = {k: 0}
        g = defaultdict(set)

        for u, v, w in times:
            g[u].add((v, w))

        while h:
            cost, curr = heappop(h)
            seen[curr] = min(cost, seen[curr])

            for nx, weight in g[curr]:
                if nx in seen:
                    if cost + weight >= seen[nx]:
                        continue

                seen[nx] = cost + weight
                heappush(h, (cost + weight, nx))

        return max(seen.values()) if len(seen) == n else -1
