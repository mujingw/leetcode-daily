from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        max_vals = [0] * N
        min_vals = [0] * N
        max_vals[0] = nums[0]
        min_vals[0] = nums[0]

        for i in range(1, N):
            max_vals[i] = max(max_vals[i - 1] * nums[i], min_vals[i - 1] * nums[i], nums[i])
            min_vals[i] = min(max_vals[i - 1] * nums[i], min_vals[i - 1] * nums[i], nums[i])

        return max(max_vals)
