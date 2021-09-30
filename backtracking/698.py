from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)

        if total % k != 0:
            return False

        nums.sort(reverse=True)

        return self.backtrack(nums, total // k, 0, 0, [False] * len(nums), total, k)

    def backtrack(self, nums, target, pos, count, used, total, k):
        if count == k:
            return True

        if target == 0:
            return self.backtrack(nums, total // k, 0, count + 1, used, total, k)

        last_failed_num = -1

        for i in range(pos, len(nums)):
            if used[i] or nums[i] > target or nums[i] == last_failed_num:
                continue

            used[i] = True

            if self.backtrack(nums, target - nums[i], i + 1, count, used, total, k):
                return True

            used[i] = False
            last_failed_num = nums[i]

        return False
