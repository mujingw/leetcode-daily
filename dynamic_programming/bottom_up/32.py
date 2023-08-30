class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) <= 1:
            return 0

        N = len(s)
        dp = [0] * N
        res = 0

        for i in range(1, N):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = 2

                    if i - 2 >= 0:
                        dp[i] += dp[i - 2]
                else:
                    if (i - 1) - dp[i - 1] >= 0 and s[(i - 1) - dp[i - 1]] == '(':
                        dp[i] = dp[i - 1] + 2

                        if (i - 1) - dp[i - 1] - 1 >= 0:
                            dp[i] += dp[(i - 1) - dp[i - 1] - 1]

            res = max(dp[i], res)

        return res
