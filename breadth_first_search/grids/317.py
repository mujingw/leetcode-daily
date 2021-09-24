from collections import deque, defaultdict
from itertools import product
from typing import List


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        def bfs(r, c):
            q = deque([(r, c, 0)])
            seen = set([(r, c)])

            while q:
                x, y, dist = q.popleft()

                if grid[x][y] == 0:
                    agg_dist[(x, y)] += dist
                    bldgs_reached[(x, y)] += 1

                for dx, dy in DIR:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == 0 and (nx, ny) not in seen:
                        seen.add((nx, ny))
                        q.append((nx, ny, dist + 1))

        R, C = len(grid), len(grid[0])
        DIR = ((0, 1), (0, -1), (-1, 0), (1, 0))
        agg_dist = defaultdict(int)
        bldgs_reached = defaultdict(int)
        total_bldgs = 0
        res = float('inf')

        for r, c in product(range(R), range(C)):
            if grid[r][c] == 1:
                bfs(r, c)
                total_bldgs += 1

        for k, v in bldgs_reached.items():
            if v == total_bldgs:
                res = min(res, agg_dist[k])

        return res if res != float('inf') else -1
