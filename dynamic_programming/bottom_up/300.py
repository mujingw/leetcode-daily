from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1] * N

        for end in range(N):
            for sub_seq_end in range(end):
                if nums[sub_seq_end] < nums[end]:
                    dp[end] = max(dp[end], dp[sub_seq_end] + 1)

        return max(dp)
