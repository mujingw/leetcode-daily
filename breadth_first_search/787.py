from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        def build_graph(flights):
            g = defaultdict(set)

            for f, t, w in flights:
                g[f].add((t, w))

            return g

        g = build_graph(flights)
        h = [(0, 0, src)]

        while h:
            price_total, stops, curr = heappop(h)

            if curr == dst:
                return price_total

            if stops <= K:
                for nx_city, price in g[curr]:
                    heappush(h, (price + price_total, stops + 1, nx_city))

        return -1
