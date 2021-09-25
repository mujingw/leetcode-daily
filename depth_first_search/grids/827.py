from collections import defaultdict
from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        DIR = ((0, 1), (0, -1), (-1, 0), (1, 0))
        R, C, next_color = len(grid), len(grid[0]), 2
        component_size = defaultdict(int)

        def paint(r, c, color):
            if (0 <= r < R and 0 <= c < C) and grid[r][c] == 1:
                grid[r][c] = color
                component_size[color] += 1

                for dx, dy in DIR:
                    paint(r + dx, c + dy, color)

        res = 0

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    continue

                paint(r, c, next_color)
                res = max(res, component_size[next_color])
                next_color += 1

        for r in range(R):
            for c in range(C):
                if grid[r][c] != 0:
                    continue

                neig_colors = set()

                for dx, dy in DIR:
                    nr, nc = r + dx, c + dy

                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != 0:
                        neig_colors.add(grid[nr][nc])

                size_formed = 1

                for color in neig_colors:
                    size_formed += component_size[color]

                res = max(res, size_formed)

        return res
