from collections import deque, defaultdict
from typing import List


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], dest: List[int]) -> int:
        DIR = ((0, 1), (1, 0), (-1, 0), (0, -1))
        R, C = len(maze), len(maze[0])
        sx, sy = start
        ex, ey = dest
        q = deque([(sx, sy, 0)])
        seen = defaultdict(lambda: float('inf'))
        seen[(sx, sy)] = 0

        while q:
            cx, cy, steps = q.popleft()

            for dx, dy in DIR:
                nx, ny, ns = cx, cy, steps

                while 0 <= nx + dx < R and 0 <= ny + dy < C and maze[nx + dx][ny + dy] == 0:
                    nx += dx
                    ny += dy
                    ns += 1

                if ns < seen[(nx, ny)]:
                    seen[(nx, ny)] = ns
                    q.append((nx, ny, ns))

        return seen[(ex, ey)] if (ex, ey) in seen else -1
