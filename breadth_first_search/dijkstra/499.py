from collections import deque
from typing import List


class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        DIR = ((1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r'), (-1, 0, 'u'))
        res = set([])
        q = deque([(ball[0], ball[1], "", 0)])
        seen = {(ball[0], ball[1]): 0}
        hx, hy = hole[0], hole[1]
        R, C = len(maze), len(maze[0])

        while q:
            cx, cy, path, dist = q.popleft()

            for dx, dy, d in DIR:
                nx, ny, new_path, local_dist = cx, cy, path + d, 0

                while 0 <= nx + dx < R and 0 <= ny + dy < C and maze[nx + dx][ny + dy] != 1:
                    nx += dx
                    ny += dy
                    local_dist += 1

                    if nx == hx and ny == hy:
                        res.add((dist + local_dist, new_path))

                if local_dist == 0:
                    continue

                if (nx, ny) not in seen or seen[(nx, ny)] >= dist + local_dist:
                    seen[(nx, ny)] = dist + local_dist
                    q.append((nx, ny, new_path, dist + local_dist))

        return sorted(res)[0][1] if res else "impossible"
