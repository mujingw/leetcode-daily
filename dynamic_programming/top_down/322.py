from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = self.dfs(coins, amount, {})

        return res if res != float('inf') else -1

    def dfs(self, coins, amount, memo):
        if amount < 0:
            return float('inf')

        if amount == 0:
            return 0

        if amount in memo:
            return memo[amount]

        res = float('inf')

        for coin in coins:
            res = min(res, 1 + self.dfs(coins, amount - coin, memo))

        memo[amount] = res

        return res
