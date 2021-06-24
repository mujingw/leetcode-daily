from functools import lru_cache


class Solution:
    def knightProbability(self, N: int, K: int, row: int, column: int) -> float:
        MOVES = ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2))

        @lru_cache(None)
        def dfs(k, x, y, P):
            if not (0 <= x < N and 0 <= y < N):
                return 0

            if k == K:
                return P

            return sum(dfs(k + 1, x + dx, y + dy, P / len(MOVES)) for dx, dy in MOVES)

        return dfs(0, row, column, 1.0)
