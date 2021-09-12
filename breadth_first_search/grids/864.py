from collections import deque
from typing import List


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        def bfs(x, y, key_count):
            q = deque([(x, y, "", 0)])
            seen = set([(x, y, "")])

            while q:
                cx, cy, keys, dist = q.popleft()

                if grid[cx][cy] in KEYS and grid[cx][cy] not in keys:
                    keys += grid[cx][cy]

                if len(keys) == key_count:
                    return dist

                for dx, dy in DIR:
                    nx, ny = cx + dx, cy + dy

                    if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] != WALL and (nx, ny, keys) not in seen:
                        next_cell = grid[nx][ny]

                        if next_cell in LOCKS and next_cell.lower() not in keys:
                            continue

                        seen.add((nx, ny, keys))
                        q.append((nx, ny, keys, dist + 1))

            return -1

        DIR = ((0, 1), (0, -1), (1, 0), (-1, 0))
        R, C = len(grid), len(grid[0])
        KEYS = "abcdef"
        LOCKS = "ABCDEF"
        WALL = "#"
        sx, sy, key_count = -1, -1, 0

        for r in range(R):
            for c in range(C):
                if grid[r][c] == "@":
                    sx, sy = r, c
                elif grid[r][c] in KEYS:
                    key_count += 1

        return bfs(sx, sy, key_count)
