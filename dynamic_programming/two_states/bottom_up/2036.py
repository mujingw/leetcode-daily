from typing import List


class Solution:
    def maximumAlternatingSubarraySum(self, nums: List[int]) -> int:
        N = len(nums)
        add = [0] * N
        sub = [0] * N
        add[0] = nums[0]
        res = nums[0]

        for i in range(1, N):
            add[i] = max(sub[i - 1] + nums[i], nums[i])
            sub[i] = add[i - 1] - nums[i]
            res = max(res, add[i], sub[i])

        return res
