from collections import deque
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        R, C = len(rooms), len(rooms[0])
        DIR = ((0, 1), (0, -1), (-1, 0), (1, 0))
        EMPTY, GATE = 2147483647, 0
        q = deque([])

        for r in range(R):
            for c in range(C):
                if rooms[r][c] == GATE:
                    q.append((r, c, 0))

        while q:
            cx, cy, dist = q.popleft()

            for dx, dy in DIR:
                nx, ny = cx + dx, cy + dy

                if 0 <= nx < R and 0 <= ny < C and rooms[nx][ny] > dist + 1:
                    rooms[nx][ny] = dist + 1
                    q.append((nx, ny, dist + 1))
