from itertools import product
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(x, y):
            if not (0 <= x < R and 0 <= y < C):
                return 0

            if grid[x][y] == 0:
                return 0

            if (x, y) in visited:
                return 0

            res = 1
            visited.add((x, y))

            for dx, dy in DIR:
                res += dfs(x + dx, y + dy)

            return res

        R, C = len(grid), len(grid[0])
        DIR = ((0, 1), (0, -1), (-1, 0), (1, 0))
        visited = set()
        res = 0

        for r, c in product(range(R), range(C)):
            res = max(res, dfs(r, c))

        return res
