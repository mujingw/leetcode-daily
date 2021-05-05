from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        DIR = ((0, 1), (0, -1), (-1, 0), (1, 0))
        visited = set()

        def dfs(x, y):
            if not (0 <= x < R and 0 <= y < C):
                return 0

            if (x, y) in visited or grid[x][y] == 0:
                return 0

            res = 1
            visited.add((x, y))

            for dx, dy in DIR:
                res += dfs(x + dx, y + dy)

            return res

        res = 0

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))

        return res
