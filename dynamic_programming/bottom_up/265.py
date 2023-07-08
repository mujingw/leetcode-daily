from typing import List


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        N = len(costs)
        k = len(costs[0])
        dp = [[float('inf') for _ in range(k)] for _ in range(N)]

        for i in range(k):
            dp[0][i] = costs[0][i]

        for i in range(1, N):
            for c in range(k):
                min_prev = float('inf')

                for prev_c in range(k):
                    if prev_c == c:
                        continue

                    min_prev = min(min_prev, dp[i - 1][prev_c])

                dp[i][c] = min_prev + costs[i][c]

        return int(min(dp[-1]))
