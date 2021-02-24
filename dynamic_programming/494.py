from functools import lru_cache
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        @lru_cache(None)
        def helper(t, pos):
            if pos == len(nums):
                return 1 if t == 0 else 0

            p = helper(t - nums[pos], pos + 1)
            n = helper(t + nums[pos], pos + 1)

            return p + n

        return helper(S, 0)
