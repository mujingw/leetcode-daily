from itertools import product
from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.R, self.C = len(grid), len(grid[0])
        self.DIR = ((0, 1), (0, -1), (-1, 0), (1, 0))
        self.visited = set([])
        self.grid = grid
        self.res = 0
        count = 0
        sx, sy = -1, -1

        for r, c in product(range(self.R), range(self.C)):
            if grid[r][c] == 0:
                count += 1

            if grid[r][c] == 1:
                sx, sy = r, c

        self.backtrack(sx, sy, count + 1)

        return self.res

    def backtrack(self, x, y, target):
        if not (0 <= x < self.R and 0 <= y < self.C):
            return

        if (x, y) in self.visited:
            return

        if self.grid[x][y] == -1:
            return

        if self.grid[x][y] == 2 and target == 0:
            self.res += 1
            return

        self.visited.add((x, y))

        for dx, dy in self.DIR:
            self.backtrack(x + dx, y + dy, target - 1)

        self.visited.remove((x, y))
