from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        N = len(prices)
        dp = [[float('-inf') for _ in range(2)] for _ in range(N)]
        dp[0][0] = 0
        dp[0][1] = -prices[0] - fee

        for day in range(1, N):
            for hold_stock in (0, 1):
                if hold_stock == 0:
                    dp[day][hold_stock] = max(dp[day - 1][0], dp[day - 1][1] + prices[day])
                else:
                    dp[day][hold_stock] = max(dp[day - 1][1], dp[day - 1][0] - prices[day] - fee)

        return max(dp[N - 1])
