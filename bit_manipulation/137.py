from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        N = len(nums)
        ones, twos = 0, 0

        for i in range(N):
            ones = (ones ^ nums[i]) & ~twos
            twos = (twos ^ nums[i]) & ~ones

        return ones
