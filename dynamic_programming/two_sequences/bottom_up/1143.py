class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)
        dp = [[0 for _ in range(N + 1)] for _ in range(M + 1)]

        for i, a in enumerate(text1):
            for j, b in enumerate(text2):
                if a == b:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[-1][-1]
