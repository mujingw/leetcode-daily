from functools import lru_cache
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        @lru_cache(None)
        def dfs(x, y):
            res = 1

            for dx, dy in DIR:
                prev_x, prev_y = x + dx, y + dy

                if 0 <= prev_x < R and 0 <= prev_y < C:
                    if matrix[x][y] > matrix[prev_x][prev_y]:
                        res = max(res, dfs(prev_x, prev_y) + 1)

            return res

        R, C = len(matrix), len(matrix[0])
        DIR = ((0, 1), (0, -1), (1, 0), (-1, 0))
        res = 0

        for end_s in range(R):
            for end_y in range(C):
                res = max(res, dfs(end_s, end_y))

        return res
