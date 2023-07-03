from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        N = len(piles)
        dp = [[0 for _ in range(N)] for _ in range(N)]

        for i in range(N):
            dp[i][i] = piles[i]

        for i in range(N - 1):
            dp[i][i + 1] = max(piles[i], piles[i + 1])

        for size in range(3, N + 1):
            for start in range(N - size + 1):
                end = start + size - 1
                dp[start][start + size - 1] = max(piles[start] - dp[start + 1][end], piles[end] - dp[start][end - 1])

        return dp[0][-1] > 0
