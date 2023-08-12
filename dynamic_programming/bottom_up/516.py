class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)
        dp = [[1 for _ in range(N)] for _ in range(N)]

        for i in range(N - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 2

        for size in range(3, N + 1):
            for start in range(N - size + 1):
                end = start + size - 1

                if s[start] == s[end]:
                    dp[start][end] = dp[start + 1][end - 1] + 2
                else:
                    dp[start][end] = max(dp[start + 1][end], dp[start][end - 1])

        return dp[0][-1]
