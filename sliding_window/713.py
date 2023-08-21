from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        product = 1
        res = 0

        while r < len(nums):
            product *= nums[r]
            r += 1

            while l < r and product >= k:
                left = nums[l]
                l += 1
                product //= left

            res += (r - l)

        return res
