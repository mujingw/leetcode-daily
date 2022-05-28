class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s

        N = len(s)
        dp = [[False for _ in range(N)] for _ in range(N)]
        res = [0, 0]

        for i in range(N):
            dp[i][i] = True

        for i in range(N - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                res = [i, i + 1]

        for r in range(N - 1, -1, -1):
            for c in range(r + 2, N):
                if s[r] == s[c] and dp[r + 1][c - 1]:
                    dp[r][c] = True

                    if c - r + 1 > res[1] - res[0]:
                        res = [r, c]

        return s[res[0]:res[1] + 1]
