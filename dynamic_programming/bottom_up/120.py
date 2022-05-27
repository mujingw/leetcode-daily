from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle[-1])
        dp = [[0] * i for i in range(1, N + 1)]
        dp[0][0] = triangle[0][0]

        for r in range(1, N):
            for c in range(r + 1):
                a = dp[r - 1][c - 1] if c - 1 >= 0 else float('inf')
                b = dp[r - 1][c] if c <= r - 1 else float('inf')
                dp[r][c] = min(a, b) + triangle[r][c]

        return min(dp[-1])
