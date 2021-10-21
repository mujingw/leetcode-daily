class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        R, C = len(t), len(s)
        dp = [[0 for c in range(C + 1)] for r in range(R + 1)]

        for i in range(R):
            for j in range(C):
                if i == 0:
                    dp[i][j] = 1

                if t[i] == s[j]:
                    dp[i + 1][j + 1] = dp[i][j] + dp[i + 1][j]
                else:
                    dp[i + 1][j + 1] = dp[i + 1][j]

        return dp[-1][-1]
