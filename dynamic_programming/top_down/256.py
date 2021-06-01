from functools import lru_cache
from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        @lru_cache(None)
        def dfs(n, no_go):
            if n == 0:
                return min(costs[n][i] for i in range(3) if i != no_go)

            return min(costs[n][i] + dfs(n - 1, i) for i in range(3) if i != no_go)

        return dfs(len(costs) - 1, -1)
