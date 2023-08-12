from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        D = days[-1]
        days = set(days)
        tickets = {1: costs[0], 7: costs[1], 30: costs[2]}
        dp = [float('inf') for _ in range(D + 1)]
        dp[0] = 0

        for i in range(1, D + 1):
            if i not in days:
                dp[i] = dp[i - 1]
                continue

            for d in tickets.keys():
                dp[i] = min(dp[i], dp[max(0, i - d)] + tickets[d])

        return dp[-1]
