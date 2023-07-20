from itertools import product
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(x, y):
            if (x, y) in visited:
                return 0

            visited.add((x, y))
            res = 1

            for dx, dy in DIR:
                nx, ny = x + dx, y + dy

                if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == 1 and (nx, ny) not in visited:
                    res += dfs(nx, ny)

            return res

        R, C = len(grid), len(grid[0])
        DIR = ((0, 1), (0, -1), (-1, 0), (1, 0))
        res, visited = 0, set()

        for r, c in product(range(R), range(C)):
            if grid[r][c] == 1:
                res = max(res, dfs(r, c))

        return res
