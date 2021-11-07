from collections import deque


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        DIR = [(1, 2), (-1, 2), (2, 1), (-2, 1), (-2, -1), (2, -1), (-1, -2), (1, -2)]
        q = deque([(0, 0, 0)])
        seen = set([(0, 0)])

        while q:
            cx, cy, steps = q.popleft()

            if cx == x and cy == y:
                return steps

            for dx, dy in DIR:
                nx, ny = cx + dx, cy + dy

                if (nx, ny) not in seen:
                    q.append((nx, ny, steps + 1))
                    seen.add((nx, ny))
