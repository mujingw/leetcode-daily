from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True

        N = len(nums)
        dp = [0] * N
        dp[0] = nums[0]

        for i in range(1, N - 1):
            if dp[i - 1] < i:
                return False

            dp[i] = max(i + nums[i], dp[i - 1])

        return dp[-2] >= N - 1
