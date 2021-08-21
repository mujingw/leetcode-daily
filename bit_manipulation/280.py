from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)

        for i in range(1, N):
            if ((i & 1) == 0) == (nums[i - 1] < nums[i]):
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
