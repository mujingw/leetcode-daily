from functools import lru_cache
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums)

        return max(nums[0] + self.house_robber_one(nums[2:-1]),
                   self.house_robber_one(nums[1:]))

    def house_robber_one(self, nums):
        @lru_cache(None)
        def helper(pos):
            if pos >= N:
                return 0

            return max(nums[pos] + helper(pos + 2), helper(pos + 1))

        N = len(nums)

        return helper(0)
