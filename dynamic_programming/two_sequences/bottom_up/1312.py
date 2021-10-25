class Solution:
    def minInsertions(self, s: str) -> int:
        return len(s) - self.lcs(s, s[::-1])

    def lcs(self, s1: str, s2: str) -> int:
        N = len(s1)
        dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

        for i, a in enumerate(s1):
            for j, b in enumerate(s2):
                dp[i + 1][j + 1] = dp[i][j] + 1 if a == b else max(dp[i + 1][j], dp[i][j + 1])

        return dp[-1][-1]
