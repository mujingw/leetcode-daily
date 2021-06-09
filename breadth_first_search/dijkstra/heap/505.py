from heapq import heappush, heappop
from typing import List


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        R, C = len(maze), len(maze[0])
        DIR = ((0, 1), (0, -1), (-1, 0), (1, 0))
        h = [(0, start[0], start[1])]
        seen = {(start[0], start[1]): 0}

        while h:
            dist, cx, cy = heappop(h)

            if cx == destination[0] and cy == destination[1]:
                return dist

            for dx, dy in DIR:
                nx, ny, new_dist = cx, cy, dist

                while 0 <= nx + dx < R and 0 <= ny + dy < C and maze[nx + dx][ny + dy] != 1:
                    nx += dx
                    ny += dy
                    new_dist += 1

                if (nx, ny) not in seen or seen[(nx, ny)] > new_dist:
                    heappush(h, (new_dist, nx, ny))
                    seen[(nx, ny)] = new_dist

        return -1
