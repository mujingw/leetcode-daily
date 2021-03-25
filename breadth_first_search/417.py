import collections
from typing import List


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        def bfs(r0, c0):
            q = collections.deque([(r0, c0)])
            seen = set([(r0, c0)])

            while q:
                cx, cy = q.popleft()

                for dx, dy in DIR:
                    nx, ny = cx + dx, cy + dy

                    if 0 <= nx < R and 0 <= ny < C and (nx, ny) not in seen and matrix[nx][ny] >= matrix[cx][cy]:
                        seen.add((nx, ny))
                        q.append((nx, ny))

            return seen

        if not matrix:
            return []

        good_pac, good_atl = set(), set()
        R, C = len(matrix), len(matrix[0])
        DIR = ((1, 0), (0, 1), (0, -1), (-1, 0))

        for i in range(C):
            good_pac |= bfs(0, i)
            good_atl |= bfs(R - 1, i)

        for i in range(R):
            good_pac |= bfs(i, 0)
            good_atl |= bfs(i, C - 1)

        return good_pac.intersection(good_atl)
