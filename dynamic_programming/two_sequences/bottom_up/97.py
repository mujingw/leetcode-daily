class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        M, N, L = len(s1), len(s2), len(s3)

        if M + N != L:
            return False

        dp = [[False for _ in range(N+1)] for _ in range(M+1)]
        dp[0][0] = True

        for i in range(1, M + 1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]

        for j in range(1, N + 1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]

        for i in range(1, M + 1):
            for j in range(1, N + 1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])

        return dp[-1][-1]
