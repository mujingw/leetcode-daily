from typing import List


class UF:
    def __init__(self):
        self.rank = {}
        self.parent = {}
        self.count = 0

    def add(self, i):
        if i not in self.parent and i not in self.rank:
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
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        uf = UF()
        DIR = ((0, 1), (0, -1), (-1, 0), (1, 0))

        for i in range(R):
            for j in range(C):
                if grid[i][j] == '1':
                    idx = self.convert(i, j, C)
                    uf.add(idx)

                    for dx, dy in DIR:
                        nx, ny = i + dx, j + dy

                        if self.is_valid(grid, nx, ny, R, C):
                            neighbor_idx = self.convert(nx, ny, C)
                            uf.add(neighbor_idx)
                            uf.union(idx, neighbor_idx)

        return uf.count

    def is_valid(self, grid, x, y, R, C):
        return 0 <= x < R and 0 <= y < C and grid[x][y] == '1'

    def convert(self, x, y, C):
        return x * C + y
