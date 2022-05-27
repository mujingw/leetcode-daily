from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        R, C = len(mat), len(mat[0])
        dp = [[0 for _ in range(C)] for _ in range(R)]

        for i in range(R):
            for j in range(C):
                if i == 0 and j == 0:
                    dp[i][j] = mat[i][j]
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] + mat[i][j]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + mat[i][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + mat[i][j]

        res = [[0 for _ in range(C)] for _ in range(R)]

        for i in range(R):
            for j in range(C):
                i0 = i - k - 1
                j0 = j - k - 1
                i1 = min(i + k, R - 1)
                j1 = min(j + k, C - 1)
                total = dp[i1][j1]
                leftcorner = dp[i0][j0] if i0 >= 0 and j0 >= 0 else 0
                left = dp[i1][j0] if i1 < R and j0 >= 0 else 0
                up = dp[i0][j1] if i0 >= 0 and j1 < C else 0

                res[i][j] = total - left - up + leftcorner

        return res
