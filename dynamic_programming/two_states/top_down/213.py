from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums)

        return max(nums[0] + self.rob_linear(nums[2:-1]),
                   self.rob_linear(nums[1:]))

    def rob_linear(self, nums):
        return self.helper(0, nums, {})

    def helper(self, pos, nums, memo):
        if pos in memo:
            return memo[pos]

        if pos >= len(nums):
            return 0

        res = max(nums[pos] + self.helper(pos + 2, nums, memo),
                  self.helper(pos + 1, nums, memo))

        memo[pos] = res

        return res
