class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        M, N = len(s), len(t)
        dp = [[0 for _ in range(N + 1)] for _ in range(M + 1)]

        for i in range(M + 1):
            dp[i][0] = 1

        for i in range(1, M + 1):
            for j in range(1, N + 1):
                dp[i][j] = dp[i - 1][j]

                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]

        return dp[-1][-1]
