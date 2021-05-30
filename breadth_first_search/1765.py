from collections import deque
from typing import List


class Solution:
    def highestPeak(self, is_water: List[List[int]]) -> List[List[int]]:
        R, C = len(is_water), len(is_water[0])
        DIR = ((0, 1), (1, 0), (-1, 0), (0, -1))
        res = [[-1 for _ in range(C)] for _ in range(R)]
        q = deque()
        seen = set()

        for r in range(R):
            for c in range(C):
                if is_water[r][c] == 1:
                    res[r][c] = 0
                    q.append((r, c, 0))
                    seen.add((r, c))

        while q:
            cx, cy, h = q.popleft()
            res[cx][cy] = h

            for dx, dy in DIR:
                nx, ny = cx + dx, cy + dy

                if 0 <= nx < R and 0 <= ny < C and (nx, ny) not in seen:
                    seen.add((nx, ny))
                    q.append((nx, ny, h + 1))

        return res
