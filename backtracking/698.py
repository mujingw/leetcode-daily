from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        self.T = total // k

        if total % k != 0:
            return False

        return self.backtrack(0, self.T, sorted(nums, reverse=True), k, [False] * len(nums))

    def backtrack(self, start, target, nums, remaining, used):
        if remaining == 1:
            return True

        if target == 0:
            return self.backtrack(0, self.T, nums, remaining - 1, used)

        for i in range(start, len(nums)):
            if used[i] or target < nums[i]:
                continue

            used[i] = True

            if self.backtrack(i + 1, target - nums[i], nums, remaining, used):
                return True

            used[i] = False

        return False
