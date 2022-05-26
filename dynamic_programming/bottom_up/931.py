from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        R, C = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(C)] for _ in range(R)]

        for r in range(R):
            for c in range(C):
                if r == 0:
                    dp[r][c] = matrix[r][c]
                else:
                    upperleft = dp[r - 1][c - 1] if c > 0 else float('inf')
                    upper = dp[r - 1][c]
                    upperright = dp[r - 1][c + 1] if c < C - 1 else float('inf')
                    dp[r][c] = min(upperleft, upper, upperright) + matrix[r][c]

        return min(dp[-1])
