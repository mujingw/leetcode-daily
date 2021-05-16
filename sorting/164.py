from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        res = 0

        for a, b in zip(nums, nums[1:]):
            res = max(res, b - a)

        return res
