from functools import lru_cache
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)

        @lru_cache(None)
        def dfs(row, col):
            if row == N:
                return 0

            width = len(triangle[row])

            if col >= width:
                return 0

            left = dfs(row + 1, col)
            right = dfs(row + 1, col + 1)

            return min(left + triangle[row][col], right + triangle[row][col])

        return dfs(0, 0)
