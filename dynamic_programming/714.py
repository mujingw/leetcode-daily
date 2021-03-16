from functools import lru_cache
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @lru_cache(None)
        def helper(day, has_stock):
            if day == 0:
                if has_stock:
                    return - prices[0] - fee
                else:
                    return 0

            res = 0

            if has_stock:
                res = max(helper(day - 1, False) - prices[day] - fee, helper(day - 1, True))
            else:
                res = max(helper(day - 1, True) + prices[day], helper(day - 1, False))

            return res

        N = len(prices)

        return max(helper(N - 1, False), helper(N - 1, True))
