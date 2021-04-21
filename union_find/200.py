from typing import List


class UF:
    def __init__(self, size):
        self.rank = [0] * size
        self.parent = [-1 for _ in range(size)]

    def union(self, u, v):
        if u != v:
            ru, rv = self.find(u), self.find(v)

            if self.rank[ru] < self.rank[rv]:
                self.parent[rv] = ru
            elif self.rank[rv] < self.rank[ru]:
                self.parent[ru] = rv
            else:
                self.parent[rv] = ru
                self.rank[ru] += 1

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        uf = UF(R * C)
        DIR = ((0, 1), (0, -1), (-1, 0), (1, 0))

        for i in range(R):
            for j in range(C):
                if grid[i][j] == '1':
                    idx = self.convert(i, j, R, C)

                    if uf.parent[idx] == -1:
                        uf.parent[idx] = idx

                    for dx, dy in DIR:
                        nx, ny = i + dx, j + dy

                        if self.is_valid(grid, nx, ny, R, C):
                            neighbor_idx = self.convert(nx, ny, R, C)

                            if uf.parent[neighbor_idx] == -1:
                                uf.parent[neighbor_idx] = idx

                            uf.union(idx, neighbor_idx)

        parents = set()

        for r in range(R):
            for c in range(C):
                if grid[r][c] == '0':
                    continue

                p = uf.find(self.convert(r, c, R, C))

                if p not in parents:
                    parents.add(p)

        return len(parents)

    def is_valid(self, grid, x, y, R, C):
        return 0 <= x < R and 0 <= y < C and grid[x][y] == '1'

    def convert(self, x, y, R, C):
        return x * C + y
