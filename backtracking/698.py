from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        self.total = sum(nums)
        self.k = k

        if self.total % self.k != 0:
            return False

        nums.sort(reverse=True)

        return self.dfs(nums, self.total // self.k, 0, 0, [False] * len(nums))

    def dfs(self, nums, target, pos, count, used):
        if count == self.k:
            return True

        if target == 0:
            return self.dfs(nums, self.total // self.k, 0, count + 1, used)

        last_failed_num = -1

        for i in range(pos, len(nums)):
            if used[i] or nums[i] > target or nums[i] == last_failed_num:
                continue

            used[i] = True

            if self.dfs(nums, target - nums[i], i + 1, count, used):
                return True

            used[i] = False
            last_failed_num = nums[i]

        return False
