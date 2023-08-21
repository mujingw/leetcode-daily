from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        res = float("inf")
        l, r = 0, 0
        total = 0

        while r < len(nums):
            total += nums[r]
            r += 1

            while total >= s:
                res = min(res, r - l)
                total -= nums[l]
                l += 1

        return res if res != float("inf") else 0
