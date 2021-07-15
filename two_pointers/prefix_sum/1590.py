from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        presum = {0: -1}
        goal = sum(nums) % p

        if goal == 0:
            return 0

        N = len(nums)
        running, res = 0, N

        for i, v in enumerate(nums):
            running = (running + v) % p
            target = (running - goal) % p

            if target in presum:
                res = min(res, i - presum[target])

            presum[running] = i

        return res if res < N else -1
