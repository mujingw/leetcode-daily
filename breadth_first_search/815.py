from collections import deque, defaultdict
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        routes = [set(x) for x in routes]
        g = self.build_graph(routes)
        seen = set()
        q = deque()

        for i, r in enumerate(routes):
            if source in r:
                q.append((i, 1))
                seen.add(i)

        while q:
            curr, dist = q.popleft()

            if target in routes[curr]:
                return dist

            for neig in g[curr]:
                if neig not in seen:
                    seen.add(neig)
                    q.append((neig, dist + 1))

        return -1

    def build_graph(self, routes):
        N = len(routes)
        g = defaultdict(list)

        for i in range(N):
            for j in range(i + 1, N):
                if routes[i].intersection(routes[j]):
                    g[i].append(j)
                    g[j].append(i)

        return g
