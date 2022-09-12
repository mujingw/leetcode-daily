from functools import lru_cache
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        self.nums = sorted(nums)
        total = sum(nums)

        if total % 2 != 0:
            return False

        return self.dfs(total // 2, 0)

    @lru_cache(None)
    def dfs(self, target, pos):
        if target < 0:
            return False

        if target == 0:
            return True

        if pos >= len(self.nums):
            return False

        return self.dfs(target - self.nums[pos], pos + 1) or self.dfs(target, pos + 1)

