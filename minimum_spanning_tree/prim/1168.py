from collections import defaultdict
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        seen, graph = set(), defaultdict(dict)

        for u, v, w in pipes:
            graph[u][v] = min(graph[v].get(u, float('inf')), w)
            graph[v][u] = min(graph[v].get(u, float('inf')), w)

        res, undone, pq = 0, n, [(w, i) for i, w in enumerate(wells, 1)]
        heapify(pq)

        while pq:
            cost, village = heappop(pq)

            if village not in seen:
                res += cost
                undone -= 1

                if undone == 0:
                    break

                seen.add(village)

                for neig, w in graph[village].items():
                    if neig not in seen:
                        heappush(pq, (w, neig))

        return res
