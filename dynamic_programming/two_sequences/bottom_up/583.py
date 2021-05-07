class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N1, N2 = len(word1), len(word2)
        dp = [[0 for _ in range(N2 + 1)] for _ in range(N1 + 1)]

        for row in range(N1 + 1):
            dp[row][0] = row

        for col in range(N2 + 1):
            dp[0][col] = col

        for i in range(1, N1 + 1):
            for j in range(1, N2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1

        return dp[N1][N2]
