from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(res, curr, nums, start):
            res.append(curr[:])

            for i in range(start, len(nums)):
                curr.append(nums[i])
                dfs(res, curr, nums, i + 1)
                curr.pop()

        res = []
        dfs(res, [], nums, 0)

        return res
