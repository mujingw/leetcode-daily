from typing import List


class UF:
    def __init__(self):
        self.rank = {}
        self.parent = {}
        self.count = 0

    def add(self, i):
        if i in self.parent or i in self.rank:
            return

        self.rank[i] = 1
        self.parent[i] = i
        self.count += 1

    def union(self, u, v):
        ru, rv = self.find(u), self.find(v)

        if ru == rv:
            return

        if self.rank[ru] < self.rank[rv]:
            self.parent[ru] = rv
        elif self.rank[rv] < self.rank[ru]:
            self.parent[rv] = ru
        else:
            self.parent[rv] = ru
            self.rank[ru] += 1

        self.count -= 1

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        DIR = ((0, 1), (0, -1), (-1, 0), (1, 0))
        res = []
        uf = UF()

        for x, y in positions:
            cid = x * n + y
            uf.add(cid)

            for dx, dy in DIR:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n:
                    nid = nx * n + ny

                    if nid in uf.parent:
                        uf.union(cid, nid)

            res.append(uf.count)

        return res
