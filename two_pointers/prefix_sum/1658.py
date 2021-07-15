from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        N = len(nums)

        if target == 0:
            return N

        presum = {0: -1}
        res = -1
        total = 0

        for i, v in enumerate(nums):
            total += v

            if total - target in presum:
                res = max(res, i - presum[total - target])

            if total not in presum:
                presum[total] = i

        return N - res if res != -1 else -1
