from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        def bfs(r, c):
            q = deque([(r, c, 0)])
            seen = {(r, c)}

            while q:
                cx, cy, dist = q.popleft()

                if matrix[cx][cy] == 0:
                    return dist

                for dx, dy in DIR:
                    nx, ny = cx + dx, cy + dy

                    if 0 <= nx < R and 0 <= ny < C and (nx, ny) not in seen:
                        seen.add((nx, ny))
                        q.append((nx, ny, dist + 1))

        R, C = len(matrix), len(matrix[0])
        DIR = ((0, 1), (0, -1), (-1, 0), (1, 0))
        res = [[-1 for _ in range(C)] for _ in range(R)]

        for r in range(R):
            for c in range(C):
                res[r][c] = bfs(r, c)

        return res
