from functools import lru_cache
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)

        @lru_cache(None)
        def dfs(row, col):
            if row == N:
                return 0

            path_sum = triangle[row][col]

            if col < len(triangle[row]):
                path_sum += min(dfs(row + 1, col), dfs(row + 1, col + 1))

            return path_sum

        return dfs(0, 0)
