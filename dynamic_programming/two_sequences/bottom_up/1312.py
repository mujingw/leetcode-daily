class Solution:
    def minInsertions(self, s: str) -> int:
        return len(s) - self.lcs(s, s[::-1])

    def lcs(self, s1: str, s2: str) -> int:
        N = len(s2)
        dp = [[0] * (N + 1) for _ in range(N + 1)]

        for i, a in enumerate(s1):
            for j, b in enumerate(s2):
                if a == b:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[-1][-1]
