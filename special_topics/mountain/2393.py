from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        N = len(nums)
        left = [1] * N
        segment_lengths = []
        res = 0

        for i in range(1, N):
            if nums[i] > nums[i - 1]:
                left[i] = left[i - 1] + 1

        left += [0]

        for i in range(1, len(left)):
            if left[i] <= left[i - 1]:
                segment_lengths.append(left[i - 1])

        for x in segment_lengths:
            res += (1 + x) * x // 2

        return res
