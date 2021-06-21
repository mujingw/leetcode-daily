from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        DIR = ((0, 1), (0, -1), (-1, 0), (1, 0))
        q = deque()
        seen = set()
        res = 0

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
                    seen.add((r, c))

        while q:
            cx, cy, rotten_mins = q.popleft()
            grid[cx][cy] = 2
            res = max(res, rotten_mins)

            for dx, dy in DIR:
                nx, ny = cx + dx, cy + dy

                if 0 <= nx < R and 0 <= ny < C and (nx, ny) not in seen and grid[nx][ny] == 1:
                    seen.add((nx, ny))
                    q.append((nx, ny, rotten_mins + 1))

        if any(grid[r][c] == 1 for r in range(R) for c in range(C)):
            return -1
        else:
            return res
