from collections import defaultdict, deque
from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], threshold: int) -> int:
        def build_graph(edges):
            g = defaultdict(set)

            for u, v, w in edges:
                g[u].add((v, w))
                g[v].add((u, w))

            return g

        def dijkstra(g, src):
            q = deque([(src, 0)])
            seen = {src: 0}

            while q:
                curr, dist = q.popleft()

                for neig, cost in g[curr]:
                    if neig not in seen or seen[neig] > dist + cost:
                        seen[neig] = dist + cost
                        q.append((neig, dist + cost))

            return seen

        g = build_graph(edges)
        src2dests = {}
        city_counts = []

        for src in range(n):
            src2dests[src] = dijkstra(g, src)

        for city in src2dests:
            count = sum(1 for v in src2dests[city].values() if 0 < v <= threshold)
            city_counts.append((city, count))

        return sorted(city_counts, key=lambda x: (x[1], -x[0]))[0][0]
