from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        R, C = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(C)] for _ in range(R)]
        res = 0

        for i in range(R):
            for j in range(C):
                if i == 0 or j == 0:
                    dp[i][j] = 0 if matrix[i][j] == '0' else 1
                else:
                    if matrix[i][j] == '1':
                        dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1

                res = max(res, dp[i][j] ** 2)

        return res
