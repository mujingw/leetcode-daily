from functools import lru_cache


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache(None)
        def dfs(r, c):
            if r == 0 or c == 0:
                return 1

            return dfs(r - 1, c) + dfs(r, c - 1)

        return dfs(m - 1, n - 1)
