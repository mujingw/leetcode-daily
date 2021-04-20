from functools import lru_cache
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def helper(pos, t):
            if pos == len(nums):
                return True if t == 0 else False

            if t == 0:
                return True

            return helper(pos + 1, t - nums[pos]) or helper(pos + 1, t)

        total = sum(nums)
        nums.sort(reverse=True)

        if total % 2 != 0:
            return False

        return helper(0, total // 2)
