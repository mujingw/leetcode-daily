from functools import lru_cache
from typing import List


class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def dfs(s1, s2, s3, s4, pos):
            sides = [s1, s2, s3, s4]

            if pos == len(nums):
                return all(s == target for s in sides)

            if any(s > target for s in sides):
                return False

            side = nums[pos]

            return dfs(s1 + side, s2, s3, s4, pos + 1) or \
                   dfs(s1, s2 + side, s3, s4, pos + 1) or \
                   dfs(s1, s2, s3 + side, s4, pos + 1) or \
                   dfs(s1, s2, s3, s4 + side, pos + 1)

        total = sum(nums)
        target = total // 4
        nums.sort(reverse=True)

        if total % 4 != 0 or target == 0:
            return False

        return dfs(0, 0, 0, 0, 0)
