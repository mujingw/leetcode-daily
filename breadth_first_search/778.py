import collections
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        def ok(T):
            if grid[0][0] > T:
                return False

            q = collections.deque([(0, 0)])
            seen = set((0, 0))

            while q:
                cx, cy = q.popleft()

                if cx == R - 1 and cy == C - 1:
                    return True

                for dx, dy in DIR:
                    nx, ny = cx + dx, cy + dy

                    if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] <= T and (nx, ny) not in seen:
                        q.append((nx, ny))
                        seen.add((nx, ny))

            return False

        DIR = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        R, C = len(grid), len(grid[0])
        l, r = 0, 50 * 50

        while l < r:
            mid = (l + r) // 2

            if not ok(mid):
                l = mid + 1
            else:
                r = mid

        return l
