class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s

        N = len(s)
        dp = [[False for _ in range(N)] for _ in range(N)]
        longest, start = 1, 0

        for i in range(N):
            dp[i][i] = True

        for i in range(N - 1, -1, -1):
            for j in range(i + 1, N):
                if s[i] == s[j] and (i + 1 == j or dp[i + 1][j - 1]):
                    dp[i][j] = True

                curr_len = j - i + 1

                if curr_len > longest and dp[i][j]:
                    longest = curr_len
                    start = i

        return s[start:start + longest]
