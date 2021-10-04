from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.dfs(nums, 0, target, {})

    def dfs(self, nums, pos, target, memo):
        if pos == len(nums):
            return 1 if target == 0 else 0

        if (pos, target) in memo:
            return memo[(pos, target)]

        res = self.dfs(nums, pos + 1, target - nums[pos], memo)
        res += self.dfs(nums, pos + 1, target + nums[pos], memo)

        memo[(pos, target)] = res

        return res
