from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        R, C = len(heights), len(heights[0])
        q_pac, q_atl = deque(), deque()

        for c in range(C):
            q_pac.append((0, c))
            q_atl.append((R - 1, c))

        for r in range(R):
            q_pac.append((r, 0))
            q_atl.append((r, C - 1))

        good_pac = self.bfs(q_pac, R, C, heights)
        good_atl = self.bfs(q_atl, R, C, heights)

        return list(good_pac.intersection(good_atl))

    def bfs(self, q, R, C, heights):
        DIR = ((1, 0), (0, 1), (0, -1), (-1, 0))
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
