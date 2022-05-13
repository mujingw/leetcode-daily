from collections import Counter
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        c = Counter(nums)
        houses = []

        for i in range(min(c.keys()), max(c.keys()) + 1):
            houses.append(i * c[i])

        return self.rob(houses)

    def rob(self, nums: List[int]) -> int:
        N = len(nums)

        if N == 1:
            return nums[0]

        if N == 2:
            return max(nums)

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]
