from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(res, curr, t, nums, start):
            if t == 0:
                res.append(curr[:])
                return

            for i in range(start, len(nums)):
                if t - nums[i] < 0:
                    break

                curr.append(nums[i])
                backtrack(res, curr, t - nums[i], nums, i)
                curr.pop()

        res = []
        backtrack(res, [], target, sorted(candidates), 0)

        return res
