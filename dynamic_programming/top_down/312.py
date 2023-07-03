from functools import lru_cache
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        self.nums = [1] + nums + [1]

        return self.backtrack(1, len(self.nums) - 2)

    @lru_cache(None)
    def backtrack(self, l, r):
        if l > r:
            return 0

        res = 0

        for i in range(l, r + 1):
            left = self.backtrack(l, i - 1)
            right = self.backtrack(i + 1, r)
            res = max(res, self.nums[l - 1] * self.nums[i] * self.nums[r + 1] + left + right)

        return res
