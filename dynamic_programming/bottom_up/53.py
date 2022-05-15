from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [nums[0]] * N

        for i in range(1, N):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])

        return max(dp)
