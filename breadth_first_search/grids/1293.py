from collections import deque
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        R, C = len(grid), len(grid[0])
        DIR = ((0, 1), (0, -1), (-1, 0), (1, 0))
        q = deque([(0, 0, 0, k)])
        seen = set([(0, 0, k)])

        while q:
            cx, cy, dist, quota = q.popleft()

            if cx == R - 1 and cy == C - 1:
                return dist

            for dx, dy in DIR:
                nx, ny = cx + dx, cy + dy

                if 0 <= nx < R and 0 <= ny < C:
                    if grid[nx][ny] == 0 and (nx, ny, quota) not in seen:
                        q.append((nx, ny, dist + 1, quota))
                        seen.add((nx, ny, quota))
                    else:
                        if quota > 0 and (nx, ny, quota - 1) not in seen:
                            q.append((nx, ny, dist + 1, quota - 1))
                            seen.add((nx, ny, quota - 1))

        return -1
