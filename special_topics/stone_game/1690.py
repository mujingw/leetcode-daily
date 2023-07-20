from itertools import accumulate
from typing import List


class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        N = len(stones)
        presum = [0] + list(accumulate(stones))
        dp = [[0 for _ in range(N)] for _ in range(N)]

        for i in range(N):
            dp[i][i] = 0

        for size in range(2, N + 1):
            for start in range(N - size + 1):
                i, j = start, start + size - 1
                dp[i][j] = max(presum[j + 1] - presum[i + 1] - dp[i + 1][j],
                               presum[j] - presum[i] - dp[i][j - 1])

        return dp[0][-1]
