from typing import List


class Solution:
    def uniquePathsWithObstacles(self, ob_grid: List[List[int]]) -> int:
        R, C = len(ob_grid), len(ob_grid[0])
        dp = [[0 for _ in range(C)] for _ in range(R)]
        dp[0][0] = 1 if ob_grid[0][0] == 0 else 0

        for i in range(R):
            for j in range(C):
                if i == 0 and j == 0:
                    continue

                if ob_grid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    left = dp[i][j - 1] if j > 0 else 0
                    up = dp[i - 1][j] if i > 0 else 0
                    dp[i][j] = left + up

        return dp[-1][-1]
