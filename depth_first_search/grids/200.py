from itertools import product
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c):
            if not (0 <= r < R and 0 <= c < C):
                return

            if grid[r][c] == '0':
                return

            if (r, c) in visited:
                return

            visited.add((r, c))

            for dx, dy in DIR:
                dfs(r + dx, c + dy)

        R, C = len(grid), len(grid[0])
        DIR = ((0, 1), (0, -1), (-1, 0), (1, 0))
        res = 0
        visited = set()

        for r, c in product(range(R), range(C)):
            if grid[r][c] == '1' and (r, c) not in visited:
                res += 1
                dfs(r, c)

        return res
