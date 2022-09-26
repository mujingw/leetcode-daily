from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])
        DIR = ((1, 0), (0, 1), (0, -1), (-1, 0))
        q_pac = deque([(r, 0) for r in range(R)] + [(0, c) for c in range(1, C)])
        q_atl = deque([(r, C-1) for r in range(R)] + [(R-1, c) for c in range(C-1)])
        good_pac = self.bfs(q_pac, R, C, DIR, heights)
        good_atl = self.bfs(q_atl, R, C, DIR, heights)

        return list(good_pac.intersection(good_atl))

    def bfs(self, q, R, C, DIR, heights):
        seen = set(list(q))

        while q:
            cx, cy = q.popleft()

            for dx, dy in DIR:
                nx, ny = cx + dx, cy + dy

                if 0 <= nx < R and 0 <= ny < C and heights[nx][ny] >= heights[cx][cy]:
                    if (nx, ny) not in seen:
                        seen.add((nx, ny))
                        q.append((nx, ny))

        return seen
