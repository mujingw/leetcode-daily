class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if s == s[::-1]:
            return len(s)

        N = len(s)
        dp = [[0 for j in range(N)] for i in range(N)]

        for i in range(N):
            dp[i][i] = 1

        for i in range(N, -1, -1):
            for j in range(i + 1, N):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][N - 1]
