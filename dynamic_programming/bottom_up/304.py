from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        R, C = len(matrix), len(matrix[0])
        self.dp = [[0 for _ in range(C)] for _ in range(R)]

        for i in range(R):
            for j in range(C):
                if i == 0 and j == 0:
                    self.dp[i][j] = matrix[i][j]
                elif i == 0:
                    self.dp[i][j] = self.dp[i][j - 1] + matrix[i][j]
                elif j == 0:
                    self.dp[i][j] = self.dp[i - 1][j] + matrix[i][j]
                else:
                    self.dp[i][j] = self.dp[i][j - 1] + self.dp[i - 1][j] + matrix[i][j] - self.dp[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.dp[row2][col2]
        leftcorner = self.dp[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        up = self.dp[row1 - 1][col2] if row1 > 0 else 0
        left = self.dp[row2][col1 - 1] if col1 > 0 else 0

        return total - up - left + leftcorner

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1, col1, row2, col2)
