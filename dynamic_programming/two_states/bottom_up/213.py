from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums)

        return max(nums[0] + self.rob_linear(nums[2:-1]),
                   self.rob_linear(nums[1:]))

    def rob_linear(self, nums: List[int]) -> int:
        N = len(nums)

        if N == 0:
            return 0

        if N == 1:
            return nums[0]

        a, b = nums[0], max(nums[0], nums[1])

        for i in range(2, N):
            a, b = b, max(a + nums[i], b)

        return b
