from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        hold = [0] * N
        not_hold = [0] * N
        hold[0] = -prices[0]

        for i in range(1, N):
            hold[i] = max(hold[i-1], not_hold[i-1] - prices[i])
            not_hold[i] = max(not_hold[i-1], hold[i-1] + prices[i])

        return max(hold[-1], not_hold[-1])
