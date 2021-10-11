from collections import Counter
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        c = Counter(nums)

        if len(c) == 1:
            return nums[0]

        lower, upper = min(c.keys()), max(c.keys())
        dp = [0] * (upper + 1)
        dp[lower] = c[lower]
        dp[lower + 1] = max(c[lower], c[lower + 1])

        for i in range(lower, upper + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + i * c[i])

        return dp[-1]
