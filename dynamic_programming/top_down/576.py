from functools import lru_cache


class Solution:
    def findPaths(self, m: int, n: int, max_moves: int, sr: int, sc: int) -> int:
        MOD = int(1e9) + 7

        @lru_cache(None)
        def dfs(r, c, k):
            if r == m or c == n or r < 0 or c < 0:
                return 1

            if k == 0:
                return 0

            return dfs(r - 1, c, k - 1) + dfs(r, c - 1, k - 1) + dfs(r + 1, c, k - 1) + dfs(r, c + 1, k - 1)

        return dfs(sr, sc, max_moves) % MOD
