from collections import deque
from itertools import product
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def mark_region(r, c, from_val, to_val):
            q = deque([(r, c)])
            seen = {(r, c)}
            DIR = ((1, 0), (0, 1), (-1, 0), (0, -1))

            while q:
                cx, cy = q.popleft()
                grid[cx][cy] = to_val

                for dx, dy in DIR:
                    nx, ny = cx + dx, cy + dy

                    if 0 <= nx < R and 0 <= ny < C:
                        if (nx, ny) not in seen and grid[nx][ny] == from_val:
                            seen.add((nx, ny))
                            q.append((nx, ny))

        R, C = len(grid), len(grid[0])
        res = 0

        for i, j in product(range(R), range(C)):
            if i == 0 or j == 0 or i == R - 1 or j == C - 1:
                if grid[i][j] == 0:
                    mark_region(i, j, 0, -1)

        for i, j in product(range(R), range(C)):
            if grid[i][j] == 0:
                res += 1
                mark_region(i, j, 0, 2)

        return res
