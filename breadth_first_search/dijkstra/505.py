from collections import deque
from typing import List


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], dest: List[int]) -> int:
        sx, sy = start[0], start[1]
        ex, ey = dest[0], dest[1]
        q = deque([(sx, sy, 0)])
        seen = {(sx, sy): 0}
        DIR = ((0, 1), (1, 0), (-1, 0), (0, -1))
        R, C = len(maze), len(maze[0])

        while q:
            cx, cy, steps = q.popleft()

            for dx, dy in DIR:
                nx, ny, ns = cx, cy, steps

                while 0 <= nx + dx < R and 0 <= ny + dy < C and maze[nx + dx][ny + dy] == 0:
                    nx += dx
                    ny += dy
                    ns += 1

                if (nx, ny) not in seen or ns < seen[(nx, ny)]:
                    seen[(nx, ny)] = ns
                    q.append((nx, ny, ns))

        return seen[(ex, ey)] if (ex, ey) in seen else -1
