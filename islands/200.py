from typing import List


class UF:
    def __init__(self):
        self.rank = {}
        self.parent = {}
        self.count = 0

    def add(self, i):
        if self.exists(i):
            return

        self.rank[i] = 1
        self.parent[i] = i
        self.count += 1

    def size(self):
        return self.count

    def exists(self, i):
        return i in self.parent or i in self.rank

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
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        DIR = ((0, 1), (0, -1), (-1, 0), (1, 0))
        uf = UF()

        for i in range(R):
            for j in range(C):
                if grid[i][j] == '0':
                    continue

                idx = i * C + j
                uf.add(idx)

                for dx, dy in DIR:
                    nx, ny = i + dx, j + dy

                    if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == '1':
                        neighbor_idx = nx * C + ny
                        uf.add(neighbor_idx)
                        uf.union(idx, neighbor_idx)

        return uf.size()
