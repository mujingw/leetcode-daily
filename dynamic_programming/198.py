from functools import lru_cache
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(None)
        def helper(location):
            if location < 0:
                return 0

            if location == 0:
                return nums[0]

            return max(nums[location] + helper(location - 2), helper(location - 1))

        return helper(len(nums) - 1)
