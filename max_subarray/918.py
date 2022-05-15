from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)
        max_sum = self.max_subarray_sum(nums)
        min_sum = self.min_subarray_sum(nums[1:-1])

        return max(max_sum, total - min_sum)

    def min_subarray_sum(self, nums):
        min_so_far = float('inf')
        total = 0

        for x in nums:
            total += x
            min_so_far = min(min_so_far, total)

            if total > 0:
                total = 0

        return min_so_far

    def max_subarray_sum(self, nums):
        max_so_far = float('-inf')
        total = 0

        for x in nums:
            total += x
            max_so_far = max(max_so_far, total)

            if total < 0:
                total = 0

        return max_so_far
