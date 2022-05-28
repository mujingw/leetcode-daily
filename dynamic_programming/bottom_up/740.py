from collections import Counter
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        lower = min(nums)
        upper = max(nums)
        c = Counter(nums)
        dp = [0] * (upper - lower + 1)
        dp[0] = lower * c[lower]
        dp[1] = (lower + 1) * c[lower + 1]

        for i in range(1, len(dp)):
            x = lower + i
            dp[i] = max(dp[i - 1], dp[i - 2] + c[x] * x)

        return dp[-1]
