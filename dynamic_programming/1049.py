from functools import lru_cache
from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        @lru_cache(None)
        def dfs(w1, w2, pos):
            if pos == len(stones):
                return abs(w1 - w2)

            x = stones[pos]
            res = min(dfs(w1 + x, w2, pos + 1), dfs(w1, w2 + x, pos + 1))

            return res

        return dfs(0, 0, 0)
