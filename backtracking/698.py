from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        used = [False] * N
        total = sum(nums)
        nums.sort(reverse=True)

        if total % k != 0:
            return False

        def dfs(target, pos, count):
            if count == k:
                return True

            if target < 0:
                return False

            if target == 0:
                return dfs(total // k, 0, count + 1)

            last_failure_num = -1

            for i in range(pos, N):
                if used[i] or nums[i] == last_failure_num:
                    continue

                used[i] = True

                if dfs(target - nums[i], i + 1, count):
                    return True

                used[i] = False
                last_failure_num = nums[i]

            return False

        return dfs(total // k, 0, 0)
