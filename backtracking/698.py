from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)

        if total % k != 0:
            return False

        self.N = len(nums)
        self.k = k
        self.nums = sorted(nums, reverse=True)
        self.used = [False] * self.N
        self.target = total // k

        return self.backtrack(total // k, 0, 0)

    def backtrack(self, t, start_at, count):
        if count == self.k:
            return True

        if t == 0:
            return self.backtrack(self.target, 0, count + 1)

        last_failed_num = -1

        for i in range(start_at, self.N):
            if self.used[i] or self.nums[i] > t or self.nums[i] == last_failed_num:
                continue

            self.used[i] = True

            if self.backtrack(t - self.nums[i], i + 1, count):
                return True

            self.used[i] = False
            last_failed_num = self.nums[i]

        return False
