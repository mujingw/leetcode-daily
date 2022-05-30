from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        N = len(nums)
        even = [0] * N
        odd = [0] * N
        even[0] = nums[0]

        for i in range(1, N):
            even[i] = max(even[i - 1], odd[i - 1] + nums[i], nums[i])
            odd[i] = max(odd[i - 1], even[i - 1] - nums[i], 0)

        return max(even[-1], odd[-1])
