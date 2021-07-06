from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        min_left_sum, total, res = 0, 0, float("-inf")

        for num in nums:
            total += num
            res = max(res, total - min_left_sum)
            min_left_sum = min(min_left_sum, total)

        return res
