from bisect import bisect
from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        res = []
        g = self.build_graph(tickets)
        self.backtrack(res, ["JFK"], "JFK", g, len(tickets) + 1)

        return res

    def build_graph(self, tickets):
        g = defaultdict(list)

        for dep, arr in tickets:
            bisect.insort(g[dep], arr)

        return g

    def backtrack(self, res, curr, dep, g, num_airports):
        if len(curr) == num_airports:
            res.extend(curr)

            return True

        for arr in g[dep]:
            curr.append(arr)
            g[dep].remove(arr)

            if self.backtrack(res, curr, arr, g, num_airports):
                return True

            bisect.insort(g[dep], arr)
            curr.pop()
