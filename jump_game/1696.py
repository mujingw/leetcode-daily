from typing import List

from sortedcontainers import SortedList


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        sl = SortedList()
        N = len(nums)
        dp = [0] * N
        dp[0] = nums[0]
        sl.add(dp[0])

        for i, val in enumerate(nums[1:], 1):
            if i - k - 1 >= 0:
                sl.remove(dp[i - k - 1])

            dp[i] = sl[-1] + val
            sl.add(dp[i])

        return dp[-1]
