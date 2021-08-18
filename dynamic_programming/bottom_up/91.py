class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        dp = [0] * (N + 1)
        dp[0] = 1
        dp[1] = 1 if 0 < int(s[0]) < 10 else 0

        for i in range(2, N + 1):
            if int(s[i - 1]) != 0:
                dp[i] = dp[i - 1]

            if 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]

        return dp[N]
