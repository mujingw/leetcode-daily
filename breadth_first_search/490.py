import collections
from typing import List


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], dest: List[int]) -> bool:
        q = collections.deque([(start[0], start[1])])
        seen = set([(start[0], start[1])])
        DIR = ((0, 1), (0, -1), (-1, 0), (1, 0))
        R, C = len(maze), len(maze[0])

        while q:
            cx, cy = q.popleft()

            if cx == dest[0] and cy == dest[1]:
                return True

            for dx, dy in DIR:
                nx, ny = cx, cy

                while 0 <= nx < R and 0 <= ny < C and maze[nx][ny] != 1:
                    nx += dx
                    ny += dy

                nx -= dx
                ny -= dy

                if 0 <= nx < R and 0 <= ny < C and (nx, ny) not in seen and maze[nx][ny] == 0:
                    q.append((nx, ny))
                    seen.add((nx, ny))

        return False
