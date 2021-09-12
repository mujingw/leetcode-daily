from collections import deque
from typing import List


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        def bfs(r0, c0, tx, ty):
            q = deque([(r0, c0, 0)])
            seen = set([(r0, c0)])

            while q:
                cx, cy, dist = q.popleft()

                if cx == tx and cy == ty:
                    forest[cx][cy] = 1

                    return dist

                for dx, dy in DIR:
                    nx, ny = cx + dx, cy + dy

                    if 0 <= nx < R and 0 <= ny < C and forest[nx][ny] > 0 and (nx, ny) not in seen:
                        seen.add((nx, ny))
                        q.append((nx, ny, dist + 1))

            return -1

        R, C = len(forest), len(forest[0])
        DIR = ((0, 1), (0, -1), (1, 0), (-1, 0))
        res = 0
        trees = []

        for r in range(R):
            for c in range(C):
                if forest[r][c] > 1:
                    trees.append((r, c, forest[r][c]))

        cr, cc = 0, 0

        for tx, ty, height in sorted(trees, key=lambda x: (x[2])):
            effort = bfs(cr, cc, tx, ty)

            if effort != -1:
                res += effort
                cr, cc = tx, ty
            else:
                return -1

        return res
