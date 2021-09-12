from collections import deque
from typing import List


class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        DIR = ((0, 1), (0, -1), (-1, 0), (1, 0))
        R, C = len(image), len(image[0])
        q = deque([(x, y)])
        seen = set([(x, y)])

        while q:
            cx, cy = q.popleft()

            for dx, dy in DIR:
                nx, ny = cx + dx, cy + dy

                if 0 <= nx < R and 0 <= ny < C and (nx, ny) not in seen and image[nx][ny] == "1":
                    seen.add((nx, ny))
                    q.append((nx, ny))

        all_x = sorted(x for x, y in seen)
        all_y = sorted(y for x, y in seen)
        x1, x2 = all_x[0], all_x[-1]
        y1, y2 = all_y[0], all_y[-1]
        width, height = abs(x1 - x2) + 1, abs(y1 - y2) + 1

        return width * height
