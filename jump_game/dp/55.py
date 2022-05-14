from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [float('inf')] * N
        dp[0] = 0

        for i in range(N):
            for j in range(i):
                if j + nums[j] >= i:
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[-1]
