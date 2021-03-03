from functools import lru_cache
from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        @lru_cache(None)
        def dfs(w1, w2, num_stones):
            if num_stones == 0:
                return abs(w1 - w2)

            x = stones.pop()
            res = min(dfs(w1 + x, w2, num_stones - 1), dfs(w1, w2 + x, num_stones - 1))
            stones.append(x)

            return res

        return dfs(0, 0, len(stones))
