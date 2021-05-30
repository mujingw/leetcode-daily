from collections import defaultdict
from collections import deque
from typing import List


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        def get_weight(dx, dy, r, c):
            if dy == 1 and grid[r][c] == 1:
                return 0
            elif dy == -1 and grid[r][c] == 2:
                return 0
            elif dx == 1 and grid[r][c] == 3:
                return 0
            elif dx == -1 and grid[r][c] == 4:
                return 0
            else:
                return 1

        DIR = ((0, 1), (0, -1), (1, 0), (-1, 0))
        g = defaultdict(set)
        R, C = len(grid), len(grid[0])

        for r in range(R):
            for c in range(C):
                for dx, dy in DIR:
                    nx, ny = r + dx, c + dy

                    if 0 <= nx < R and 0 <= ny < C:
                        w = get_weight(dx, dy, r, c)
                        g[(r, c)].add((nx, ny, w))

        q = deque([(0, 0, 0)])
        seen = {(0, 0): 0}

        while q:
            cx, cy, dist = q.popleft()

            for nx, ny, w in g[(cx, cy)]:
                if (nx, ny) not in seen or seen[(nx, ny)] > dist + w:
                    seen[(nx, ny)] = dist + w
                    q.append((nx, ny, dist + w))

        return seen[(R - 1, C - 1)]
