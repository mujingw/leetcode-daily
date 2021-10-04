from itertools import product
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        DIR = ((0, 1), (0, -1), (1, 0), (-1, 0))
        res = 0

        for r, c in product(range(R), range(C)):
            if grid[r][c] == 0:
                continue

            for dx, dy in DIR:
                nx, ny = r + dx, c + dy

                if not (0 <= nx < R and 0 <= ny < C):
                    res += 1
                elif grid[nx][ny] == 0:
                    res += 1

        return res
