from functools import lru_cache
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dfs(target):
            if target == 0:
                return 1

            if target < 0:
                return 0

            ways = 0

            for num in nums:
                ways += dfs(target - num)

            return ways

        return dfs(target)
