import collections
from typing import List


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        def bfs(x, y, R, C, DIR):
            q = collections.deque([(x, y)])
            seen = set((x, y))
            res = [False, False]

            while q:
                cx, cy = q.popleft()

                if cx == 0 or cy == 0:
                    res[0] = True

                if cx == R - 1 or cy == C - 1:
                    res[1] = True

                for dx, dy in DIR:
                    nx, ny = cx + dx, cy + dy

                    if 0 <= nx < R and 0 <= ny < C and (nx, ny) not in seen and matrix[nx][ny] <= matrix[cx][cy]:
                        seen.add((nx, ny))
                        q.append((nx, ny))

            return all(res)

        if not matrix or not matrix[0]:
            return []

        R, C = len(matrix), len(matrix[0])
        DIR = ((1, 0), (0, 1), (0, -1), (-1, 0))
        res = []

        for r in range(R):
            for c in range(C):
                if bfs(r, c, R, C, DIR):
                    res.append([r, c])

        return res
