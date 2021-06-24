from functools import lru_cache


class Solution:
    def findPaths(self, m: int, n: int, max_moves: int, sr: int, sc: int) -> int:
        MOD = int(1e9) + 7
        DIR = ((0, 1), (0, -1), (-1, 0), (1, 0))

        @lru_cache(None)
        def dfs(r, c, k):
            if r == m or c == n or r < 0 or c < 0:
                return 1

            if k == 0:
                return 0

            return sum(dfs(r + dr, c + dc, k - 1) for dr, dc in DIR)

        return dfs(sr, sc, max_moves) % MOD
