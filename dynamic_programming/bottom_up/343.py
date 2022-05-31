class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [i for i in range(n + 1)]
        dp[1] = 1
        dp[n] = 0

        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], dp[i - j] * dp[j])

        return dp[-1]
