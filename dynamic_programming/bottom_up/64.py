from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        dp = [[0 for _ in range(C)] for _ in range(R)]

        for r in range(R):
            for c in range(C):
                if r == 0 and c == 0:
                    dp[0][0] = grid[0][0]
                elif r == 0:
                    dp[r][c] = dp[r][c - 1] + grid[r][c]
                elif c == 0:
                    dp[r][c] = dp[r - 1][c] + grid[r][c]
                else:
                    dp[r][c] = min(dp[r - 1][c], dp[r][c - 1]) + grid[r][c]

        return dp[-1][-1]
