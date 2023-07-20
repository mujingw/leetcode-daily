from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        curr = nums[0]

        for i in range(1, N):
            if nums[i] > nums[i - 1]:
                curr += nums[i]
            else:
                res = max(res, curr)
                curr = nums[i]

        return max(res, curr)
