from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            if i == 1:
                dp[i] = max(dp[0], nums[1])
            else:
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return max(dp)
