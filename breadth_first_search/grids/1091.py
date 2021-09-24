from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        R, C = len(grid), len(grid[0])
        DIR = ((0, 1), (0, -1), (-1, 0), (1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1))
        q = deque([(0, 0, 1)])
        seen = {(0, 0)}

        while q:
            x, y, dist = q.popleft()

            if x == R - 1 and y == C - 1:
                return dist

            for dx, dy in DIR:
                nx, ny = x + dx, y + dy

                if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == 0 and (nx, ny) not in seen:
                    seen.add((nx, ny))
                    q.append((nx, ny, dist + 1))

        return -1
