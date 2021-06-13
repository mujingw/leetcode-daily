from collections import deque
from typing import List


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        q = deque([(start[0], start[1])])
        seen = {(start[0], start[1])}
        DIR = ((0, 1), (0, -1), (-1, 0), (1, 0))
        R, C = len(maze), len(maze[0])

        while q:
            cx, cy = q.popleft()

            if cx == destination[0] and cy == destination[1]:
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
