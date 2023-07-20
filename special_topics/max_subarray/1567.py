from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        N = len(nums)
        pos = [0] * N
        neg = [0] * N
        pos[0] = 1 if nums[0] > 0 else 0
        neg[0] = 1 if nums[0] < 0 else 0

        for i in range(1, N):
            if nums[i] < 0:
                pos[i] = (1 + neg[i - 1]) if neg[i - 1] else 0
                neg[i] = (1 + pos[i - 1]) if pos[i - 1] else 1
            elif nums[i] > 0:
                pos[i] = (1 + pos[i - 1]) if pos[i - 1] else 1
                neg[i] = (1 + neg[i - 1]) if neg[i - 1] else 0

        return max(pos)
