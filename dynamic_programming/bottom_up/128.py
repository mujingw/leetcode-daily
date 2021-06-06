from collections import defaultdict
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dp = defaultdict(int)

        for num in sorted(nums):
            if num - 1 in dp:
                dp[num] = dp[num - 1] + 1
            else:
                dp[num] = 1

        return max(dp.values()) if dp else 0
