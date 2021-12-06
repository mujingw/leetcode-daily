from collections import deque, defaultdict
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        g = self.build_graph(flights)
        seen = defaultdict(lambda: float('inf'))
        q = deque([(src, -1, 0)])

        while q:
            city, stops, cost = q.popleft()

            if city == dst or stops == K:
                continue

            for ng, price in g[city]:
                if cost + price < seen[ng]:
                    seen[ng] = cost + price
                    q.append((ng, stops + 1, cost + price))

        return seen[dst] if seen[dst] < float('inf') else -1

    def build_graph(self, flights):
        g = defaultdict(set)

        for f, t, w in flights:
            g[f].add((t, w))

        return g
