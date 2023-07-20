from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)
        curr = nums[0]
        res = curr

        for i in range(1, N):
            curr = max(curr + nums[i], nums[i])
            res = max(curr, res)

        return res
