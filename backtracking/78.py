from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrack(res, nums, [], 0)
        return res

    def backtrack(self, res, nums, curr, pos):
        if pos == len(nums):
            res.append(curr[:])
            return

        curr.append(nums[pos])
        self.backtrack(res, nums, curr, pos + 1)
        curr.pop()

        self.backtrack(res, nums, curr, pos + 1)
