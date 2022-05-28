from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        dp = [0] * N
        lowest = prices[0]

        for i in range(1, N):
            dp[i] = max(dp[i - 1], prices[i] - lowest)
            lowest = min(lowest, prices[i])

        return dp[-1]
