from heapq import heappush, heappop
from typing import List


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Edge:

    def __init__(self, u, v):
        self.u = u
        self.v = v
        self.weight = abs(u.x - v.x) + abs(u.y - v.y)

    def __lt__(self, other):
        return self.weight < other.weight


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        res = 0
        h = []
        cx, cy = points[0][0], points[0][1]
        visited = {Point(cx, cy)}

        for i in range(1, N):
            x, y = points[i][0], points[i][1]
            heappush(h, Edge(Point(cx, cy), Point(x, y)))

        while len(visited) < N:
            edge = heappop(h)
            v = edge.v

            if v in visited:
                continue

            visited.add(v)
            res += edge.weight

            for x, y in points:
                p = Point(x, y)

                if p not in visited:
                    heappush(h, Edge(v, p))

        return res
