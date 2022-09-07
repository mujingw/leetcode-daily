from collections import deque
from typing import List


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        DIR = ((0, 1), (0, -1), (-1, 0), (1, 0))
        R, C = len(maze), len(maze[0])
        sx, sy = start
        q = deque([(sx, sy)])
        seen = {sx, sy}
        gx, gy = destination

        while q:
            cx, cy = q.popleft()

            if cx == gx and cy == gy:
                return True

            for dx, dy in DIR:
                nx, ny = cx, cy

                while 0 <= nx + dx < R and 0 <= ny + dy < C and maze[nx + dx][ny + dy] != 1:
                    nx += dx
                    ny += dy

                if (nx, ny) not in seen:
                    seen.add((nx, ny))
                    q.append((nx, ny))

        return False
