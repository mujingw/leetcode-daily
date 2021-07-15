from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res, left, right = [1] * N, nums[0], nums[-1]

        for i in range(1, N):
            res[i] *= left
            left *= nums[i]

        for i in range(N - 2, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res
