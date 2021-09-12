from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def reachableNodes(self, edges: List[List[int]], max_moves: int, n: int) -> int:
        g = defaultdict(dict)

        for u, v, w in edges:
            g[u][v] = w
            g[v][u] = w

        pq = [(-max_moves, 0)]
        seen = defaultdict(int)
        seen[0] = max_moves

        while pq:
            moves_left, curr = heappop(pq)

            for neig in g[curr]:
                updated_moves_left = -moves_left - g[curr][neig] - 1

                if ((neig not in seen) or seen[neig] < updated_moves_left) and updated_moves_left >= 0:
                    heappush(pq, (-updated_moves_left, neig))
                    seen[neig] = updated_moves_left

        res = len(seen)

        for u, v, w in edges:
            res += min(seen[u] + seen[v], g[u][v])

        return res
