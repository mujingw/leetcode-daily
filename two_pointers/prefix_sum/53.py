from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        min_left, total, res = 0, 0, float('-inf')

        for x in nums:
            total += x
            res = max(res, total - min_left)
            min_left = min(min_left, total)

        return res
