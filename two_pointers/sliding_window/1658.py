from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        l, r = 0, 0
        target = sum(nums) - x
        sum_in_window = 0
        res = float("-inf")

        while r < len(nums):
            sum_in_window += nums[r]
            r += 1

            while sum_in_window > target and l < r:
                sum_in_window -= nums[l]
                l += 1

            if sum_in_window == target:
                res = max(res, r - l)

        return len(nums) - res if res != float("-inf") else -1
