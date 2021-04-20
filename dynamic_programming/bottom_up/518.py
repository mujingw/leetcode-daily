from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for val in range(1, amount + 1):
                if val >= coin:
                    dp[val] += dp[val - coin]

        return dp[amount]
