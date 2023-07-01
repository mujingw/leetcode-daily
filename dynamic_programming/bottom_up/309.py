from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        hold = [0] * N
        sell = [0] * N
        cool = [0] * N
        hold[0] = -prices[0]

        for i in range(1, N):
            hold[i] = max(hold[i-1], cool[i-1] - prices[i])
            sell[i] = hold[i-1] + prices[i]
            cool[i] = max(cool[i-1], sell[i-1])

        return max(sell[-1], cool[-1])
